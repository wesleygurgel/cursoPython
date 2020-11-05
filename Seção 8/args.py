"""
Entendendo o *args

- O *args é um parametro como outr qualquer, isso significa que voce podera chamar de qualquer coisa
desde que comece com asterisco.

Exemplo:
*xis

Mas por convenção, utilizamos o *args para definí-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras em uma tupla

NÃO É LEGAL:
def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(1,2,3))

# print(soma_todos_numeros(1,2)) TypeERROR


def soma_todos_numeros(nome, email, *args):
    print(sum(args))

soma_todos_numeros('Wesley', 'Gurgel')
soma_todos_numeros('Wesley', 'Gurgel', 1)
soma_todos_numeros('Wesley', 'Gurgel', 1,2)
soma_todos_numeros('Wesley', 'Gurgel', 1,2,3)
soma_todos_numeros('Wesley', 'Gurgel', 1,2,3,4)
soma_todos_numeros('Wesley', 'Gurgel', 1,2,3,4.5)
"""

def verifica_info(*args):
    if 'Wesley' in args and 'Gurgel' in args:
        return 'Bem vindo Wesley Gurgel'
    return 'Quem é você?:'

# print(verifica_info())
# print(verifica_info(1, True, 'Gurgel', 'Wesley'))
# print(verifica_info(1, 'Gurgel', 3.14))


def soma_todos_numeros(*args):
    return sum(args)

numeros = [1,2,3,4,5,6]

# Desempacotador
print(soma_todos_numeros(*numeros))

# OBS O * serve para que informemos ao python que estamos passando ao python uma coleção de argumentos.
# Desta forma, ele saberá que precisará desempacotar estes dados.