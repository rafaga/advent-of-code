import statistics
ids = []
limite = 0
buffer = 0
diff = 0
commonstr = ""

# deteccion de cadenas similares
# para que puedan ser consideradas similares
# la suma de los caracteres no debe ser mayor a 25
# aquellos que contengan una suma identica se excluyen
# a excepcion del primero para optimizar el recuso de cpu
with open("input/day2.txt",'rt') as archivo:
    cuenta=0
    for linea in archivo:
        suma=0
        for char in linea:
            if char is '\n':
                continue
            else:
                suma += ord(char)
        ids.append([suma,cuenta])
        cuenta+=1
        ids.sort()
    cuenta=0
    for cuenta in range (0,len(ids)-1):
        if buffer == ids[cuenta][0]:
            continue
        if cuenta == len(ids)-1:
            break
        buffer = ids[cuenta][0]
        limite = buffer + 25
        for cuenta2 in range(cuenta + 1, len(ids)-1):
            if limite >= ids[cuenta2][0]:
                ids[cuenta].append(ids[cuenta2][1])
archivo.close()

with open("input/day2.txt",'rt') as archivo:
    linea=archivo.readlines()
archivo.close()
    
for boxid in ids:
    if len(boxid) <= 2:
        continue
    i = 0
    j = 0
    for i in range(1,len(boxid)-1):
        for j in range(i+1,len(boxid)-1):
            diff = 0
            commonstr=""
            for cuenta in range(0,len(linea[boxid[1]])-1):
                if linea[boxid[i]][cuenta] == "\n":
                    continue
                if diff > 1:
                    break
                if linea[boxid[i]][cuenta] != linea[boxid[j]][cuenta]:
                    diff+=1
                else:
                    commonstr += linea[boxid[i]][cuenta]
            if diff == 1:
                print(commonstr)

            