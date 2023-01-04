x = int(input('digite a largura: '))
y = int(input('digite a altura: '))
cont = cont2 = 0
while cont < y:
    while cont2 < x:
        if cont == 0 or cont == y - 1:
            print('#', end="")
        else:
            if cont2 == 0 or cont2 == x - 1:
                print('#', end="")
            else:
                print(' ', end='')
        cont2 += 1
    print()
    cont += 1
    cont2 = 0