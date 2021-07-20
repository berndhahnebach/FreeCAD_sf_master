# ***************************************************************************
# *   Copyright (c) 2019 Bernd Hahnebach <bernd@bimstatik.org>              *
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

__title__ = "OOFEM Writer"
__author__ = "Bernd Hahnebach"
__url__ = "http://www.freecadweb.org"

## \addtogroup FEM
#  @{

import time

import FreeCAD

from .. import writerbase
from femmesh import meshtools


class FemInputWriterOOFEM(writerbase.FemInputWriter):
    def __init__(
        self,
        analysis_obj,
        solver_obj,
        mesh_obj,
        member,
        dir_name=None,
        write_comments=True
        # write comments is a parameter value in this inherited class only
        # thus we do not pass it to instantiate the FemInputWriter class
    ):
        writerbase.FemInputWriter.__init__(
            self,
            analysis_obj,
            solver_obj,
            mesh_obj,
            member,
            dir_name
        )
        # comments
        self.write_comments = write_comments

        # volume cross section container
        self.volumesection_objects = []
        if len(self.shellthickness_objects) == 0:
            # no shells and one volume cross section
            self.volumesection_objects = [{}]
            self.volumesection_objects[0]["tf_number"] = 1
        # TODO should be in tasks module
        elif len(self.shellthickness_objects) > 1:
            sh_name = self.shellthickness_objects[0]["Objects"].Name
            message = (
                "Multiple Shellthicknesses for OOFEM not yet supported, "
                "the first thickness object is taken for all elements: {0}\n"
                .format(sh_name)
            )
            FreeCAD.Console.PrintError(message)
            self.shellthickness_objects = [self.shellthickness_objects[0]]

        # working dir and input file
        from os.path import join
        self.main_file_name = self.mesh_object.Name + ".in"
        self.file_name = join(self.dir_name, self.main_file_name)
        FreeCAD.Console.PrintLog(
            "FemInputWriterOOFEM --> self.dir_name  -->  {}\n"
            .format(self.dir_name)
        )
        FreeCAD.Console.PrintLog(
            "FemInputWriterOOFEM --> self.main_file_name  -->  {}\n"
            .format(self.main_file_name)
        )
        FreeCAD.Console.PrintMessage(
            "FemInputWriterOOFEM --> self.file_name  -->  {}\n"
            .format(self.file_name)
        )

    def write_solver_input(self):

        timestart = time.clock()

        """
        # once we gone need the nodes, we may recode the mesh writer
        # because we would get the nodes twice
        if not self.femnodes_mesh:
            self.femnodes_mesh = self.femmesh.Nodes
        """
        if not self.femelement_table:
            self.femelement_table = meshtools.get_femelement_table(self.femmesh)
            self.element_count = len(self.femelement_table)

        inpfile = open(self.file_name, "w")

        self.write_output_file_record(inpfile)

        self.write_job_description_record(inpfile)

        self.write_analysis_record(inpfile)

        self.write_domain_record(inpfile)

        self.write_output_manager_record(inpfile)

        self.write_components_size_record(inpfile)

        self.write_dof_manager_record(inpfile)

        self.write_node_and_element_records(inpfile)

        self.write_cross_section_record(inpfile)

        self.write_material_type_record(inpfile)

        self.write_boundary_condition_record(inpfile)

        self.write_nodal_load_record(inpfile)

        self.write_time_function_record(inpfile)

        self.write_set_record(inpfile)

        # footer
        self.write_footer(inpfile)
        inpfile.close()
        writing_time_string = (
            "Writing time input file: {} seconds"
            .format(round((time.clock() - timestart), 2))
        )
        FreeCAD.Console.PrintMessage(writing_time_string + " \n\n")
        return self.file_name

    def write_output_file_record(self, f):
        """ output filename String """
        if self.write_comments is True:
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# OOFEM Output File Name Record\n")
            f.write("#\n")
        f.write(self.mesh_object.Name + ".out\n")

    def write_job_description_record(self, f):
        """ Job description string """
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# Description Record\n")
            f.write("#\n")
        f.write(self.document.Name + "\n")

    def write_analysis_record(self, f):
        """ *AnalysisType
                *nsteps # (in)
                 [renumber # (in) ]
                 [profileopt # (in) ]
                 attributes # (string)
                 [ninitmodules # (in) ]
                 [nmodules # (in) ]
                 [nxfemman # (in) ]

                *StaticStructural
                 nsteps # (in)
                 [deltat # (...) ]
                 [prescribedtimes # (...) ]
                 [stiffmode # (...) ]
                 [nonlocalext # (...) ]
                 [sparselinsolverparams # (...) ]

                *LinearStability
                 nroot # (in)
                 rtolv # (rn)
                 [eigensolverparams # (...) ]

                *NonLinearStatic
                 [nmsteps # (in) ]
                 nsteps # (in)
                 [contextOutputStep # (in) ]
                 [sparselinsolverparams # (string) ]
                 [nonlinform # (in) ]
                 [nonlocstiff # (in) ]
                 [nonlocalext]
                 [loadbalancing]
        """
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# Analysis and extra Output Modules Record\n")
            f.write("#\n")
        f.write("LinearStatic  nsteps 1  nmodules 1\n")
        f.write("vtkxml tstep_all domain_all  primvars 1 1  vars 5 1 2 4 5 27  stype 2\n")

    def write_domain_record(self, f):
        """ domain *domainType
                *2dPlaneStress
                 two default dofs per node (u-displacement, v-displacement)
                 1, 2
                *2d-Truss
                 three default dofs per node (u-displacement, v-displacement, w-displacement)
                 1, 2, 3
                *3d
                 three default dofs per node (w-displacent, u-rotation, v-rotation)
                 1, 2, 3
                *2dMindlinPlate
                 six default dofs per node (displacement and rotation along each axis)
                 1, 2, 3, 4, 5, 6
                *3dShell
                 three default dofs per node (u-displacement, w-displacement, v-rotation)
                 1, 2, 5
                *2dBeam
                 three default dofs per node (u-velocity, v-velocity, and pressure)
                 7, 8, 11
        available dofs
            u-displacement=1
            v-displacement=2
            w-displacement=3
            u-rotation=4
            v-rotation=5
            w-rotation=6
            u-velocity=7
            v-velocity=8
            w-velocity=9
            temperature=10
            pressure=11
            special dofs for gradient-type constitutive models=12 and 13
            mass concentration=14
            special dofs for extended finite elements (XFEM)=15–30
        """
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# Domain Record\n")
            f.write("#\n")
        if meshtools.is_zplane_2D_mesh(self.femmesh):
            self.domain = "2dPlaneStress"
        else:
            self.domain = "3d"
        f.write("domain " + self.domain + "\n")

    def write_output_manager_record(self, f):
        """ OutputManager
                [tstep all]
                [tstep step # (in) ]
                [tsteps out # (rl) ]
                [dofman all]
                [dofman output # (rl) ]
                [dofman except # (rl) ]
                [element all]
                [element output # (rl) ]
                [element except # (rl) ]
                ndofman # (in)
                nelem # (in)
                ncrosssect # (in)
                nmat # (in)
                nbc # (in)
                nic # (in)
                nltf # (in)
                [nbarrier # (in) ]
        """
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# Output Manager Record\n")
            f.write("#\n")
        f.write("OutputManager tstep_all dofman_all element_all\n")

    def write_components_size_record(self, f):
        """ Components size record, describes the number of components in related domain
                ndofman #(in)
                nelem #(in)
                ncrosssect #(in)
                nmat #(in)
                nbc #(in)
                nic #(in)
                nltf #(in)
                [nbarrier #(in)]
                neset #[in]
        """
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# Components Size Record\n")
            f.write("#\n")

        # count mesh nodes and elements
        # HAAACK, we gone write the mesh into a tmp file to geth the count of written elements
        from tempfile import mkstemp
        filepath, filename = mkstemp()
        tmpfile = open(filepath, "w")
        from feminout.importOofemMesh import write_oofem_mesh_to_file as write_mesh
        nd_count, self.ele_count = write_mesh(tmpfile, self.femmesh, self.femelement_table, None)
        tmpfile.close()
        # print(nd_count, self.ele_count)

        # count cross sections
        # only one cross section is supported
        cs_count = 0
        allcss = self.volumesection_objects + self.shellthickness_objects
        for femobj in allcss:
            # femobj --> dict, FreeCAD document object is femobj["Object"]
            cs_count += 1
            femobj["cs_number"] = cs_count
        self.cs_count = cs_count  # we need for the set numbers, the bc sets start after cs sets

        # count materials
        # only one material is supported
        # check should be in tasks module
        if len(self.material_objects) != 1:
            mat_name = self.material_objects[0]["Objects"].Name
            message = (
                "Multiple Materials for OOFEM not yet supported, "
                "the first material is taken for all elements: {0}\n"
                .format(mat_name)
            )
            FreeCAD.Console.PrintError(message)
            self.material_objects = [self.material_objects[0]]
        # the only material we have, will have no 1
        self.material_objects[0]["mat_number"] = 1
        mat_count = len(self.material_objects)

        # count boundary conditions including loads
        # delete force constraints on Edges and Faces
        # count bcs
        bc_count = 0
        all_bcs = self.displacement_objects
        for femobj in all_bcs:
            # femobj --> dict, FreeCAD document object is femobj["Object"]
            bc_count += 1
            femobj["bc_number"] = bc_count

        # count initial conditions
        # no initial conditions are supported, thus = 0
        ic_count = 0

        # count time functions and their associated records
        # no special time functions are supported, thus = 1
        tltf_count = 1

        # count node- and elementsets
        # on set for every boundary condition or load
        # one material and one cross section is used for all elements
        # set 1 is used for this
        set_count = bc_count + self.cs_count

        # write values
        f.write(
            "ndofman {0}  "
            "nelem {1}  "
            "ncrosssect {2}  "
            "nmat {3}  "
            "nbc {4}  "
            "nic {5}  "
            "nltf {6}  "
            "nset {7}\n"
            .format(
                nd_count,
                self.ele_count,
                self.cs_count,
                mat_count,
                bc_count,
                ic_count,
                tltf_count,
                set_count
            )
        )

    def write_dof_manager_record(self, f):
        """ *DofManagerType
             (num#) (in)
             [load # (ra) ]
             [DofIDMask # (ia) ]
             [bc # (ia) ]
             [ic # (ia) ]
             [doftype # (ia) masterMask # (ia) ]
             [shared]i | h[remote]i | h[null]
             [partitions # (ia) ]
        """
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# DOF Manager Record\n")

    def write_node_and_element_records(self, f):
        """ Mesh writer, see OOFEM mesh file writer module """
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# Node and Element Records\n")
            f.write("#\n")
        from feminout.importOofemMesh import write_oofem_mesh_to_file as write_mesh
        write_mesh(f, self.femmesh, self.femelement_table, None, self.write_comments)

    def write_cross_section_record(self, f):
        """ *CrossSectType (num#) (in)
                *SimpleCS [thick # (rn) ] [width # (rn) ] [area # (rn) ]
                 [iy # (rn) ] [iz # (rn) ] [ik # (rn) ]
                 [shearareay # (rn) ] [shearareaz # (rn) ] beamshearcoeff # (rn)

                *VariableCS [thick # (expr) ] [width # (expr) ] [area # (expr) ]
                 [iy # (expr) ] [iz # (expr) ] [ik # (expr) ]
                 [shearareay # (expr) ] [shearareaz # (expr) ]

                *LayeredCS nLayers # (in)
                 LayerMaterials # (ia)
                 Thicks # (ra) Widths # (ra)
                 midSurf # (rn)
        """
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# Cross Section Record\n")
            f.write("#\n")
        mat_number = self.material_objects[0]["mat_number"]
        # we only have one cs set, late we gone write this inside the femobj
        # (like we did with cs_number)
        self.cs_set_number = 1
        if self.domain == "2dPlaneStress":
            thickness = self.shellthickness_objects[0]["Object"].Thickness.getValueAs("mm")
            cs_number = self.shellthickness_objects[0]["cs_number"]
            f.write(
                "SimpleCS {0}  thick {1}  material {2}  set {3}\n"
                .format(cs_number, thickness, mat_number, self.cs_set_number)
            )
        elif self.domain == "3d":
            cs_number = self.volumesection_objects[0]["cs_number"]
            f.write(
                "SimpleCS {0}  material {1}  set {2}\n"
                .format(cs_number, mat_number, self.cs_set_number)
            )

    def write_material_type_record(self, f):
        """ *MaterialType (num#) (in) d # (rn)
                 Linear isotropic elastic material
                *IsoLE num (in) # d (rn) # E (rn) # n (rn) # tAlpha (rn) #
                 Mooney-Rivlin
                *MooneyRivlin (in) # d (rn) # K (rn) # C1 (rn) # C2 (rn) #
                 Large-strain master material material
                *LSmasterMat (in) # m (rn) # slavemat (in) #
                 DP material
                *DruckerPrager
                    num (in) # d (rn) # tAlpha (rn) # E (rn) #
                    n (rn) # alpha (rn) # alphaPsi (rn) # ht (in) #
                    iys (rn) # lys (rn) # hm (rn) # kc (rn) #
                    [ yieldtol (rn) #]
                 Mises plasticity model with isotropic hardening
                *MisesMat
                    (in) # d (rn) # E (rn) # n (rn) # sig0 (rn) #
                    H (rn) # omega crit (rn) #a (rn) #
                 Rotating crack model for concrete
                *Concrete3
                    d (rn) # E (rn) # n (rn) # Gf (rn) #
                    Ft (rn) # exp soft (in) # tAlpha (rn) #
                 EC2CreepMat model for concrete creep and shrinkage
                *EC2CreepMat
                    n (rn) # [ begOfTimeOfInterest (rn) #] [ end-OfTimeOfInterest (rn) #]
                    relMatAge (rn) # [ timeFactor (rn) #] stiffnessFactor (rn) #
                    [ tAlpha (rn) #] fcm28 (rn) # t0 (rn) # cem- Type (in) # [ henv (rn) #]
                    h0 (rn) # shType (in) # [ spectrum ][ temperatureDependent ]
        """
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# Material Type Record\n")
            f.write("#\n")
            # same as CalculiX writer, but I can not believe this is right?!
            f.write("# unit density: t/mm^3\n")
            f.write("# unit Youngs Modulus: MPa = N/mm2\n")
            f.write("# unit Thermal Expansion Coefficient: 1/K\n")
        # the first mat object is taken for all elements
        mat_obj = self.material_objects[0]["Object"]
        mat_number = self.material_objects[0]["mat_number"]
        ds = FreeCAD.Units.Quantity(mat_obj.Material["Density"])
        ds_in_t_per_mm3 = float(ds.getValueAs("t/mm^3"))
        ym = FreeCAD.Units.Quantity(mat_obj.Material["YoungsModulus"])
        ym_in_MPa = ym.getValueAs("MPa")
        pr = float(mat_obj.Material["PoissonRatio"])
        th = FreeCAD.Units.Quantity(mat_obj.Material["ThermalExpansionCoefficient"])
        th_in_mm_per_mmK = th.getValueAs("mm/mm/K")
        f.write(
            "IsoLE {0}  d {1}  E {2}  n {3}  talpha {4}\n"
            .format(mat_number, ds_in_t_per_mm3, ym_in_MPa, pr, th_in_mm_per_mmK)
        )

    def write_boundary_condition_record(self, f):
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# Boundary Condition Record\n")
            f.write("#\n")

        # displacement constraints
        # get nodes of displacement constraints
        self.get_constraints_displacement_nodes()

        # write displacement constraints
        if self.write_comments is True:
            f.write("# FreeCAD displacement constraints\n")
        for femobj in self.displacement_objects:
            # femobj --> dict, FreeCAD document object is femobj["Object"]

            # begin and bc number
            line_begin = "BoundaryCondition {0}  loadTimeFunction 1".format(femobj["bc_number"])

            # dofs and values, prescribed (http://www.oofem.org/forum/viewtopic.php?pid=7130#p7130)
            disp_obj = femobj["Object"]
            dofs_count = 0
            dofs_numbers = ""
            val_value = ""
            if self.domain == "2dPlaneStress":
                # x, y (FreeCAD) = u, v (OOFEM) = 1, 2 (dof numbers)
                # z and 3 rotations are ignored
                if (disp_obj.xFix is True) \
                        and (disp_obj.xFree is False) \
                        and (disp_obj.xDisplacement == 0.0):
                    dofs_count += 1
                    dofs_numbers += "1"
                    val_value += " 0"
                elif (disp_obj.xFix is False) \
                        and (disp_obj.xFree is False) \
                        and (disp_obj.xDisplacement != 0):
                    dofs_count += 1
                    dofs_numbers += " 1"
                    val_value += " {0}".format(disp_obj.xDisplacement)
                if (disp_obj.yFix is True) \
                        and (disp_obj.yFree is False) \
                        and (disp_obj.yDisplacement == 0.0):
                    dofs_count += 1
                    dofs_numbers += " 2"
                    val_value += " 0"
                elif (disp_obj.yFix is False) \
                        and (disp_obj.yFree is False) \
                        and (disp_obj.yDisplacement != 0):
                    dofs_count += 1
                    dofs_numbers += " 2"
                    val_value += " {0}".format(disp_obj.yDisplacement)
            elif self.domain == "3d":
                # x, y, z (FreeCAD) = u, v, w (OOFEM) = 1, 2, 3 (dof numbers)
                # 3 rotations are ignored
                if (disp_obj.xFix is True) \
                        and (disp_obj.xFree is False) \
                        and (disp_obj.xDisplacement == 0.0):
                    dofs_count += 1
                    dofs_numbers += "1"
                    val_value += " 0"
                elif (disp_obj.xFix is False) \
                        and (disp_obj.xFree is False) \
                        and (disp_obj.xDisplacement != 0):
                    dofs_count += 1
                    dofs_numbers += " 1"
                    val_value += " {0}".format(disp_obj.xDisplacement)
                if (disp_obj.yFix is True) \
                        and (disp_obj.yFree is False) \
                        and (disp_obj.yDisplacement == 0.0):
                    dofs_count += 1
                    dofs_numbers += " 2"
                    val_value += " 0"
                elif (disp_obj.yFix is False) \
                        and (disp_obj.yFree is False) \
                        and (disp_obj.yDisplacement != 0):
                    dofs_count += 1
                    dofs_numbers += " 2"
                    val_value += " {0}".format(disp_obj.yDisplacement)
                if (disp_obj.zFix is True) \
                        and (disp_obj.zFree is False) \
                        and (disp_obj.zDisplacement == 0.0):
                    dofs_count += 1
                    dofs_numbers += " 3"
                    val_value += " 0"
                elif (disp_obj.zFix is False) \
                        and (disp_obj.zFree is False) \
                        and (disp_obj.zDisplacement != 0):
                    dofs_count += 1
                    dofs_numbers += " 3"
                    val_value += " {0}".format(disp_obj.zDisplacement)
            # delete leading spaces and create lines
            dofs_numbers = dofs_numbers.lstrip()
            val_value = val_value.lstrip()
            line_dofs = "dofs {0} {1}".format(dofs_count, dofs_numbers)
            line_values = "values {0} {1}".format(dofs_count, val_value)

            # set
            line_set = "set " + str(femobj["bc_number"] + self.cs_count)

            # build  and write line
            line_all = (
                line_begin + "  "
                + line_dofs + "  "
                + line_values + "  "
                + line_set + "\n"
            )
            f.write(line_all)

    def write_nodal_load_record(self, f):
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# Nodal Load Record\n")
            f.write("#\n")
        f.write("NodalLoad 3 loadTimeFunction 1 dofs 2 1 2 components 2 2.5 0.0 set 3\n")

    def write_time_function_record(self, f):
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# Time Function Record\n")
            f.write("#\n")
        f.write("ConstantFunction 1 f(t) 1.0\n")

    def write_set_record(self, f):
        """ Set (num#) (in)
            [elements # (ia) ] [elementranges # (rl) ] [allElements]
            [nodes # (ia) ] [noderanges # (rl) ] [allNodes]
            [elementboundaries # (ia) ] [elementedges # (ia) ]
        """
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# Set Record\n")
            f.write("#\n")

        # cross section and mataerial set, set 1 is used
        # on mesh writing the elements are renumbered starting with 1
        # means the ele_count == max ele number
        ele_start = 1
        ele_end = self.ele_count
        line_cs_start = "Set {0}".format(self.cs_set_number)
        line_cs_range = "elementranges {" + "({0} {1})".format(ele_start, ele_end) + "}"
        f.write(line_cs_start + "  " + line_cs_range + "\n")

        # separator line
        if self.write_comments is True:
            f.write("#\n")

        # bc displacement constraints sets
        for femobj in self.displacement_objects:
            # femobj --> dict, FreeCAD document object is femobj["Object"]
            line_start = (
                "Set {0}  nodes {1}"
                .format((femobj["bc_number"] + self.cs_count), len(femobj["Nodes"]))
            )
            line_nodes = ""  # init
            for n in femobj["Nodes"]:
                line_nodes = line_nodes + str(n) + " "
            line_nodes = line_nodes.rstrip()  # remove white space at the end
            f.write(line_start + "  " + line_nodes + "\n")

        # one of the bc set lines is used for the node load set too

    def write_footer(self, f):
        if self.write_comments is True:
            f.write("#\n")
            f.write("#\n")
            f.write("# {}\n".format(67 * "*"))
            f.write("# End of Input File\n")
            f.write("#\n")


example_input_file = """2DPlaneStress.out
Patch test of PlaneStress2d elements -> pure compression
LinearStatic nsteps 1 nmodules 1
vtkxml tstep_all domain_all  primvars 1 1 vars 5 1 2 4 5 27 stype 2
domain 2dPlaneStress
OutputManager tstep_all dofman_all element_all
ndofman 8 nelem 5 ncrosssect 1 nmat 1 nbc 3 nic 0 nltf 1 nset 3
node 1 coords 3  0.0   0.0   0.0
node 2 coords 3  0.0   4.0   0.0
node 3 coords 3  2.0   2.0   0.0
node 4 coords 3  3.0   1.0   0.0
node 5 coords 3  8.0   0.8   0.0
node 6 coords 3  7.0   3.0   0.0
node 7 coords 3  9.0   0.0   0.0
node 8 coords 3  9.0   4.0   0.0
PlaneStress2d 1 nodes 4 1 4 3 2  NIP 1
PlaneStress2d 2 nodes 4 1 7 5 4  NIP 1
PlaneStress2d 3 nodes 4 4 5 6 3  NIP 1
PlaneStress2d 4 nodes 4 3 6 8 2  NIP 1
PlaneStress2d 5 nodes 4 5 7 8 6  NIP 1
Set 1 elementranges {(1 5)}
Set 2 nodes 2 1 2
Set 3 nodes 2 7 8
SimpleCS 1 thick 1.0 width 1.0 material 1 set 1
IsoLE 1 d 0. E 15.0 n 0.25 talpha 1.0
BoundaryCondition 1 loadTimeFunction 1 dofs 2 1 2 values 1 0.0 set 2
BoundaryCondition 2 loadTimeFunction 1 dofs 1 2 values 1 0.0 set 3
NodalLoad 3 loadTimeFunction 1 dofs 2 1 2 components 2 2.5 0.0 set 3
ConstantFunction 1 f(t) 1.0
"""

##  @}
