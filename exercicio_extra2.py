#gerenciador de login básico
import subprocess
user_and_password = {}
tentativas = 0

while True:
    subprocess.run('clear')

    saudacao = 'BEM VINDO AO SISTEMA DE LOGIN'
    print('=' * 50)
    print(f'{saudacao:-^50}')
    print('=' * 50)

    print('MENU:\n' \
    '1. Cadastrar usuário\n' \
    '2. Fazer login\n' \
    '3. Sair\n')

    try:
        opcao = int(input('Escolha uma das opções do menu acima: '))
    except:
        print('Por favor, digite apenas números inteiros entre 1 e 4.')
        input('Aperte enter para voltar ao menu.')
        continue
    if opcao == 1:
        email = input('E-mail: ')
        senha = input('Senha: ')
        user_and_password.update({email:senha})
        input('Aperte enter para continuar.')
        continue

    elif opcao == 2:
        print('Forneça seu e-mail e senha para logar.')
        entrada_email = input('E-mail: ')
        entrada_senha = input('Senha: ')

        if entrada_email in user_and_password and entrada_senha == user_and_password.get(email):
            print('Acesso concedido.')
            input('Pressione enter para continuar.')
        else:
            print('Acesso negado.')
            tentativas += 1
            if tentativas == 3:
                print('Esqueceu a senha?')
            input('Pressione enter para continuar.')

    
    if opcao == 3:
        break
