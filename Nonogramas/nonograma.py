def fusion(primero, segundo, salidaFilasOrden, izqNumFila, derNumFila, salidaNumFila):
    primero.append(-float("inf"))
    segundo.append(-float("inf"))
    k = f = s = 0
    while f < len(primero) - 1 or s < len(segundo) - 1:
        if segundo[s] > primero[f] and s < len(segundo) - 1:
            salidaFilasOrden[k] = segundo[s]
            salidaNumFila[k] = derNumFila[s]
            s += 1
        else:
            salidaFilasOrden[k] = primero[f]
            salidaNumFila[k] = izqNumFila[f]
            f += 1
        k += 1


def ordenarListas(num_fila, filasOrden):
    if len(filasOrden) < 2:
        return
    medio = len(filasOrden) // 2
    # divide
    izqFilasOrden = filasOrden[:medio]  # copia desde 0 hasta mid
    izqNumFila = num_fila[:medio]
    derFilasOrden = filasOrden[medio:]
    derNumFila = num_fila[medio:]

    # conquer
    ordenarListas(izqNumFila, izqFilasOrden)
    ordenarListas(derNumFila, derFilasOrden)

    # Combine
    fusion(izqFilasOrden, derFilasOrden, filasOrden, izqNumFila, derNumFila, num_fila)


#  Inicializa el tablero con casillas sin rellenar ("-")
def inicializarTablero(filas, columnas):
    tablero = []
    for _ in range(filas):
        tablero.append(["-"] * columnas)
    return tablero


#  Método que pinta el tablero
def pintarTablero(tablero):
    for i in range(len(tablero)):
        for caracter in tablero[i]:
            print(caracter, end="")
        print()



def comprobarSolucion(tablero, num_fila, copia_fila, num_col):
    i = 0
    #Comprueba que no hay filas que tengan casillas pintadas de más o por el contrario, hay de menos
    while i < len(num_fila):
        if num_fila[i] != 0:
            return False
        columna = 0
        contador = 0
        while columna < len(num_col) and contador < copia_fila[i]:
            #Si esa casilla está pintada, sumamos 1 a un contador para determinar un criterio de parada en el bucle
            if tablero[i][columna] == "#":
                contador += 1
            else:
                #Si ya había alguna casilla correctamente colocada y hay un hueco, no es solución
                if contador != 0:
                    return False
            columna += 1
        i += 1
    return True


#  Determina que las casillas que se vayan a colorear sean factibles
def esFactible(tablero, ini, fila_fin, num_fila, columna):
    i = 0
    #Esta lista guardará el número de fila que tenía en su columna anterior una casilla pintada para evitar espacios
    lista = []
    #Determina si en la anterior columna de cada fila había alguna casilla pintada y que debería tener una en su columna actual
    colocadoAnterior = False
    while i < len(num_fila) and columna > 0:
        #num_fila[i] sirve para comprobar si ya hemos terminado de colocar las casillas pintadas en esa fila
        if tablero[i][columna-1] == "#" and num_fila[i] > 0:
            colocadoAnterior = True
            #Guarda ese índice para después
            lista.append(i)
        i += 1
    #Si hay alguna fila cuya columna anterior está pintada y requiere de otra de manera consecutiva
    if colocadoAnterior:
        #Comprueba que no superemos el límite del tablero
        if fila_fin < len(num_fila):
            valido = False
            i = ini
            while i <= fila_fin:
                #Si hay alguna fila que no necesite más casillas no es factible
                if num_fila[i] <= 0:
                    return False
                if tablero[i][columna - 1] == "#":
                    valido = True
                    lista.remove(i)
                i += 1
            if lista:
                return False
            return valido
        return False

    if not colocadoAnterior or columna == 0:
        i = ini
        if fila_fin < len(num_fila):
            if num_col[columna] == 0 or num_col[columna] == len(num_col):
                return True
            while i <= fila_fin:
                if num_fila[i] <= 0:
                    return False
                i += 1
            return True
        return False


def nonogramaVA(tablero, num_fila, num_col, columna, copia_fila, filas):
    if columna >= len(num_col):
        esSol = comprobarSolucion(tablero, num_fila, copia_fila, num_col)

    else:
        esSol = False
        i = 0
        while i < len(filas) and not esSol:
            if esFactible(tablero, filas[i], filas[i] + (num_col[columna] - 1), num_fila, columna):
                if num_col[columna] != 0:
                    for a in range(filas[i], filas[i] + num_col[columna]):
                        tablero[a][columna] = "#"
                        num_fila[a] -= 1

                tablero, esSol = nonogramaVA(tablero, num_fila, num_col, columna + 1, copia_fila, filas)
                if not esSol:
                    for a in range(filas[i], filas[i] + num_col[columna]):
                        tablero[a][columna] = "-"
                        num_fila[a] += 1
            i += 1
    return tablero, esSol


filas, columnas = map(int, input().strip().split())
tablero = inicializarTablero(filas, columnas)
if (filas and columnas) > 0:
    num_fila = [int(x) for x in input().split()]
    num_col = [int(x) for x in input().split()]
    #  necesito una copia para el Factible
    filasOrden = list(range(len(num_fila)))

    i = 0
    contadorF = 0
    while i < len(num_fila):
        contadorF += num_fila[i]
        i += 1
    i = 0

    contadorC = 0
    while i < len(num_col):
        contadorC += num_col[i]
        i += 1

    if not (contadorC != contadorF or len(num_fila) != filas or len(num_col) != columnas):
        n_fila = num_fila[:]
        copia_fila = num_fila[:]
        ordenarListas(filasOrden, num_fila)
        # ORDENO POR NÚMERO DE CASILLAS EN NEGRO DE CADA FILA PARA IR PONIENDO A PARTIR DE AHÍ
        [tablero, esSol] = nonogramaVA(tablero, n_fila, num_col, 0, copia_fila, filasOrden)
        if esSol:
            pintarTablero(tablero)
        else:
            print("IMPOSIBLE")
    else:
        print("IMPOSIBLE")