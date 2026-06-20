class ContaBancaria():
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
    
    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo'
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')
        else:
            print(f'Saque NEGADO de R${valor:,.2f} na conta {self.id}. SALDO INSUFICIENTE')

    def depositar(self, valor):
        self.saldo += valor
        print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')

c1 = ContaBancaria(123, 'Carlos', 3203)
c1.sacar(30000)
c1.depositar(500)
print(c1)