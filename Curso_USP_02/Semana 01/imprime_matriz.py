def imprime_matriz(matriz):
    tamanho_matriz = len(matriz[1])
    sublista = []
    if tamanho_matriz == 1:
        for i in matriz:
            sublista = i
            for j in sublista:
                print(j)
    else:
        for i in matriz:
            sublista = i
            for j in sublista:
                print(j, end=' ')
            print()
            sublista.clear()


print(imprime_matriz([[1, 2], [4, 3]]))
