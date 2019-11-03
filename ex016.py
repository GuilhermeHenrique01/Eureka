from math import trunc

print('{} DESAFIO 016 {}'.format('='*16, '='*24))
print('{}'.format('	'*20))

print('Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.')
print('{}'.format('	'*20))

n = float(input('-Digite um numero: '))
print('{}'.format('	'*20)print(f'A porção inteira do numero {n:.2f} é {trunc(n)}')