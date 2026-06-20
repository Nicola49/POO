from random import *

class PorcaGorda:
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.nomeporca = ''

    def porca(self):
        porcas = ['Porca Imunda', 'Porca Gorda', 'Porca Indecisa', 'Porca Chupadora', 'Porca Bebe Esperma', 'Porca Lixo', 'Porca Fedida']
        self.nomeporca = choice(porcas)
    
    def msg(self):
        return f"A Porca {self.nome} tem {self.idade} anos e é uma {self.nomeporca}"
    
Ra = PorcaGorda()
Ra.idade = 18
Ra.nome = 'Raysson'
Ra.porca()
print(Ra.msg())