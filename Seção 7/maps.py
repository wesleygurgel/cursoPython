"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Mês {chave}, valor = {receita[chave]}')


#Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

#Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

#Desempacotamento
print(receita.items())

for chave, valor in receita.items():
    print(f'Chave={chave} e valor= {valor}')

print(max(receita.values()))
print(min(receita.values()))
print(sum(receita.values()))
print(len(receita))
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)





