"""
Listas determinadas por colchetes: []
type([1,2])
"""

lista1 = [1, 99, 4, 2, 31, 33, 21, 18, 10, 1]
lista2 = ['W', 'e', 's', 'l', 'e', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Wesley Gurgel')  #mesma coisa da Lista 2

print('Checar se determinado valor está na lista:')
num = 9
if num in lista1:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o numero {num}')
print('--------------------------')

print('Ordenar uma lista de números:')
lista1.sort()
print(lista1)
print('\nOrdenar uma lista de Strings:')
lista5.sort()
print(lista5)
#lista1.reverse() - faz o contrário do sort ou lista1[::-1]
print('--------------------------')

print('Contar número de ocorrências de um valor em uma lista:')
print(lista1.count(1))
print(lista5.count('e'))
print('--------------------------')

print('Adicionar elementos em listas, função append:\nOBS: 1 POR VEZ APENAS')
print(f'Lista 1 sem o append: {lista1}')
lista1.append(42)
print(f'Lista 1 com o append: {lista1}')

print('\nAdicionando mais de um valor por vez:')
lista1.extend([30,40,50])
print(f'Lista com extend: {lista1}')


lista1.append([1,2,3])
print(f'\nLista dentro da lista: {lista1}')

if [1,2,3] in lista1:
    print('Encontrei a Lista dentro da lista')
else:
    print('Não encontrei nada')
print('--------------------------')

print('Inserir elemento na lista informando a posição que ele deve ficar:')
lista1.insert(0, 'Oi')
lista1.insert(0,0)
print(lista1)
print('--------------------------')

print('Juntando duas listas:')
lista6 = lista2 + lista1
#Da pra fazer com extend também: lista1.extend(lista2) - 47:50
print(lista6)
print('--------------------------')

print('Copiar uma lista:')
lista7 = lista1.copy()
print(f'Lista1 Copiada: {lista7}')
print('--------------------------')

print('Tamanho de uma Lista:')
print(f'Tamanho da lista5: {len(lista5)}')
print('--------------------------')

print('Remover o ultimo elemento de uma lista e guardar em uma variável')
print(f'Lista: {lista1}')
print(f'Pop: {lista1.pop()}')
print('\nRemover um elemento pelo indíce: lista1.pop(indice)')
print(f'Lista1 com indíce (4): {lista1.pop(4)}')
print('\nRemover todos os elementos da lista: lista1.clear()')
print('--------------------------')

print('Podemos repetir valores da lista:')
nova = [1, 2, 3]
print(f'Nova: {nova}')
print(f'Nova * 3: {nova*3}')
print('--------------------------')

print('Converter String para Lista:')
curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(f'curso.split(): {curso}') #SPLIT SEPARA PELOS ESPAÇOS

print('\nPodemos definir o separador do split: curso.split(",")')
curso2 = 'Programação,em,Python:Essencial'
print(curso2)
curso2 = curso2.split(',')
print(curso2)
print('--------------------------')

print('Transformar lista em String:')
listacurso = ['Programação', 'em', 'Python:', 'Essencial']
print(listacurso)
listacurso = ' '.join(listacurso)
print(listacurso)
print(type([listacurso]))
print('--------------------------')

"""print('Iterando sobre listas:')
print('Exemplo1, no momento apenas imprimindo, mas pode fazer qualquer coisa.:')
for elemento in lista1:
    print(elemento)

print('Exemplo2 com while:')
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto ao Carrinho ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
    print('--------------------------')
"""
numeros = [1, 2, 3, 4, 5]
letra = 'a'
numeros.insert(1,letra)
print(numeros)
print('--------------------------') # 1:30:00 da VideoAula

"""cores = ['verde', 'amarelo', 'azul', 'branco', 'preto', 'branco', 'azul']
for indice, cores in enumerate(cores):
    print(indice,cores)"""

print('Encontrar o Indíce de um elemento na lista:')
numeros.pop(1) #removendo o 'a'
numeros.extend([6, 7, 8, 9, 10, 2])
print(numeros.index(2)) #Retorna apenas o primeiro valor
print(numeros.index(10))
print(numeros.index(2, 3)) # Encontre o valor 2, a partir do indice 3
print(numeros.index(2, 2, 11))# Encontre o valor 2, entre os indices 2 e 11
print('--------------------------')

print('Revisão de Slicing')
# lista[inicio:fim:passo]
# range[inicio:fim:passo]
lista1.clear()
lista1 = [1, 2, 3, 4, 5, 6]
print(lista1[1:]) # Iniciando do índice 1 e pegando todos os elementos restantes
print(lista1[:2]) # do inicio até o indice 2-1
print(lista1[1:4]) # Iniciando do indice 1 até o 4-1
print(lista1[0:6:2]) # Do 0 ao 6-1, com passo 2
print(lista1[0::2]) # Do 0 com passo 2, observe que tem dois :, pulando o parametro do meio que seria o fim
print(lista1[::2]) #Mesma coisa apenas com parametro do passo

print('----------------------------')
print(f'Soma: {sum(lista1)}')
print(f'Maaximo: {max(lista1)}')
print(f'Minimo: {min(lista1)}')
print(f'Tammanho: {len(lista1)}')















