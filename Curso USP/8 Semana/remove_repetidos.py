def remove_repetidos(x):
    nlista = []
    n = 0
    t = 0
    while True:
        if x.count(x[n]) != 1:
            t = n + 1
            while t < len(x):
                if x[n] == x[t]:
                    x.pop(t)
                    t += 1
                else:
                    t += 1
        else:
            n += 1
            if n == len(x):
                break
    x.sort()
    return x

lista = [2, 4, 2, 2, 3, 3, 1]
novalista = remove_repetidos(lista)
lista = [1, 2, 3, 3, 3, 3, 4]
novalista = remove_repetidos(lista)
