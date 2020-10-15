# Módulo Collections - Counter
"""
Collections -: High-Perfomance Container Datetypes

Counter -: Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
dicionário, contendo como chave o elemento ad lista passada como parâmetro e como valor a quantidade de ocorrências
desse elemento.

"""
from collections import Counter

# Podemos utilizar qualquer iterável
lista = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,6,6,6,6,7,7,7,7,8,8,9,34,21,3,12,123,121]

res = Counter(lista)
print(type(res))
print(res)
# Counter({3: 7, 5: 7, 2: 6, 4: 6, 1: 5, 6: 4, 7: 4, 8: 2, 9: 1, 34: 1, 21: 1, 12: 1, 123: 1, 121: 1})


print('\nExemplo 2')
print(Counter('Wesley Gurgel'))
# Counter({'e': 3, 'l': 2, 'W': 1, 's': 1, 'y': 1, ' ': 1, 'G': 1, 'u': 1, 'r': 1, 'g': 1})


print('\nExemplo 3')
texto = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

palavras = texto.split()
myCounter = Counter(palavras)
print(myCounter)

# Encontrando as 5 palavras mais ocorrência
print(myCounter.most_common(5))









