"""Executa o loop principal do programa"""

from modules.menu_options import get_menu_option, execute_option
from constants.unitys import OPTIONS, UNITYS_DF


def main():
    """
    Executa o loop principal do programa, permitindo ao usuário escolher opções até decidir sair.

    O programa continua solicitando uma opção no menu e executa a ação correspondente.

    """

    products = []
    option = "x"

    while option != "D":

        option = get_menu_option()

        result = execute_option(option, OPTIONS, UNITYS_DF)

        if option != "D":
            if result:
                print("\nOperação realizada com sucesso.")

            else:
                print("Operação falhou.")

    print("Saindo...")


if __name__ == "__main__":
    main()
