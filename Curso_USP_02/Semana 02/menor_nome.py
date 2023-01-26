def menor_nome(nomes):
    lista_nomes = nomes
    tamanho_nome_lista = []
    posicao_menor = 0
    posicao = 0
    menor = 0
    for nomes in lista_nomes:
        lista_nomes.pop(posicao)
        lista_nomes.insert(posicao, nomes.strip().capitalize())
        posicao += 1
    for nomes in lista_nomes:
        tamanho_nome_lista.append(len(nomes))


    for numero in tamanho_nome_lista:
        
        if posicao_menor == 0:

            posicao_menor = numero
            #print(posicao_menor)
        elif numero < posicao_menor:
            posicao_menor = numero
            #print(posicao_menor)

    posicao_menor = tamanho_nome_lista.index(posicao_menor)

    menor = lista_nomes[posicao_menor]

    return menor






menor_nome(['zé', ' lu', 'fê'])