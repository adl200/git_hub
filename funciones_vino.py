import pandas as pd
import numpy as np


def eliminaDecimales(df, col):
    """
    Recibe un DataFrame y el nombre de una columna.
    Crea una nueva columna <col>_sin_decimales con el mismo valor pero truncado (sin decimales).
    Devuelve el DataFrame modificado.
    """
    nuevo_nombre = f"{col}_sin_decimales"
    df[nuevo_nombre] = np.trunc(df[col])
    return df


def calculaRatio(df, col1, col2):
    """
    Calcula el ratio entre dos columnas: col1 / col2.
    Lanza una excepción si algún valor del ratio es mayor que 1.
    Devuelve una Serie con el ratio.
    """
    ratio = df[col1] / df[col2]

    if (ratio > 1).any():
        raise ValueError(f"Hay valores del ratio {col1}/{col2} mayores que 1")

    return ratio
    