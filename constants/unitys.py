"""
Arquivo que contém constantes importantes para a manipulação de opções de unidades
"""

import pandas as pd

# Dicionário para opções de unidades
UNITYS = {
    "name": [
        "quilograma",
        "grama",
        "litro",
        "mililitro",
        "unidade",
        "metro",
        "centimetro",
    ],
    "abreviation": [
        "kg",
        "g",
        "L",
        "ml",
        "unidades",
        "m",
        "cm",
    ],
    "option": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
    ],
}

# Transformando Dicionário em Dataframe
UNITYS_DF = pd.DataFrame(UNITYS)

# Pegando só a coluna de opções ex: "A"
OPTIONS = UNITYS_DF["option"]
