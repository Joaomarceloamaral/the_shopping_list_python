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


def execute_option(option: str, options, unitys_df) -> bool:
    """
    Executa uma ação com base na opção selecionada pelo usuário.

    Parâmetros:
        option (str): A opção escolhida pelo usuário.
        options (list): Lista de opções disponíveis.
        unitys_df (pd.DataFrame): DataFrame contendo as unidades de medida.

    Retorna:
        bool: True após a execução da opção.
    """

    match option:

        case "A":
            print("\n\n---------------------- Adicionar Produto----------------------")

            name = str(input("Informe o nome do produto: "))
            unity = get_unity_option(options, unitys_df)

            # Verificando nas opções de unidades o nome correspondente a opção escolhida
            option_name = unitys_df.loc[unitys_df["option"] == unity, "name"].item()

            print(
                "\n\n---------------------- Produto Adicionado ----------------------"
            )
            print(f"Nome do Produto: {name}")
            print(f"Unidade: {option_name}")

            return True

        case "B":
            print("Remover")

            return True

        case "C":
            print("Pesquisar")

            return True


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
