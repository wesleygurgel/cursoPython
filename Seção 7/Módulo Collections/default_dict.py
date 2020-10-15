from collections import defaultdict

dicionario = {'curso': 'Python'}
print(dicionario)
print(dicionario['curso'])

# Default Dict -> Se não existir valor definido ele insere um valor default.
# Se a chave nãoe xistir a chave será criada com o valor Default
# OBS: Lambdas sãu func sem nomes, podem ou nao receber parametro de entrada e retorna valores.

print('Default Dict:')
default_dicionario = defaultdict(lambda: 0)
default_dicionario['curso'] = 'Python'

print(default_dicionario)
print(default_dicionario['Nome']) # Normal daria KeyError por não existir
print(default_dicionario) # Adicionou
