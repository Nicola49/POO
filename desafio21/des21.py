from rich import print

class Caneta:
    def __init__(self, cor='azul'):
        escolha = ''
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelha':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case _:
                escolha = '[white]'
        self.cor = escolha
        self.tampa = True

    def destampar(self):
        if self.tampa == True:
            self.tampa = False
        

    def escrever(self, txt):
        if self.tampa == False:
            print(f'{self.cor}{txt}[/]', end='')
        else:
            print(f':prohibited: A {self.cor}caneta[/] está tampada!')
    
    def quebra_linha(self, n = 1):
        print('\n'*n, end='')


c1 = Caneta('verde')
c2 = Caneta()
c3 = Caneta('vermelha')
c1.destampar()
c2.destampar()
c3.destampar()
c1.escrever('Chuca master!')
c2.escrever('Felipe Silva')
c2.quebra_linha(2)
c3.escrever('Raysson Lima')