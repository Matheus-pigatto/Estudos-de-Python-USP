n = int(input('Digite um número inteiro: '))
if n == 2 or n == 3 or n == 5 or n == 7:
    print('primo')
elif n // n == 1 and n // 1 == n and not(n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
    print('primo')
else:
    print('não primo')

