from abc import ABC, abstractmethod

class Bebida(ABC):
    def preparar(self):
        print("--- Iniciando o preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida pronta ---")

    def ferver_agua(self):
        print("1. Fervendo a água a 100 graus Celsius.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Leite(Bebida):
    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico do leite.")

    def servir(self):
        print("3. Servindo na caneca grande, já com café.")

class Cafe(Bebida):
    def misturar(self):
        print("2. Passando água pressurizada pelo pó de café moído.")

    def servir(self):
        print("3. Servindo em xícara pequena.")

class Cha(Bebida):
    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água.")

    def servir(self):
        print("3. Servindo na caneca de porcelana com limão.")