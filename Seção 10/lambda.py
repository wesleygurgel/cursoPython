"""
Expressões Lambdas: funções sem nome, anônimas.

def soma(a, b):
    return a + b

"""


# Função normal
def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Função lambda
calc = lambda x: 3 * x + 1
print(calc(4))

# Lambda com + entradas # Strip remove espaços
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' wesley', 'GUrgel'))

# Sem entrada
amar = lambda: 'Como não amar Python?'
print(amar())

# Exemplo
jogadores = ['Neymar Junior', 'Mbappe Kante', 'Juninho Pernambucano', 'Ronaldinho Gaucho', 'Ronaldo Fenomeno',
             'Romario dos Santos', 'Cristiano Ronaldo', 'Lionel Messi', 'Van Djak', 'Wesley G. Marcelino',
             'L. E. Gurgel']
print(jogadores)
jogadores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(jogadores)


# Funcao Quadratica
def geradora_funcao_quadratica(a, b, c):
    """f(X) = ax² + bx + c"""
    return lambda x: a * x ** 2 + b * x + c


f = geradora_funcao_quadratica(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))
