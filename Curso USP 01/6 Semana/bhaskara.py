import math


def delta(a, b, c):
    return b**2-4*a*c


def main():
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    imprime_raizes(a, b, c)


def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    print('delta:', d)
    if d < 0:
        print('Esta equação não possui raízes reais')
    elif d == 0:
        x1 = (-b + d) / (2 * a)
        x2 = (-b - d) / (2 * a)
        print(f'a raiz dupla desta equação é {x1} = {x2}')
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        if x1 > x2:
            print(f'as raízes da equação são {x2} e {x1}')
        else:
            print(f'as raízes da equação são {x1} e {x2}')


main()
