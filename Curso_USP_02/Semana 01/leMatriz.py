def cria_matriz(num_linhas, num_colunas):
    ''' (int, int, valor) -> matriz ( lista de listas)
     Cria e retorna uma matriz com num_linhas linhas e num_colunas
     colunas em que cada elemento [e igual ao valor dado.
     '''
    matriz = [] # lista vazia
    for i in range(num_linhas):
        #cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas):
            valor = int(input(f'Digite o elemento [{i}][{j}]'))
            linha.append(valor)
    # adiciona linhas à matriz
        matriz.append(linha)
    return matriz

def le_matriz():
    lin = int(input('Digite o número de linhas da matriz: '))
    col = int(input('Digite o número de colunas da matriz: '))
    matriz = cria_matriz(lin, col)
    return matriz

def imprime_matriz():
    matriz = le_matriz()
    for i in matriz:
        print(f'{i}')

print(imprime_matriz())