def soma_com(a):
    b = 3
    c = a + b
    return c

a = 5
soma3 = soma_com(a)
print(soma3)


print('\nDefault:')
def elevado(numero=2, potencia=2):
    #Função com parametro padrão
    return numero ** potencia

print(elevado(3)) #Muda numero
print(elevado())
print(elevado(potencia=3))