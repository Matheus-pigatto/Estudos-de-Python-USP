import os
import cores as c


def menu():
    print('-' * 30)
    print(c.cor('2'), f'{"MENU PRINCIPAL":^30}', c.cor(0))
    print('-' * 30)


def conteudo():
    print(f'{c.cor(1)} 1{c.cor(0)} - {c.cor(3)} Ver pessoas cadastrdas {c.cor(0)}')
    print(f'{c.cor(1)} 2{c.cor(0)} - {c.cor(3)} Cadastrar nova Pessoa {c.cor(0)}')
    print(f'{c.cor(1)} 3{c.cor(0)} - {c.cor(3)} Sair do Sistema {c.cor(0)}')

print(os.listdir())
menu()
conteudo()
