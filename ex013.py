print('{} DESAFIO 13 {}'.format('='*10, '='*15))
print('Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de desconto.')

s = float(input('-Qual o valor atual do seu salario? R$'))

print(f'*Com o seu salario atual de R${s}, aumentando 15% de desconto fica R${s+(s*15/100):.2f}.')