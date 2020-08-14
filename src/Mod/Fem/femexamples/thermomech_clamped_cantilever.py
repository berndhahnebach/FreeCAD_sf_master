# ***************************************************************************
# *   Copyright (c) 2020 Sudhanshu Dubey <sudhanshu.thethunder@gmail.com>   *
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
from femexamples.thermomech_clamped_cantilever import setup
setup()

"""

import FreeCAD

import Fem
import ObjectsFem


mesh_name = "Mesh"  # needs to be Mesh to work with unit tests


def init_doc(doc=None):
    if doc is None:
        doc = FreeCAD.newDocument()
    return doc


def get_information():
    info = {
        "name": "Thermomech Clamped Cantilever",
        "meshtype": "solid",
        "meshelement": "Tet10",
        "constraints": ["fixed", "temperature", "initial temperature"],
        "solvers": ["calculix", "elmer"],
        "material": "solid",
        "equation": "thermomechanical"
    }
    return info


def setup(doc=None, solvertype="ccxtools"):
    # setup self weight cantilever base model

    if doc is None:
        doc = init_doc()

    # geometry object
    # name is important because the other method in this module use obj name
    geom_obj = doc.addObject("Part::Box", "Box")
    geom_obj.Height = geom_obj.Width = 50
    geom_obj.Length = 1000
    doc.recompute()

    if FreeCAD.GuiUp:
        geom_obj.ViewObject.Document.activeView().viewAxonometric()
        geom_obj.ViewObject.Document.activeView().fitAll()

    # analysis
    analysis = ObjectsFem.makeAnalysis(doc, "Analysis")

    # solver
    if solvertype == "calculix":
        solver_object = analysis.addObject(
            ObjectsFem.makeSolverCalculix(doc, "SolverCalculiX")
        )[0]
    elif solvertype == "ccxtools":
        solver_object = analysis.addObject(
            ObjectsFem.makeSolverCalculixCcxTools(doc, "CalculiXccxTools")
        )[0]
        solver_object.WorkingDir = u""
    elif solvertype == "elmer":
        solver_object = analysis.addObject(
            ObjectsFem.makeSolverElmer(doc, "SolverElmer")
        )[0]
        eq_elasticity = ObjectsFem.makeEquationElasticity(doc, solver_object)
        eq_elasticity.CalculateStresses = True
        eq_elasticity.Priority = 10
        eq_heat = ObjectsFem.makeEquationHeat(doc, solver_object)
        eq_heat.Priority = 20
    else:
        FreeCAD.Console.PrintWarning(
            "Not known or not supported solver type: {}. "
            "No solver object was created.\n".format(solvertype)
        )
    if solvertype == "calculix" or solvertype == "ccxtools":
        solver_object.AnalysisType = "thermomech"
        solver_object.GeometricalNonlinearity = "linear"
        solver_object.ThermoMechSteadyState = True
        solver_object.MatrixSolverType = "spooles"  # thomas
        solver_object.SplitInputWriter = False
        solver_object.IterationsThermoMechMaximum = 2000

    # material
    material_object = analysis.addObject(
        ObjectsFem.makeMaterialSolid(doc, "FemMaterial")
    )[0]
    mat = material_object.Material
    mat["Name"] = "CalculiX-Steel"
    mat["YoungsModulus"] = "205000 MPa"
    mat["PoissonRatio"] = "0.30"
    mat["Density"] = "7900 kg/m^3"
    mat["SpecificHeat"] = "590 J/kg/K"
    mat["ThermalConductivity"] = "43 W/m/K"
    mat["ThermalExpansionCoefficient"] = "0.000012 m/m/K"
    material_object.Material = mat

    # fixed_constraint
    fixed_constraint = analysis.addObject(
        ObjectsFem.makeConstraintFixed(doc, name="ConstraintFixed")
    )[0]
    fixed_constraint.References = [(geom_obj, "Face1"), (geom_obj, "Face2")]

    # constraint initial temperature
    constraint_initialtemp = analysis.addObject(
        ObjectsFem.makeConstraintInitialTemperature(doc, "ConstraintInitialTemperature")
    )[0]
    constraint_initialtemp.initialTemperature = 293.0

    # constraint temperature
    constraint_temperature = analysis.addObject(
        ObjectsFem.makeConstraintTemperature(doc, "ConstraintTemperature")
    )[0]
    constraint_temperature.References = [
        (geom_obj, "Face3"),
        (geom_obj, "Face4"),
        (geom_obj, "Face5"),
        (geom_obj, "Face6")]
    constraint_temperature.Temperature = 303.0
    constraint_temperature.CFlux = 0.0

    # mesh
    from .meshes.mesh_clamped_cantilever_tetra10 import create_nodes, create_elements
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

    doc.recompute()
    return doc
