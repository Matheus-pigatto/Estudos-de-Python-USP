def dimensoes(a):
    matriz = a
    ncolunas = len(matriz)
    temp_nlinhas = 0
    nlinhas = 0
    for linhas in matriz:
        nlinhas = len(linhas)
        if temp_nlinhas < nlinhas:
            temp_nlinhas = nlinhas
    nlinhas = temp_nlinhas
    print(f'{ncolunas}x{nlinhas}')



minha_matriz = [[1], [2], [3]]

dimensoes(minha_matriz)