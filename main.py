"""Executa o loop principal do programa"""

from classes.product import Product
from modules.menu_options import get_menu_option, execute_option, show_clas_by_id
from constants.unitys import OPTIONS, UNITYS_DF


def main():
    """
    Executa o loop principal do programa, permitindo ao usuário escolher opções até decidir sair.

    O programa continua solicitando uma opção no menu e executa a ação correspondente.

    """

    # Lista que vai conter os produtos criados/adicionados
    products = []

    # Opção aleatória apenas para inicializar a variável
    option = "x"

    # Enquanto a opção não for D - Sair, continua a repetir
    while option != "D":

        # Monstra o menu e pega a opção escolhida
        option = get_menu_option()

        # Executa uma das opções escolhidas
        result = execute_option(option, OPTIONS, UNITYS_DF, Product, products)

        # Se a opção não for sair temos que printar algum resultado
        if option != "D":

            # Se o retorno for uma lista então um produto foi exluído
            if type(result) == type(products):
                products = result

                print("\nOperação realizada com sucesso.")

            # Se o retorno não for um boolean então um produto vai ser adicionado
            elif type(result) != type(True):

                products.append(result)

                # Verfica a posição do produto adicionado e adiciona um id baseado nela
                last_product = len(products) - 1
                products[last_product].add_class_id(last_product)

                print("\n")

                # Mostra o produto baseado no id, nesse caso o último produto adicionado
                show_clas_by_id(products, last_product, UNITYS_DF)
                print("\nOperação realizada com sucesso.")

            elif result:
                print("\nOperação realizada com sucesso.")

            else:
                print("\nOperação falhou.")

    print("Saindo...")


if __name__ == "__main__":
    main()
