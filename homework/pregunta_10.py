"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    data = []

    with open("./files/input/data.csv") as file:
        for line in file:
            columna = line.strip().split("\t")
            letra = columna[0]
            columna4 = len(columna[3].split(","))
            columna5 = len(columna[4].split(","))
            data.append(tuple([letra, columna4, columna5]))
    return data


pregunta_10()
