x = 1
lista = []
while x != 0:
    x = int(input('Digite um número:'))
    if x != 0:
        lista.append(x)
n = len(lista) - 1
print()
while n > -1:
    print(lista[n])
    n -= 1
