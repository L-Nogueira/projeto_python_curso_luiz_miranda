#Parte 1 solicitação e conferência de um número inteiro

numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    texto_par_impar = 'par' if numero_int % 2 == 0 else 'impar'

    print(f'O número {numero_int}, é {texto_par_impar}.')

except:
    try:
        numero_float = float(numero)
        print(f'O número {numero_float}, não é inteiro.')
    except:
        print(f'Você não digitou um número.')


print('\n')

#--------------------------------------------------------------------------
#Solicitação da hora ao usuário e saudação adaptativa

print('=' * 30)
hora = input('Digite a hora atual no formato (24h) sem os minutos: ')

try:
    hora_num = int(hora)
    if hora_num >= 0 and hora_num <= 11:
        print('Bom dia!!!')
    elif hora_num >=12 and hora_num <=17:
        print('Boa tarde!!!')
    elif hora_num >=18 and hora_num <=23:
        print('Boa noite!!!')
    else:
        print(f'O valor {hora_num}, não é um horário válido.')
except:
    print('O(s) caractére(s) digitado(s) não é/são numérico(s).')

print('\n')

#---------------------------------------------------------------------
#Pedir o nome do usuário, e avaliar o tamanho do nome

print('=' * 30)
nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(nome)
try:
    if nome.isalpha():
        if tamanho_nome <= 4:
            print('O seu nome é curto.')
        elif tamanho_nome >= 5 and tamanho_nome <=6:
            print ('Seu nome é normal.')
        elif tamanho_nome > 6:
            print ('Seu nome é muito grande.')
    else:
        print('Digite somente caracteres alfabéticos.')
except:
    print(f'{Exception}')
