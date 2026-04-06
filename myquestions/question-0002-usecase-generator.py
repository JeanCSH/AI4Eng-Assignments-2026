import pandas as pd
import numpy as np

def detectar_inestabilidad_fisiologica(df_vitales, ventana):
    df = df_vitales.copy()
    df['media_movil'] = df['frecuencia_cardiaca'].rolling(window=ventana).mean()
    df['desviacion'] = (df['frecuencia_cardiaca'] - df['media_movil']).abs()
    df = df.dropna(subset=['media_movil'])
    return df[df['desviacion'] > (df['media_movil'] * 0.15)]

def generar_caso_de_uso_detectar_inestabilidad_fisiologica():
    n_puntos = 100
    base_hr = np.random.randint(60, 100, size=n_puntos).astype(float)
    base_hr[np.random.randint(0, 100, 5)] += 50 
    df = pd.DataFrame({'frecuencia_cardiaca': base_hr})
    v = 10
    
    entrada = {"df_vitales": df, "ventana": v}
    salida_esperada = detectar_inestabilidad_fisiologica(df, v)
    
    return entrada, salida_esperada
