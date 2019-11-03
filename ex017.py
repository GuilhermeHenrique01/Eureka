from math import hypot

print('{} DESAFIO 017 {}'.format('='*16, '='*24))
print('{}'.format('	'*20))

print('Crie um programa que leia o cateto oposto e do cateto adjecente de um triangulo retangulo calcule e mostre o comprimento da Hipotenusa')
print('{}'.format('	'*20))

ost = float(input('-Digite o tamanho do cateto oposto: '))
adj = float(input('-Digite o tamanho do cateto adjecente: '))

print(f'*De acordo com os numeros digitados o cateto oposto é {ost} e o cateto adjecente {adj}, resultando ao valor da hipotenusa que é {hypot(ost, adj):.2f}')