n = input('Digite um número inteiro: ')
casa_deci = len(n)
n = int(n)
total = 0
for c in range(casa_deci+1):
    rest1 = n // (10 ** (casa_deci-c))
    soma = rest1 % 10
    total += soma
print(total)