import pandas as pd
import numpy as np

def filtrar_genes_criticos(df, umbral_varianza, max_nans):
    limite_nulos = len(df) * max_nans
    df_filtrado = df.loc[:, df.isnull().sum() <= limite_nulos]
    df_imputado = df_filtrado.fillna(df_filtrado.mean())
    return df_imputado.loc[:, df_imputado.var() > umbral_varianza]

def generar_caso_de_uso_filtrar_genes_criticos():
    n_genes, n_muestras = np.random.randint(10, 20), np.random.randint(50, 100)
    data = np.random.rand(n_muestras, n_genes)
    mask = np.random.choice([True, False], size=data.shape, p=[0.1, 0.9])
    data[mask] = np.nan
    df = pd.DataFrame(data, columns=[f"Gene_{i}" for i in range(n_genes)])
    
    u_var, m_nans = 0.05, 0.15
    
    # Preparamos la entrada y la salida esperada
    entrada = {"df": df, "umbral_varianza": u_var, "max_nans": m_nans}
    salida_esperada = filtrar_genes_criticos(df, u_var, m_nans)
    
    return entrada, salida_esperada
