# ***************************************************************************
# *   Copyright (c) 2021 Bernd Hahnebach <bernd@bimstatik.org>              *
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

__title__ = "Mystran build model"
__author__ = "Bernd Hahnebach"
__url__ = "http://www.freecadweb.org"

## \addtogroup FEM
#  @{


def build_model(f, model):

    # write the pyNastran code which will be executed into the file
    f.write(plate_pynas_code)

    # print(model)
    # print(model.get_bdf_stats())
    exec(plate_pynas_code)
    # print(model)
    # print(model.get_bdf_stats())

    return model


plate_pynas_code = """
from pyNastran.bdf.bdf import CaseControlDeck


# mat1 card, material properties for linear isotropic material
mat = model.add_mat1(mid=1, E=210000.0, G=None, nu=0.3)


# grid cards, geometric mesh points
model.add_grid(1, [0., 0., 0.])
model.add_grid(2, [2., 0., 0.])
model.add_grid(3, [4., 0., 0.])
model.add_grid(4, [6., 0., 0.])
model.add_grid(5, [8., 0., 0.])
model.add_grid(6, [10., 0., 0.])
model.add_grid(7, [0., 2., 0.])
model.add_grid(8, [2., 2., 0.])
model.add_grid(9, [4., 2., 0.])
model.add_grid(10, [6., 2., 0.])
model.add_grid(11, [8., 2., 0.])
model.add_grid(12, [10., 2., 0.])
model.add_grid(13, [0., 4., 0.])
model.add_grid(14, [2., 4., 0.])
model.add_grid(15, [4., 4., 0.])
model.add_grid(16, [6., 4., 0.])
model.add_grid(17, [8., 4., 0.])
model.add_grid(18, [10., 4., 0.])
model.add_grid(19, [0., 6., 0.])
model.add_grid(20, [2., 6., 0.])
model.add_grid(21, [4., 6., 0.])
model.add_grid(22, [6., 6., 0.])
model.add_grid(23, [8., 6., 0.])
model.add_grid(24, [10., 6., 0.])
model.add_grid(25, [0., 8., 0.])
model.add_grid(26, [2., 8., 0.])
model.add_grid(27, [4., 8., 0.])
model.add_grid(28, [6., 8., 0.])
model.add_grid(29, [8., 8., 0.])
model.add_grid(30, [10., 8., 0.])
model.add_grid(31, [0., 10., 0.])
model.add_grid(32, [2., 10., 0.])
model.add_grid(33, [4., 10., 0.])
model.add_grid(34, [6., 10., 0.])
model.add_grid(35, [8., 10., 0.])
model.add_grid(36, [10., 10., 0.])


# cquad4 cards, isoparametric quadrilateral plate element
model.add_cquad4(1, 1, [1, 2, 8, 7])
model.add_cquad4(2, 1, [2, 3, 9, 8])
model.add_cquad4(3, 1, [3, 4, 10, 9])
model.add_cquad4(4, 1, [4, 5, 11, 10])
model.add_cquad4(5, 1, [5, 6, 12, 11])
model.add_cquad4(6, 1, [7, 8, 14, 13])
model.add_cquad4(7, 1, [8, 9, 15, 14])
model.add_cquad4(8, 1, [9, 10, 16, 15])
model.add_cquad4(9, 1, [10, 11, 17, 16])
model.add_cquad4(10, 1, [11, 12, 18, 17])
model.add_cquad4(11, 1, [13, 14, 20, 19])
model.add_cquad4(12, 1, [14, 15, 21, 20])
model.add_cquad4(13, 1, [15, 16, 22, 21])
model.add_cquad4(14, 1, [16, 17, 23, 22])
model.add_cquad4(15, 1, [17, 18, 24, 23])
model.add_cquad4(16, 1, [19, 20, 26, 25])
model.add_cquad4(17, 1, [20, 21, 27, 26])
model.add_cquad4(18, 1, [21, 22, 28, 27])
model.add_cquad4(19, 1, [22, 23, 29, 28])
model.add_cquad4(20, 1, [23, 24, 30, 29])
model.add_cquad4(21, 1, [25, 26, 32, 31])
model.add_cquad4(22, 1, [26, 27, 33, 32])
model.add_cquad4(23, 1, [27, 28, 34, 33])
model.add_cquad4(24, 1, [28, 29, 35, 34])
model.add_cquad4(25, 1, [29, 30, 36, 35])


# pshell card, thin shell element properties
model.add_pshell(1, mid1=1, t=0.3, mid2=1, mid3=1)


# force cards, mesh node loads
model.add_force(sid=1, node=6, mag=100, xyz=(1.0, 0.0, 0.0))
model.add_force(sid=1, node=12, mag=100, xyz=(1.0, 0.0, 0.0))
model.add_force(sid=1, node=18, mag=100, xyz=(1.0, 0.0, 0.0))
model.add_force(sid=1, node=24, mag=100, xyz=(1.0, 0.0, 0.0))
model.add_force(sid=1, node=30, mag=100, xyz=(1.0, 0.0, 0.0))
model.add_force(sid=1, node=36, mag=100, xyz=(1.0, 0.0, 0.0))


# load card, static load combinations
model.add_load(sid=2, scale=1.0, scale_factors=1.0, load_ids=1)


# spc1 card, Defines a set of single-point constraints
fixed_nodes = [1, 7, 13, 19, 25, 31]
model.add_spc1(conid=1, components="123456", nodes=fixed_nodes)


# spcadd card, Single-Point Constraint Set Combination from SPC or SPC1 cards
model.add_spcadd(conid=2, sets=[1],)


# executive control
model.sol = 101


# params cards
model.add_param(key="POST", values=-1)
model.add_param(key="PRTMAXIM", values="YES")


# case control
cc = CaseControlDeck([
    "ECHO = NONE",
    "TITLE = pyNastran plate example for Mystran",
    "SUBCASE 1",
    "  SUBTITLE = Default",
    "  LOAD = 2",
    "  SPC = 2",
    "  SPCFORCES(SORT1,REAL) = ALL",
    "  STRESS(SORT1,REAL,VONMISES,BILIN) = ALL",
    "  DISPLACEMENT(SORT1,REAL) = ALL",
])
model.case_control_deck = cc
# model.validate()  # creates an error
"""


##  @}
