from rich import print



class Funcionario:
    def __init__(self, nome, setor, cargo, empresa='Curso em Vídeo'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa

    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} no setor de {self.setor} na empresa {self.empresa}'


f1 = Funcionario('Carlos', 'Ti', 'Programador', 'CEUNSP')
print(f1.apresentacao())