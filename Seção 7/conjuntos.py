# Conjuntos são bons quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles. Quando não precisamos nos precoupar com chaves, valores e itens duplicados.

# São referenciados em python com {}

"""
Diferença entre Conjuntos (Sets) e Mapas (Dicionários)
    - Dicionario = chave/valor
    - Sets = valor
"""

# Definindo um conjunto
# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Valores repetidos
print(s)
print(type(s))

# Obs: Caso exista valor repetido, é ignorado.
# Forma 2 = Mais Comum
s2 = {1, 2, 3, 4, 5, 6, 5}
print(s2)

# Verificando se elemento está contido.
if 3 in s2:
    print('S2 tem 3')
else:
    print('S2 não tem 3')



# Importante lembrar que também não temos ordem.
lista = [99, 30, 12, 1, 33, 1, 30]
print(f'\nLista={lista} com {len(lista)}')

tupla = (99, 30, 12, 1, 33, 1, 30)
print(f'Tupla={tupla} com {len(tupla)}')

dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionario={dicionario} com {len(dicionario)}')

conjunto = {99, 30, 12, 1, 33, 1, 30}
print(f'Conjunto={conjunto} com {len(conjunto)}')
print()



# Misturar tipos de Dados
misturar = {1, 'b', True, 34.22}
print(misturar)
print(type(misturar))

# Iterar sobre um set
for valor in misturar:
    print(valor)



# Usos interessantes com sets
print()
# Imagine que fizemos um formulario de cadastro de visitantes em um museu
# Eles informar manualmente a cidade de onde vieram
# Nós adicionamos cada cidade em uma lista Python, já que na lista podemos adicionar novos elementos e ter repetição

cidades = ['Natal', 'São Paulo', 'Campo Grande', 'Cuiaba', 'São Paulo', 'Campo Grande']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas temos.
cidades_unicas = set(cidades)
print(cidades_unicas)
print(len(cidades_unicas))
print()


# Adicionando elementos em um conjunto
simples = {1, 2, 3}
simples.add(4)
print(simples)

# Remover Elementos
# Forma 1
simples.remove(3) # Não é índice
print(f'Removendo da Forma1: {simples}')

simples.add(3)

# Forma 2
simples.discard(3)  # Discard não GERA ERROR caso não seja encontrado.
print(f'Removendo da Forma2: {simples}')

