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
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def loadData(catalog):
    catalog = model.initCatalog(catalog)
    infofile1 = cf.data_dir + 'user_track_hashtag_timestamp-small.csv'
    input_file1 = csv.DictReader(open(infofile1, encoding="utf-8"),
                                delimiter=",")
    for event in input_file1:
        model.addEvent1(catalog, event)
        model.addEvent1_v2(catalog, event)

    infofile2 = cf.data_dir + 'context_content_features-small.csv'
    input_file2 = csv.DictReader(open(infofile2, encoding="utf-8"),
                                delimiter=",")
    for event in input_file2:
        model.addEvent2(catalog, event)
        model.addEvent3(catalog, event)
    
    infofile3 = cf.data_dir + 'sentiment_values.csv'
    input_file3 = csv.DictReader(open(infofile3, encoding="utf-8"),
                                delimiter=",")
    for event in input_file3:
        model.addEvent4(catalog, event)
        
    return catalog

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def def_generos(contador, generos, elemento):
    if elemento.lower() == "reggae":
        nuevo = ["reggae", 60.0, 90.0]
    elif elemento.lower() == "down-tempo":
        nuevo = ["down-tempo", 70.0, 100.0]
    elif elemento.lower() == "chill-out":
        nuevo = ["chill-out", 90.0, 120.0]
    elif elemento.lower() == "hip-hop":
        nuevo = ["hip-hop", 85.0, 115.0]
    elif elemento.lower() == "jazz and funk":
        nuevo = ["jazz and funk", 120.0, 125.0]
    elif elemento.lower() == "pop":
        nuevo = ["pop", 100.0, 130.0]
    elif elemento.lower() == "r&b":
        nuevo = ["r&b", 60.0, 80.0]
    elif elemento.lower() == "rock":
        nuevo = ["rock", 110.0, 140.0]
    elif elemento.lower() == "metal":
        nuevo = ["metal", 100.0, 160.0]
    lt.changeInfo(generos, contador, nuevo)

def req1(catalog, caracteristica, minimo, maximo):
    return model.req1(catalog, caracteristica, minimo, maximo)

def req3(catalog, min_instr, max_instr, min_tempo, max_tempo):
    return model.req3(catalog, min_instr, max_instr, min_tempo, max_tempo)

def req4(catalog, generos):
    contador = 1
    while contador <= lt.size(generos):
        genero = lt.getElement(generos, contador)
        if type(genero) != list:
            def_generos(contador, generos, genero)
        contador += 1
    return model.req4(catalog, generos)

def req5(catalog, minimo, maximo):
    return model.req5(catalog, minimo, maximo)