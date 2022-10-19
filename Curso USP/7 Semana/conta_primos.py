def n_primos(n):
    cont = 0
    cont2 = 0
    i = 1
    while i <= n:
        for c in range(1, i+1):
            if i % c == 0:
                cont += 1
        if cont == 2:
            cont2 += 1
        cont = 0
        i += 1

    print(cont2)
    return cont2

n = int(input('Informe valor de n: '))
n_primos(n)

def test_nprimo():
    print()
    assert n_primos(4) == 2
    assert n_primos(5) == 3
    assert n_primos(7) == 4
    assert n_primos(15) == 6
    assert n_primos(121) == 30

