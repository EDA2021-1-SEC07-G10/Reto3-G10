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
    catalog = {'fechas': None, 'propiedades': None}
    catalog['fechas'] = om.newMap(omaptype='RBT')
    catalog['propiedades'] = {'instrumentalness': om.newMap(omaptype='RBT'),
                              'acousticness': om.newMap(omaptype='RBT'),
                              'liveness': om.newMap(omaptype='RBT'),
                              'speechiness': om.newMap(omaptype='RBT'),
                              'energy': om.newMap(omaptype='RBT'),
                              'danceability': om.newMap(omaptype='RBT'),
                              'valence': om.newMap(omaptype='RBT')}
    return catalog

# Funciones para agregar informacion al catalogo

def addEvent1(catalog, event):
    key = event['created_at']
    contains = om.contains(catalog['fechas'], key)
    if not contains:
        structure = {'eventos': lt.newList(datastructure="ARRAY_LIST")}
        lt.addLast(structure['eventos'], event)
        om.put(catalog['fechas'], key, structure)
    else:
        obtained = om.get(catalog['fechas'], key)
        value = obtained['value']
        lt.addLast(value['eventos'], event)
        om.put(catalog['fechas'], key, value)
    return catalog


def processForAE2(place, event, key, catalog):
    contains = om.contains(place, key)
    if not contains:
        structure = {'eventos': lt.newList(datastructure="ARRAY_LIST")}
        lt.addLast(structure['eventos'], event)
        om.put(place, key, structure)
    else:
        obtained = om.get(place, key)
        value = obtained['value']
        lt.addLast(value['eventos'], event)
        om.put(place, key, value)
    return catalog


def addEvent2(catalog, event):
    
    # 'instrumentalness'
    key = event['instrumentalness']
    place = catalog['propiedades']['instrumentalness']
    catalog = processForAE2(place, event, key, catalog)
    # 'acousticness'
    key = event['acousticness']
    place = catalog['propiedades']['acousticness']
    catalog = processForAE2(place, event, key, catalog)
    # 'liveness'
    key = event['liveness']
    place = catalog['propiedades']['liveness']
    catalog = processForAE2(place, event, key, catalog)
    # 'speechiness'
    key = event['speechiness']
    place = catalog['propiedades']['speechiness']
    catalog = processForAE2(place, event, key, catalog)
    # 'energy'
    key = event['energy']
    place = catalog['propiedades']['energy']
    catalog = processForAE2(place, event, key, catalog)
    # 'danceability'
    key = event['danceability']
    place = catalog['propiedades']['danceability']
    catalog = processForAE2(place, event, key, catalog)
    # 'valence'
    key = event['valence']
    place = catalog['propiedades']['valence']
    catalog = processForAE2(place, event, key, catalog)
    
    #Prueba 1

    return catalog

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
