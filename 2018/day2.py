boxid = {}
contador = [0, 0]
with open("input/day2.txt",'rt') as archivo:
    for linea in archivo:
        boxid.clear()
        flags = [False, False]
        for char in linea:
            if char is '\n':
                continue
            if char in boxid:
                boxid[char]+=1
            else:
                boxid[char]=1
        for key, value in boxid.items():
            if value == 2 and not flags[0]:
                flags[0] = True
                contador[0] += 1
            if value == 3 and not flags[1]:
                flags[1] = True
                contador[1] += 1
        
print(contador[0]*contador[1])
            