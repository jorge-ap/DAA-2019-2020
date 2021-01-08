from random import randint

#el valor del for determina el numero de casos creados en cada ejecucion
for _ in range(10):
    #num depositos
    amount = randint(600,10000)
    count = 0
    fila = []
    columna = []
    for i in range(amount):
        int1 = randint(500, 10000)
        int2 = randint(800, 10000)
        columna.append(int1)
        fila.append(int2)
        count += int1

    arrVol = [0] * max(fila)

    for i in range(len(fila)):
        for j in range(fila[i]):
            arrVol[j] += columna[i]

    for i in range(1, len(arrVol)):
        arrVol[i] += arrVol[i - 1]

    #genera una altura aleatoria
    altura = randint(1, len(arrVol))
    count = arrVol[altura-1]
    print(count)
    print(amount)
    for i in range(amount):
        print(columna[i], end=" ")
        print(fila[i],"\n", end="" )
    print("\nSALIDA = " , altura)
    print("----------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------")
