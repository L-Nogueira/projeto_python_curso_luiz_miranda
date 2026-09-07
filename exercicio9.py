import subprocess
palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0

while True:
    tentativas += 1

    chute = input('Digite uma letra: ')
    if len(chute) > 1:
        print('Digite apenas uma letra.')
        input('Aperte enter para continuar.')
        continue
        

    if chute in palavra_secreta:
        letras_acertadas += chute

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    if palavra_formada == palavra_secreta:
        subprocess.run('clear')
        print(f'Parabéns você acertou, a palavra era {palavra_secreta}!')
        if tentativas <= len(palavra_formada):
            print('UAU você não errou uma!!!')
            input('Aperte enter para encerrar.')
            break
        else:
            print(f'Foram necessárias {tentativas} tentativas.')
            input('Aperte enter para encerrar.')
            break


    else:
        print(palavra_formada)



