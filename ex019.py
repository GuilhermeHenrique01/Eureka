from random import choices

print('{} DESAFIO 019 {}'.format('='*16, '='*24))
print('{}'.format('	'*20))

print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.')
print('{}'.format('	'*20))

a1 = input('-Aluno 1: ')
a2 = input('-Aluno 2: ')
a3 = input('-Aluno 3: ')
a4 = input('-Aluno 4: ')

print('{}'.format('	'*20))

print(f'*O aluno escolhido é {choices([a1, a2, a3, a4])}')