from models.cliente import Cliente
from utils.helper import formata_float_str_moeda

class Conta:
    codigo: int = 1001 #um atributo classe que inicia com o valor 1001. 
    #Ele é utilizado para atribuir números únicos a cada conta
    
    def __init__(self: object, cliente: Cliente) -> None: 
        #inicializa uma instancia da classe "Conta" com os seguintes atributos:
        self.__numero: int = Conta.codigo #número da conta, inicializando com o valor de "Conta.codigo"
        #cada vez que uma nova conta é criada, "Conta.codigo" é incrementado
        self.__cliente: Cliente = cliente #Um objeto da classe "Cliente" que representa o titular da conta
        self.__saldo: float = 0.0 #saldo da conta, inicializando como 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo +=1
    
    def __str__(self: object) -> str: #método __str__ retorna uma representação em string da conta, exibindo o 
    # número da conta, o nome do cliente e o saldo total.
         return f'Número da conta: {self.numero} \nCliente: {self.cliente.nome} \nSaldo Total: {formata_float_str_moeda(self.saldo_total)}'
    @property
    def numero(self: object) -> int: #retorna o número da conta
        return self.__numero 
    
    @property
    def cliente(self: object) -> Cliente: #retorna o objeto "Cliente" associado à conta
        return self.__cliente
    
    @property
    def saldo(self: object) -> float:
        return self.__saldo
    
    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor
    
    @property
    def limite(self: object) -> float:
        return self.__limite
    
    @limite.setter
    def limite (self: object, valor: float) -> None:
        self.__limite = valor
          
    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total
    
    @saldo_total.setter 
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor
        
    @property
    def _calcula_saldo_total(self: object) -> float: #Um método que retorna o asldo total da conta (soma do saldo e do limite de crédito)
        return self.saldo + self.limite

    #Método para realizar um depósito em uma conta
    #parametros:
        #self: Referência à instância da classe
        #valor: (float): o valor a ser depositado na conta
        
    #Retorna:
        #None: este método não retorna nehnum valor
    def depositar(self: object, valor: float) -> None:
        if valor > 0 : #verifica se o valor do depósito é maior que zero
            self.saldo = self.saldo + valor #se for maior que zero, atualiza o saldo da conta e o saldo total
            self.saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso! ')
        else: 
            print('Erro ao efetuar depósito. Tente novamente')
    
    def sacar(self: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
            print('Saque efetuado com sucesso')
        else: 
            print('Saque não realizado. Tente novamente')
    
    def transferir(self: object, destino: object, valor: float) -> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + restante
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            print('Transferência realizada com sucesso. ')
            
        else: 
            print('Transferencia não realizada. Tente novamente')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    