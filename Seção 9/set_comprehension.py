# Exemplos

numeros = {num for num in range(0,7)}
print(numeros)

# Outro Ex
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Alteração na estrutura acima par agerar um dicionario
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Strings
letras = {letra for letra in 'Wesley Gurgel'}
print(letras)