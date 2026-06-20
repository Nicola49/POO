from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick, jogos=list()):
        self.nome = nome
        self.nick = nick
        self.jogos = jogos

    def add_favoritos(self, jogo):
        self.jogos.append(jogo)
        self.jogos = sorted(self.jogos, key=str.lower)

    def ficha(self):
        jogos = "\n".join(f':video_game: [bright_blue]{i}[/]' for i in self.jogos)
        painel = Panel(f'''Nome Real: [bold black on bright_blue] {self.nome} [/]
Jogos favoritos:
{jogos}''', title=f'Jogador <{self.nick}>')
        print(painel)

g1 = Gamer('Carlos', 'Mix49')
g1.add_favoritos('Roblox')
g1.add_favoritos('Minecraft')
g1.add_favoritos('GTA 5')
g1.ficha()