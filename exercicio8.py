frase = 'O Python é uma linguagem de programação ' \
'multiparadigma. ' \
'Python foi criado por Guido van Rossum.'

i = 0
frase_sem_espaços = frase.replace(' ', '')

anterior = 0
aparece_mais = ''

while i < len(frase_sem_espaços):
    letra_atual = frase_sem_espaços[i]
    quantas_vezes_letra = frase_sem_espaços.count(letra_atual)

    if quantas_vezes_letra > anterior:
        anterior = quantas_vezes_letra
        aparece_mais = letra_atual

    i += 1

print(f'A letra que aparece mais é ({aparece_mais}), ela surge na frase {anterior} vezes!')