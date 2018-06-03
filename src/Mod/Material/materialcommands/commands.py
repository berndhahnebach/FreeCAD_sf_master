# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2018 - Bernd Hahnebach <bernd@bimstatik.org>            *
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


import FreeCAD
import FreeCADGui
from PySide import QtCore


# Python command definitions

class _CommandMaterialEditor():
    "The Material_MaterialEditor command definition"
    def IsActive(self):
        return True

    def GetResources(self):
        res = {'Pixmap': 'Arch_Material_Group',
               'MenuText': QtCore.QT_TRANSLATE_NOOP("Material Editor", "opens the FreeCAD material editor"),
               # 'Accel': "Z, Z",
               'ToolTip': QtCore.QT_TRANSLATE_NOOP("Material Editor", "opens the FreeCAD material editor")}
        return res

        # self.is_active = 'allways'

    def Activated(self):
        FreeCADGui.addModule("MaterialEditor")
        FreeCADGui.doCommand("MaterialEditor.openEditor()")


# the string in add command will be the page name on FreeCAD wiki
FreeCADGui.addCommand('Material_MaterialEditor', _CommandMaterialEditor())
