"""
Dictionary Comprehension:

CRIAR UMA LISTA:
lista = [1,2,3,4]

CRIAR UMA TUPLA:
tupla = 1,2,3,4

CRIAR UM SET:
conjunto = {1, 2, 3, 4}

CRIAR UM DICTIONARY:
dictionary = {'a': 1, 'b':2}

# SINTAXY:

{chave:valor for valor in iteravel}
[valor for valor in iteravel]


"""

# Exemplos
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in dictionary.items()}

print(quadrado)

# Exemplo 2
numero = [1, 2, 3, 4, 5]
quadrados = {valor: valor ** 2 for valor in numero}
print(quadrados)

# Exemplo 3
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo lógica condicional
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numero}
print(res)
