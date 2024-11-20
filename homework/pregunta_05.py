"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    data = {}

    with open("./files/input/data.csv") as file:
        for line in file:
            columna = line.strip().split("\t")
            letra = columna[0]
            valor = int(columna[1])

            if letra in data:
                data[letra].append(valor)

            else:
                data[letra] = [valor]

    resultado = [(letra, max(valores), min(valores)) for letra, valores in data.items()]
    resultado.sort()

    return resultado


pregunta_05()
