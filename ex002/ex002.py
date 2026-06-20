from random import *

class PorcaGorda:
    """
    Essa classe cria uma porca gorda usando o nome e a idade dela, criando também
    uma apelido de porca para ela.
    Porca = PorcaGorda(nome, idade)
    """
    def __init__(self, nome = '', idade = 0, nomeporca = ''):
        self.nome = nome
        self.idade = idade
        self.nomeporca = nomeporca
        porcas = ['Porca Imunda', 'Porca Gorda', 'Porca Indecisa', 'Porca Chupadora', 'Porca Bebe Esperma', 'Porca Lixo', 'Porca Fedida']
        self.nomeporca = choice(porcas)
    
    def __str__(self):
        return f"A Porca {self.nome} tem {self.idade} anos e é uma {self.nomeporca}"
    
Ra = PorcaGorda(nome='Raysson', idade=18)
print(Ra)
print(Ra.__dict__)
print(Ra.__getstate__())
print(Ra.__doc__)
print(Ra.__class__)