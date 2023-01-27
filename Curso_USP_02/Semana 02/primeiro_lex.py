def primeiro_lex(lista):
    lista = sorted(lista, key = str.lower)
    return lista[0]

primeiro_lex(['oĺá', 'A', 'a', 'casa'])