valor = float(input('Qul o valor do produto? '))
porcentagem = valor * 10 / 100
desconto = valor - porcentagem
print('O valor do produto com o desconto de 10% fica de {:.2f}'.format(desconto))