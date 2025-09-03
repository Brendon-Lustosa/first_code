a = float(input('Qual a sua altura? '))
p = float(input('Qual o seu peso? '))
imc = a / p ** 2
print('Seu imc é de {:.2f}'.format(imc))