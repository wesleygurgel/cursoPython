"""
**kwargs

Este é só mais um parametro, mas diferente do *args que coloca os valores extras em uma tupla
o **kwargs utiliza parametros nomeados e transforma esses parametros em um dict

"""

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: os parametros *args e **kwargs não são obrigatorios.

cores_favoritas()
cores_favoritas(geek='navy')

print('---------------------------------------------------')

def cumprimento_espacial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é'

print(cumprimento_espacial())
print(cumprimento_espacial(geek='Python'))
print(cumprimento_espacial(geek='Oi'))
print(cumprimento_espacial(geek='Especial'))

print('---------------------------------------------------')

# Podemos ter Parametros Obrigatorios, *args, Default e **kwargs.    NESSA ORDEM!!!!!

def myfuncao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)
    print('-------------')

myfuncao(8, 'Julia')
myfuncao(18, 'Felicity', 4, 5, 3, solteiro=True)
myfuncao(34, 'Felipe', eu='nao', voce='vai')
myfuncao(19, 'Carla', 9, 4, 3, java=False, python=True)

print('---------------------ORDEM CORRETA------------------------------')

# Por que é importante a ordem dos parametros.

# Função com a ordem correta de parametros
def mostra_info(a, b, *args, instrutor='Wesley', **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='Gurgel', cargo='TI'))

print('\n---------------------ORDEM INCORRETA------------------------------')

# Função com a ordem incorreta de parametros
def mostra_info2(a, b, instrutor='Wesley', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info2(1, 2, 3, sobrenome='Gurgel', cargo='TI'))

print('\n------------------Desempacotar---------------------------------')

# Desempacotar
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {
    'nome': 'Felicity',
    'sobrenome': 'Jones'
}

print(mostra_nomes(**nomes))

print('\n------------------Desempacotar 2---------------------------------')
def soma_multiplos_numeros(a,b,c):
    print(a+b+c)

lista = [1,2,3] # Funciona para lista, tupla e set (conjunto)
tupla = 1, 2, 3
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

# NOME DAS CHAVES DO DICIONARIO = PARAMETROS DA FUNÇÃO!!!!
