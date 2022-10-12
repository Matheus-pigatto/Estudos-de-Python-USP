x = int(input('digite a largura: '))
y = int(input('digite a altura: '))
cont = cont2 = 0
while cont < y:
    while cont2 < x:
        print('#', end="")
        cont2 += 1
    print()
    cont += 1
    cont2 = 0