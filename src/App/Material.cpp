/***************************************************************************
 *   Copyright (c) 2005 Jürgen Riegel <juergen.riegel@web.de>              *
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

#ifndef _PreComp_
# include <cstring>
#endif

#include <boost/format.hpp>
#include <assert.h>
#include <Base/Exception.h>
#include "Material.h"
#include "MaterialPy.h"
#include "MaterialSource.h"
#include "MaterialDatabase.h"

using namespace App;

static int ambientColorId = -1;
static int diffuseColorId = -1;
static int specularColorId = -1;
static int emissiveColorId = -1;
static int shininessId = -1;
static int transparencyId = -1;
static int nameId = -1;

//===========================================================================
// Material
//===========================================================================

Material::Material(const MaterialSource * matSource, const std::vector<boost::any> &properties)
 : _matSource(matSource)
 , _matProperties(properties)
{
    assert(matSource != nullptr);
    setInternalIds();
    PythonObject = new MaterialPy(this);
}

Material::~Material() 
{
}

void Material::setInternalIds()
{
    if (ambientColorId == -1)
        ambientColorId = getPropertyId("AmbientColor");
    if (diffuseColorId == -1)
        diffuseColorId = getPropertyId("DiffuseColor");
    if (specularColorId == -1)
        specularColorId = getPropertyId("SpecularColor");
    if (emissiveColorId == -1)
        emissiveColorId = getPropertyId("EmissiveColor");
    if (shininessId == -1)
        shininessId = getPropertyId("Shininess");
    if (transparencyId == -1)
        transparencyId = getPropertyId("Transparency");
    if (nameId == -1)
        nameId = getPropertyId("Name");
}

const boost::any &Material::getProperty(const char *propName) const
{
    int id = getPropertyId(propName);

    return getProperty(id);
}

void Material::setProperty(const char *propName, const boost::any &value)
{
    setProperty(getPropertyId(propName), value);
}

const char * Material::getPropertyName(int id) const
{
    return _matSource->getPropertyName(id);
}

void Material::setProperty(int id, const boost::any &value)
{
    if (id < 0)
        throw Base::RuntimeError("Cannot set property: Invalid property id");

    if (_matSource->isReadOnly())
        throw Base::RuntimeError(str(boost::format("Unable to set property %1%: material source is read-only.") % getPropertyName(id)));

    if (static_cast<size_t>(id) >= _matProperties.size())
        _matProperties.resize(static_cast<size_t>(id) + 1);

    _matProperties[static_cast<size_t>(id)] = value;
}

void Material::setProperties(const std::vector<boost::any> &properties)
{
    _matProperties = properties;
}

void Material::removeProperty(const char *propName)
{
    removeProperty(getPropertyId(propName));
}

void Material::removeProperty(int id)
{
    if (id < 0)
        throw Base::RuntimeError("Cannot remove property: Invalid property id");
    if (static_cast<size_t>(id) < _matProperties.size())
        _matProperties.resize(static_cast<size_t>(id) + 1);

    _matProperties[static_cast<size_t>(id)] = deleted_property_t();
}

int Material::getPropertyId(const char *propName) const
{
    if (_matSource)
        return _matSource->getPropertyId(propName);
    else
        return -1;
}

const boost::any &Material::getProperty(int id) const
{
    if (id < 0)
        throw Base::RuntimeError("Cannot get property: Invalid property ID");
    else {
        static boost::any empty;
        const boost::any & value = static_cast<size_t>(id) < _matProperties.size() ?_matProperties[static_cast<size_t>(id)] : empty;

        // If value is empty, ask the Father material
        if (value.empty()) {
            size_t fatherId = static_cast<size_t>(getPropertyId("Father"));
            const boost::any & fatherProp = fatherId < _matProperties.size() ?_matProperties[fatherId] : empty;

            if (!fatherProp.empty()) {
                Material * father = getDatabase()->getMaterial(boost::any_cast<std::string>(fatherProp).c_str());

                if (father)
                    return father->getProperty(id);
            }
        }
        else if (value.type() == typeid(deleted_property_t))
            return empty;

        return value;
    }
}

PyObject *Material::getPropertyAsPyObject(const char *propName) const
{
    _matType = MatType;
    switch (MatType)
    {
    case BRASS:
        ambientColor .set(0.3294f,0.2235f,0.0275f);
        diffuseColor .set(0.7804f,0.5686f,0.1137f);
        specularColor.set(0.9922f,0.9412f,0.8078f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.2179f;
        transparency = 0.0000f;
        break;
    case BRONZE:
        ambientColor .set(0.2125f,0.1275f,0.0540f);
        diffuseColor .set(0.7140f,0.4284f,0.1814f);
        specularColor.set(0.3935f,0.2719f,0.1667f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.2000f;
        transparency = 0.0000f;
        break;
    case COPPER:
        ambientColor .set(0.3300f,0.2600f,0.2300f);
        diffuseColor .set(0.5000f,0.1100f,0.0000f);
        specularColor.set(0.9500f,0.7300f,0.0000f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.9300f;
        transparency = 0.0000f;
        break;
    case GOLD:
        ambientColor .set(0.3000f,0.2306f,0.0953f);
        diffuseColor .set(0.4000f,0.2760f,0.0000f);
        specularColor.set(0.9000f,0.8820f,0.7020f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.0625f;
        transparency = 0.0000f;
        break;
    case PEWTER:
        ambientColor .set(0.1059f,0.0588f,0.1137f);
        diffuseColor .set(0.4275f,0.4706f,0.5412f);
        specularColor.set(0.3333f,0.3333f,0.5216f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.0769f;
        transparency = 0.0000f;
        break;
    case PLASTER:
        ambientColor .set(0.0500f,0.0500f,0.0500f);
        diffuseColor .set(0.1167f,0.1167f,0.1167f);
        specularColor.set(0.0305f,0.0305f,0.0305f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.0078f;
        transparency = 0.0000f;
        break;
    case PLASTIC:
        ambientColor .set(0.1000f,0.1000f,0.1000f);
        diffuseColor .set(0.0000f,0.0000f,0.0000f);
        specularColor.set(0.0600f,0.0600f,0.0600f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.0078f;
        transparency = 0.0000f;
        break;
    case SILVER:
        ambientColor .set(0.1922f,0.1922f,0.1922f);
        diffuseColor .set(0.5075f,0.5075f,0.5075f);
        specularColor.set(0.5083f,0.5083f,0.5083f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.2000f;
        transparency = 0.0000f;
        break;
    case STEEL:
        ambientColor .set(0.0020f,0.0020f,0.0020f);
        diffuseColor .set(0.0000f,0.0000f,0.0000f);
        specularColor.set(0.9800f,0.9800f,0.9800f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.0600f;
        transparency = 0.0000f;
        break;
    case STONE:
        ambientColor .set(0.1900f,0.1520f,0.1178f);
        diffuseColor .set(0.7500f,0.6000f,0.4650f);
        specularColor.set(0.0784f,0.0800f,0.0480f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.1700f;
        transparency = 0.0000f;
        break;
    case SHINY_PLASTIC:
        ambientColor .set(0.0880f,0.0880f,0.0880f);
        diffuseColor .set(0.0000f,0.0000f,0.0000f);
        specularColor.set(1.0000f,1.0000f,1.0000f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 1.0000f;
        transparency = 0.0000f;
        break;
    case SATIN:
        ambientColor .set(0.0660f,0.0660f,0.0660f);
        diffuseColor .set(0.0000f,0.0000f,0.0000f);
        specularColor.set(0.4400f,0.4400f,0.4400f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.0938f;
        transparency = 0.0000f;
        break;
    case METALIZED:
        ambientColor .set(0.1800f,0.1800f,0.1800f);
        diffuseColor .set(0.0000f,0.0000f,0.0000f);
        specularColor.set(0.4500f,0.4500f,0.4500f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.1300f;
        transparency = 0.0000f;
        break;
    case NEON_GNC:
        ambientColor .set(0.2000f,0.2000f,0.2000f);
        diffuseColor .set(0.0000f,0.0000f,0.0000f);
        specularColor.set(0.6200f,0.6200f,0.6200f);
        emissiveColor.set(1.0000f,1.0000f,0.0000f);
        shininess    = 0.0500f;
        transparency = 0.0000f;
        break;
    case CHROME:
        ambientColor .set(0.3500f,0.3500f,0.3500f);
        diffuseColor .set(0.9176f,0.9176f,0.9176f);
        specularColor.set(0.9746f,0.9746f,0.9746f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.1000f;
        transparency = 0.0000f;
        break;
    case ALUMINIUM:
        ambientColor .set(0.3000f,0.3000f,0.3000f);
        diffuseColor .set(0.3000f,0.3000f,0.3000f);
        specularColor.set(0.7000f,0.7000f,0.8000f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.0900f;
        transparency = 0.0000f;
        break;
    case OBSIDIAN:
        ambientColor .set(0.0538f,0.0500f,0.0662f);
        diffuseColor .set(0.1828f,0.1700f,0.2253f);
        specularColor.set(0.3327f,0.3286f,0.3464f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.3000f;
        transparency = 0.0000f;
        break;
    case NEON_PHC:
        ambientColor .set(1.0000f,1.0000f,1.0000f);
        diffuseColor .set(1.0000f,1.0000f,1.0000f);
        specularColor.set(0.6200f,0.6200f,0.6200f);
        emissiveColor.set(0.0000f,0.9000f,0.4140f);
        shininess    = 0.0500f;
        transparency = 0.0000f;
        break;
    case JADE:
        ambientColor .set(0.1350f,0.2225f,0.1575f);
        diffuseColor .set(0.5400f,0.8900f,0.6300f);
        specularColor.set(0.3162f,0.3162f,0.3162f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.1000f;
        transparency = 0.0000f;
        break;
    case RUBY:
        ambientColor .set(0.1745f,0.0118f,0.0118f);
        diffuseColor .set(0.6142f,0.0414f,0.0414f);
        specularColor.set(0.7278f,0.6279f,0.6267f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.6000f;
        transparency = 0.0000f;
        break;
    case EMERALD:
        ambientColor .set(0.0215f,0.1745f,0.0215f);
        diffuseColor .set(0.0757f,0.6142f,0.0757f);
        specularColor.set(0.6330f,0.7278f,0.6330f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.6000f;
        transparency = 0.0000f;
        break;
    case USER_DEFINED:
        break;
    default:
        ambientColor .set(0.2000f,0.2000f,0.2000f);
        diffuseColor .set(0.8000f,0.8000f,0.8000f);
        specularColor.set(0.0000f,0.0000f,0.0000f);
        emissiveColor.set(0.0000f,0.0000f,0.0000f);
        shininess    = 0.2000f;
        transparency = 0.0000f;
        break;
    }
    return _matSource->toPyObject(propName, getProperty(propName));
}

void Material::setPropertyFromPyObject(const char *propName, const PyObject *value)
{
    boost::any anyvalue(_matSource->fromPyObject(propName, value));
    setProperty(propName, anyvalue);
}

bool Material::canUndo() const
{
    return _matSource->canUndo();
}

std::string Material::getName() const
{
    return boost::any_cast<std::string>(_matProperties[static_cast<size_t>(nameId)]);
}

Color Material::getAmbientColor() const
{
    return boost::any_cast<Color>(getProperty(ambientColorId));
}

void Material::setAmbientColor(const Color &color)
{
    setProperty(ambientColorId, color);
}

Color Material::getDiffuseColor() const
{
    return boost::any_cast<Color>(getProperty(diffuseColorId));
}

void Material::setDiffuseColor(const Color &color)
{
    setProperty(diffuseColorId, color);
}

Color Material::getSpecularColor() const
{
    return boost::any_cast<Color>(getProperty(specularColorId));
}

void Material::setSpecularColor(const Color &color)
{
    setProperty(specularColorId, color);
}

Color Material::getEmissiveColor() const
{
    return boost::any_cast<Color>(getProperty(emissiveColorId));
}

void Material::setEmissiveColor(const Color &color)
{
    setProperty(emissiveColorId, color);
}

float Material::getShininess() const
{
    return boost::any_cast<float>(getProperty(shininessId));
}

void Material::setShininess(float value)
{
    setProperty(shininessId, value);
}

float Material::getTransparency() const
{
    return boost::any_cast<float>(getProperty(transparencyId));
}

void Material::setTransparency(float value)
{
    setProperty(transparencyId, value);
}

PyObject *Material::getPyObject()
{
    return Py::new_reference_to(PythonObject);
}

App::MaterialDatabase *Material::getDatabase() const {
    return _matSource->getDatabase();
>>>>>>> Better Material support for solid objects.
}
