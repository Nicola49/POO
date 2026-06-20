from des25 import *
from rich import print
from rich.table import Table

def main():
    dist = 80

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    # entrega = Caminhao(dist)
    # print(f"Frete de {type(entrega).__name__} em {dist}km = {entrega.calcular_frete()}")

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for item in viagem:
        tabela.add_row(f"{dist}km", f"{type(item).__name__}", f"{item.calcular_frete()}")

    print(tabela)


if __name__ == '__main__':
    main()