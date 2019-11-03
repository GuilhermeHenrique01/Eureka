print('{} DESAFIO 015 {}'.format('='*16, '='*24))
print('{}'.format('	'*20))

print('Escreva um programa que pergunte a quantidade de km percorridos por um carro aluga e a quantidade de dia pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0.15 por km rodado')

d = int(input('-Quantos dias o carro foi alugado? '))
km = float(input('-Quantos km foram rodados? '))
print('{}'.format('	'*20))

print(f'*Com base nos valores digitados acima o total a pagar é R${(60*d)+ km*0.15:.2f}')