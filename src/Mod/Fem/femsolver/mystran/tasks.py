# ***************************************************************************
# *   Copyright (c) 2017 Bernd Hahnebach <bernd@bimstatik.org>              *
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

__title__ = "FreeCAD FEM solver Z88 tasks"
__author__ = "Bernd Hahnebach"
__url__ = "https://www.freecadweb.org"

## \addtogroup FEM
#  @{

import os
import os.path
import subprocess

import FreeCAD


try:
    import hfcMystranNeuIn
    result_reading = True
except Exception:
    FreeCAD.Console.PrintWarning("Module to read results not found.\n")
    result_reading = False


from . import writer
from .. import run
# from .. import settings
from femtools import femutils
from femtools import membertools


_inputFileName = None


class Check(run.Check):

    def run(self):
        self.pushStatus("Checking analysis...\n")
        # self.checkMesh()
        # self.checkMaterial()


class Prepare(run.Prepare):

    def run(self):
        global _inputFileName
        self.pushStatus("Preparing input files...\n")
        w = writer.FemInputWriterMystran(
            self.analysis,
            self.solver,
            None,
            membertools.AnalysisMember(self.analysis),
            self.directory
        )
        path = w.write_solver_input()
        # report to user if task succeeded
        if path is not None:
            self.pushStatus("Write completed!")
        else:
            self.pushStatus("Writing Mystran input files failed!")
        # print(path)
        _inputFileName = os.path.splitext(os.path.basename(path))[0]
        # print(_inputFileName)


class Solve(run.Solve):

    def run(self):
        # print(_inputFileName)
        if not _inputFileName:
            # TODO do not run solver, do not try to read results in a smarter way than an Exception
            raise Exception("Error on writing Mystran input file.\n")
        infile = _inputFileName + ".bdf"
        FreeCAD.Console.PrintMessage("Mystran: solver input file: {} \n\n".format(infile))

        self.pushStatus("Executing solver...\n")
        # binary = settings.get_binary("Mystran")
        # if something goes wrong the binary path could be set for debugging
        # binary = "C:/0_BHA_privat/progr/PortableMystran/MYSTRAN.exe"
        binary = "/home/hugo/Documents/dev/mystran/mystran_org/build/Binaries/mystran"

        """
        self._process = subprocess.Popen(
            [binary, "", infile],
            cwd=self.directory,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        self.signalAbort.add(self._process.terminate)
        self._process.communicate()
        self.signalAbort.remove(self._process.terminate)
        # for chatching the output see CalculiX or Elmer solver task module
        """

        process = subprocess.Popen([binary, infile], cwd=self.directory)
        # es wird nicht gewartet bis process fertig ist ...
        # HACK
        import time
        time.sleep(5)
        del process


class Results(run.Results):

    def run(self):
        prefs = FreeCAD.ParamGet(
            "User parameter:BaseApp/Preferences/Mod/Fem/General")
        if not prefs.GetBool("KeepResultsOnReRun", False):
            self.purge_results()
        if result_reading is True:
            self.load_results()  # ToDo in all solvers generischer name

    def purge_results(self):
        for m in membertools.get_member(self.analysis, "Fem::FemResultObject"):
            if femutils.is_of_type(m.Mesh, "Fem::MeshResult"):
                self.analysis.Document.removeObject(m.Mesh.Name)
            self.analysis.Document.removeObject(m.Name)
        self.analysis.Document.recompute()
        # deletes all results from any solver
        # TODO: delete only the mystran results, fix in all solver

    def load_results(self):
        self.pushStatus("Import results...\n")
        neu_result_file = os.path.join(self.directory, _inputFileName + ".NEU")
        if os.path.isfile(neu_result_file):
            hfcMystranNeuIn.import_neu(neu_result_file)
            # Workaround to move result object into analysis
            for o in self.analysis.Document.Objects:
                if o.Name == "Displacement0":
                    self.analysis.addObject(o)
                    break
        else:
            raise Exception(
                "FEM: No results found at {}!".format(neu_result_file))

##  @}
