#Strings
'''

Python possui tipagem = Dinâmica / Forte
    Dinâmica - Quer dizer que o python interpreta o tipo de dado sem que esse seja declarado explicitamente
    Forte - Significa que a linguagem não aceita operações entre dois tipos diferentes, é necessário converter um em outro
    
str -> string -> texto
Strings são textos dentro de aspas, simples ou duplas

'''

print('Lavouisier')
print("Lavouisier")

#Caractere de escape (útil para mostrar elementos que geralmente o interpretador leria como parte da sintaxe)
print("Lavouisier \"Nogueira\"")

#Para não ter que usar elementos de escape, que poluem o código, é possivel somente usar os dois tipos de aspas combinados
print('Lavouisier "Nogueira"')

#raw string (imprime inclusive os elementos de escape, útil para trabalhar com expressões regulares)
print(r"Lavouisier \"Nogueira\"")
