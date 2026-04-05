import pandas as pd
import numpy as np

def generar_caso_de_uso_detectar_inestabilidad_fisiologica():
    n_puntos = np.random.randint(100, 200)
    base_hr = np.random.randint(60, 100, size=n_puntos).astype(float)
    # Añadir picos de inestabilidad
    ruido = np.random.normal(0, 5, n_puntos)
    base_hr += ruido
    
    df = pd.DataFrame({'frecuencia_cardiaca': base_hr})
    ventana = np.random.randint(5, 15)
    
    return {"df_vitales": df, "ventana": ventana}