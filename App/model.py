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
from DISClib.DataStructures import listiterator as it
import random
import statistics as stat
assert cf

# Construccion de modelos

def initCatalog(catalog):
    """
    Crea la estructura que almacenará los datos a analizar
    """
    catalog = {'fechas-hashtag': None, 'propiedades': None, 'fechas-eventos': None, 'hashtags-eventos': None, 'sentiments': None}
    catalog['fechas-hashtag'] = om.newMap(omaptype='RBT')
    catalog['propiedades'] = {'instrumentalness': om.newMap(omaptype='RBT', comparefunction=cmpf_properties),
                              'acousticness': om.newMap(omaptype='RBT', comparefunction=cmpf_properties),
                              'liveness': om.newMap(omaptype='RBT', comparefunction=cmpf_properties),
                              'speechiness': om.newMap(omaptype='RBT', comparefunction=cmpf_properties),
                              'energy': om.newMap(omaptype='RBT', comparefunction=cmpf_properties),
                              'danceability': om.newMap(omaptype='RBT', comparefunction=cmpf_properties),
                              'valence': om.newMap(omaptype='RBT', comparefunction=cmpf_properties), 
                              'tempo': om.newMap(omaptype='RBT', comparefunction=cmpf_properties)}
    catalog['fechas-eventos'] = om.newMap(omaptype='RBT')
    catalog['hashtags-eventos'] = om.newMap(omaptype='RBT')
    catalog['sentiments'] = om.newMap(omaptype='RBT')

    return catalog

# Funciones para agregar informacion al catalogo

def addEvent1(catalog, event):
    date = event['created_at']
    key = date[11:]
    contains = om.contains(catalog['fechas-hashtag'], key)
    if not contains:
        structure = {'eventos': lt.newList(datastructure="ARRAY_LIST")}
        lt.addLast(structure['eventos'], event)
        om.put(catalog['fechas-hashtag'], key, structure)
    else:
        obtained = om.get(catalog['fechas-hashtag'], key)
        value = obtained['value']
        lt.addLast(value['eventos'], event)
        om.put(catalog['fechas-hashtag'], key, value)
    return catalog

def addEvent1_v2(catalog, event):
    key = event["track_id"]
    contains = om.contains(catalog['hashtags-eventos'], key)
    if not contains:
        structure = {'eventos': lt.newList(datastructure="ARRAY_LIST")}
        lt.addLast(structure['eventos'], event)
        om.put(catalog['hashtags-eventos'], key, structure)
    else:
        obtained = om.get(catalog['hashtags-eventos'], key)
        value = obtained['value']
        lt.addLast(value['eventos'], event)
        om.put(catalog['hashtags-eventos'], key, value)
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
    # 'tempo'
    key = event['tempo']
    place = catalog['propiedades']['tempo']
    catalog = processForAE2(place, event, key, catalog)
    
    return catalog

def addEvent3(catalog, event):
    date = event['created_at']
    key = date[11:]
    contains = om.contains(catalog['fechas-eventos'], key)
    if not contains:
        structure = {'eventos': lt.newList(datastructure="ARRAY_LIST")}
        lt.addLast(structure['eventos'], event)
        om.put(catalog['fechas-eventos'], key, structure)
    else:
        obtained = om.get(catalog['fechas-eventos'], key)
        value = obtained['value']
        lt.addLast(value['eventos'], event)
        om.put(catalog['fechas-eventos'], key, value)
    return catalog

def addEvent4(catalog, event):
    key = event['hashtag']
    place = catalog['sentiments']
    om.put(place, key, event)
    return catalog

# Funciones para creacion de datos

# Funciones de consulta

def req1(catalog, caracteristica, minimo, maximo):
    """
    Dada una característica de contenido y un rango para la misma,
    devuelve la cantidad total de eventos de escucha y de artistas únicos.

    Entradas:
    - catalog: Estructura donde se almacenan los datos
    - caracteristica: característica con la que se hará la consulta
    - minimo: Valor mínimo para filtrar dentro de la característica
    - maximo: Valor máximo para filtrar dentro de la característica

    Salidas:
    - Lista que almacena el total de eventos, y el total de artistas. 
    """
    # Se filtra por la característica y el rango dados
    carac = caracteristica.lower()
    carac_total = catalog["propiedades"][carac]
    carac_filtrado = om.values(carac_total, minimo, maximo)

    total_events = 0
    artists_map = om.newMap('RBT')

    # Se recorren los datos obtenidos en el filtro
    for value in lt.iterator(carac_filtrado):
        for event in lt.iterator(value['eventos']):
            total_events += 1
            key = event['artist_id']
            val = 0
            om.put(artists_map, key, val)

    total_artists = om.size(artists_map)

    return [total_events, total_artists]
def req_2(min_Energy,max_Energy, min_Danceability, max_Danceability, catalog):
    arbol= catalog['propiedades']['danceability']
    lista= om.values(arbol,min_Danceability,max_Danceability)
    lista_tracks= lt.newList("ARRAY_LIST")
    cancion_completa=lt.newList("ARRAY_LIST")
    
    for elementos in lt.iterator(lista):
        for canciones in lt.iterator(elementos['eventos']):
            if (float(canciones["energy"])>= min_Energy and float(canciones["energy"])<=max_Energy):
                track_ID=canciones["track_id"]
                if int(lt.isPresent(lista_tracks, track_ID))== 0:
                    lt.addLast(lista_tracks, track_ID)
                    lt.addLast(cancion_completa, canciones)
                else: 
                    lt.addLast(cancion_completa, canciones)



    return lista_tracks, cancion_completa

def req3(catalog, min_instr, max_instr, min_tempo, max_tempo):
    """
    Soluciona el primer requerimiento.
    Entradas:
    - catalog: Estructura donde se almacenan los datos
    - min_instr: Valor mínimo para Instrumentalness
    - max_instr: Valor máximo para Instrumentalness
    - min_tempo: Valor mínimo para Tempo
    - max_tempo: Valor máximo para Tempo
    """
    # Se filtra por Instrumentalness y el rango dado
    instr_total = catalog["propiedades"]["instrumentalness"]
    instr_filtrado = om.values(instr_total, min_instr, max_instr)

    tracks_list = lt.newList(datastructure='ARRAY_LIST')

    # Se recorren los datos obtenidos en el filtro
    for value in lt.iterator(instr_filtrado):
        for event in lt.iterator(value['eventos']):
            if ((float(event["tempo"])) >= min_tempo) and ((float(event["tempo"])) <= max_tempo):
                elem = [event['track_id'], event['instrumentalness'], event['tempo']]
                contiene = lt.isPresent(tracks_list, elem)
                if contiene:
                    pass
                else:
                    lt.addLast(tracks_list, elem)
    
    # Se seleccionan 5 elementos aleatorios de la lista de tracks
    resultado = [(lt.size(tracks_list))]
    contador = 1
    while contador <= 5:
        list_size = lt.size(tracks_list)
        pos = random.randint(1, list_size)
        elem = lt.getElement(tracks_list, pos)
        resultado.append(elem)
        lt.deleteElement(tracks_list, pos)
        contador += 1
    
    return resultado


def req4(catalog, generos):
    tempo_total = catalog["propiedades"]["tempo"]

    nuevos_generos = lt.newList(datastructure='ARRAY_LIST')
    events_map = om.newMap('RBT')
    contador = 1
    while contador <= lt.size(generos):
        artists_list = lt.newList(datastructure='ARRAY_LIST')
        total_events = 0
        genero = lt.getElement(generos, contador)
        tempo_filtrado = om.values(tempo_total, genero[1], genero[2])
        for value in lt.iterator(tempo_filtrado):
            for event in lt.iterator(value['eventos']):
                total_events += 1
                val = 0
                om.put(events_map, event['id'], val)
                elem = event['artist_id']
                contiene = lt.isPresent(artists_list, elem)
                if contiene:
                    pass
                else:
                    lt.addLast(artists_list, elem)
        total_artists = lt.size(artists_list)
        ten_artists = lt.subList(artists_list, 1, 10)
        nuevo = {}
        nuevo["info"] = genero
        nuevo["artistas"] = total_artists
        nuevo["eventos"] = total_events
        nuevo["10artistas"] = ten_artists
        lt.addLast(nuevos_generos, nuevo)
        contador += 1
    total_tot_eventos = om.size(events_map)

    return [nuevos_generos, total_tot_eventos]
    
def determinarGeneros(event, generos):
    if (float(event["tempo"]) >= 60.0) and (float(event["tempo"]) <= 90.0):
        generos.append("reggae,60.0,90.0")
    if (float(event["tempo"]) >= 70.0) and (float(event["tempo"]) <= 100.0):
        generos.append("down-tempo,70.0,100.0")
    if (float(event["tempo"]) >= 90.0) and (float(event["tempo"]) <= 120.0):
        generos.append("chill-out,90.0,120.0")
    if (float(event["tempo"]) >= 85.0) and (float(event["tempo"]) <= 115.0):
        generos.append("hip-hop,85.0,115.0")
    if (float(event["tempo"]) >= 120.0) and (float(event["tempo"]) <= 125.0):
        generos.append("jazz and funk,120.0,125.0")
    if (float(event["tempo"]) >= 100.0) and (float(event["tempo"]) <= 130.0):
        generos.append("pop,100.0,130.0")
    if (float(event["tempo"]) >= 60.0) and (float(event["tempo"]) <= 80.0):
        generos.append("r&b,60.0,80.0")
    if (float(event["tempo"]) >= 110.0) and (float(event["tempo"]) <= 140.0):
        generos.append("rock,110.0,140.0")
    if (float(event["tempo"]) >= 100.0) and (float(event["tempo"]) <= 160.0):
        generos.append("metal,100.0,160.0")
    return generos


def req5(catalog, minimo, maximo):
    eventos = catalog["fechas-eventos"]
    eventos_filtrado = om.values(eventos, minimo, maximo)

    map_tempo = om.newMap('RBT')
    generos = []

    for value in lt.iterator(eventos_filtrado):
        for event in lt.iterator(value['eventos']):
            key = str(event['tempo']) + "," + str(event['user_id']) + "," + str(event['track_id']) + "," + str(event['created_at'])
            om.put(map_tempo, key, 0)
            generos_event = determinarGeneros(event, generos)

    genero_moda = stat.mode(generos)
    genmod_datos = genero_moda.split(",")
    min_tempo = genmod_datos[1]
    max_tempo = genmod_datos[2]
    tempo_filtrado = om.keys(map_tempo, min_tempo, max_tempo)


    generos_top = lt.newList(datastructure='ARRAY_LIST')
    contador = 1
    while contador <= 10:
        list_size = lt.size(tempo_filtrado)
        pos = random.randint(1, list_size)
        elem = lt.getElement(tempo_filtrado, pos)

        datos_elem = elem.split(",")
        track = datos_elem[1:]
        map_hashtags = catalog['hashtags-eventos']
        events = om.get(map_hashtags, track[1])
        datos_event = {'info': track, 'hashtags': [], 'vader_prom': 0, 'conteo': 0}
        for ev in lt.iterator(events['value']['eventos']):
            if (str(ev['user_id']) == str(track[0])) and (str(ev['created_at']) == str(track[2])):
                datos_event['hashtags'].append(ev['hashtag'])
        
        map_sentiments = catalog['sentiments']
        promedio = 0
        conteo = 0

        for hasht in datos_event['hashtags']:
            sent_hashtag = om.get(map_sentiments, hasht.lower())
            if sent_hashtag != None:
                try:
                    vader = float(sent_hashtag['value']['vader_avg'])
                except:
                    print(sent_hashtag['value']['vader_avg'])
                if vader != None:
                    promedio += vader
                    conteo += 1

        if conteo != 0:
            promedio = float(promedio)/float(conteo)
        else:
            promedio = 0
        datos_event['vader_prom'] = promedio
        datos_event['conteo'] = conteo

        lt.addLast(generos_top, datos_event)
        lt.deleteElement(tempo_filtrado, pos)
        contador += 1

    resultado = {'genero': genero_moda[0], 'cantidad_genero': lt.size(tempo_filtrado), 'tracks': generos_top}
    return resultado

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpf_properties(key1, key2):
    """
    Función de comparación para los RBT de las características de contenido
    """
    if (float(key1)) == (float(key2)):
        return 0
    elif (float(key1)) < (float(key2)):
        return -1
    else:
        return 1

# Funciones de ordenamiento

