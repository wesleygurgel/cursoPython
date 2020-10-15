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
simples.remove(3) # Não é índice - Não retorna nenhum valor
print(f'Removendo da Forma1: {simples}')

simples.add(3)

# Forma 2
simples.discard(3)  # Discard não GERA ERROR caso não seja encontrado.
print(f'Removendo da Forma2: {simples}\n')



# Copiando um Conjunto para outro...
c1 = {1,2,3}

# Forma 1 - Deep Copy
print('Deep Copy - Não copia para a origem')
novo = c1.copy()
print(novo)
novo.add(4)
print(novo)
print(c1)


print('\nShallow Copy - Copia para origem')
novo = c1
novo.add(4)
print(novo)
print(c1)



# Podemos remover todos os itens de um conjunto
c1.clear()
print('\nCLEAR')
print(c1)



# Métodos matemáticos de conjuntos
print('\nMétodos matemáticos de Conjuntos')
estudantes_python = {'Marcos', 'Patricia', 'Wesley', 'Clara', 'Guilherme', 'Fabiano'}
estudantes_java = {'Narcos', 'Pedro', 'Wesley', 'Luis', 'André', 'Clara'}

# Gerar conjunto com nomes de estudantes únicos.
# Forma 1 - Union
unicos1 = estudantes_python.union(estudantes_java)
print(f'Usando Uniom {unicos1}')

# Forma 2 - utilizando o pipe |
unicos2 = estudantes_python | estudantes_java
print(f'Usando Pipe {unicos2}')


print('\nGerar um conjunto de estudantes que estão em ambos os cursos')
# Forma 1  intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(f'Usando intersection {ambos1}')

# Forma 2 = Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(f'Usando & {ambos2}')


print('\nGerar um conjunto de estudantes que não estão no outro curso')
so_python = estudantes_python.difference(estudantes_java)
print(f'Estudam apenas python: {so_python}')

so_java = estudantes_java.difference(estudantes_python)
print(f'Estudam apenas java: {so_java}')


print('\nSoma, Valor Max, Valor Min, Tamanho.')
conjuntosvt = {1,2,3,4,5,6,7}
print(conjuntosvt)
print(sum(conjuntosvt))
print(max(conjuntosvt))
print(min(conjuntosvt))
print(len(conjuntosvt))