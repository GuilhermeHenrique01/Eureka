from math import cos, sin, tan

print('{} DESAFIO 018 {}'.format('='*16, '='*24))
print('{}'.format('	'*20))

print('Faça um programa que leia um qualquer e mostre na tela o valor do seno cosseno e tangente.')
print('{}'.format('	'*20))

a = float(input('-Digite o angulo: '))
print('{}'.format('	'*20))

print(f'*Cosseno: {cos(a):.2f} \n*Seno: {sin(a):.2f} \n*Tangente: {tan(a):.2f}')