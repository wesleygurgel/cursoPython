from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('====================================')
    print('=========== Bem-vindo(a) ===========')
    print('===========   WSL Shop   ===========')
    print('====================================\n')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produtos')
    print('3 - Comprar Produtos')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Obrigado pela preferência, volte sempre! WSL Shop')
        sleep(2)
        exit(0)
    else:
        print('######### ALERTA ######### ')
        print('Digite uma opção válida!')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Informe o nome do Produto: ')
    preco: float = float(input('Informe o preço do Produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    print('Listar Produtos')
    print('===============')

    if produtos:
        for produto in produtos:
            print(produto)
            print('-----------------')
            sleep(1)

    else:
        print('Ainda não existem produtos cadastrados!')

    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('--------------------------------------------------------------')
        print('-------------------- Produtos Disponíveis --------------------')
        print('--------------------------------------------------------------')

        for produto in produtos:
            print(produto)
            print('--------------------------------------------------------------\n')
            sleep(1)
        print('Informe o código do Produto que deseja adicionar ao carrinho: ')
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto: # Produto existe
            if len(carrinho) > 0:   # Existe coisa no carrinho
                tem_no_carrinho: bool = False
                for item in carrinho:   # Itera itens do carrinho
                    print(f'Item: {item}')
                    quant: int = item.get(produto)
                    if quant:   # Se já estiver o produto passado, incrementa
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()

                if not tem_no_carrinho: # Não existir o produto passado no carrinho
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()

            else:   # Não tem nada no carrinho
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao Carrinho!')
                sleep(2)
                menu()
        else:   # Código errado
            print(f'O produto de código {codigo} não foi encontrado!')
            sleep(2)
            menu()

    else:
        print('Ainda não existem produtos para vender.')

    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')
        for item in carrinho:
            for produto, quantidade in item.items():
                print(produto)
                print(f'Quantidade: {quantidade}')
                print('--------------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')

    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print('Produtos do Carrinho: ')

        for item in carrinho:
            for produto, quantidade in item.items():
                print(produto.nome)
                print(f'Quantidade: {quantidade}')
                valor_total += produto.preco * quantidade

        print(f'Valor total do carrinho: {formata_float_str_moeda(valor_total)}\nVolte Sempre!')
        carrinho.clear()
        sleep(3)

    else:
        print('Ainda não existem produtos no carrinho!')

    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto

    return p


if __name__ == '__main__':
    main()
