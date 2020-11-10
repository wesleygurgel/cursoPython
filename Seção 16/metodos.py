"""
POO - Métodos

- Métodos (Funções). Comportamento dos Objetos, ações que este objeto pode realizar no seu sistema.

Métodos:
    Métodos de Instância:

    Métodos de Classe:
        Conhecidos como Métodos Estáticos em outras linguagens

"""
from passlib.hash import pbkdf2_sha256 as cryp
import getpass


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
    contador = 0

    @classmethod    # Método de Classes - Acesso a atributos de Classe
    def conta_usuarios(cls):
        print(f'Classe {cls}')
        print(f'Temos {cls.contador} usuários no sistema')

    @staticmethod   # Método Estático
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        Usuario.contador = self.__id

        # usando cryp - passlib
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        print(f'Usuário Criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    # Método Privado
    def __gera_usuario(self):
        return self.__email.split('@')[0]

    # Não utilizar dunder para não bater com o do python
    def __correr__(self, metros):
        print(f'{self.__nome} corrend {metros} metros')


# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

# Métodos Privados

# Métodos Estáticos
print(Usuario.contador)
print(Usuario.definicao())
user1 = Usuario('Wesley', 'Gurgel', 'wesleygurgel27@gmail.com', '123456')
print(user1.contador)
print(user1.definicao())
# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

# Métodos de Classe
# user1 = Usuario('Wesley', 'Gurgel', 'wesleygurgel27@gmail.com', '123456')
# user2 = Usuario('Clara', 'Camara', 'mariaclara@gmail.com', '654321')
#
# Usuario.conta_usuarios() # Forma Correta
# user1.conta_usuarios() # Possível, mas incorreta


# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------
# nome = input('Informe o nome: ')
# sobrenome = input('Informe o sobrenome: ')
# email = input('Informe o email: ')
# senha = input('Informe a senha: ')
# confirma_senha = input('Confirme a senha: ')

# if senha == confirma_senha:
#     user = Usuario(nome, sobrenome, email, senha)
#     print('Usuário criado com sucesso!')
# else:
#     print('Senha não confere...')
#     exit(1)

# senha = input('Informe a senha para acesso: ')
# if user.checa_senha(senha):
#     print(f'Acesso permitido! Bem vindo {user.nome_completo()}')
# else:
#     print('Acesso negado')

# print(f'Senha User Criptografada: {user._Usuario__senha}') # Acesso Errado para verificar apenas

# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

# p1 = Produto('Ps4', 'Video Game', 2300)
# print(p1.desconto(50))
# print(Produto.desconto(p1, 50))  # self, desconto1
# print('---------------------------------')
#
#
# user1 = Usuario('Wesley', 'Gurgel', 'wesleygurgel27@gmail.com', '123456')
# user2 = Usuario('Clara', 'Camara', 'mariaclara@gmail.com', '654321')
#
# print(user1.nome_completo())
# # Forma alternativa
# print(Usuario.nome_completo(user1))
#
# print(user2.nome_completo())
# print(f'Senha User 2: {user2._Usuario__senha}') # FORMA INCORRETA DE ACESSAR ATRIBUTO DE CLASSE!!! Pegando atributo privado
