"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("")
    print("Bienvenido")
    print("1 - Cargar información en el catálogo")
    print("2 - Caracterizar las reproducciones")
    print("3 - Encontrar música para festejar")
    print("4 - Encontrar música para estudiar")
    print("5 - Estudiar los géneros musicales")
    print("6 - Indicar el género musical más escuchado en el tiempo")
    print("0 - Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.loadData(catalog)
        
    elif int(inputs[0]) == 2:
        print("")
        print("-------------------------------------------------  Requerimiento #1  --------------------------------------------------------")
        print("")
        print("Se pide obtener información filtrándola por característica de contenido y un cierto rango dentro de la misma.")
        print("Por ello se propone la solución de crear un RBT por cada característica.")
        print("Así, el filtro por característica y rango es mucho más fácil:")
        print(" > Directamente se escoge para analizar el Map de la característica dada por el usuario.")
        print(" > Ya en el Map, teniendo el rango dado, se analizan solo los elementos dentro de las llaves que estén dentro de dicho rango.")
        print("Por cada valor existente de la característica se almacenan los eventos que presentan dicho valor.")
        print("")
        print("A continuación se presentan los parámetros de altura y cantidad de entradas para cada Map (característica):")
        print("")
        print(" > Instrumentalness: Altura = " + str(om.height(catalog["propiedades"]["instrumentalness"])) + " || Entradas = " + str(om.size(catalog["propiedades"]["instrumentalness"])))
        print(" > Acousticness: Altura = " + str(om.height(catalog["propiedades"]["acousticness"])) + " || Entradas = " + str(om.size(catalog["propiedades"]["acousticness"])))
        print(" > Liveness: Altura = " + str(om.height(catalog["propiedades"]["liveness"])) + " || Entradas = " + str(om.size(catalog["propiedades"]["liveness"])))
        print(" > Speechiness: Altura = " + str(om.height(catalog["propiedades"]["speechiness"])) + " || Entradas = " + str(om.size(catalog["propiedades"]["speechiness"])))
        print(" > Energy: Altura = " + str(om.height(catalog["propiedades"]["energy"])) + " || Entradas = " + str(om.size(catalog["propiedades"]["energy"])))
        print(" > Danceability: Altura = " + str(om.height(catalog["propiedades"]["danceability"])) + " || Entradas = " + str(om.size(catalog["propiedades"]["danceability"])))
        print(" > Valence: Altura = " + str(om.height(catalog["propiedades"]["valence"])) + " || Entradas = " + str(om.size(catalog["propiedades"]["valence"])))

    else:
        sys.exit(0)
sys.exit(0)
