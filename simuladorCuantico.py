import math
from matplotlib import pyplot as plt
from Complex_Vector_Spaces import *

"""
El salto de lo clasico a lo cuantico - CNYT
Autor: Kristhian Segura
Fecha: 5/03/2021
"""

"""
Funcion para obtener la transpuesta de una matriz o un vector
param: matriz o vector que se desea trasponer
return: resultado, matriz o vector transpuesto
"""


def transpuesta(matriz):
    if isinstance(matriz[0], int):
        resultado = [[0 for j in range(1)] for i in range(len(matriz))]

        for i in range(len(resultado)):
            for j in range(1):
                resultado[i][j] = matriz[i]

        return resultado

    elif len(matriz[0]) == 1:
        resultado = []
        for i in range(len(matriz)):
            for j in range(1):
                resultado.append(matriz[i][j])
        return resultado

    else:
        filas = len(matriz)
        columnas = len(matriz[0])
        if filas == columnas:
            result = [[0 for j in range(columnas)] for i in range(filas)]

        else:
            result = [[0 for j in range(filas)] for i in range(columnas)]

        for i in range(filas):
            for j in range(columnas):
                result[j][i] = matriz[i][j]

        return result


"""
Funcion para obtener el producto entre dos matrices de tamaños compatibles
param: m1, la matriz de numeros reales que se va a operar en el lado izquierdo
param: m2, la matriz de numeros reales que se va a operar en el lado derecho
return: resultado, el producto entre ambas matrices
"""


def productoMatrices(m1, m2):
    filasM1 = len(m1)
    filasM2 = len(m2)
    columnasM1 = len(m1[0])
    columnasM2 = len(m2[0])

    assert columnasM1 == filasM2, "Las matrices no son compatibles para hacer un producto entre ellas"

    resultado = [[0 for j in range(columnasM2)] for i in range(filasM1)]

    for i in range(filasM1):
        for j in range(columnasM2):
            suma = 0
            for k in range(filasM2):
                suma += (m1[i][k] * m2[k][j])
            resultado[i][j] = suma

    return resultado


"""
Funcion para obtener el resultado de multiplicar 
un escalar por una matriz
param: escalar, el numero por el cual se quiere multiplicar la matriz
param: matriz, la matriz de numeros reales a la que se le quiere hacer el producto por el escalar
return: resultado, el resultado de multiplicar el escalar por la matriz
"""


def escalarXMatriz(escalar, matriz):
    resultado = [[0 for j in range(len(matriz[0]))] for i in range(len(matriz))]

    for i in range(len(resultado)):
        for j in range(len(resultado[0])):
            resultado[i][j] = escalar * matriz[i][j]

    return resultado


"""
Funcion para crear la matriz probabilistica
param: nRendijas, numero de rendijas que va a tener el experimento
param: nBlancos, numero de blancos que va a tener el experimento
return: matrizResultado, la matriz resultante 
"""


def crearMatrizProb(nRendijas, nBlancos):
    total = nRendijas + nBlancos + 1
    probRendija = 1 / nRendijas
    probBlanco = 1 / 3
    matrizResultado = [[0 for j in range(total)] for i in range(total)]
    cont = 0
    contR = 1
    col = 1
    inicio = nRendijas + 1

    for i in range(1, nRendijas + 1):
        matrizResultado[i][0] = probRendija

    for i in range(nRendijas + 1, nRendijas + nBlancos + 1):
        for j in range(1, nRendijas + 1):
            if j == col:
                matrizResultado[i][j] = probBlanco
                cont += 1

            if cont == 3 and contR < nRendijas:
                col += 1
                cont = 0
                contR += 1

    for i in range(total):
        for j in range(total):
            if i == inicio and j == inicio:
                matrizResultado[i][j] = 1
                inicio += 1

    return matrizResultado


"""
"""


def crearMatrizCuant(nRendijas, nBlancos):
    total = nRendijas + nBlancos + 1
    probRendija = (1 / math.sqrt(nRendijas), 0)
    probBlanco = [(-1 / math.sqrt(6), 1 / math.sqrt(6)),
                  (-1 / math.sqrt(6), -1 / math.sqrt(6)),
                  (1 / math.sqrt(6), -1 / math.sqrt(6))]
    matrizResultado = [[(0, 0) for j in range(total)] for i in range(total)]
    cont = 0
    contR = 1
    contB = 0
    col = 1
    inicio = nRendijas + 1

    for i in range(1, nRendijas + 1):
        matrizResultado[i][0] = probRendija

    for i in range(nRendijas + 1, nRendijas + nBlancos + 1):
        for j in range(1, nRendijas + 1):
            if j == col:
                matrizResultado[i][j] = probBlanco[contB]
                contB += 1
                cont += 1

            if cont == 3 and contR < nRendijas:
                col += 1
                cont = 0
                contB = 0
                contR += 1

    for i in range(total):
        for j in range(total):
            if i == inicio and j == inicio:
                matrizResultado[i][j] = (1, 0)
                inicio += 1

    return matrizResultado


"""
Funcion para realizar el experimento de las canicas 
param: matriz, matriz de adyacencia
param: vector_col, el vector de estados
param: clicks, la cantidad de veces que se quiere realizar el experimento
return: resultado, la matriz resultado
"""


def operarClicksSistemaD(matriz, vector_col, clicks):
    resultado = productoMatrices(matriz, vector_col)
    if clicks == 0:
        return matriz
    else:
        for i in range(clicks - 1):
            resultado = productoMatrices(matriz, resultado)

        return resultado


"""
Funcion de las multiples rendijas clásico probabilístico, con más de dos rendijas
param: rendijas, el numero de rendijias del experimento
param: blancos, el numero de blancos que va a haber en el experimento
param: clicks, el numero de veces que se quiere realizar el experimento
return: tupla, contiene la matriz resultante y el vector de estados resultante
"""


def operarClicksSistemaP(rendijas, blancos, clicks):
    matriz = crearMatrizProb(rendijas, blancos)
    vector = [0 for i in range(len(matriz))]
    vector[0] = 1
    vectorCol = transpuesta(vector)
    matrizResultado = productoMatrices(matriz, matriz)

    if clicks == 0:
        return matriz, vectorCol
    else:
        for times in range(clicks - 1):
            matrizResultado = productoMatrices(matriz, matrizResultado)

        vectorCol = productoMatrices(matrizResultado, vectorCol)

        return matrizResultado, vectorCol


def operarClicksSistemaC(rendijas, blancos, clicks):
    matriz = crearMatrizCuant(rendijas, blancos)
    matrizResultado = productoMatricesComp(matriz, matriz)
    vectorCol = [[(0, 0) for j in range(1)] for i in range(len(matriz))]
    vectorCol[0][0] = (1, 0)

    if clicks == 0:
        return matriz, vectorCol
    else:
        for times in range(clicks - 1):
            matrizResultado = productoMatricesComp(matriz, matrizResultado)

        vectorCol = productoMatricesComp(matrizResultado, vectorCol)

        return matrizResultado, vectorCol


"""
Funcion para hacer una grafica de barras del vector de estados
param: valores, el vector de valores de estados
"""


def graficarEstados(valores):
    posiciones = [i for i in range(len(valores))]
    plt.bar(posiciones, valores, color="#8848FF", label="Probabilidades")
    plt.legend()
    plt.title("Probabilidades del vector de estados")
    plt.xlabel("Posicion")
    plt.ylabel("Probabilidad")
    plt.show()


def imprimirMatriz(matriz):
    for i in matriz:
        print(i)
    print()


def main():
    print(operarClicksSistemaC(2, 5, 1)[1])


if __name__ == '__main__':
    main()
