from des27 import *

def main():
    p1 = Guerreiro("Pikachu", 1500)
    p2 = Mago("Joao", 1000)
    p3 = Druida("Jefferson", 1200)

    p1.atacar(p2, 100)
    p1.atacar(p3, 100)
    p2.atacar(p1, 100)
    p1.curar()
    p2.curar()
    p3.curar()


if __name__ == "__main__":
    main()