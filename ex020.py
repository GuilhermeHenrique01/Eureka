from random import sample

print('{} DESAFIO 020 {}'.format('='*16, '='*24))
print('{}'.format('	'*20))

print('O mesmo professor do desafio anterior quer sortear a ordem de apresentações do trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')

a1 = input('-Aluno 1: ')
a2 = input('-Aluno 2: ')
a3 = input('-Aluno 3: ')
a4 = input('-Aluno 4: ')
s = [a1, a2, a3, a4]

print('{}'.format('	'*20))

print(f'|A ordem sorteada para o trabalho foi {sample(s, 4)}.')