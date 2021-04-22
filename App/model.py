"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

# Construccion de modelos

def initCatalog(catalog):
    catalog = {'eventos': None}
    catalog['eventos'] = om.newMap(omaptype='RBT')
    return catalog

# Funciones para agregar informacion al catalogo

def addEvent(catalog, event):
    
    key = event['created_at']
    #print(catalog)
    contains = om.contains(catalog['eventos'], key)
    if not contains:
        structure = {'eventos': lt.newList(datastructure="ARRAY_LIST")}
        lt.addLast(structure['eventos'], event)
        om.put(catalog['eventos'], key, structure)
    else:
        obtained = om.get(catalog['eventos'], key)
        value = obtained['value']
        lt.addLast(value['eventos'], event)
        om.put(catalog['eventos'], key, value)
    return catalog

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
