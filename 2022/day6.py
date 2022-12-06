from pathlib import Path
from collections import deque


def day6(linea, chars=1):
    detector = deque(maxlen=chars)
    cont = 1
    dictz = dict()
    for char in linea:
        dictz.clear()
        detector.append(char)
        for c in detector:
            dictz[ord(c)] = 1
        if len(dictz) == chars:
            return (cont)
        cont += 1


with open(Path(".").joinpath('day6.txt'), 'r') as arch:
    linea = arch.readline()
    print(day6(linea,4)) # day6 part 1
    print(day6(linea,14)) # day6 part 2
