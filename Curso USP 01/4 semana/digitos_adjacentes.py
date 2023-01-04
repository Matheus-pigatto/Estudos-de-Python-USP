n = input('Digite um número inteiro: ')
a = len(n)
n = int(n)
c = 1
anterior = 0
adjacentes = False
if a > 1:
    while c != a+1:
        divint = n // 10**(a-c)
        resto = divint % 10
        if anterior == resto:
            anterior = resto
            adjacentes = True
        else:
            anterior = resto
        c += 1
    if adjacentes == True:
        print('sim')

    else:
        print('não')
else:
    print('não')

    print('sera que vai')