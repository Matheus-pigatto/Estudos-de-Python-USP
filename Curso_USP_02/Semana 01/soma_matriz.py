def soma_matrizes(m1, m2):
    dm1 = dimensoes_matriz(m1)
    dm2 = dimensoes_matriz(m2)

    if dm2 == dm1 == (1, 1):
        nova_matriz = [m1[0]+m2[0]]
        return nova_matriz

    elif dm2 == dm1 != (1, 1):
        nova_matriz = []
        temp_matriz = []
        for x, y in enumerate(m1):
            for z, w in enumerate(y):
                temp_matriz.append(w + m2[x][z])
            nova_matriz.append(temp_matriz[:])
            temp_matriz.clear()
        print(nova_matriz)
        return nova_matriz
    else:
        print(False)
        return False

def dimensoes_matriz(x):
    matriz = x
    ncolunas = len(matriz)
    temp_nlinhas = 0
    nlinhas = 0
    if ncolunas != 1:
        for linhas in matriz:
            nlinhas = len(linhas)
            if temp_nlinhas == 0:
                temp_nlinhas = nlinhas
            if temp_nlinhas == nlinhas:
                pass
            elif temp_nlinhas > nlinhas:
                temp_nlinhas = nlinhas
        nlinhas = temp_nlinhas
    else:
        nlinhas = ncolunas
    return ncolunas, nlinhas


m1 = [1]
m2 = [3]
print(soma_matrizes(m1, m2))
