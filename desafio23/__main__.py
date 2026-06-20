from des23 import Quadrado, Circulo
from rich import print, inspect

def main():
    q = Quadrado(20)
    c = Circulo(12)
    # inspect(q, methods=True)
    print(f'Um quadrado de {q.lado} tem perímetro de {q.perimetro():.1f} e área de {q.area():.1f}')
    print(f'Um círculo de {c.raio} tem perímetro de {c.perimetro():.1f} e área de {c.area():.1f}')
if __name__ == "__main__":
    main()