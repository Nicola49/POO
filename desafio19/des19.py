from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, pgs):
        self.titulo = titulo
        self.pgs = pgs
        self.pgatual = 1
        print(f'''[blue]:open_book: Você acabou de abrir o livro [red]"{self.titulo}"[/][blue] que tem [green]{self.pgs}
 [/][blue]páginas no total. Você está na [yellow]página {self.pgatual}[/]''')

    def passar_pagina(self, pgs):
        cont = 0
        while self.pgatual < self.pgs and cont < pgs:
            cont += 1
            self.pgatual += 1
            print(f'Pág{self.pgatual} :play_button: ', end='')
            sleep(0.4)
        print(f'[blue]Você avançou {cont} páginas e agora está na [yellow]página {self.pgatual}[/]')
        if self.pgatual == self.pgs:
            print(f':closed_book: [red]Você chegou no final do livro "{self.titulo}"[/]')
            

l1 = Livro('Sonic Boom e suas aventuras', 20)
l1.passar_pagina(5)
l1.passar_pagina(19)