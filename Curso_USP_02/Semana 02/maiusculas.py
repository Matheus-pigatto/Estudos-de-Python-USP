def maiusculas(frase):
    texto = list(frase)
    tabela_maiuscula = []
    n = 0


    for letras in texto:
        n = ord(letras)
        tabela_ascii = n > 64 and n < 91
        if tabela_ascii:
            tabela_maiuscula.append(chr(n))
    tabela_maiuscula = ''.join(tabela_maiuscula)
    return tabela_maiuscula



x = maiusculas('PrOgRaMaMoS em python!')
