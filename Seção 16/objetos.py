"""
POO - Objetos

Objetos -> Instâncias da Classe

"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente=None):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def definir_cliente(self, cliente):
        self.__cliente = cliente
        print('Cliente definido')

    def mostra_cliente(self):
        if self.__cliente == None:
            print('Cliente da conta não informado.')
        else:
            print(f'O cliente da conta {self.__numero} é o (a) {self.__cliente._Cliente__nome}, seu CPF é : {self.__cliente._Cliente__cpf}')


class Usuario:
    contador = 0

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuario.contador = self.__id


# Instâncias/Objetos
lamp1 = Lampada('branca', 110, 60)
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cliente1 = Cliente('Wesley Gurgel', '703.837.754-00')

cc1 = ContaCorrente(5000, 20000)
cc1.mostra_cliente()
cc1.definir_cliente(cliente1)
cc1.mostra_cliente()

user1 = Usuario('wesley', 'gurgel', 'wesley@gmail.com', '123456')
