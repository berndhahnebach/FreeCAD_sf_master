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

__title__ = "FreeCAD FEM material Elmer freetextinput ViewProvider for the document object"
__author__ = "Bernd Hahnebach"
__url__ = "http://www.freecadweb.org"

## @package view_material_elmer_freetextinput
#  \ingroup FEM
#  \brief view provider for elmer freetextinput material object

from femtaskpanels import task_material_elmer_freetextinput
from . import view_base_femconstraint


class VPMaterialElmerFreetextinput(view_base_femconstraint.VPBaseFemConstraint):
    """
    A View Provider for the MaterialElmerFreetextinput object
    """

    def setEdit(self, vobj, mode=0):
        view_base_femconstraint.VPBaseFemConstraint.setEdit(
            self,
            vobj,
            mode,
            task_material_elmer_freetextinput._TaskPanel
        )

    def getIcon(self):
        return ":/icons/FEM_MaterialElmerFreetextinput.svg"
