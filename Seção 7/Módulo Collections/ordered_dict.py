from collections import OrderedDict

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dicionario)

for key, value in dicionario.items():
    print(f'Chave: {key}, Valor: {value}')

print('\nOrdered Dict:')
ordered_dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for key, value in dicionario.items():
    print(f'Chave: {key}, Valor: {value}')

# Garante a ordem de inserção dos elementos

# Entendo a diferença
# Dict comum
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print('\nEntendendo Diferença') # Ordem não importa
print(dict1 == dict2)

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2) # Ordem importa


