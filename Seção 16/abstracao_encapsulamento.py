"""
POO - Abstração e Encapsulamento

conta1 = Conta('Wesley', '2000', '600')
print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

conta1.numero = 42
conta1.titular = 'Xuxa'
conta1.saldo = 1
conta1.limite = 1

print(conta1.__dict__)

# Atributos públicos são mutáveis facilmente, segurança muito baixa.

conta1.extrato()

# Após colocarmos os '__' agora não podemos mas fazer nada disso.

print(conta1.__dict__)
"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de R$ {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        taxa_transferencia = 0.05
        if self.__saldo >= valor:
            self.sacar(valor + valor*taxa_transferencia)
            print(f'{self.__titular} transferiu R$ {valor} para {destino.__titular}')
            destino.depositar(valor)


conta1 = Conta('Wesley', 2000, 600)
conta1.extrato()

conta2 = Conta('Wagner', 1000, 600)
conta2.extrato()

conta1.transferir(200, conta2)
conta1.extrato()
conta2.extrato()