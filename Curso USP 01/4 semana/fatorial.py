n = int(input('Digite o valor de n: '))
b = n
i = n-1
if n != 0:
    while i > 0:
        n = n * (b-i)
        i-=1
    print(n)
else:
    print(1)