/***************************************************************************
 *   Copyright (c) 2010 Werner Mayer <wmayer[at]users.sourceforge.net>     *
 *                                                                         *
 *   This file is part of the FreeCAD CAx development system.              *
 *                                                                         *
 *   This library is free software; you can redistribute it and/or         *
 *   modify it under the terms of the GNU Library General Public           *
 *   License as published by the Free Software Foundation; either          *
 *   version 2 of the License, or (at your option) any later version.      *
 *                                                                         *
 *   This library  is distributed in the hope that it will be useful,      *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU Library General Public License for more details.                  *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this library; see the file COPYING.LIB. If not,    *
 *   write to the Free Software Foundation, Inc., 59 Temple Place,         *
 *   Suite 330, Boston, MA  02111-1307, USA                                *
 *                                                                         *
 ***************************************************************************/


#include "PreCompiled.h"

#include <boost/any.hpp>

#include "App/Material.h"
#include "App/Application.h"
#include "App/MaterialDatabase.h"

// inclusion of the generated files (generated out of MaterialPy.xml)
#include "MaterialPy.h"
#include "MaterialPy.cpp"

using namespace App;

#if 0
// EK: FIXME
PyObject *MaterialPy::PyMake(struct _typeobject *, PyObject *, PyObject *)  // Python wrapper
{
    // create a new instance of MaterialPy and the Twin object
    return new MaterialPy(new Material);
}

// constructor method
int MaterialPy::PyInit(PyObject* args, PyObject* kwds)
{
    PyObject* diffuse = 0;
    PyObject* ambient = 0;
    PyObject* specular = 0;
    PyObject* emissive = 0;
    PyObject* shininess = 0;
    PyObject* transparency = 0;
    static char* kwds_colors[] = { "DiffuseColor", "AmbientColor", "SpecularColor", "EmissiveColor", "Shininess", "Transparency", NULL };

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOOOOO", kwds_colors,
        &diffuse, &ambient, &specular, &emissive, &shininess, &transparency))
        return -1;

    if (diffuse) {
        setDiffuseColor(Py::Tuple(diffuse));
    }

    if (ambient) {
        setAmbientColor(Py::Tuple(ambient));
    }

    if (specular) {
        setSpecularColor(Py::Tuple(specular));
    }

    if (emissive) {
        setEmissiveColor(Py::Tuple(emissive));
    }

    if (shininess) {
        setShininess(Py::Float(shininess));
    }

    if (transparency) {
        setTransparency(Py::Float(transparency));
    }

    return 0;
}

#endif

// returns a string which represents the object e.g. when printed in python
std::string MaterialPy::representation(void) const
{
    return std::string("<Material object>");
}

#if 0
PyObject* MaterialPy::set(PyObject * args)
{
    char *pstr;
    if (!PyArg_ParseTuple(args, "s", &pstr))     // convert args: Python->C
        return NULL;                             // NULL triggers exception

    getMaterialPtr()->set(pstr);

    Py_Return;
}

Py::Tuple MaterialPy::getAmbientColor(void) const
{
    Py::Tuple tuple(4);
    tuple.setItem(0, Py::Float(getMaterialPtr()->getAmbientColor().r));
    tuple.setItem(1, Py::Float(getMaterialPtr()->getAmbientColor().g));
    tuple.setItem(2, Py::Float(getMaterialPtr()->getAmbientColor().b));
    tuple.setItem(3, Py::Float(getMaterialPtr()->getAmbientColor().a));
    return tuple;
}

void MaterialPy::setAmbientColor(Py::Tuple arg)
{
  // EK: FIXME
}
#endif

PyObject *MaterialPy::getCustomAttributes(const char* attr) const
{
    return getMaterialPtr()->getPropertyAsPyObject(attr);
}

int MaterialPy::setCustomAttributes(const char* attr, PyObject* obj)
{
    getMaterialPtr()->setPropertyFromPyObject(attr, obj);
    return 0;
}
