"""
Named Tuple -: Tuplas que possuem um nome para e mesma e também para parâmetros
"""

from collections import namedtuple

# Definir nome e parametros

# Forma 1 - Declaração
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração
gato = namedtuple('gato', 'idade, raca, nome')

# Forma 3 - Declaração
macaco = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='Pug', nome='Ray')
print(ray)

# Acesso ao elemento
print(ray[0]) #idade
print(ray[1]) #raca
print(ray[2]) #nome

print('\nForma 2:')
print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Pug'))
