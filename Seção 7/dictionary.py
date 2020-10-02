
# Dicionários
#
# OBS: São como mapas
# São coleções do tipo chave/valor.
# São representados por {}
print(type({}))

# OBS:
# 1- Chave e valor são separados por dois pontos 'chave:valor'
# 2- Tanto chave quanto valor podem ser de qualquer tipo de dado
# 3- Podemos misturar tipos de dados


# Criação de Dicionários
# Forma 1 - Mais Comum
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 - Menos Comum
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))


# Acessando elementos
# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])

# Forma 2- acessando via get - recomendado
print(paises.get('br'))
print(paises.get('eua'))

pais = paises.get('ru')

if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('Não encontrei o país')


# Se não achar o RU vai colocar não encontrado.
pais = paises.get('ru', 'Não Encontrado')
print(pais)
pais = paises.get('py', 'Não Encontrado')
print(pais)


print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'br' in paises:
    brasil = paises['br']
    print(brasil)

# Podemos utilizar qualquer tipo de dado, inclusive lista, tupla e etc...

# Tuplas são interessantes de usar como chave de Dicionarios por serem imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7126, 32.3212): 'Escritório em Nova York',
    (77.7388, 65.1234): 'Escritório em Tókio'
}

print(localidades)
print(type(localidades))


# Adicionar elementos em um dicionário
# Forma 1
receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário

receita['mai'] = 550
print(receita)
receita.update({'mai': 600})
print(receita)

# Conclusão 1: A forma de adicionar novos elementos/atualizar é a mesma
# Conclusão 2: Não podemos ter chaves repetidas


# Remover dados de um dicionário
receita = {'jan': 100, 'fev': 200, 'mar': 300}
ret = receita.pop('mar')
print(ret)
print(receita)
receita.update({'mar': 320})

# OBS 1: Sempre informar a chave
# OBS 2: POP remove e retorna o valor

del receita['fev'] # Nesse caso o valor removido não é retornado
print(receita)


# # Imagine que voce tem um comercio eletrônico, onde temos um carrinho de compras.
# Carrinho de Compras:
#     Produto 1:
#         - nome
#         - quantidade
#         - preço
#     Produto 2:
#         - nome
#         - quantidade
#         - preço

# 1 - Poderiamos utilizar uma lista? Sim
print('\nUsando Lista:')
carrinho = []
produto1 = ['Playstation 4', 1,  399.99]
produto2 = ['Playstation 3', 1,  199.99]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Teriamos que saber o indice de cada informação no produto.

# 2 - Poderiamos utilizar uma tupla? Sim
print('\nUsando Tupla:')
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('Playstation 3', 1, 1300.00)
carrinho = (produto1,produto2)
print(carrinho)

# Teriamos que saber o indice de cada informação no produto.

# 3 - Poderiamos utilizar um dicionario? Sim
print('\nUsando Dicionario:')
carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'Playstation 3', 'quantidade': 1, 'preço': 1000.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Desta forma facilmente adicionamos ou removemos produtos do carrinho e temos
# A certeza sobre cada informação


# Métodos de Dicionários

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

#Limpar Dicionarios
d.clear()
print(d)

# Copiando um dicionario para outro
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)

# Shallow Copy
novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)

# Criando dicionarios de forma diferente
outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

# Método fromkeys recebe dois parametros um interavel e um valor
# Ele vai gerar para cada valor do interavel uma chave e irá atribuir a esta chave o valor informado
# .fromkeys(range(1,11), 'novo')


# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Métodos de Dicionários

# d = dict(a=1, b=2, c=3)
# print(d)
# print(type(d))
# print('')











