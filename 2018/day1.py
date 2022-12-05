suma = 0
values = [0]
winner = None
while winner is None:
    with open("input/day1.txt",'rt') as archivo:
        for linea in archivo:
            suma = suma + int(linea)
            # Part 2
            if winner is None:
                if suma in values:
                    winner = suma
                    print("winner=",suma)
                else:
                    values.append(suma)
    print("---[pass]---")
    archivo.close()
print("Answer: ", winner)