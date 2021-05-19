from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('===================================')
    print('=============== ATM ===============')
    print('===================================\n')

    print('Selecione uma opção abaixo: ')
    print('1 - Criar Conta')
    print('2 - Efetuar Saque')
    print('3 - Efetuar Depósito')
    print('4 - Efetuar Transferência')
    print('5 - Listar Contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Obrigado pela preferência, volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('######### ALERTA ######### ')
        print('Digite uma opção válida!')
        sleep(1)
        menu()


def criar_conta() -> None:
    print('===================================')
    print('Digite os Dados do Cliente:')

    nome: str = input('Nome: ')
    email: str = input('Email: ')
    cpf: str = input('CPF: ')
    data_nascimento: str = input('Data Nascimento dd/mm/YYYY: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da Conta: ')
    print('--------------------------')
    print(conta)
    sleep(1)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com o número {numero}')

    else:
        print('Ainda não existem contas cadastradas!')

    sleep(1)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com o número {numero}')

    else:
        print('Ainda não existem contas cadastradas!')

    sleep(1)
    print()
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        numero_destino: int = int(input('Informe o número da conta de destino: '))

        conta_destino: Conta = buscar_conta_por_numero(numero_destino)

        if conta:
            if conta_destino:
                valor: float = float(input('Informe o valor que deseja transferir: '))
                conta.transferir(valor, conta_destino)
            else:
                print(f'A conta de destino com o número {numero} não foi encontrada.')
        else:
            print(f'A sua conta com o número {numero} não foi encontrada.')

    else:
        print('Ainda não existem contas cadastradas!')

    sleep(1)
    print()
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de Contas: ')

        for conta in contas:
            print(conta)
            print('-----------------')
    else:
        print('Ainda não existem contas para listar!')

    sleep(1)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta

    return c


if __name__ == '__main__':
    main()