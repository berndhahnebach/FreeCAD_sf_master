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

__title__ = "FreeCAD FEM material Elmer freetextinput task panel for the document object"
__author__ = "Bernd Hahnebach"
__url__ = "http://www.freecadweb.org"

## @package task_material_Elmer_freetextinput 
#  \ingroup FEM
#  \brief task panel for Elmer freetextinput material object

import sys
from PySide import QtCore
from PySide import QtGui

import FreeCAD
import FreeCADGui

from femguiutils import selection_widgets


class _TaskPanel:
    """
    The editmode TaskPanel for Elmer freetextinput  objects
    """

    def __init__(self, obj):

        self.obj = obj

        # parameter widget
        self.parameterWidget = FreeCADGui.PySideUic.loadUi(
            FreeCAD.getHomePath() + "Mod/Fem/Resources/ui/MaterialElmerFreetextinput.ui"
        )
        QtCore.QObject.connect(
            self.parameterWidget.plainTextEdit_elmer_freetextinput,
            QtCore.SIGNAL("textChanged()"),
            self.elmer_freetextinput_changed
        )
        self.init_parameter_widget()

        # geometry selection widget
        # start with Solid in list!
        self.selectionWidget = selection_widgets.GeometryElementsSelection(
            obj.References,
            ["Solid", "Face", "Edge", "Vertex"]
        )

        # form made from param and selection widget
        self.form = [self.parameterWidget, self.selectionWidget]

    def accept(self):
        self.obj.ElmerFreetextinput = self.parameterWidget.plainTextEdit_elmer_freetextinput.toPlainText()
        self.obj.References = self.selectionWidget.references
        self.recompute_and_set_back_all()
        return True

    def reject(self):
        self.recompute_and_set_back_all()
        return True

    def recompute_and_set_back_all(self):
        doc = FreeCADGui.getDocument(self.obj.Document)
        doc.Document.recompute()
        self.selectionWidget.setback_listobj_visibility()
        if self.selectionWidget.sel_server:
            FreeCADGui.Selection.removeObserver(self.selectionWidget.sel_server)
        doc.resetEdit()

    def init_parameter_widget(self):
        self.parameterWidget.plainTextEdit_elmer_freetextinput.insertPlainText(self.obj.ElmerFreetextinput)
	

    def elmer_freetextinput_changed(self):
        self.obj.ElmerFreetextinput = self.parameterWidget.plainTextEdit_elmer_freetextinput.toPlainText()


