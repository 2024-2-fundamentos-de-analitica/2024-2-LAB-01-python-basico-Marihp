"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    # Leer el archivo
    with open("./files/input/data.csv") as file:
        suma = 0

        for line in file:
            columna = line.strip().split("\t")
            suma += int(columna[1])

        return suma
