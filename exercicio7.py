#Importação do módulo subprocess para fazer a plimpeza do terminal após cada execução
import subprocess

#Loop que irá executar o menu ate que o usuário escolha sair (opção 5)
while True:
    subprocess.run('clear')

    #Cabeçalho formatado e opções do menu
    saudacao = ' BEM VINDO A CALCULADORA EM PYTHON '
    print('-' * 50)
    print(f'{saudacao:=^50}')
    print('-' * 50)

    print('MENU:\n' \
    '1. Somar\n' \
    '2. Subtrair\n' \
    '3. Multiplicar\n' \
    '4. Dividir\n' \
    '5. Sair\n')

    #Input do usuário para escolha da opção do menu
    opcao = input('Escolha a opção desejada: ')

    #O try sera executado somente se a entrada do usuário puder ser convertida para int, ou seja
    #se for uma string composta somente por números inteiros.
    try:
        opcao_int = int(opcao)

        #Condicional para avaliar o valor da entrada do usuário e direcionar à opção do menu
        if opcao_int > 0  and opcao_int <= 5:
            if opcao_int == 5:
                break

            prim_num = float(input('Digite o primeiro número: '))
            seg_num = float(input('Digite o segundo número: '))

            if opcao_int == 1:
                resultado = prim_num + seg_num
                print('-' * 50 )
                print(f'RESULTADO: {prim_num} + {seg_num} = {resultado}\n')
                input('Aperte enter para continuar.')

            elif opcao_int == 2:
                resultado = prim_num - seg_num
                print('-' * 50 )
                print(f'RESULTADO: {prim_num} - {seg_num} = {resultado}\n')
                input('Aperte enter para continuar.')


            elif opcao_int == 3:
                resultado = prim_num * seg_num
                print('-' * 50 )
                print(f'RESULTADO: {prim_num} x {seg_num} = {resultado}\n')
                input('Aperte enter para continuar.')


            elif opcao_int == 4:
                resultado = prim_num / seg_num
                print('-' * 50 )
                print(f'RESULTADO: {prim_num} / {seg_num} = {resultado:.2f}\n')
                input('Aperte enter para continuar.')

        else:
            print('Por favor digite uma opção entre 1 e 5.')
            input('Aperte enter para continuar.')

    #O except será executado se o usuário digitar qualquer coisa diferente de um número inteiro
    except:
        print('Por favor digite somente números.')
        input('Aperte enter para continuar.')

