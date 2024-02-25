def ordenar_fila(matriz, fila):
    # Utilizamos el método de ordenación de selección para ordenar la fila específica
    n = len(matriz[fila])
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if matriz[fila][j] < matriz[fila][min_index]:
                min_index = j
        matriz[fila][i], matriz[fila][min_index] = matriz[fila][min_index], matriz[fila][i]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    # Definir una matriz bidimensional de 3x3 con valores numéricos
    matriz = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    # Mostrar la matriz original
    print("Matriz original:")
    mostrar_matriz(matriz)

    # Ordenar la fila 1 (índice 0) en orden ascendente
    ordenar_fila(matriz, 1)

    # Mostrar la matriz con la fila ordenada
    print("\nMatriz con la fila ordenada:")
    mostrar_matriz(matriz)

if __name__ == "__main__":
    main()