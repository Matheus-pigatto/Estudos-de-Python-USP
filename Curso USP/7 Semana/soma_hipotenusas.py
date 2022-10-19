from math import sqrt
def éhipotenusa(x):
    f = True
    cont = 0
    cont2 = 1
    while f == True:
        for a in range(1, x+1):
            for b in range(1, x+1):
                z = a**2 + b**2
                cont2 += 1
                #print(f'{z}={a}²+{b}²')
                #print(cont2)
                if x == sqrt(z):
                    cont = x
                    f = False
                    break
                if cont2 >= x:
                    f = False

    #print(cont)
    return cont
def soma_hipotenusas(x):
    y = 1
    soma = 0
    while y <= x:
        #print(y)
        z = éhipotenusa(y)
        if z != 0:
            soma += z
            #print(z)
        y+=1
    print(soma)
    return soma

#éhipotenusa(1)
soma_hipotenusas(25)

#def test_soma_hipotenusa():
#    assert soma_hipotenusas(5) == 5
#    assert soma_hipotenusas(10) == 15
#    assert soma_hipotenusas(13) == 28
#    assert soma_hipotenusas(25) == 105