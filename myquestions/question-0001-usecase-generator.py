import pandas as pd
import numpy as np

def generar_caso_de_uso_filtrar_genes_criticos():
    n_genes = np.random.randint(10, 20)
    n_muestras = np.random.randint(50, 100)
    data = np.random.rand(n_muestras, n_genes)
    
    # Introducir nulos aleatorios
    mask = np.random.choice([True, False], size=data.shape, p=[0.1, 0.9])
    data[mask] = np.nan
    
    df = pd.DataFrame(data, columns=[f"Gene_{i}" for i in range(n_genes)])
    umbral_var = 0.05
    max_nans = 0.15
    
    return {"df": df, "umbral_varianza": umbral_var, "max_nans": max_nans}

