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

__title__ = "importBlockMeshDict"
__author__ = "Bernd Hahnebach"
__url__ = "http://www.freecadweb.org"

## @package importBlockMeshDict
#  \ingroup FEM
#  \brief FreeCAD blockMeshDict reader for FEM workbench

import FreeCAD
import os


########## generic FreeCAD import and export methods ##########
if open.__module__ == '__builtin__':
    # because we'll redefine open below (Python2)
    pyopen = open
elif open.__module__ == 'io':
    # because we'll redefine open below (Python3)
    pyopen = open


def open(filename):
    "called when freecad opens a file"
    docname = os.path.splitext(os.path.basename(filename))[0]
    insert(filename, docname)


def insert(filename, docname):
    "called when freecad wants to import a file"
    try:
        doc = FreeCAD.getDocument(docname)
    except NameError:
        doc = FreeCAD.newDocument(docname)
    FreeCAD.ActiveDocument = doc
    vertices_from_file = importBlockMeshDict(filename)

    # display the point and labels by the use of draft module
    import Draft
    for vertexNum, vertex in enumerate(vertices_from_file):
        p = Draft.makePoint(vertex[0], vertex[1], vertex[2])
        p.Label = str(vertexNum)
        Draft.makeText([str(vertexNum)], point=FreeCAD.Vector(vertex[0], vertex[1], vertex[2]))


########## module specific methods ##########
def importBlockMeshDict(filename, Analysis=None):
    in_vertices = readBlockMeshDict(filename)
    return in_vertices


# read a CFD blockMeshDict file and extract the data
def readBlockMeshDict(dat_input):
    dat_file = pyopen(dat_input, "r")

    # read file contents into one string
    data = dat_file.read().replace('\n', '')
    # print(data)

    import re
    # clean up the C/C++ comments
    re.sub('//.*?(\r\n?|\n)|/\*.*?\*/', '', data, flags=re.S)
    # extract the vertices into a list of tuples
    r1 = re.search(r'vertices\s*\(\s*(.*)\s*\)', data, re.DOTALL)
    vertices = [(float(v[0]), float(v[1]), float(v[2])) for v in re.findall(r'\(\s*([-0-9.]+)\s+([-0-9.]+)\s+([-0-9.]+)\s*\)', r1.group(1))]

    dat_file.close()
    return vertices
