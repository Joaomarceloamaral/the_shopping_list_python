"""Classe Produto"""


class Product:
    """
    Representa um produto com nome, unidade de medida, descrição e quantidade.

    Atributos:
        name (str): O nome do produto.
        unity (str): A unidade de medida do produto.
        description (str): A descrição do produto.
        quantity (int, opcional): A quantidade do produto (padrão é 0).
    """

    def __init__(self, name: str, unity: str, description: str, quantity=0):

        self.id = 0
        self.name = name
        self.unity = unity
        self.description = description
        self.quantity = quantity

    def add_class_id(self, id_number: int):
        """
        Define o ID da instância da classe.

        Parâmetros:
        - id_number (int): Número do ID a ser atribuído.

        Retorno:
        - Nenhum. Apenas define o atributo 'id' da instância.
        """
        self.id = id_number
