import pandas as pd
import numpy as np

def normalizar_por_grupo(df, group_col):
    # 1. Identificar las columnas numéricas (todas excepto la columna de grupo)
    cols_numericas = df.columns.drop(group_col)
    
    # 2. Agrupar y aplicar la transformación Z-score por grupo
    # El método transform() de pandas garantiza que se conserve el orden original de las filas.
    # Se especifica ddof=0 para calcular la desviación estándar poblacional.
    df_normalizado = df.groupby(group_col)[cols_numericas].transform(
        lambda x: (x - x.mean()) / x.std(ddof=0)
    )
    
    # 3. Retornar únicamente el array de numpy con los valores transformados
    return df_normalizado.to_numpy()
