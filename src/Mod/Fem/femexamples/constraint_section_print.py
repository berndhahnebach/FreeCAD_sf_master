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

"""

# constraint section print with volume elements
# https://forum.freecadweb.org/viewtopic.php?f=18&t=43044&start=10

import FreeCAD
from FreeCAD import Rotation
from FreeCAD import Vector

import Fem
import ObjectsFem
import Part
import Sketcher
import BOPTools.SplitFeatures
import CompoundTools.CompoundFilter

mesh_name = "Mesh"  # needs to be Mesh to work with unit tests


def init_doc(doc=None):
    if doc is None:
        doc = FreeCAD.newDocument()
    return doc


def get_information():
    info = {
            "name": "Constraint Section Print",
            "meshtype": "solid",
            "meshelement": "Tet10",
            "constraints": ["section_print", "fixed", "pressure"],
            "solvers": ["ccx"],
            "material": "solid",
            "equation": "mechanical"
            }
    return info


def setup(doc=None, solvertype="ccxtools"):

    if doc is None:
        doc = init_doc()

    # geometry object
    # name is important because the other method in this module use obj name
    arc_sketch = doc.addObject('Sketcher::SketchObject', 'Arc_Sketch')
    arc_sketch.Placement = FreeCAD.Placement(
            Vector(0.000000, 0.000000, 0.000000),
            Rotation(0.000000, 0.000000, 0.000000, 1.000000)
            )
    arc_sketch.MapMode = "Deactivated"
    geoList = [
        Part.ArcOfCircle(
            Part.Circle(Vector(0.000000, 0.000000, 0), Vector(0, 0, 1), 80.453387),
            0.005226,
            3.139832),
        Part.ArcOfCircle(
            Part.Circle(Vector(16.713875, -0.141644, 0), Vector(0, 0, 1), 47.309633),
            -0.005988,
            3.131067),
        Part.LineSegment(Vector(-80.452286, -0.000000, 0), Vector(-30.593138, -0.000000, 0)),
        Part.LineSegment(Vector(64.022659, -0.000000, 0), Vector(80.452286, -0.000000, 0))
        ]
    arc_sketch.addGeometry(geoList, False)

    conList = [
        Sketcher.Constraint('Coincident', 0, 3, -1, 1),
        Sketcher.Constraint('PointOnObject', 0, 2, -1),
        Sketcher.Constraint('PointOnObject', 0, 1, -1),
        Sketcher.Constraint('Coincident', 1, 3, 0, 3),
        Sketcher.Constraint('PointOnObject', 1, 2, -1),
        Sketcher.Constraint('PointOnObject', 1, 1, -1),
        Sketcher.Constraint('Coincident', 2, 1, 0, 2),
        Sketcher.Constraint('Coincident', 2, 2, 1, 2),
        Sketcher.Constraint('Coincident', 3, 1, 1, 1),
        Sketcher.Constraint('Coincident', 3, 2, 0, 1)
        ]
    arc_sketch.addConstraint(conList)
    # arc_sketch.setDatum(11, Units.Quantity('50.000000 mm'))
    # arc_sketch.setDatum(12, Units.Quantity('16.000000 mm'))

    extrude_part = doc.addObject('Part::Extrusion', 'Extrude')
    extrude_part.Base = arc_sketch
    extrude_part.DirMode = "Custom"
    extrude_part.Dir = Vector(0.00, 0.00, 1.00)
    extrude_part.DirLink = None
    extrude_part.LengthFwd = 30.00
    extrude_part.LengthRev = 0.00
    extrude_part.Solid = True
    extrude_part.Reversed = False
    extrude_part.Symmetric = True
    extrude_part.TaperAngle = 0.00
    extrude_part.TaperAngleRev = 0.00

    section_sketch = doc.addObject('Sketcher::SketchObject', 'Section_Sketch')
    section_sketch.Placement = FreeCAD.Placement(
            Vector(0.000000, 0.000000, 0.000000),
            Rotation(0.000000, 0.000000, 0.000000, 1.000000)
            )
    section_sketch.MapMode = "Deactivated"
    section_sketch.addGeometry(
            Part.LineSegment(Vector(-6.691961, -16.840161, 0), Vector(75.156087, 79.421394, 0)),
            False)
    # section_sketch.ExternalGeometry = extrude_part

    extrude_section_plane = doc.addObject('Part::Extrusion', 'Extrude001')
    extrude_section_plane.Base = section_sketch
    extrude_section_plane.DirMode = "Custom"
    extrude_section_plane.Dir = Vector(0.00, 0.00, -1.00)
    extrude_section_plane.DirLink = None
    extrude_section_plane.LengthFwd = 40.00
    extrude_section_plane.LengthRev = 0.00
    extrude_section_plane.Solid = False
    extrude_section_plane.Reversed = False
    extrude_section_plane.Symmetric = True
    extrude_section_plane.TaperAngle = 0.00
    extrude_section_plane.TaperAngleRev = 0.00

    Slice = BOPTools.SplitFeatures.makeSlice(name='Slice')
    Slice.Base = extrude_part
    Slice.Tools = extrude_section_plane
    Slice.Mode = 'Split'
    # Slice.Proxy.execute(Slice)
    Slice.purgeTouched()

    compound_one = CompoundTools.CompoundFilter.makeCompoundFilter(name='Compound_One')
    compound_one.Base = Slice
    compound_one.FilterType = "specific items"
    compound_one.items = "1"
    # compound_one.Proxy.execute(compound_one)
    compound_one.purgeTouched()
    compound_one.Base.ViewObject.hide()

    compound_two = CompoundTools.CompoundFilter.makeCompoundFilter(name='Compound_Two')
    compound_two.Base = Slice
    compound_two.FilterType = "specific items"
    compound_two.items = "0"
    # compound_two.Proxy.execute(compound_two)
    compound_two.purgeTouched()
    compound_two.Base.ViewObject.hide()

    geom_obj = BOPTools.SplitFeatures.makeBooleanFragments(name='BooleanFragments')
    geom_obj.Objects = [compound_one, compound_two]
    geom_obj.Mode = 'Standard'
    # geom_obj.Proxy.execute(geom_obj)
    geom_obj.purgeTouched()

    if FreeCAD.GuiUp:
        geom_obj.ViewObject.Document.activeView().viewAxonometric()
        geom_obj.ViewObject.Document.activeView().fitAll()

    doc.recompute()

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
        analysis.addObject(ObjectsFem.makeSolverElmer(doc, "SolverElmer"))
    elif solvertype == "z88":
        analysis.addObject(ObjectsFem.makeSolverZ88(doc, "SolverZ88"))
    if solvertype == "calculix" or solvertype == "ccxtools":
        solver_object.SplitInputWriter = False
        solver_object.AnalysisType = "static"
        solver_object.GeometricalNonlinearity = "linear"
        solver_object.ThermoMechSteadyState = False
        solver_object.MatrixSolverType = "default"
        solver_object.IterationsControlParameterTimeUse = False

    # material
    material_object = analysis.addObject(
        ObjectsFem.makeMaterialSolid(doc, "FemMaterial")
    )[0]
    mat = material_object.Material
    mat["Name"] = "CalculiX-Steel"
    mat["YoungsModulus"] = "210000 MPa"
    mat["PoissonRatio"] = "0.30"
    material_object.Material = mat

    # constraint fixed
    fixed_constraint = analysis.addObject(
        ObjectsFem.makeConstraintFixed(doc, name="ConstraintFixed")
    )[0]
    fixed_constraint.References = [(geom_obj, "Face3")]

    # constraint pressure
    pressure_constraint = analysis.addObject(
        ObjectsFem.makeConstraintPressure(doc, name="FemConstraintPressure")
    )[0]
    pressure_constraint.References = [(geom_obj, "Face7")]
    pressure_constraint.Pressure = 100.0
    pressure_constraint.Reversed = False

    # constraint section print
    section_constraint = analysis.addObject(
        ObjectsFem.makeConstraintSectionPrint(doc, name="ConstraintSectionPrint")
    )[0]
    section_constraint.References = [(geom_obj, "Face5")]

    # mesh
    from .meshes.mesh_section_print_tetra10 import create_nodes, create_elements
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

    return doc
