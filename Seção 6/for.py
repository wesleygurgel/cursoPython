nome = "Wesley Gurgel"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

"""for letra in nome:
    print(letra)

print('----------------------')

for numero in lista:
    print(numero)

print('----------------------')

for numero in range(1, 10):
    print(numero)

print('----------------------')
for numero in numeros:
    print(numero)

print('--------índice---------')"""

"""# Descobrir o índice da letra
#i -> indice, v -> valor
#((0, 'W'), (1, 'E')...
for indice, letra in enumerate(nome):
    if letra == 'y':
        print(f'A letra Y está na posição {indice}')

print('--------------------------------')

for valor in enumerate(nome):
    print(valor)
"""

"""quantidade = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1,quantidade+1):
    num = int(input(f'Informe o {n}/{quantidade} valor: '))
    soma = soma+num

print(f'A soma total deu {soma}')"""

"""                            #Tirar quebra de linha
for letra in nome:
    print(letra, end='')
    
tabela dos emojis: https://apps.timwhitlock.info/emoji/tables/unicode    
"""

#Original: U+1F60D
#Modificado: U0001F60D

for num in range(1, 11):
    print('\U0001F60D '*num)





