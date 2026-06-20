from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print


class Funcionario(ABC):
    salario_minimo = 1612
    inss = 7.5
    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0
        self.salario_minimo = 1612
        self.inss = 7.5

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        Analise = Panel(f"O salário de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.salario/Funcionario.salario_minimo:.1f} salários mínimos[/]", title="Análise de salário", width=45)
        print(Analise)
        
class FuncionarioHorista(Funcionario):
    def __init__(self, nome, hora_trab, valor_hora):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.hora_trab = hora_trab

    def calc_sal(self):
        self.sal_bruto = self.hora_trab * self.valor_hora
        self.salario = self.sal_bruto - self.sal_bruto * (Funcionario.inss / 100)

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto - self.sal_bruto * (Funcionario.inss / 100)