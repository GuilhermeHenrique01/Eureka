print('{} DESAFIO 11 {}'.format('='*10, '='*15))

print('Faça uma programa que leia a altura e largura em metros. Calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta 2m quadrados ')

a = float(input('-Quanto mede sua parede em altura? '))
l = float(input('-E de largura? '))

print(f'*Para pintar uma parede de {a}m de altura e {l}m de largura, precisa-sa de {a*l/2:.2f} Litros de tinta.')