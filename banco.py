from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()
    
def menu() -> None:
    print('=======================================')
    print('=================ATM===================')
    print('==============PRAIA BANK===============')
    
    print('Selecione uma opção no menu:')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')


#opcao = int(input())
    opcao: int = int(input())#esta linha declara uma variável chamada 'opcao' e a anota
# com o tipo 'int', indicando que é uma variável do tipo inteiro. O valor após a igualdade
# ('=') é o resultado da conversão do 'input()' para inteiro. 

    if opcao == 1: #verifica se a variavel 'opcao' é igual a 1
    #se verdadeiro, chama a função 'criar conta(). presumivelmente, esta função seria responsável
    # por criar uma nova conta do sistema. 
        criar_conta()
    
    elif opcao ==2: #caso a condição anterior seja falsa, verifica se 'opcao' é igual a 2. Se verdadeiro,
    #chama a funcao 'efetuar_saque()'. Esta função provavelmente lidaria com o processo de saque de dinheiro da conta.
        efetuar_saque()
        
    elif opcao ==3:
        efetuar_deposito()
        
    elif opcao ==4:
        efeutar_transferencia()
        
    elif opcao ==5:
        listar_contas()
        
    elif opcao ==6: #Se a 'opcao' for 6, exibe uma mensagem de despedida, aguardada por 2 segundo (usando a função sleep do módulo time)
    #e encerra o programa com 'exit(0) 
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(2)
        menu()
    

def criar_conta() -> None:
    print('Informe os dadados do cliente: ')
    
    nome: str = input('Nome do cliente: ')
    email: str = input(' E-mail do  cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: ')
    
    #cria um objeto da classe 'Cliente' utilizando os dados coletados.
    cliente: Cliente= Cliente(nome, email, cpf, data_nascimento)
    #cria um objeto da classe 'Conta' utilizando o objeto 'cliente' criado anteriormente como argumento.
    conta: Conta = Conta(cliente)
    #Adiciona a nova conta criada à lista 'contas'. Presume-se que 'contas' seja uma lista
    # global ou acessivel dentro do escopo em que a função está sendo chamada.
    contas.append(conta)
    print('Conta criada com sucesso.')
    print('Dados da conta')
    print('-------------------')
    print(conta)
    sleep(2)
    menu()

def efetuar_saque() -> None:
    if len(contas) >0:
        numero: int = int(input('Informe o número da sua conta: '))
        
        conta: Conta = buscar_conta_por_numero(numero)
        
        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            
            conta.sacar(valor)
        else: 
            print(f'Não foi encontrada a conta com número {numero}')     
        
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()

def efetuar_deposito() -> None:
    #verifica se há pelo menos uma conta cadastrada 'contas' parece ser uma lista
#que armazena objetos do tipo 'Conta'.
    if len(contas) >0:
        #Solicita ao usuário que insira o número da conta que deseja usar o depósito
      numero: int = int(input('Informe o número da sua conta: '))
#utiliza uma função chamada 'buscar_conta_por_numero' para encontrar a conta correspondente ao número fornecido.
      conta: Conta = buscar_conta_por_numero(numero)
      if conta:
          valor: float = float(input('Informe o valor do depósito: '))
                
          conta.depositar(valor)
          
      else:
        
        print(f'Não foi encontrada um conta com número {numero}')
    else:
        print('Ainda não existem contas cadastradas')
        
    sleep(2)
    menu()
    
def efeutar_transferencia() -> None:
    if len(contas) >0:
        numero_o: int = int(input('Informe o número da sua conta: '))
        
        conta_o: Conta = buscar_conta_por_numero(numero_o)
        
        if conta_o: #origem da conta
            numero_d: int= int(input('Informe o número da conta destino: '))
            
            conta_d: Conta = buscar_conta_por_numero(numero_d)
            
            if conta_d: #destino da conta
                valor: float = float(input('Informe o valor da transferencia: '))
                conta_o.transferir(conta_d, valor)
            else:
                print('A conta destino com numero {numero_d) não foi ecnontrada')
        else:
            print(f'A sua conta com número {numero_o} não foi encontrada.')
        
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()

def listar_contas() -> None:
    if len(contas) > 0 :
        print('Listagem de contas')
        
        for conta in contas:
            print(conta)
            print('--------------')
            sleep(1)
        
        
    else:
        print('Não existem contas cadastradas.')
    sleep(2)
    menu()

def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None #vairavel c do tipo Conta
    
    if len(contas) >0:
        for conta in contas:
            if conta.numero ==numero:
                c = conta
    return c
        

if __name__ == '__main__':
    main()
    
    