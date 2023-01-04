n1 = int(input('Digite 1º número: '))
n2 = int(input('Digite 2º número: '))
n3 =int(input('Digite 3º número: '))

if n3 > n2:
    if n2 > n1:
        print('Crescente')
    else:
        print('não está em ordem crescente')
else:
    print('não está em ordem crescente')