from pathlib import Path
from collections import deque


def EvalRes2(datos):
    datos[0] = ord(datos[0]) - ord('A')
    datos[1] = ord(datos[1]) - ord('X')
    res = 0
    if datos[1] == 2:  # ganar
        res = (datos[0] + 1) % 3
    if datos[1] == 1:  # empatar
        res = datos[0]
    if datos[1] == 0:  # perder
        res = (datos[0] + 2) % 3
    return res + 1 + (datos[1]*3)


def EvalRes(datos):
    bwin = False
    datos[0] = ord(datos[0]) - ord('A') + 1
    datos[1] = ord(datos[1]) - ord('X') + 1
    if datos[0] == datos[1]:
        return datos[1] + 3
    else:
        if (datos[1] == 1 and datos[0] == 3) or (datos[1] == 2 and datos[0] == 1) or (datos[1] == 3 and datos[0] == 2):
            bwin = True
    if bwin:
        return datos[1] + 6
    else:
        return datos[1]


ssum = 0
with open(Path(".").joinpath('day2.txt'), 'r') as arch:
    lineas = arch.readlines()
    res = []
    for lin in lineas:
        res = lin.strip().split(' ')
        points = EvalRes2(res)
        ssum += points

print(ssum)
