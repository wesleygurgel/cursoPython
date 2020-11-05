"""
Programação Orienta a Objetos = POO

Principais elementos:
- Classe -: Modelo do Objeto do mundo real sendo representado computacionalmente
- Atributo -: Caracteristicas do Objeto
- Método -: ComportamentO do Objeto
- Construtor -: Criar Objetos
- Objeto -: Instância da Classe.


Atributos divididos em 3 grupos:
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos

# Atributos de Instância:
    class Lampada:

        def __init__(self, voltagem, cor):
            self.voltagem = voltagem
            self.cor = cor
            self.ligada = False

# Atributos Públicos e Privados
    - Atributos privados só podem ser usado/acessado dentro da classe que foi declarado.
        Exemplo: self.__voltagem = voltagem
    - Por convenção todos os atributos são públicos em uma classe, acessado em todo projeto.


"""


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


# class Produto:
#
#     def __init__(self, nome, descricao, valor):
#         self.nome = nome
#         self.descricao = descricao
#         self.valor = valor


class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


user = Acesso('wesleygurgel27@gmail.com', '123456')

print(user.email)
#print(user.__senha) # AtributeError - PRIVADO

print(user._Acesso__senha)
user.mostra_email()
user.mostra_senha()

# Atributos de Instância:
#     Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncisa terão estes atributos

# user2 = Acesso('user2@gmail.com', '543221')
# user3 = Acesso('user3@gmail.com', 'laskdlsak')
#
# user2.mostra_email()
# user3.mostra_email()

# Atributos de Classe:

# p1 = Produto('Playstation 4', 'Video Game', 2300)
# p2 = Produto('Xbox S', 'Video Game', 4500)

# São atributos declarados diretamente na Classe, fora do Construtor, geralmente já inicializamos um valor
# e esse valor é compartilhado entre todas as instâncias da classe.

# Refatorar a Classe Produto

class Produto:
    # Atributo de Classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


# p1 = Produto('Playstation 4', 'Video Game', 2300)
# p2 = Produto('Xbox S', 'Video Game', 4500)
#
# print(p1.valor)
# print(p2.valor)
#
# print(Produto.imposto)
# # ou
# print(p1.imposto) # Acesso possível, mas incorreto.
#
# print(p1.id)
# print(p2.id)

# Atributos Dinâmicos
#   Atributo de Instância criado em tempo de execução
#   OBS: Será Exclusio da instância que o criou

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

# Criando atributos dinâmico

p2.controles = 1

print(f'Produto {p2.nome}, Descrição {p2.descricao}, Valor {p2.valor}, Quant de Controles {p2.controles}')

# Deletando atributos

print(p2.__dict__) #Analisando seu objeto
print(p1.__dict__)

del p2.controles

print(p2.__dict__)
print(p1.__dict__)
