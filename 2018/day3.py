claim = {}
predims = []
id_claim = 0
collisions = 0
avance=0
with open("input/day3.txt",'rt') as archivo:
    for linea in archivo:
        rawClaim=linea.split(' ')
        bounds = [0, 0, 0, 0]
        predims = rawClaim[2][:-1].split(',')
        id_claim = int(rawClaim[0][1::])
        claim[id_claim]=[int(predims[0]),int(predims[1])]
        predims = rawClaim[3][:-1].split('x')
        claim[id_claim].append(claim[id_claim][0]+int(predims[0]))
        claim[id_claim].append(claim[id_claim][1]+int(predims[1]))
archivo.close()

def collision(claim1 = None, claim2 = None):
    col = []
    if claim1 is None or claim2 is None:
        return False
    rect1 = [[claim1[0], claim1[1]], [claim1[0], claim1[3]],
             [claim1[2], claim1[1]], [claim1[2], claim1[3]]]
    rect2 = [[claim2[0], claim2[1]], [claim2[0], claim2[3]],
             [claim2[2], claim2[1]], [claim2[2], claim2[3]]]
    for punto in range(0,3):
        if rect1[0][0] <= rect2[punto][0] <= rect1[3][0] and rect1[0][1] <= rect2[punto][1] <= rect1[3][1]:
            if punto == 0:
                col.append(rect1[3][0] - rect2[punto][0])
                col.append(rect1[3][1] - rect2[punto][1])
                col.append(col[0]*col[1])
            if punto == 1:
                col.append(rect1[2][0] - rect2[punto][0])
                col.append(rect2[punto][1] - rect1[2][1])
                col.append(col[0]*col[1])
            if punto == 2:
                col.append(rect2[punto][0] - rect1[1][0])
                col.append(rect1[1][1] - rect2[punto][1])
                col.append(col[0]*col[1])
            if punto == 3:
                col.append(rect2[punto][0] - rect1[0][0])
                col.append(rect2[punto][1] - rect1[0][1])
                col.append(col[0]*col[1])
            col.append(punto)
            return col
    return False

#lsorted = sorted_by_value = sorted(claim.items(), key=lambda kv: kv[1][1])
cords=[]
for key, value in claim.items():
    cord = [[value[0], value[1]], [value[0], value[3]],
            [value[2], value[1]], [value[2], value[3]]]
    cords.append(cord)

matrix = [[0] * 1000 for i in range(1000)]
for cord in cords:
    for i in range(cord[0][0], cord[3][0]):
        for j in range(cord[0][1], cord[3][1]):
            matrix[i][j] += 1

colisiones=0
for row in matrix:
    for cell in row:
        if cell > 1:
            colisiones+=1

print(colisiones)
#print(lsorted)
""" for i in range(0,len(lsorted)-1):
    for j in range(i, len(lsorted)-1):
        area = collision(lsorted[i][1], lsorted[j][1])
        if area is not False:
            print(area) """

""" for x in range(1,1000):
    for y in range(1,1000):
        suma=0
        for id_claim, area in claim.items():
            if (area[0] <= x and x <= area[2]) and (area[1] <= y and y <= area[3]):
                suma+=1
            if suma > 1:
                break
        if suma > 0:
            collisions += 1
    avance+=1
    print((avance/10),"%:",collisions," colisiones detectadas") """
            
#print(collisions)
            
