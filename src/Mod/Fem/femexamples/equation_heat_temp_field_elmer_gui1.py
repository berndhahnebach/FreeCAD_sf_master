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
from femexamples.equation_heat_temp_field_elmer_gui1 import setup
setup()

"""

import os

import FreeCAD
import Import

import Fem
import ObjectsFem

mesh_name = "Mesh"  # needs to be Mesh to work with unit tests


def init_doc(doc=None):
    if doc is None:
        doc = FreeCAD.newDocument()
    return doc


def get_information():
    info = {"name": "Heat Temperature Field - Elmer GUI1",
            "meshtype": "solid",
            "meshelement": "",
            "constraints": [
                "temperature",
                "body heat source"],
            "solvers": ["elmer"],
            "material": "solid",
            "equation": "heat"
            }
    return info


def setup(doc=None, solvertype="elmer"):
    # setup model

    if doc is None:
        doc = init_doc()

    # geometry objects
    path = os.path.dirname(os.path.realpath(__file__))
    stp_path = os.path.join(path, "pump_carter_sup.stp")
    Import.insert(stp_path, doc.Name)
    geom_obj = doc.Part__Feature
    doc.recompute()

    if FreeCAD.GuiUp:
        geom_obj.ViewObject.Transparency = 50
        geom_obj.ViewObject.Document.activeView().viewAxonometric()
        geom_obj.ViewObject.Document.activeView().fitAll()

    # analysis
    analysis = ObjectsFem.makeAnalysis(doc, "Analysis")

    # solver
    if solvertype == "elmer":
        solver_object = analysis.addObject(ObjectsFem.makeSolverElmer(doc, "SolverElmer"))[0]
        solver_object.SteadyStateMaxIterations = 10
        ObjectsFem.makeEquationHeat(doc, solver_object)
    else:
        FreeCAD.Console.PrintWarning(
            "Not known or not supported solver type: {}. "
            "No solver object was created.\n".format(solvertype)
        )

    # material
    material_object = analysis.addObject(
        ObjectsFem.makeMaterialSolid(doc, "FemMaterial")
    )[0]
    mat = material_object.Material
    mat["Name"] = "Aluminium"
    mat["Density"] = "2700 kg/m^3"
    mat["YoungsModulus"] = "70000 MPa"
    mat["UltimateTensileStrength"] = "310 MPa"
    mat["PoissonRatio"] = "0.35"
    mat["ThermalConductivity"] = "237 W/m/K"
    mat["ThermalExpansionCoefficient"] = "23.1 um/m/K"
    mat["SpecificHeat"] = "897 J/kg/K"
    material_object.Material = mat

    # body_heat_source_constraint
    heat_source_constraint = analysis.addObject(
        ObjectsFem.makeConstraintBodyHeatSource(doc, "ConstraintBodyHeatSource")
    )[0]
    heat_source_constraint.HeatSource = 10000.00

    # temperature_constraint
    temp_constraint = analysis.addObject(
        ObjectsFem.makeConstraintTemperature(doc, "ConstraintTemperature")
    )[0]
    temp_constraint.References = [
        (geom_obj, "Face57"),
        (geom_obj, "Face58"),
        (geom_obj, "Face67"),
        (geom_obj, "Face68"),
        (geom_obj, "Face77"),
        (geom_obj, "Face78")]
    temp_constraint.Scale = 8
    temp_constraint.Temperature = 293

    # mesh
    from .meshes.mesh_temp_field_elmer_gui1_tetra10 import create_nodes, create_elements
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
