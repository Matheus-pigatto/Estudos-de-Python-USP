def primo(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        print('primo')
    elif n // n == 1 and n // 1 == n and not (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
        print('primo')
    else:
        print('não primo')

n = int(input('Digite um número inteiro >1 : '))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n/fator
    if multiplicidade > 0 :
        print(f'fator {fator} multiplicidade = {multiplicidade}')
        primo(fator)

    fator = fator + 1
    multiplicidade = 0