# created by Python
'''
from femtest.app.support_utils import get_fem_test_defs
get_fem_test_defs()


'''

# modules
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_ccxtools
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_common
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_femimport
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_material
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_object
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_open
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_problems
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_result
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_elmer
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_z88
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solverframework
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools


# classes
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_ccxtools.TestCcxTools
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_common.TestFemCommon
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_femimport.TestFemImport
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_femimport.TestObjectExistance
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_material.TestMaterialUnits
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshCommon
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshEleTetra10
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshGroups
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_object.TestObjectCreate
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_object.TestObjectType
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_open.TestObjectOpen
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_problems.TestCantileverEndLoad
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_problems.TestCantileverUniformLoad
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_result.TestResult
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_elmer.TestSolverElmer
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_z88.TestSolverZ88
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solverframework.TestSolverFrameWork
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestCreateObject
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestFindAnalysisOfMember
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetMember
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestIsDerivedFrom
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetSingleMember
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetSeveralMember
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetMeshToSolve
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestTypeOfObj
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestIsOfType
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetBoundBoxOfAllDocumentShapes
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetRefshapeType
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestPydecode


# methods
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_ccxtools.TestCcxTools.test_box_frequency
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_ccxtools.TestCcxTools.test_box_static
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_ccxtools.TestCcxTools.test_thermomech_flow1D
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_ccxtools.TestCcxTools.test_thermomech_spine
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_common.TestFemCommon.test_adding_refshaps
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_common.TestFemCommon.test_pyimport_all_FEM_modules
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_femimport.TestFemImport.test_import_fem
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_femimport.TestObjectExistance.test_objects_existance
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_material.TestMaterialUnits.test_known_quantity_units
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_material.TestMaterialUnits.test_material_card_quantities
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshCommon.test_mesh_seg2_python
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshCommon.test_mesh_seg3_python
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshCommon.test_unv_save_load
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshCommon.test_writeAbaqus_precision
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshEleTetra10.test_tetra10_create
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshEleTetra10.test_tetra10_inp
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshEleTetra10.test_tetra10_unv
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshEleTetra10.test_tetra10_vkt
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshEleTetra10.test_tetra10_yml
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshEleTetra10.test_tetra10_z88
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshGroups.test_add_groups
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshGroups.test_delete_groups
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_mesh.TestMeshGroups.test_add_group_elements
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_object.TestObjectCreate.test_femobjects_make
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_object.TestObjectType.test_femobjects_type
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_object.TestObjectType.test_femobjects_isoftype
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_object.TestObjectType.test_femobjects_derivedfromfem
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_object.TestObjectType.test_femobjects_derivedfromstd
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_open.TestObjectOpen.test_femobjects_open_head
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_open.TestObjectOpen.test_femobjects_open_de9b3fb438
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_problems.TestCantileverEndLoad.testWithElmer
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_problems.TestCantileverEndLoad.testWithCcx
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_problems.TestCantileverUniformLoad.testWithElmer
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_problems.TestCantileverUniformLoad.testWithCcx
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_result.TestResult.test_read_frd_massflow_networkpressure
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_result.TestResult.test_stress_von_mises
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_result.TestResult.test_stress_principal_std
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_result.TestResult.test_stress_principal_reinforced
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_result.TestResult.test_rho
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_result.TestResult.test_disp_abs
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_box_frequency
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_box_static
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_ccxcantilever_faceload
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_ccxcantilever_hexa20
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_ccxcantilever_nodeload
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_ccxcantilever_prescribeddisplacement
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_constraint_contact_shell_shell
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_constraint_contact_solid_solid
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_constraint_sectionprint
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_constraint_selfweight_cantilever
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_constraint_tie
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_material_multiple_bendingbeam_fiveboxes
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_material_multiple_bendingbeam_fivefaces
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_material_multiple_tensionrod_twoboxes
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_material_nonlinear
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_square_pipe_end_twisted_edgeforces
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_square_pipe_end_twisted_nodeforces
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_thermomech_bimetall
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_thermomech_flow1D
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_calculix.TestSolverCalculix.test_thermomech_spine
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_elmer.TestSolverElmer.test_box_static_0_mm
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_elmer.TestSolverElmer.test_ccxcantilever_faceload_0_mm
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_elmer.TestSolverElmer.test_ccxcantilever_faceload_1_si
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_elmer.TestSolverElmer.test_ccxcantilever_nodeload_0_mm
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_elmer.TestSolverElmer.test_ccxcantilever_prescribeddisplacement_0_mm
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_z88.TestSolverZ88.test_ccxcantilever_faceload
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_z88.TestSolverZ88.test_ccxcantilever_hexa20
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solver_z88.TestSolverZ88.test_ccxcantilever_nodeload
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solverframework.TestSolverFrameWork.test_solver_calculix
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_solverframework.TestSolverFrameWork.test_solver_elmer
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestCreateObject.testSimpleCreateObject
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestCreateObject.testNameConflictOnCreation
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestCreateObject.testAutomaticNameGeneration
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestCreateObject.testDocArgumentNone
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestCreateObject.testNameArgumentNone
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestCreateObject.testProxyArgumentNone
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestFindAnalysisOfMember.testMemberInFirstAnalysis
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestFindAnalysisOfMember.testMemberInLastAnalysis
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestFindAnalysisOfMember.testMemberInOnlyAnalysis
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestFindAnalysisOfMember.testMemberInNoAnalysis
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestFindAnalysisOfMember.testMemberInGroup
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetMember.testEmptyAnalysis
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetMember.testFemTypesystem
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetMember.testFCTypesystem
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetMember.testFCTypesystemWithInheritance
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetMember.testWithMultipleAnalysisObjects
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestIsDerivedFrom.testFemTypesystemObject
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestIsDerivedFrom.testFCTypesystemObject
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestIsDerivedFrom.testInvalidTypes
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetSingleMember.testWithNoMatch
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetSingleMember.testWithSingleMatch
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetSingleMember.testWithMultipleMatches
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetSeveralMember.testWithEmptyAnalysis
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetSeveralMember.testWithoutMatch
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetSeveralMember.testVertexSubtype
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetMeshToSolve.testWithEmptyAnalysis
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetMeshToSolve.testWithoutMesh
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetMeshToSolve.testMultipleMeshes
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetMeshToSolve.testSingleMesh
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestTypeOfObj.testFemTypesystem
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestTypeOfObj.testFCTypesystem
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestIsOfType.testFemTypesystem
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestIsOfType.testFCTypesystem
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetBoundBoxOfAllDocumentShapes.testEmptyDocument
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetBoundBoxOfAllDocumentShapes.testSingleShape
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetBoundBoxOfAllDocumentShapes.testMultipleShapes
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetRefshapeType.testVertexSubtype
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetRefshapeType.testEdgeSubtype
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetRefshapeType.testFaceSubtype
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestGetRefshapeType.testSolidSubtype
make -j 4 && ./bin/FreeCADCmd -t femtest.app.test_tools.TestPydecode.testConvertString


# methods in FreeCAD

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_ccxtools.TestCcxTools.test_box_frequency'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_ccxtools.TestCcxTools.test_box_static'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_ccxtools.TestCcxTools.test_thermomech_flow1D'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_ccxtools.TestCcxTools.test_thermomech_spine'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_common.TestFemCommon.test_adding_refshaps'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_common.TestFemCommon.test_pyimport_all_FEM_modules'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_femimport.TestFemImport.test_import_fem'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_femimport.TestObjectExistance.test_objects_existance'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_material.TestMaterialUnits.test_known_quantity_units'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_material.TestMaterialUnits.test_material_card_quantities'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshCommon.test_mesh_seg2_python'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshCommon.test_mesh_seg3_python'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshCommon.test_unv_save_load'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshCommon.test_writeAbaqus_precision'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshEleTetra10.test_tetra10_create'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshEleTetra10.test_tetra10_inp'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshEleTetra10.test_tetra10_unv'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshEleTetra10.test_tetra10_vkt'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshEleTetra10.test_tetra10_yml'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshEleTetra10.test_tetra10_z88'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshGroups.test_add_groups'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshGroups.test_delete_groups'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_mesh.TestMeshGroups.test_add_group_elements'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_object.TestObjectCreate.test_femobjects_make'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_object.TestObjectType.test_femobjects_type'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_object.TestObjectType.test_femobjects_isoftype'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_object.TestObjectType.test_femobjects_derivedfromfem'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_object.TestObjectType.test_femobjects_derivedfromstd'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_open.TestObjectOpen.test_femobjects_open_head'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_open.TestObjectOpen.test_femobjects_open_de9b3fb438'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_problems.TestCantileverEndLoad.testWithElmer'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_problems.TestCantileverEndLoad.testWithCcx'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_problems.TestCantileverUniformLoad.testWithElmer'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_problems.TestCantileverUniformLoad.testWithCcx'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_result.TestResult.test_read_frd_massflow_networkpressure'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_result.TestResult.test_stress_von_mises'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_result.TestResult.test_stress_principal_std'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_result.TestResult.test_stress_principal_reinforced'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_result.TestResult.test_rho'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_result.TestResult.test_disp_abs'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_box_frequency'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_box_static'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_ccxcantilever_faceload'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_ccxcantilever_hexa20'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_ccxcantilever_nodeload'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_ccxcantilever_prescribeddisplacement'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_constraint_contact_shell_shell'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_constraint_contact_solid_solid'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_constraint_sectionprint'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_constraint_selfweight_cantilever'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_constraint_tie'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_material_multiple_bendingbeam_fiveboxes'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_material_multiple_bendingbeam_fivefaces'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_material_multiple_tensionrod_twoboxes'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_material_nonlinear'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_square_pipe_end_twisted_edgeforces'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_square_pipe_end_twisted_nodeforces'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_thermomech_bimetall'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_thermomech_flow1D'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_calculix.TestSolverCalculix.test_thermomech_spine'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_elmer.TestSolverElmer.test_box_static_0_mm'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_elmer.TestSolverElmer.test_ccxcantilever_faceload_0_mm'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_elmer.TestSolverElmer.test_ccxcantilever_faceload_1_si'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_elmer.TestSolverElmer.test_ccxcantilever_nodeload_0_mm'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_elmer.TestSolverElmer.test_ccxcantilever_prescribeddisplacement_0_mm'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_z88.TestSolverZ88.test_ccxcantilever_faceload'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_z88.TestSolverZ88.test_ccxcantilever_hexa20'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_solver_z88.TestSolverZ88.test_ccxcantilever_nodeload'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestCreateObject.testSimpleCreateObject'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestCreateObject.testNameConflictOnCreation'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestCreateObject.testAutomaticNameGeneration'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestCreateObject.testDocArgumentNone'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestCreateObject.testNameArgumentNone'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestCreateObject.testProxyArgumentNone'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestFindAnalysisOfMember.testMemberInFirstAnalysis'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestFindAnalysisOfMember.testMemberInLastAnalysis'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestFindAnalysisOfMember.testMemberInOnlyAnalysis'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestFindAnalysisOfMember.testMemberInNoAnalysis'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestFindAnalysisOfMember.testMemberInGroup'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetMember.testEmptyAnalysis'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetMember.testFemTypesystem'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetMember.testFCTypesystem'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetMember.testFCTypesystemWithInheritance'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetMember.testWithMultipleAnalysisObjects'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestIsDerivedFrom.testFemTypesystemObject'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestIsDerivedFrom.testFCTypesystemObject'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestIsDerivedFrom.testInvalidTypes'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetSingleMember.testWithNoMatch'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetSingleMember.testWithSingleMatch'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetSingleMember.testWithMultipleMatches'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetSeveralMember.testWithEmptyAnalysis'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetSeveralMember.testWithoutMatch'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetSeveralMember.testVertexSubtype'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetMeshToSolve.testWithEmptyAnalysis'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetMeshToSolve.testWithoutMesh'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetMeshToSolve.testMultipleMeshes'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetMeshToSolve.testSingleMesh'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestTypeOfObj.testFemTypesystem'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestTypeOfObj.testFCTypesystem'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestIsOfType.testFemTypesystem'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestIsOfType.testFCTypesystem'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetBoundBoxOfAllDocumentShapes.testEmptyDocument'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetBoundBoxOfAllDocumentShapes.testSingleShape'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetBoundBoxOfAllDocumentShapes.testMultipleShapes'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetRefshapeType.testVertexSubtype'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetRefshapeType.testEdgeSubtype'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetRefshapeType.testFaceSubtype'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestGetRefshapeType.testSolidSubtype'
))

import unittest
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName(
    'femtest.app.test_tools.TestPydecode.testConvertString'
))
