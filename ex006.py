print('{} DESAFIO 006 {}'.format('='*10, '='*15))
print('Crie um algoritimo que leia um nuemero e mostre p seu dobro, triplo e raiz quadrada.')

n = int(input('-Digite um numero: '))
#d = n * 2
#t = n * 3
#r = n ** (1/2)

#print('*Dobro: {}, Triplo: {}, Raiz Quadrada: {:.2f}'.format(n * 2, n * 3, n**(1/2)))

#print('*Raiz Quadrada: {:.2f}'.format(pow(n , (1/2))))

print(f'*O dobro do numero {n} é {n*2} \nO triplo do numero {n} é {n*3} \nA Raiz quadrada do numero {n} é {pow(n, (1/2)):.2f}')