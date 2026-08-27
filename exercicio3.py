#exercício para prática de condicionais e operadores de comparação

#inputs do usuário
valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

try:
#conversão explícita de tipos com verificação da entrada
    valor1_int = int(valor1)
    valor2_int = int(valor2)


    #condicionais para comparação do maior e menor valor
    if valor1_int > valor2_int:
        print(f'O primeiro valor = {valor1_int}, é maior que o segundo valor = {valor2_int}!')

    elif valor2_int > valor1_int:
        print(f'O segundo valor = {valor2_int}, é maior que o primeiro valor = {valor1_int}!')

    else:
        print(f'O primeiro e o segundo valor, são iguais: {valor1_int}.')

except:
    print('Algum, ou ambos os caracteres fornecidos, não são numéricos.')