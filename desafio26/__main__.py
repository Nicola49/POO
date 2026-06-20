from des26 import *

def main():
    f1 = FuncionarioMensalista("João", 9500)
    f1.calc_sal()
    f1.analisar_sal()
    f2 = FuncionarioHorista("Paulo", 200, 12)
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == '__main__':
    main()