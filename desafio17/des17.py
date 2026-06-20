from rich.panel import Panel
from rich import print

class Produto:
    def __init__(self, nome, preco):
        self.preco = preco
        self.nome = nome
    
    def etiqueta(self):
        self.preco = f'R${self.preco:,.2f}'
        self.painel = Panel(f"{self.nome:^26}\n{'-'*26}\n{self.preco:.^26}", title='Produto', width=30)
        print(self.painel)

p1 = Produto('Iphone 18', 18000)
p1.etiqueta()

p2 = Produto('Camiseta Adidas', 80)
p2.etiqueta()