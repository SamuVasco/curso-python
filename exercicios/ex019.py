from random import choice
n1 = input('Digite um nome: ')
n2 = input('Digite um nome: ')
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')
lista = [n1, n2, n3, n4]
sorteio = choice(lista)
print(f'O escolhido(a) foi: {sorteio}')
