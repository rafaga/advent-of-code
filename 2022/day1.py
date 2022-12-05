from pathlib import Path
from collections import deque

smax = []
with open(Path(".").joinpath('day1.txt'), 'r') as arch:
    lineas = arch.readlines()
    a = []
    for lin in lineas:
        if lin == '\n':
            ssum = sum(a)
            smax.append(ssum)
            a.clear()
            continue
        a.append(int(lin))

smax.sort(reverse=True)

print(sum(smax[:3]))
