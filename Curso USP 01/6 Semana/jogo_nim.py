def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print()
    print('1 - para jogar uma partida isolada \n2 - para jogar um campeonato ')
    while True:
        resp = int(input())
        if resp == 1:
            print('Você escolheu partida isolada\n')
            partida()
            break
        elif resp == 2:
            print('Você escolheu um campeonato!\n')
            campeonato()
            break
        else:
            print('Digite uma opção valida')


def partida():
    computador = 0
    jogador = 0
    cont = 1
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    if n % (m+1) == 0:
        print()
        print('Você começa!')
        while n != 0:
            if cont % 2 != 0:
                n -= usuario_escolhe_jogada(n, m)
                cont += 1
                if n == 0:
                    print('Jogador ganhou')
                    jogador = 1
                    break

            else:
                n -= computador_escolhe_jogada(n, m)
                cont += 1
                if n == 0:
                    print('Computador ganhou')
                    computador = 1
                    break

            if n == 1:
                print(f'Agora resta apenas uma peça no tabuleiro')
            else:
                print(f'Agora restam apenas {n} peças no tabuleiro')
    else:
        print()
        print('Computador começa! ')
        print()
        while n != 0:
            if cont % 2 != 0:
                n -= computador_escolhe_jogada(n, m)
                cont += 1
                if n == 0:
                    print('Fim do jogo! O computador ganhou')
                    computador = 1
                    break
            else:
                n -= usuario_escolhe_jogada(n, m)
                cont += 1
                if n == 0:
                    print('Fim do jogo! O Jogador ganhou')
                    jogador = 1
                    print()
                    break
            if n == 1:
                print(f'Agora resta apenas uma peça no tabuleiro')
                print()
            else:
                print(f'Agora restam apenas {n} peças no tabuleiro')
                print()
    return computador


def campeonato():
    contador_vitoria_computador = 0
    contador_vitoria_jogador = 0
    print(f'**** Rodada 1 ****\n')
    resultado = partida()
    print(resultado)
    if resultado == 0:
        contador_vitoria_jogador += 1
    else:
        contador_vitoria_computador += 1

    print(f'**** Rodada 2 ****\n')
    resultado = partida()
    if resultado == 0:
        contador_vitoria_jogador += 1
    else:
        contador_vitoria_computador += 1

    print(f'**** Rodada 3 ****\n')
    resultado = partida()
    if resultado == 0:
        contador_vitoria_jogador += 1
    else:
        contador_vitoria_computador += 1

    print('**** Final do campeonato!****\n')
    print(f'Placar:Você {contador_vitoria_jogador} X {contador_vitoria_computador} Computador')


def computador_escolhe_jogada(n, m):
    marcacao = False
    for i in range(1, m+1):
        #print(i)
        if (n-i) % (m+1) == 0:
            print(f'O computador tirou {i} peças.')
            marcacao = True
            return i

    if marcacao == False:
        print(f'O computador retirou {m} peças')
        print()
        return m


def usuario_escolhe_jogada(n, m):
    while True:
        r = int(input('Quantas peças você vai tirar? '))
        print()
        if r > m or r <= 0 or r > n:
            print('Oops! Jogada inválida! Tente de novo.\n')
        else:
            print(f'Você tirou {r} peças\n')
            break
    return r


main()