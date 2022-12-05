from pathlib import Path
from collections import deque

queues = []


def transfer(lim, from_stack, to_stack):
    for cont in range(lim):
        queues[to_stack-1].append(queues[from_stack-1].pop())


def transfer2(lim, from_stack, to_stack):
    temp = deque()
    for cont in range(lim):
        temp.append(queues[from_stack-1].pop())
    for cont in range(lim):
        queues[to_stack-1].append(temp.pop())


def day5_1(lineas):
    for lin in lineas:
        k = lin.strip().split(',')
        transfer(int(k[0]), int(k[1]), int(k[2]))


def day5_2(lineas):
    for lin in lineas:
        k = lin.strip().split(',')
        transfer2(int(k[0]), int(k[1]), int(k[2]))

with open(Path(".").joinpath('day5-queues.txt'), 'r') as arch:
    lineas = arch.readlines()
    k = []
    for lin in lineas:
        k = lin.strip().split(',')
        queues.append(deque(k))

with open(Path(".").joinpath('day5.txt'), 'r') as arch:
    lineas = arch.readlines()
    # print(queues)
    # day5_1(lineas)
    day5_2(lineas)
    result = ""
    for q in queues:
        result += q.pop()
print(result)
