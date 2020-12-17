"""
Tuplas são bastantes parecidas com Listas, basicamente duas diferenças básicas.

1- Tuplas são representadas por ( ) e não por [ ]
print(type(()))

2- As tuplas são imutáveis: Ao criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla.

3- # Cuidado 1: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))

tupla2 = 5, 4, 3, 2, 1
print(tupla2)
print(type(tupla2))

#Cuidado 2: Tuplas com 1 elemento
tupla3 = (4) # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é uma também tupla4 = 4,
print(tupla4)
print(type(tupla4))

# Tuplas são definidas pela vírgula e não pelo uso do parênteses

# Tupla dinamicamente
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de Tupla
tupla = ('Wesley Gurgel', 'Marcelino de Oliveira')
escola, curso = tupla
print(escola)
print(curso)

# Métodos para Adição, Remoção de elementos nas tuplas não existem, dado o fato de serem imutáveis.

# Se os valores forem todos inteiros ou reais (Soma, Valor Max, Valor Min, Tamanho)
tupla = 1, 2, 3, 4, 5, 6
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de Tuplas
tupla1 = 1, 2, 3
print(tupla1)
tupla2 = 4, 5, 6
print(tupla2)
print(tupla1+tupla2)
print(tupla1)
print(tupla2)
tupla3 = tupla2 + tupla1
print(tupla3)
tupla1 = tupla1 + tupla2
print(tupla1)

# Verificar se elementos existes na tupla
tupla = 1, 2, 3, 4, 5
print(3 in tupla)

# Iterando sobre uma tupla
tupla = 1, 2, 3, 4, 5
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla = 'a', 'b', 'c', 'd', 'a', 'a', 'b'
print(tupla.count('a'))

escola = tuple('Wesley Gurgel Marcelino')
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas
# Devems utilizar tuplas sempre que não precisarmos modificar dados contidos em uma coleção
# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Acesso a elementos
print(meses[2])

i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

print(meses.index('Junho')) # Posição de Junho na lista

# Slicing
# tupla[inicio:fim:passo]

print(meses[0::2])

# Por quê utilizar tuplas?
1- São mais rapidas que as listas.
2- Seu código mais seguro (Imutabilidade)
"""
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

tupla = (1, 2, 3, 4, 5)
for n in tupla:
    print(n)













