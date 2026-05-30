import pandas as pd
import numpy as np

def promedio_top3_por_grupo(df):
    # 1. Ordenar los datos: agrupando primero y asegurando que las puntuaciones 
    # vayan de mayor a menor (descendente) dentro de cada grupo.
    df_ordenado = df.sort_values(by=['grupo', 'puntuacion'], ascending=[True, False])
    
    # 2. Identificar el top 3: tomar las primeras 3 filas de cada grupo
    top3 = df_ordenado.groupby('grupo').head(3)
    
    # 3. Calcular el promedio: agrupar nuevamente el top 3 y sacar la media de la puntuación
    promedios = top3.groupby('grupo')['puntuacion'].mean()
    
    # 4. Retornar el resultado como un array de numpy
    return promedios.to_numpy()
