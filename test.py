from models.cliente import Cliente
from models.conta import Conta

rebeca: Cliente = Cliente('Rebeca Praia', 'rebecapraia4@gmail.com', '026.587.682-65', '19/02/1999')
samuel: Cliente = Cliente ('Samuel Lopes', 'samuellopes2@gmail.com', '026.587.682.65', '04/03/1999')

print(rebeca)
print(samuel)


contaf: Conta = Conta(rebeca)
contaa:Conta = Conta(samuel)

print(contaf)
print(contaa)