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

def preguntar_generos():
    """
    Función que, en el req. 4, se utiliza para recibir las entradas de géneros
    Valida si el usuario quiere crear géneros nuevos o añadir existentes
    """
    opcion = int(input("Si desea añadir un género existente, ingrese 0. Si desea crear uno nuevo, ingrese 1: "))
    if opcion == 0:
        genero = input("Ingrese el nombre del género: ")
        return genero
    elif opcion == 1:
        genero = input("Ingrese el nombre del género: ")
        min_genero = float(input("Ingrese el valor mínimo de Tempo para el género: "))
        max_genero = float(input("Ingrese el valor máximo de Tempo para el género: "))
        rta = [genero, min_genero, max_genero]
        return rta        

def preguntar_crear():
    """
    Función que, en el req. 4, se utiliza para validar si quieren añadirse más géneros
    """
    opcion = int(input("Si desea añadir un género nuevo, ingrese 1. De lo contrario, ingrese 0: "))
    if opcion == 0:
        return False
    elif opcion == 1:
        return True

def print_genero(genero):
    info_genero = genero["info"]
    nombre = info_genero[0]
    minimo = info_genero[1]
    maximo = info_genero[2]
    cant_artistas = genero["artistas"]
    cant_eventos = genero["eventos"]
    ten_artists = genero["10artistas"]
    print("=======  " + nombre.upper() + "  =======")
    print("Para " + nombre.lower() + " con Tempo entre " + str(minimo) + " y " + str(maximo) + " BPM:")
    print("Se encontraron " + str(cant_eventos) + " eventos, y " + str(cant_artistas) + " artistas únicos. Algunos de ellos son:")
    for artist in lt.iterator(ten_artists):
        print("> " + str(artist))

def print_Req5(resultado, minimo, maximo):
    print("Para el rango de horas " + str(minimo) + " a " + str(maximo) + " el género más escuchado fue " + resultado['genero'] + 
    " con " + str(resultado['cantidad_genero']) + " reproducciones")
    print("El promedio Vader de 10 pistas aleatorias en dicho género fue:")
    for track in lt.iterator(resultado['tracks']):
        print("> Track " + track['info'][1] + " con " + str(track['conteo']) + " hashtags, y vader " + str(track['vader_prom']))

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    print("")
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.loadData(catalog)
        
    elif int(inputs[0]) == 2:
        print("")
        print("-------------------------------------------------  Requerimiento #1  --------------------------------------------------------")
        print("")
        caracteristica = input("Ingrese la característica de contenido: ")
        minimo = str(input("Ingrese el valor mínimo para la característica: "))
        maximo = str(input("Ingrese el valor máximo para la característica: "))
        print("")
        resultado = controller.req1(catalog, caracteristica, minimo, maximo)
        print("Para la característica " + caracteristica + ", en el rango " + minimo + " a " + maximo + ":")
        print("> Total de eventos o reproducciones: " + str(resultado[0]))
        print("> Total de artistas únicos: " + str(resultado[1]))

    elif int(inputs[0]) == 4:
        print("")
        print("-------------------------------------------------  Requerimiento #3  --------------------------------------------------------")
        print("")
        min_instr = float(input("Ingrese el valor mínimo para Instrumentalness: "))
        max_instr = float(input("Ingrese el valor máximo para Instrumentalness: "))
        min_tempo = float(input("Ingrese el valor mínimo para Tempo: "))
        max_tempo = float(input("Ingrese el valor máximo para Tempo: "))
        print("")
        resultado = controller.req3(catalog, min_instr, max_instr, min_tempo, max_tempo)
        print("Para un Instrumentalness entre " + str(min_instr) + " y " + str(max_instr) + ", y un Tempo entre " + str(min_tempo) + " y " + str(max_tempo) + ":")
        print("> Total de Tracks únicos: " + str(resultado[0]))
        print("> Track 1: " + str(resultado[1][0]) + " con Instrumentalness de " + str(resultado[1][1]) + " y Tempo de " + str(resultado[1][2]))
        print("> Track 2: " + str(resultado[2][0]) + " con Instrumentalness de " + str(resultado[2][1]) + " y Tempo de " + str(resultado[2][2]))
        print("> Track 3: " + str(resultado[3][0]) + " con Instrumentalness de " + str(resultado[3][1]) + " y Tempo de " + str(resultado[3][2]))
        print("> Track 4: " + str(resultado[4][0]) + " con Instrumentalness de " + str(resultado[4][1]) + " y Tempo de " + str(resultado[4][2]))
        print("> Track 5: " + str(resultado[5][0]) + " con Instrumentalness de " + str(resultado[5][1]) + " y Tempo de " + str(resultado[5][2]))
    
    elif int(inputs[0]) == 5:
        print("")
        print("-------------------------------------------------  Requerimiento #4  --------------------------------------------------------")
        print("")
        generos = lt.newList(datastructure='ARRAY_LIST')
        continuar = True
        while continuar:
            nuevo = preguntar_generos()
            lt.addLast(generos, nuevo)
            continuar = preguntar_crear()
        resultado = controller.req4(catalog, generos)
        print("El total de eventos para los siguientes géneros fue de: " + str(resultado[1]))
        for genero in lt.iterator(resultado[0]):
            print_genero(genero)

    elif int(inputs[0]) == 6:
        print("")
        print("-------------------------------------------------  Requerimiento #5  --------------------------------------------------------")
        print("")
        minimo = input("Ingrese el valor mínimo de hora (únicamente en formato hh:mm:ss): ")
        maximo = input("Ingrese el valor máximo de hora (únicamente en formato hh:mm:ss): ")
        resultado = controller.req5(catalog, minimo, maximo)
        print_Req5(resultado, minimo, maximo)

    else:
        sys.exit(0)
sys.exit(0)

