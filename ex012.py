print('{} DESAFIO 12 {}'.format('='*10, '='*15))
print('Faça um algoritmo que leia o valor de um produto e mostre seu novo preço com 5% de desconto.')

v = int(input('-Digite um valor a receber o desconto: R$'))

print(f'*O valor de R${v}, com 5% de desconto fica {v-(v*5/100):.2f}')