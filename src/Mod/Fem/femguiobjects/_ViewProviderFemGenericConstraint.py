# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2018 qingfeng Xia <qingfeng.xia@gmail.coom>             *
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

__title__ = "FreeCAD FEM generic constraint ViewProvider"
__author__ = "JBernd Hahnebach, Qingfeng Xia"
__url__ = "http://www.freecadweb.org"

## @package ViewProviderFemBodySource
#  \ingroup FEM
#  \brief FreeCAD FEM view provider for constraint initial flow velocity object

import FreeCAD
# from FreeCAD import Units
import FreeCADGui
from . import ViewProviderFemConstraint

# for the panel
from . import FemSelectionWidgets
from .ConstraintInputWidget import ConstraintInputWidget


class _ViewProvider(ViewProviderFemConstraint.ViewProxy):

    def __init__(self, vobj):
        vobj.Proxy = self
        self.obj = vobj.Object  # needed in getIcon()

    def getIcon(self):
        # todo: dynamically generate icon by overlaying physical field symbol
        if "Category" in self.obj.PropertiesList:
            if self.obj.Category == "Source":
                return ":/icons/fem-add-body-source"
            elif self.obj.Category == "InitialValue":
                return ":/icons/fem-add-initial-value"
            else:
                return ":/icons/fem-add-initial-value"  # todo: fem-generic-constraint
        else:
            FreeCAD.Console.Error("Document object does not have Category property")
            return ":/icons/fem-add-initial-value"  # todo: fem-generic-constraint

    def setEdit(self, vobj, mode=0):
        # hide all meshes
        for o in FreeCAD.ActiveDocument.Objects:
            if o.isDerivedFrom("Fem::FemMeshObject"):
                o.ViewObject.hide()
        # show task panel
        task = _TaskPanel(vobj.Object)
        FreeCADGui.Control.showDialog(task)
        return True

    def unsetEdit(self, vobj, mode=0):
        FreeCADGui.Control.closeDialog()
        return True

    def __getstate__(self):
        return None

    def __setstate__(self,state):
        return None


class _TaskPanel:
    """The editmode TaskPanel for generic constraint objects (FemBodySource and FemInitialValue)"""

    def __init__(self, obj):
        self.obj = obj

        self.ConstraintSettings = self.obj.Settings
        if "Category" in self.obj.PropertiesList:
            if self.obj.Category == "Source":
                self.ConstraintSettings["Category"] = "Source"
            elif self.obj.Category == "InitialValue":
                self.ConstraintSettings["Category"] = "InitialValue"
            else:
                self.ConstraintSettings["Category"] = "Constraint"
        else:
            FreeCAD.Console.Error("Document object does not have Category property")
            self.ConstraintSettings["Category"] = "Constraint"

        self.ConstraintSettings["ShapeType"] = self.obj.ShapeType
        # shapeTypes = [self.obj.ShapeType]
        shapeTypes = ["Solid", "Face", "Edge", "Vertext"]   # start with Solid in list!

        self.parameterWidget = ConstraintInputWidget(self.ConstraintSettings)
        # geometry selection widget,  if only solid will be select, using SolidSelector()
        self.selectionWidget = FemSelectionWidgets.GeometryElementsSelection(
            obj.References, shapeTypes, False
        )

        # form made from param and selection widget
        self.form = [self.parameterWidget, self.selectionWidget]

        # check references, has to be after initialisation of selectionWidget
        self.selectionWidget.has_equal_references_shape_types()

    # ********* leave task panel *********
    def accept(self):
        # print(self.material)
        if self.selectionWidget.has_equal_references_shape_types():

            self.obj.Settings = self.parameterWidget.constraintSettings()
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
