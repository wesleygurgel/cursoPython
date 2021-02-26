"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro
iterável.

# Sintaxe

[ dado for dado in iterável ]

def funcao(valor):
    return valor*valor

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

res = [numero/2 for numero in numeros]
print(res)

res = [funcao(numero) for numero in numeros]
print(res)



# List Comprehension vs Loop

numeros = [1, 2, 3, 4, 5]
# Loop
numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero*2)

print(numeros_dobrados)

# List Comprehension
print([numero*2 for numero in numeros])
"""

nome = 'Wesley Gurgel'
print([letra.upper() for letra in nome])

amigos = ['maria', 'joao', 'wesley', 'clara', 'wagner']
print([amigo.title() for amigo in amigos])

print([numero*3 for numero in range(1,10)])

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

print([str(numero) for numero in range(1,6)])






