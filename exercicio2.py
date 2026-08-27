'''
This exercise has as goal develop a simple calculator to verify the BMI of a person
'''

name = 'Greg'
heigh = 1.80
weigh = 95
bmi = weigh / (heigh**2)

print(f'{name} is {heigh:.2f} m tall,')
print(f'He has {weigh} kg')
print(f'and his BMI is: {bmi:.2f}')

'''
A formatação com f-string possúi uma sintaxe própria que permite definir
elementos para preenchimento de espaçõs.
O alinhamento (< ^ >), a largura do espaçamento, o separador (. , _), 
a precisão e o tipo de dado.

Mas só funciona se estiver na órdem certa 
:[preenchimento][alinhamento][largura][separador][.precisão][tipo]

Exemplo usando preenchimento, alinhamento, largura, separador, precisão e tipo

itens = [('Processador', 1200.0), ('RAM 16GB', 700.25), ('SSD 1TB', 500.50)]

print(f'{'Item':-<20}{'Preço':->12}')
print('-' * 32)
for item, preco in itens:
    print(f'{item:.<20}R${preco:>9,.2f}')
'''