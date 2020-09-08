valoresdigitados = 0
soma = 0
quantidade = int(input('Digite quantos números deseja para a operação:'))

while(valoresdigitados != quantidade):
    print(f'Digite o valor da casa {valoresdigitados+1}/{quantidade}:')
    numero = int(input())
    soma += numero
    valoresdigitados = valoresdigitados + 1

print(f'A média foi de: {soma/valoresdigitados}')









