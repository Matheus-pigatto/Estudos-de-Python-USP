
def maior_primo(x):
    p = 0
    y = 1
    z = False
    if (éPrimo(x)) == True:
       return x
    else:
        while z == False:
            x-=1
            if éPrimo(x) == False:
                continue
            else:
                z = True

        return x


def éPrimo(n):
    x = False
    i = 2
    for i in range(i, n):
        if n % i == 0:
            x = False
            break
        else:
            x = True

    return x



x = maior_primo(961)
print(x)