#O objetivo deste exercício é demonstrar que o excesso de complexiidade em expressões condicionais 
#dificulta o entendimento do código, e mostrar como escrever a mesma lógica de forma mais organizada.
#Radar de trânsito
#O radar de transito neste exercício tem um range de alcance de + ou - 1 à partir da sua posição

velocidade_carro = 61 #velocidade atual do carro
posicao_carro = 100 #local na estrada em que o carro está

RADAR_1 = 60 #velocidade máxima permitida pelo radar
LOCAL_RADAR = 100 #local na estrada em que está o radar
RADAR_RANGE = 1 #distancia para mais ou para menos onde o radar é capaz de atuar

#O código abaixo funciona perfeitamente, mas possui excesso de complexidade desnecessário

# if ((posicao_carro >= LOCAL_RADAR - RADAR_RANGE) and (posicao_carro <= LOCAL_RADAR + RADAR_RANGE))\
#     and velocidade_carro > RADAR_1:
#     print(f'Você foi autuado por excesso de velocidade por transitar à {velocidade_carro} Km/h, em uma via de {RADAR_1} Km/h.')

#Para diminuir a complexidade a maioria das comparações e expressões podem ser transferidas para variáveis
DENTRO_RANGE_SUPERIOR = posicao_carro <= (LOCAL_RADAR + RADAR_RANGE)
DENTRO_RANGE_INFERIOR = posicao_carro >= (LOCAL_RADAR - RADAR_RANGE)
EXCESSO_VELOCIDADE = velocidade_carro > RADAR_1

if (DENTRO_RANGE_INFERIOR and DENTRO_RANGE_SUPERIOR) and EXCESSO_VELOCIDADE:
    print(f'Você foi autuado por excesso de velocidade por transitar à {velocidade_carro} Km/h, em uma via de {RADAR_1} Km/h.')
elif (DENTRO_RANGE_INFERIOR and DENTRO_RANGE_SUPERIOR) and (not EXCESSO_VELOCIDADE):
    print(f'O veículo passou pelo radar, dentro do limite de velocidade da via: {RADAR_1} Km/h.')
