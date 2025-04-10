"""
Arquivo que contem funções importantes para as opções da lista de compras
"""


def validate_unity_option(option_selected: str, options) -> bool:
    """
    Verifica se a opção selecionada é válida com base na lista de opções disponíveis.

    Parâmetros:
        option_selected (str): A opção escolhida pelo usuário.

    Retorna:
        bool: True se a opção for válida, False caso contrário.
    """

    # Verifica se a opção que foi selecionada é válida
    option_validator = False

    # Verifica se a opção selecionada existe na coluna options do dataframe
    for option in options:
        if option_selected == option:
            option_validator = True

    if option_validator is True:

        return True

    else:

        return False


def get_unity_option(options, unitys_df) -> str:
    """
    Solicita ao usuário que escolha uma unidade de medida válida e retorna a opção selecionada.

    Retorna:
        str: A opção escolhida pelo usuário.
    """

    # Verifica se a opção que foi selecionada é válida
    validator = False

    while validator is False:

        print("\n\n---------------------- Unidades Disponíveis ----------------------")

        print("A - Quilograma")
        print("B - Grama")
        print("C - Litro")
        print("D - Mililitro")
        print("E - Unidade")
        print("F - Metro")
        print("G - Centímetro")

        # Coleta a opção digitada pelo usuário
        option_selected = str(
            input("\nEscolha uma das unidades de medias para o produto: ")
        ).upper()

        # Verifica se a opção escolhida é válida
        validator = validate_unity_option(option_selected, options)

        if validator is True:

            # Verificando nas opções de unidades o nome correspondente a opção escolhida
            option_name = unitys_df.loc[
                unitys_df["option"] == option_selected, "name"
            ].item()

            print(f"\nOpção {option_selected} - {option_name} escolhida!")

            return option_selected

        else:
            print(f"Opção {option_selected} não está na lista, tente novamente!")


def show_clas_by_id(products_list, id_number, unitys_df):
    """
    Exibe informações sobre um produto específico com base no seu ID.

    Parâmetros:
    - products_list (list): Lista de produtos disponíveis.
    - id_number (int): ID do produto desejado.
    - unitys_df (DataFrame): DataFrame contendo abreviações das unidades.

    Retorno:
    - Nenhum. A função apenas imprime as informações do produto.
    """

    product = products_list[id_number]

    # Verificando nas opções de unidades a abreviação correspondente a opção escolhida
    option_abreviation = unitys_df.loc[
        unitys_df["name"] == product.unity, "abreviation"
    ].item()

    print(f"------ Produto ID: {id_number} ------")
    print(f"ID do Produto: {product.id}")
    print(f"Nome do Produto: {product.name}")
    print(f"Unidade: {product.unity}")
    print(f"Quantidade: {product.quantity} {option_abreviation}")
    print(f"Descrição: {product.description}")


def execute_option(option: str, options, unitys_df, product, products_list):
    """
    Executa uma ação com base na opção selecionada pelo usuário.

    Parâmetros:
        option (str): A opção escolhida pelo usuário.
        options (list): Lista de opções disponíveis.
        unitys_df (pd.DataFrame): DataFrame contendo as unidades de medida.
        product (class): Classe Produto com atributos e metodos.
        products_list (products_list): Lista com as instancias da classe Produtos.

    Retorna:
        bool: True após a execução da opção.
        object: Classe com produto que foi adicionado

    """

    match option:

        case "A":
            print("\n\n---------------------- Adicionar Produto----------------------")

            name = str(input("Informe o nome do produto: "))
            unity = get_unity_option(options, unitys_df)

            # Verificando nas opções de unidades o nome correspondente a opção escolhida
            option_name = unitys_df.loc[unitys_df["option"] == unity, "name"].item()

            # Verificando nas opções de unidades a abreviação correspondente a opção escolhida
            option_abreviation = unitys_df.loc[
                unitys_df["option"] == unity, "abreviation"
            ].item()

            if option_name == "unidade":
                quantity = int(
                    input(
                        f"Informe a quantidade do produto em {option_abreviation}, numero inteiro: "
                    )
                )

            else:
                quantity = float(
                    input(f"Informe a quantidade do produto em {option_abreviation}: ")
                )

            description = str(input("Dê uma breve descrição do produto: "))

            produto = product(name, option_name, description, quantity)

            return produto

        case "B":
            print("\n\n---------------------- Remover Produto ----------------------")

            id_validator = False
            while id_validator is False:
                try:
                    id_number = int(input("Informe o ID do produto para remover: "))

                    id_validator = True

                except ValueError:

                    print(
                        "Valor que você inseriu é inválido, tente com um numero inteiro!\n"
                    )

            try:

                print("\n\nProduto Removido:")
                show_clas_by_id(products_list, id_number, unitys_df)

                products_list.pop(id_number)

                return products_list

            except IndexError:

                print("\nNão existe produto com esse ID!")

                return False

        case "C":
            print("\n\n---------------------- Pesquisar Produto ----------------------")

            print("\n\n----------- Lista de Produtos -----------")
            for i in range(len(products_list)):
                print("\n")
                show_clas_by_id(products_list, i, unitys_df)

            id_validator = False
            while id_validator is False:
                try:
                    id_number = int(input("\nInforme o ID do produto para pesquisar: "))

                    id_validator = True

                except ValueError:

                    print(
                        "Valor que você inseriu é inválido, tente com um numero inteiro!\n"
                    )

            try:

                print("\n")
                show_clas_by_id(products_list, id_number, unitys_df)

                return True

            except IndexError:

                print("\nNão existe produto com esse ID!")

                return False


def get_menu_option() -> str:
    """
    Exibe o menu principal e solicita ao usuário que escolha uma opção.

    Retorna:
        str: A opção escolhida pelo usuário.
    """

    print("\n\n---------------------- Lista de Compras Simples ----------------------")

    print("A - Adicionar produto")
    print("B - Remover produto")
    print("C - Pesquisar produto")
    print("D - Sair do programa")

    option = str(input("\nEscolha uma das opções acima: ")).upper()

    return option
