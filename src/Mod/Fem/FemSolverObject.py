# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2017 - Markus Hovorka <m.hovorka@live.de>               *
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


__title__ = "Elmer Solver Object"
__author__ = "Markus Hovorka"
__url__ = "http://www.freecadweb.org"


import FreeCAD as App
import FemRun

if App.GuiUp:
    import FreeCADGui as Gui
    import PyGui._TaskPanelFemSolverControl


class Proxy(object):

    BaseType = "Fem::FemSolverObjectPython"

    def __init__(self, obj):
        obj.Proxy = self
        obj.addExtension("App::GroupExtensionPython", self)

    def createMachine(self, obj, directory):
        raise NotImplementedError()

    def createEquation(self, obj, eqId):
        raise NotImplementedError()

    def isSupported(self, equation):
        raise NotImplementedError()

    def addEquation(self, obj, eqId):
        obj.addObject(self.createEquation(
            obj.Document, eqId))

    def editSupported(self):
        return False

    def edit(self, directory):
        raise NotImplementedError()

    def execute(self, obj):
        return True


class ViewProxy(object):
    """Proxy for FemSolverElmers View Provider."""

    def __init__(self, vobj):
        vobj.Proxy = self
        vobj.addExtension("Gui::ViewProviderGroupExtensionPython", self)

    def setEdit(self, vobj, mode=0):
        machine = FemRun.getMachine(vobj.Object)
        task = PyGui._TaskPanelFemSolverControl.ControlTaskPanel(machine)
        Gui.Control.showDialog(task)
        return True

    def unsetEdit(self, vobj, mode=0):
        Gui.Control.closeDialog()

    def doubleClicked(self, vobj):
        if Gui.Control.activeDialog():
            Gui.Control.closeDialog()
        Gui.ActiveDocument.setEdit(vobj.Object.Name)
        return True

    def attach(self, vobj):
        pass
