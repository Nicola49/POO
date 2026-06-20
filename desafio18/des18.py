from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo='Churrasco', quant=0, kg=82.4):
        self.titulo = titulo
        self.pessoas = quant
        self.recomend = 0.4 * self.pessoas
        self.total = self.recomend * kg
        self.kg = kg
        self.ppessoa = kg * 0.4

    def analisar(self):
        painel = Panel(f'''Analisando [green]{self.titulo}[/] com [blue]{self.pessoas}[/] convidados
Cada participante comerá 0.4Kg e cada Kg custa R${self.kg:,.2f}
Recomendo [blue]comprar {self.recomend:.3f}[/] de carne
O custo total será de [green]R${self.total:,.2f}[/]
Cada pessoa pagará [yellow]R${self.ppessoa}[/] para participar''',title=self.titulo, width=70)
        return painel
    
c1 = Churrasco(quant=40, titulo='Churracos dos Cachorrus')
print(c1.analisar())