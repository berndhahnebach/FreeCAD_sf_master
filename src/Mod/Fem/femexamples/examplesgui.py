# ***************************************************************************
# *   Copyright (c) 2020 Bernd Hahnebach <bernd@bimstatik.org>              *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with FreeCAD; if not, write to the Free Software        *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

import os

from PySide import QtCore
from PySide import QtGui

import FreeCADGui


class FemExamples(QtGui.QWidget):
    def __init__(self):
        super(FemExamples, self).__init__()
        self.init_ui()

    def __del__(self,):
        # need as fix for qt event error
        # --> see http://forum.freecadweb.org/viewtopic.php?f=18&t=10732&start=10#p86493
        return

    def init_ui(self):

        # Title
        self.macrotitle_label = QtGui.QLabel("<b>FEM Examples</b>", self)

        # init widgets
        self.view = QtGui.QTreeWidget()

        path = os.path.dirname(os.path.realpath(__file__))
        meshes_path = str(path) + "/meshes"
        files = [f for f in os.listdir(str(path))]
        not_files = [
            "examplesgui.py",
            "manager.py",
            "meshes",
            "__init__.py",
            "__pycache__",
        ]

        files = [str(f) for f in files if f not in not_files]
        files.sort()

        all_examples = QtGui.QTreeWidgetItem(self.view, ["All"])
        for f in files:
            if f.endswith(".py"):
                QtGui.QTreeWidgetItem(all_examples, [f[:-3]])

        self.view.addTopLevelItem(all_examples)

        meshes_files = [f for f in os.listdir(str(meshes_path))]
        meshes_files = [str(f) for f in meshes_files if f not in not_files]
        meshes_files.sort()

        all_meshes = QtGui.QTreeWidgetItem(self.view, ["Meshes"])
        for f in meshes_files:
            if f.endswith(".py"):
                QtGui.QTreeWidgetItem(all_meshes, [f[:-3]])

        self.view.addTopLevelItem(all_meshes)
        self.view.setHeaderHidden(True)

        # Ok buttons:
        self.ok_button = QtGui.QDialogButtonBox(self)
        self.ok_button.setOrientation(QtCore.Qt.Horizontal)
        self.ok_button.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok
        )

        # Layout:
        layout = QtGui.QGridLayout()
        layout.addWidget(self.macrotitle_label, 1, 0, 1, 2)
        layout.addWidget(self.view, 2, 0, 1, 2)
        layout.addWidget(self.ok_button, 3, 1)
        self.setLayout(layout)

        # Connectors:
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL("accepted()"), self.accept)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL("rejected()"), self.reject)

    def accept(self):
        print("\nExample will be run.")
        item = self.view.selectedItems()[0]
        example = item.text(0)
        # if done this way the Python commands are printed in Python console
        FreeCADGui.doCommand("from femexamples." + str(example) + "  import setup")
        FreeCADGui.doCommand("setup()")

    def reject(self):
        print("\nWe close the widget.")
        self.close()
        d.close()


def show_examplegui():
    mw = FreeCADGui.getMainWindow()
    d = QtGui.QDockWidget()
    d.setWidget(FemExamples())
    mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, d)
