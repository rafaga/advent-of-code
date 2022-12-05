from pathlib import Path


def day4_1(linea):
    k = []
    l = []
    cont = 0
    for lin in lineas:
        k.clear()
        l.clear()
        k = lin.strip().split(',')
        l.append(k[0].split("-"))
        l.append(k[1].split("-"))
        k = []
        k.append(int(l[0][0]) - int(l[1][0]))
        k.append(int(l[0][1]) - int(l[1][1]))
        if (int(k[0]) >= 0 and int(k[1]) <= 0) or (int(k[0]) <= 0 and int(k[1]) >= 0):
            cont+=1
        # print(l, cont)
    print(cont)


def day4_2(linea):
    k = []
    l = []
    cont = 0
    for lin in lineas:
        k.clear()
        l.clear()
        k = lin.strip().split(',')
        l.append(k[0].split("-"))
        l.append(k[1].split("-"))
        k = []
        k.append(range(int(l[0][0]), int(l[0][1])+1))
        k.append(range(int(l[1][0]), int(l[1][1])+1))
        set1 = set(k[0])
        set2 = set(k[1])
        if not set1.isdisjoint(set2):
            cont += 1
    print(cont)


with open(Path(".").joinpath('day4.txt'), 'r') as arch:
    lineas = arch.readlines()
    day4_1(lineas)
    day4_2(lineas)
