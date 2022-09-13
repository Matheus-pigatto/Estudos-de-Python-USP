c = int(input('Digite o valor de n: '))
n = 0
while c > 0:
    r = n % 2
    if r != 0:
        print(n)
        c -= 1
        n += 1
    else:
        n += 1

