# AUTOR: Jorge Adame Prudencio
# TITULACION: Doble Grado en Ingenieria Informatica + Ingenieria del Software
# UNIVERSIDAD REY JUAN CARLOS
# CURSO: 2019/20
# ASIGNATURA: Diseño y Analisis de Algoritmos
# GRADO: Ingenieria del Software


# TODO ESTA SIN TILDES POR SI NO FUNCIONA POR LA CODIFICACION


#  Esta funcion forma parte del mergesort y ordena combinando los arrays recortados
def fusion(primero, segundo, salidaFilasOrden, izqNumFila, derNumFila, salidaNumFila):
    #  Centinelas. Como tienen ambos array el mismo tamaño y combinamos sincronamente
    primero.append(-float("inf"))
    segundo.append(-float("inf"))
    k = f = s = 0
    #  Si el 2º valor es mayor estricto que el primero, lo ponemos delante y a su vez las posiciones de filasOrden
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


#  Funcion mergesort en la que se ordena la lista de num_fila por tamaño de ocupacion (mayor a menor)
#  Esta ordenacion tambien se producira sobre filasOrden, que tendra los indices ordenados segun el valor de num_fila
def ordenarListas(num_fila, filasOrden):
    if len(filasOrden) < 2:
        return
    medio = len(filasOrden) // 2
    # Divide
    izqFilasOrden = filasOrden[:medio]  # copia desde 0 hasta mid
    izqNumFila = num_fila[:medio]
    derFilasOrden = filasOrden[medio:]
    derNumFila = num_fila[medio:]

    # Venceras
    ordenarListas(izqNumFila, izqFilasOrden)
    ordenarListas(derNumFila, derFilasOrden)

    # Combina
    fusion(izqFilasOrden, derFilasOrden, filasOrden, izqNumFila, derNumFila, num_fila)


#  Inicializa el tablero con casillas sin rellenar ("-")
def inicializarTablero(filas, columnas):
    tablero = []
    for _ in range(filas):
        tablero.append(["-"] * columnas)
    return tablero


#  Metodo que pinta el tablero
def pintarTablero(tablero):
    for i in range(len(tablero)):
        for caracter in tablero[i]:
            print(caracter, end="")
        print()


#  Funcion que comprueba que el nonograma cumpla las restricciones
def comprobarSolucion(tablero, num_fila, copia_fila, num_col):
    i = 0
    # Comprueba que no hay filas que tengan casillas pintadas de mas o por el contrario, hay de menos
    while i < len(num_fila):
        if num_fila[i] != 0:
            return False
        columna = 0
        #  El contador guardara cuantas casillas consecutivas estan pintadas
        contador = 0
        #  Si ya he comprobado que he pintado todas las casillas correspondientes al numero que habia en esa fila,
        #  puede tener casillas sin pintar despues
        while columna < len(num_col) and contador < copia_fila[i]:
            # Si esa casilla esta pintada, sumamos 1 a un contador para determinar un criterio de parada en el bucle
            if tablero[i][columna] == "#":
                contador += 1
            else:
                # Si ya habia alguna casilla correctamente colocada y hay otra vacia en medio, no es solucion
                if contador != 0:
                    return False
            columna += 1
        i += 1
    return True


#  Determina que las casillas que se vayan a pintar sean factibles
def esFactible(tablero, ini, fila_fin, num_col, num_fila, columna):
    i = 0
    #  Esta lista guardara el numero de fila que tiene en su columna anterior una casilla pintada para evitar espacios
    lista = []
    # Determina si en la anterior columna de cada fila habia alguna casilla pintada y que deberia tener una en la
    # columna en la que estamos
    colocadoAnterior = False
    while i < len(num_fila) and columna > 0:
        #  num_fila[i] sirve para comprobar si la casilla de la fila anterior esta pintada y debo seguir colocando mas
        if tablero[i][columna - 1] == "#" and num_fila[i] > 0:
            colocadoAnterior = True
            # Guarda este indice para despues
            lista.append(i)
        i += 1

    #  Si hay alguna fila cuya columna anterior esta pintada y requiere de otra de manera consecutiva
    if colocadoAnterior:
        #  Comprueba que no superemos el limite del tablero
        if fila_fin < len(num_fila):
            #  Valido va a comprobar que minimo en una fila ha encontrado una casilla cuya columna anterior este pintada
            valido = False
            i = ini
            #  Recorre todas las filas para comprobar que todas sean validas
            while i <= fila_fin:
                # Si hay alguna fila que no necesite mas casillas pintadas no es factible
                if num_fila[i] <= 0:
                    return False
                #  Si en todas puedo pintar en la fila una casilla comprobamos si esta pintada la columna anterior
                if tablero[i][columna - 1] == "#":
                    valido = True
                    lista.remove(i)
                i += 1
            #  Esta comprobacion se realiza para comprobar que haya pintado todas las filas cuya columna
            #  anterior estuviera pintada
            if lista:
                return False
            #  Si no he visto ninguna casilla pintada en la columna anterior de alguna fila pero no la ha comprobado, da fallo
            return valido
        #  Si se sale del tablero
        return False

    #  Si la columna es 0, no hay ninguna casilla cuya columna anterior este pintada
    #  Si no hay ninguna casilla pintada en la columna anterior

    if not colocadoAnterior or columna == 0:
        i = ini
        if fila_fin < len(num_fila):
            # Si no hay puede haber ninguna casilla pintada en esa columna, o bien tiene que pintar todas las filas de
            # esta columna y esta dentro del tablero, siempre es Verdadero
            if num_col[columna] == 0 or num_col[columna] == len(num_col):
                return True
            # Si hay alguna fila que no necesite  casillas pintadas no es factible
            while i <= fila_fin:
                if num_fila[i] <= 0:
                    return False
                i += 1
            #  Si cumple todas las restricciones, es valido
            return True
        return False


def nonogramaVA(tablero, num_fila, num_col, columna, copia_fila, filas):
    #  Si ya ha recorrido todas las columnas del tablero, comprueba que el nonograma cumple las condiciones
    if columna >= len(num_col):
        esSol = comprobarSolucion(tablero, num_fila, copia_fila, num_col)
    else:
        esSol = False
        i = 0
        #  Recorre la lista de numeros posibles de fila previamente ordenados por capacidad (Si una fila tiene 8
        #  y otra tiene 6, primero intentara colocar en la que tiene 8)
        while i < len(filas) and not esSol:
            #  Comprueba que desde esa fila hasta esa fila mas el numero de casillas que hay que pintar en esa columna
            #  sean validas
            if esFactible(tablero, filas[i], filas[i] + (num_col[columna] - 1), num_col, num_fila, columna):
                if num_col[columna] != 0:
                    #  Pinta todas las casillas que tiene esa columna
                    for a in range(filas[i], filas[i] + num_col[columna]):
                        tablero[a][columna] = "#"
                        #  Resta uno en el numero de casillas restantes por pintar
                        num_fila[a] -= 1
                # Llamada recursiva
                tablero, esSol = nonogramaVA(tablero, num_fila, num_col, columna + 1, copia_fila, filas)
                if not esSol:
                    #  Si no es solucion, vuelve a la situacion anterior a llegar a esa columna y comprueba mas posibilidades
                    for a in range(filas[i], filas[i] + num_col[columna]):
                        tablero[a][columna] = "-"
                        num_fila[a] += 1
            i += 1
    return tablero, esSol


def iniciarAlgoritmo():
    #  Recibe el numero de filas y de columnas que tendra el nonograma
    filas, columnas = map(int, input().strip().split())
    tablero = inicializarTablero(filas, columnas)
    #  Si no hay filas o columnas
    num_fila = [int(x) for x in input().split()]
    num_col = [int(x) for x in input().split()]
    #  Crea una lista ordenada ascendente del numero de filas que tiene el nonograma
    filasOrden = list(range(len(num_fila)))

    #  Cuenta el numero casillas pintadas totales de todas las filas
    i = 0
    contadorF = 0
    while i < len(num_fila):
        contadorF += num_fila[i]
        i += 1
    i = 0

    #  Cuenta el numero casillas pintadas totales de todas las columnas
    contadorC = 0
    while i < len(num_col):
        contadorC += num_col[i]
        i += 1

    #  Si hay que pintar mas casillas en las columnas que en las filas, o se introducen mas datos de los dichos,
    #  es imposible
    if not (contadorC != contadorF or len(num_fila) != filas or len(num_col) != columnas):
        #  Guardan una copia de los valores de cada fila
        n_fila = num_fila[:]
        copia_fila = num_fila[:]
        #  Las listas se van a ordenar porque por estadistica, si una fila necesita mas casillas pintadas es probable
        #  que comenzando por esa casilla llegue antes a la solucion
        ordenarListas(filasOrden, num_fila)
        #  Ejecucion de la Vuelta Atras
        [tablero, esSol] = nonogramaVA(tablero, n_fila, num_col, 0, copia_fila, filasOrden)
        #  Si hay solucion, se escribe por pantalla
        if esSol:
            pintarTablero(tablero)
        else:
            # En caso contrario, pintamos IMPOSIBLE
            print("IMPOSIBLE")
    else:
        print("IMPOSIBLE")


#  Funcion que ejecuta el algoritmo entero
iniciarAlgoritmo()
