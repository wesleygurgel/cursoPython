from models.conta import Conta
from models.cliente import Cliente

wesley: Cliente = Cliente('Wesley Gurgel', 'wesleygurgel27@gmail.com', '703.837.754-00', '27/06/1998')
clara: Cliente = Cliente('Maria Clara', 'mcccruz@gmail.com', '156.754.619-88', '16/04/2002')

wesley_conta = Conta(wesley)
clara_conta = Conta(clara)

print(wesley_conta)
print(clara_conta)