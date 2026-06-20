from rich import print
from rich.panel import Panel
from os import *

class Controle:
    canal_max:int = 6
    canal_min:int = 1
    volume_max:int = 5
    volume_min:int = 1
    def __init__(self, canal=1, volume=2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado
    
    def mostrar_tv(self):
        if self.ligado == False:
            conteudo = f':prohibited: [red]A TV está desligada[/]'
        else:
            conteudo = f'Canal  = '
            for canal in range(Controle.canal_min, Controle.canal_max+1):
                if canal == self.canal_atual:
                    conteudo += f'[black on yellow] {canal} [/]'
                else:
                    conteudo += f' {canal} '
            conteudo += f'\nVolume = '
            for vol in range(Controle.volume_min, Controle.volume_max+1):
                if vol <= self.volume_atual:
                    conteudo += '[black on cyan] [/]'
                else:
                    conteudo += '[black on white] [/]'
        tv = Panel(conteudo, title=' [ TV ] ', width=30)
        print(tv)
    
    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == Controle.canal_max:
                self.canal_atual = Controle.canal_min
            else:
                self.canal_atual += 1
    
    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == Controle.canal_min:
                self.canal_atual = Controle.canal_max
            else:
                self.canal_atual -= 1

    def vol_mais(self):
        if self.ligado:
            if self.volume_atual != Controle.volume_max:
                self.volume_atual += 1

    def vol_menos(self):
        if self.ligado:
            if self.volume_atual != Controle.volume_min:
                self.volume_atual -= 1
tv = Controle()

while True:
    tv.mostrar_tv()
    comando = str(input(f'\n < CH{tv.canal_atual} >  - VOL{tv.volume_atual} + '))
    system('cls')
    match comando:
        case '0':
            break
        case '@':
            tv.liga_desliga()
        case '<':
            tv.canal_menos()
        case '>':
            tv.canal_mais()
        case '+':
            tv.vol_mais()
        case '-':
            tv.vol_menos()