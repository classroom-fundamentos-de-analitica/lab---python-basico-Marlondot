"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
from optparse import Values
import os
import sys

with open(os.path.join(sys.path[0],"data.csv"),"r") as file:
    datos=file.readlines()

clean_data=[row.rstrip("\n").split("\t")  for row in datos]




def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    answer=[int(row[1]) for row in clean_data]

    return sum(answer)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    Values=["A","B","C","D","E"]
    answer=list()
    for letter in Values:
        list_per_value=[1 for row in clean_data if row[0]==letter]
        answer.append((letter,sum(list_per_value)))


    return answer


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    Values=["A","B","C","D","E"]
    answer=list()
    for letter in Values:
        list_per_value=[int(row[1]) for row in clean_data if row[0]==letter]
        answer.append((letter,sum(list_per_value)))


    return answer


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    values=[row[2].split("-")[1] for row in clean_data]
    valuesSet=set(values)
    values=list(valuesSet)
    values.sort()

    answer=list()
    for value in values:
        list_per_value=[1 for row in clean_data if row[2].split("-")[1]==value]
        answer.append((value,sum(list_per_value)))


    return answer


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    values=["A","B","C","D","E"]
    
    answer=list()
    for value in values:
        list_per_value=[int(row[1]) for row in clean_data if row[0]==value]
        answer.append((value,max(list_per_value),min(list_per_value)))


    return answer


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    values=[row1.split(":")[0] for row0 in clean_data for row1 in row0[-1].split(",")]
    values=list(set(values))
    values.sort()

    answer=list()
    for value in values:
        list_per_value=[int(row1.split(":")[1]) for row0 in clean_data for row1 in row0[-1].split(",") if row1.split(":")[0]==value]
        answer.append((value,min(list_per_value),max(list_per_value)))


    return answer


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    
    values=[int(row[1]) for row in clean_data]
    valuesSet=set(values)
    values=list(valuesSet)
    values.sort()

    answer=list()
    for value in values:
        list_per_value=[row[0] for row in clean_data if int(row[1])==value]
        answer.append((value,list_per_value))


    return answer


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    values=[int(row[1]) for row in clean_data]
    valuesSet=set(values)
    values=list(valuesSet)
    values.sort()

    answer=list()
    for value in values:
        list_per_value=[row[0] for row in clean_data if int(row[1])==value]
        answer.append((value,sorted(list(set(list_per_value)))))

    return answer


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    values=[row1.split(":")[0] for row0 in clean_data for row1 in row0[-1].split(",")]
    values=list(set(values))
    values.sort()

    answer=list()
    for value in values:
        list_per_value=[1 for row0 in clean_data for row1 in row0[-1].split(",") if row1.split(":")[0]==value]
        answer.append((value,sum(list_per_value)))
    return dict(answer)


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    answer=list()
    for row in clean_data:
        answer.append((row[0],len(row[-2].split(",")),len(row[-1].split(","))))

    return answer


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    values=[row1 for row0 in clean_data for row1 in row0[-2].split(",")]
    values=list(set(values))
    values.sort()

    answer=list()
    for value in values:
        list_per_value=[int(row0[1]) for row0 in clean_data if value in row0[-2].split(",")]
        answer.append((value,sum(list_per_value)))
    return dict(answer)


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    values=[row[0] for row in clean_data]
    values=list(set(values))
    values.sort()

    answer=list()
    for value in values:
        list_per_value=[int(row1.split(":")[1]) for row0 in clean_data for row1 in row0[-1].split(",") if row0[0]==value]
        answer.append((value,sum(list_per_value)))
    return dict(answer)
