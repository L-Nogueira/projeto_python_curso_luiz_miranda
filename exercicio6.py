#Utilizando while para iterar sobre strings
''' Declaração da variável à ser iterada, da variável de controle e da variável que vai armazenar
o resultado da operação desejada. '''

nome = 'Lavouisier Nogueira'
i = 0
nova_string = ''

''' Declaração do loop, usando i como variável de controle, e iterando sobre {nome}, enquanto
i < que o tamanho de {nome}.'''

while i < len(nome):
    nova_string += '*' + nome[i]
    i += 1

'''Print do resultado.'''
print(nova_string)