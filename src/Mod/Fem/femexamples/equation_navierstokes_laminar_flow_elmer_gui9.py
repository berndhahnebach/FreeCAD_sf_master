# ***************************************************************************
# *   Copyright (c) 2020 Sudhanshu Dubey <sudhanshu.thethunder@gmail.com    *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

# to run the example use:
"""
from femexamples.equation_navierstokes_laminar_flow_elmer_gui9 import setup
setup()

"""

import FreeCAD
from FreeCAD import Vector

import Fem
import ObjectsFem
from Draft import makeWire

mesh_name = "Mesh"  # needs to be Mesh to work with unit tests


def init_doc(doc=None):
    if doc is None:
        doc = FreeCAD.newDocument()
    return doc


def get_information():
    info = {"name": "Navier-Stokes Laminar Flow - Elmer GUI9",
            "meshtype": "solid",
            "meshelement": "Tria6",
            "constraints": [
                "temperature",
                "initial temperature",
                "flow velocity",
                "initial flow velocity"],
            "solvers": ["elmer"],
            "material": "fluid",
            "equation": "flow"
            }
    return info


def setup(doc=None, solvertype="elmer"):
    # setup model

    if doc is None:
        doc = init_doc()

    # geometry objects
    p1 = Vector(400.0, 5.197639294753229e-12, -50.0)
    p2 = Vector(400.0, 1.559191788425969e-11, -150.0)
    p3 = Vector(1400.0, 1.559191788425969e-11, -150.0)
    p4 = Vector(1400.0, -5.197639294753229e-12, 50.0)
    p5 = Vector(0.0, -5.197639294753229e-12, 50.0)
    p6 = Vector(0.0, 5.197639294753229e-12, -50.0)
    points = [
        p1, p2, p3, p4, p5, p6
    ]
    geom_obj = makeWire(
        points,
        closed=True,
        face=True,
        support=None
    )
    doc.recompute()

    if FreeCAD.GuiUp:
        geom_obj.ViewObject.Document.activeView().viewAxonometric()
        geom_obj.ViewObject.Document.activeView().fitAll()

    # analysis
    analysis = ObjectsFem.makeAnalysis(doc, "Analysis")

    # solver
    if solvertype == "elmer":
        solver_object = analysis.addObject(ObjectsFem.makeSolverElmer(doc, "SolverElmer"))[0]
        eq_heat = ObjectsFem.makeEquationHeat(doc, solver_object)
        eq_heat.LinearPreconditioning = "ILU1"
        eq_heat.Bubbles = True
        eq_heat.Stabilize = False
        eq_heat.Priority = 8
        eq_flow = ObjectsFem.makeEquationFlow(doc, solver_object)
        eq_flow.Bubbles = True
        eq_flow.Stabilize = False
        eq_flow.LinearPreconditioning = "ILU1"
        eq_flow.Priority = 10
    else:
        FreeCAD.Console.PrintWarning(
            "Not known or not supported solver type: {}. "
            "No solver object was created.\n".format(solvertype)
        )

    # material
    material_object = analysis.addObject(
        ObjectsFem.makeMaterialFluid(doc, "FemMaterial")
    )[0]
    mat = material_object.Material
    mat["Name"] = "Air-Generic"
    mat["Density"] = "1.20 kg/m^3"
    mat["KinematicViscosity"] = "15.11 mm^2/s"
    mat["DynamicViscosity"] = "1.8e-5 kg/s/m"
    mat["VolumetricThermalExpansionCoefficient"] = "0.00 µm/m/K"
    mat["ThermalConductivity"] = "0.03 W/m/K"
    mat["ThermalExpansionCoefficient"] = "0.0034/K"
    mat["SpecificHeat"] = "1.00 J/kg/K"
    mat["CompressibilityModel"] = "Perfect Gas"
    mat["ReferencePressure"] = "1e5 N/m^2"
    mat["SpecificHeatRatio"] = "1.4"
    material_object.Material = mat

    # inital_temperature_constraint
    init_temp_constraint = analysis.addObject(
        ObjectsFem.makeConstraintInitialTemperature(doc, "InitialTemperature")
    )[0]
    init_temp_constraint.initialTemperature = 293.15

    # temperature_constraint_1
    temp_constraint_1 = analysis.addObject(
        ObjectsFem.makeConstraintTemperature(doc, "Temperature_293K")
    )[0]
    temp_constraint_1.References = [
        (geom_obj, "Edge1"),
        (geom_obj, "Edge2"),
        (geom_obj, "Edge4"),
        (geom_obj, "Edge6")]
    temp_constraint_1.Scale = 33
    temp_constraint_1.Temperature = 293.15

    # temperature_constraint_2
    temp_constraint_2 = analysis.addObject(
        ObjectsFem.makeConstraintTemperature(doc, "Temperature_350K")
    )[0]
    temp_constraint_2.References = [(geom_obj, "Edge5")]
    temp_constraint_2.Scale = 10
    temp_constraint_2.Temperature = 350

    # velocity_constraint1
    inlet_vel_constraint = analysis.addObject(
        ObjectsFem.makeConstraintFlowVelocity(doc, "Inlet_Velocity")
    )[0]
    inlet_vel_constraint.References = [(geom_obj, "Edge5")]
    inlet_vel_constraint.NormalToBoundary = True
    inlet_vel_constraint.VelocityXEnabled = True
    inlet_vel_constraint.VelocityX = -0.02
    inlet_vel_constraint.VelocityYEnabled = True
    inlet_vel_constraint.VelocityZEnabled = True

    # velocity_constraint2
    outlet_vel_constraint = analysis.addObject(
        ObjectsFem.makeConstraintFlowVelocity(doc, "Outlet_Velocity")
    )[0]
    outlet_vel_constraint.References = [(geom_obj, "Edge3")]
    outlet_vel_constraint.VelocityXEnabled = False
    outlet_vel_constraint.VelocityYEnabled = True
    outlet_vel_constraint.VelocityZEnabled = True

    # velocity_constraint3
    wall_vel_constraint = analysis.addObject(
        ObjectsFem.makeConstraintFlowVelocity(doc, "Wall_Velocity")
    )[0]
    wall_vel_constraint.References = [
        (geom_obj, "Edge1"),
        (geom_obj, "Edge2"),
        (geom_obj, "Edge4"),
        (geom_obj, "Edge6")]
    wall_vel_constraint.VelocityXEnabled = True
    wall_vel_constraint.VelocityYEnabled = True
    wall_vel_constraint.VelocityZEnabled = True

    # initial_velocity_constraint
    init_vel_constraint = analysis.addObject(
        ObjectsFem.makeConstraintInitialFlowVelocity(doc, "Initial_Flow_Velocity")
    )[0]
    init_vel_constraint.VelocityXEnabled = True
    init_vel_constraint.VelocityYEnabled = True
    init_vel_constraint.VelocityZEnabled = True

    # face_elmer_freetextinput_constraint
    freetextinput = analysis.addObject(
        ObjectsFem.makeConstraintFaceElmerFreetextinput(doc)
    )[0]
    freetextinput.References = [(geom_obj, "Edge5")]
    freetextinput.ElmerFreetextinput = """
      Normal-Tangential Velocity = Logical True
      Velocity 1 = Variable Coordinate 3
      Real
        -0.05    0
        0.0   -0.02
        0.05    0
      End
      Velocity 2 = 0
      Velocity 3 = 0"""

    # mesh
    from .meshes.mesh_laminar_flow_elmer_gui9_tria6 import create_nodes, create_elements
    fem_mesh = Fem.FemMesh()
    control = create_nodes(fem_mesh)
    if not control:
        FreeCAD.Console.PrintError("Error on creating nodes.\n")
    control = create_elements(fem_mesh)
    if not control:
        FreeCAD.Console.PrintError("Error on creating elements.\n")
    femmesh_obj = analysis.addObject(
        ObjectsFem.makeMeshGmsh(doc, mesh_name)
    )[0]
    femmesh_obj.FemMesh = fem_mesh
    femmesh_obj.Part = geom_obj
    femmesh_obj.SecondOrderLinear = False

    # mesh_region_1
    mesh_region_1 = ObjectsFem.makeMeshRegion(doc, femmesh_obj)
    mesh_region_1.CharacteristicLength = '20 mm'
    mesh_region_1.References = [(geom_obj, "Edge1"), (geom_obj, "Face1")]

    # mesh_region_2
    mesh_region_2 = ObjectsFem.makeMeshRegion(doc, femmesh_obj)
    mesh_region_2.CharacteristicLength = '5 mm'
    mesh_region_2.References = [(geom_obj, "Edge5")]

    doc.recompute()
    return doc
