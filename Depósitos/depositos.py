# AUTOR: Jorge Adame Prudencio
# TITULACION: Doble Grado en Ingenieria Informatica + Ingenieria del Software
# UNIVERSIDAD REY JUAN CARLOS
# CURSO: 2019/20
# ASIGNATURA: Diseño y Analisis de Algoritmos
# GRADO: Ingenieria del Software

# TODO ESTA SIN TILDES POR SI NO FUNCIONA POR LA CODIFICACION


def rec_binarySearch(e, elements):
    return __rec_bs__(e, 0, len(elements) - 1, elements)


def __rec_bs__(e, start, end, elements):
    # Si no hay volumen, no hay ninguna parte de los depositos lleno. Por tanto, altura 0
    if e == 0:
        return 0
    mid = (start + end) // 2
    if elements[mid] == e:
        # El índice siempre es 1 mayor que la posicion en el array, ya que este ultimo empieza en 0
        return mid + 1
    elif elements[mid] > e:
        return __rec_bs__(e, start, mid - 1, elements)
    else:
        return __rec_bs__(e, mid + 1, end, elements)


def iniciarAlgoritmo():
    volumen = int(input())
    depositos = int(input())
    base = []
    altura = []

    # Guarda la altura máxima para poder crear un array donde guarda el volumen necesario para llenar cada nivel
    filaMax = 0
    for _ in range(depositos):
        columna, fila = map(int, input().strip().split())
        base.append(columna)
        altura.append(fila)
        if fila >= filaMax:
            filaMax = fila
    volumenesNivel = [0] * filaMax
    # Guarda en el vector de los niveles de volumen el valor de la base(el numero de columna) en la altura maxima de ese
    # depósito. Esto se hace para saber que de ahí hacia abajo esa base se sumara en los niveles inferiores
    for i in range(len(base)):
        volumenesNivel[altura[i] - 1] += base[i]

    # Acumula el volumen que hay en cada nivel
    for i in range(len(volumenesNivel) - 2, -1, -1):
        if volumenesNivel[i] == 0:
            # Si en i no empieza ningun deposito nuevo, conservamos el valor del volumen del nivel superior
            volumenesNivel[i] = volumenesNivel[i + 1]
        else:
            # Si aparece un nuevo deposito que tenia menor altura, se suma ese valor y si no hay mas depositos nuevos,
            # conserva ese valor para el resto de alturas
            volumenesNivel[i] += volumenesNivel[i + 1]

    # Calcula el volumen necesario para llenar cada nivel, empezando ahora por el nivel mas bajo
    # e incrementando las alturas de cada nivel
    for i in range(1, len(volumenesNivel)):
        volumenesNivel[i] += volumenesNivel[i - 1]

    # Para saber hasta que nivel puedo llenar, se usa la busqueda binaria
    index = rec_binarySearch(volumen, volumenesNivel)
    print(index)


# Llamada al algoritmo
iniciarAlgoritmo()
