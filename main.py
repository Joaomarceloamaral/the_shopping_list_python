"""Executa o loop principal do programa"""

from classes.product import Product
from modules.menu_options import get_menu_option, execute_option, show_clas_by_id
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

        result = execute_option(option, OPTIONS, UNITYS_DF, Product, products)

        if option != "D":

            if type(result) == type(products):
                products = result

                print("\nOperação realizada com sucesso.")

            elif type(result) != type(True):

                products.append(result)

                last_product = len(products) - 1

                products[last_product].add_class_id(last_product)

                print("\n")
                show_clas_by_id(products, last_product, UNITYS_DF)
                print("\nOperação realizada com sucesso.")

            elif result:
                print("\nOperação realizada com sucesso.")

            else:
                print("\nOperação falhou.")

    print("Saindo...")


if __name__ == "__main__":
    main()
