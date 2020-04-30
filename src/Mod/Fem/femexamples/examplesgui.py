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

import FreeCAD
import FreeCADGui


class FemExamples(QtGui.QWidget):
    def __init__(self):
        super(FemExamples, self).__init__()
        self.init_ui()

    def __del__(
        self,
    ):  # need as fix for qt event error --> see http://forum.freecadweb.org/viewtopic.php?f=18&t=10732&start=10#p86493
        return

    def init_ui(self):

        # Title
        self.macrotitle_label = QtGui.QLabel("<b> FEM examples <b>", self)

        # Dimension
        self.label1 = QtGui.QLabel("Here should be some QtTreeWidget or similar.", self)
        self.label2 = QtGui.QLabel(
            "At the moment a contact example will be run on ok.", self
        )
        # init widgets
        self.view = QtGui.QTreeView()
        self.view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.model = QtGui.QStandardItemModel()
        # self.model.setHorizontalHeaderLabels(["col1", "col2", "col3"])
        self.view.setModel(self.model)
        self.view.setUniformRowHeights(True)

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
        for f in files:
            for not_file in not_files:
                if str(f) == not_file:
                    files.remove(f)
        all_examples = QtGui.QStandardItem("All")
        for f in files:
            example = QtGui.QStandardItem(str(f))
            all_examples.appendRow(example)
        self.model.appendRow(all_examples)

        meshes_files = [f for f in os.listdir(str(meshes_path))]
        all_meshes = QtGui.QStandardItem("Meshes")
        for f in meshes_files:
            mesh = QtGui.QStandardItem(str(f))
            all_meshes.appendRow(mesh)
        self.model.appendRow(all_meshes)

        # span container columns
        # self.view.setFirstColumnSpanned(1, self.view.rootIndex(), True)

        # Ok buttons:
        self.ok_button = QtGui.QDialogButtonBox(self)
        self.ok_button.setOrientation(QtCore.Qt.Horizontal)
        self.ok_button.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok
        )

        # show widget elements
        self.macrotitle_label.show()

        # Layout:
        layout = QtGui.QGridLayout()
        # layout.addWidget(self.label1, 1, 0)
        # layout.addWidget(self.label2, 2, 0)
        layout.addWidget(self.view, 1, 0)
        layout.addWidget(self.ok_button, 2, 1)
        self.setLayout(layout)

        # Connectors:
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL("accepted()"), self.accept)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL("rejected()"), self.reject)

    def accept(self):
        print("\nExample will be run.")
        # if done this way the Python commands are printed in Python console
        FreeCADGui.doCommand(
            "from femexamples.constraint_contact_solid_solid import setup"
        )
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
