"""
Lista Aninhadas (Nested Lists)

- Algumas linguagens C/JAVA/PHP possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays ou Vetores)
    - Multidimensionais (Matrizes)

Em python nós temos as listas:

numeros = [1, 2, 3, 4, 5]

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3
print(listas[0][1])

# Iterando com loops em uma lista aninhada

for lista in listas:
    for elemento in lista:
        print(elemento)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3

# Gerando um tabuleiro/Matrix 3x3

tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1,4)] for valor in range(1,4)]
print(velha)
"""

r10 = [[1 if numero % 2 == 0 else 0 for numero in range(1,4)] for qualquercoisa in range(1,4)]
print(r10)

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3

for lista in listas:
    for elemento in lista:
        print(f'|{elemento:^3}|', end='')
    print()


