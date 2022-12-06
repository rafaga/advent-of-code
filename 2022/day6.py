from pathlib import Path
from collections import deque


def day6_1(linea):
    detector = deque(maxlen=4)
    cont = 1
    dictz = dict()
    for char in linea:
        dictz.clear()
        detector.append(char)
        for c in detector:
            dictz[ord(c)] = 1
        if len(dictz) == 4:
            return (cont)
        cont += 1


def day6_2(linea):
    detector = deque(maxlen=14)
    cont = 1
    dictz = dict()
    for char in linea:
        dictz.clear()
        detector.append(char)
        for c in detector:
            dictz[ord(c)] = 1
        if len(dictz) == 14:
            return (cont)
        cont += 1


with open(Path(".").joinpath('day6.txt'), 'r') as arch:
    linea = arch.readline()
    print(day6_1(linea))
    print(day6_2(linea))
