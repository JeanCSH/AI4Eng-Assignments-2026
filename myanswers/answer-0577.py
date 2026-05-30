import pandas as pd
import numpy as np

def filtrar_por_sigma(df, columna, n_sigmas=3):
    # 1. Calcular la media (μ) y la desviación estándar (σ) usando numpy
    # Se extraen los valores de la columna para usar las funciones de np
    valores = df[columna].to_numpy()
    mu = np.mean(valores)
    sigma = np.std(valores)
    
    # 2. Definir los límites inferior y superior del rango permitido
    limite_inferior = mu - (n_sigmas * sigma)
    limite_superior = mu + (n_sigmas * sigma)
    
    # Filtrar el DataFrame manteniendo solo los valores dentro del rango
    df_filtrado = df[(df[columna] >= limite_inferior) & (df[columna] <= limite_superior)]
    
    # 3. Retornar el DataFrame filtrado
    return df_filtrado
