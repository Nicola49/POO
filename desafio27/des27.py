from rich import print
from rich.panel import Panel
from abc import ABC, abstractmethod
import random

class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"[blue]{self.nome}[/] recebeu [red]{fator} de dano![/]")

    def atacar(self, alvo, força):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]

            print(f"[green]{self.nome}[/] ({self.vida}) atacou [red]{alvo.nome}[/] ({alvo.vida}) com um [blue]{golpe}[/] de força [lightblue]{força}[/]!")
        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer.")
        alvo.receber_dano(força)

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Corte Lateral", "Golpe Giratório"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e recuperou [green]{fator}[/] pontos de vida!")


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio Místico", "Cristais de Gelo"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] usou a magia [purple]Curar Ferimentos[/] e recuperou [green]{fator}[/] pontos de vida!")

class Druida(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Golpe de Vinhas", "Raio Solar", "Lanças de Água"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] pediu ajuda aos espíritos da ágia e recuperou [green]{fator}[/] pontos de vida!")
