"""
POO - Métodos

- Métodos (Funções). Comportamento dos Objetos, ações que este objeto pode realizar no seu sistema.

Métodos:
    Métodos de Instância:


"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    # Não utilizar dunder para não bater com o do python
    def __correr__(self, metros):
        print(f'{self.__nome} corrend {metros} metros')


p1 = Produto('Ps4', 'Video Game', 2300)
print(p1.desconto(50))
print(Produto.desconto(p1, 50))  # self, desconto1
print('---------------------------------')


user1 = Usuario('Wesley', 'Gurgel', 'wesleygurgel27@gmail.com', '123456')
user2 = Usuario('Clara', 'Camara', 'mariaclara@gmail.com', '654321')

print(user1.nome_completo())

print(user2.nome_completo())

