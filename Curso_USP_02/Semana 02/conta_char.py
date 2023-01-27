def conta_letras(frase, conta="vogais"):
    texto = list(frase.strip().lower().replace(" ", ""))
    n_letras = len(texto)
    contador_vogais = 0
    contador_consoantes = 0
    vogais = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    print(n_letras)
    if conta == 'vogais':
        for letras in texto:
            if letras in vogais:
                contador_vogais += 1
        print(contador_vogais)
        return contador_vogais
    else:
        for letras in texto:
            if letras in vogais:
                contador_vogais += 1
        contador_consoantes = n_letras - contador_vogais
        print(contador_consoantes)
        return contador_consoantes


conta_letras('programamos em python', 'consoante')
