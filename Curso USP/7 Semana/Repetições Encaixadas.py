def fatorial(n):
    b = n
    i = n - 1
    if n != 0:
        while i > 0:
            n = n * (b - i)
            i -= 1
        print(n)
    else:
        print(1)

def lernumero():
    n = int(input('Digite um número inteiro: '))
    return n

n = 1
while n >= 0:
    n = lernumero()
    fatorial(n)
