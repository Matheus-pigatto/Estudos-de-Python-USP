def cor(c):
    c = str(c)
    cores = {'1': '\033[1;93m', # amarelo
             '2': '\033[1;32m', #verde
             '3': '\033[1;34m', #azul
             '4': '\033[1;35m', #magenta
             '5': '\033[1;36m', #cy
             '6': '\033[1;94m', #azul claro
             '0': '\033[m'
             }

    return (cores[c])
