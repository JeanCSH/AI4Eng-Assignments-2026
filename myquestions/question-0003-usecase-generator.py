import pandas as pd
import numpy as np

def analizar_degradacion_critica(df_material, umbral=20):
    df = df_material.copy()
    m_inicial = df['masa_restante'].iloc[0]
    df['porcentaje_perdida'] = ((m_inicial - df['masa_restante']) / m_inicial) * 100
    criticos = df[df['porcentaje_perdida'] > umbral]
    return criticos['tiempo_horas'].mean()

def generar_caso_de_uso_analizar_degradacion_critica():
    n = 50
    tiempos = np.arange(n)
    masa = 15.0 * np.exp(-0.02 * tiempos) + np.random.normal(0, 0.1, n)
    df = pd.DataFrame({'tiempo_horas': tiempos, 'masa_restante': masa})
    u = float(np.random.randint(15, 25))
    
    entrada = {"df_material": df, "umbral": u}
    salida_esperada = analizar_degradacion_critica(df, u)
    
    return entrada, salida_esperada
