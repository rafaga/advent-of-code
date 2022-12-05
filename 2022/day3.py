from pathlib import Path

def convertLetter2Number(letra):
    num = 0
    if letra >= 'a' and letra <= 'z':
        num = ord(letra) - ord('a') + 1
    if letra >= 'A' and letra <= 'Z':
        num = ord(letra) - ord('A') + 27
    return (num)


def day3_1(lin):
    letters = [0]*53
    ssum = 0
    for letra in range(len(lin)//2):
        letters[convertLetter2Number(lin[letra])] = 1
    for letra in range(len(lin)//2, len(lin)):
        if letters[convertLetter2Number(lin[letra])] == 1:
            letters[convertLetter2Number(lin[letra])] = 2
    for letra in range(len(letters)):
        if letters[letra] > 1:
            ssum += letra
    return (ssum)


def day3_1mod(letters, lin, row):
    for letra in range(len(lin)):
        if letters[convertLetter2Number(lin[letra])] == row-1 and convertLetter2Number(lin[letra]) > 0:
            letters[convertLetter2Number(lin[letra])] = row
    return (letters)


def day3_2(lineas):
    ssum = 0
    cont = 0
    letters = []
    for lin in lineas:
        if cont % 3 == 0:
            letters = [0]*53
        letters = day3_1mod(letters, lin, (cont % 3)+1)
        if cont % 3 == 2:
            ssum += letters.index(max(letters))
        cont += 1
    return (ssum)


with open(Path(".").joinpath('day3.txt'), 'r') as arch:
    lineas = arch.readlines()
    ssum = 0
    res = []
    for lin in lineas:
        lin = lin.strip()
        ssum += day3_1(lin)
    print(ssum)
    print(day3_2(lineas))

