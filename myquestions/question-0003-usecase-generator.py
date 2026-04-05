import pandas as pd
import numpy as np

def generar_caso_de_uso_analizar_degradacion_critica():
    n_puntos = np.random.randint(50, 100)
    masa_inicial = np.random.uniform(10.0, 15.0)
    # Generar degradación progresiva con ruido
    tiempos = np.arange(n_puntos)
    masa = masa_inicial * np.exp(-0.02 * tiempos) + np.random.normal(0, 0.1, n_puntos)
    
    df = pd.DataFrame({'tiempo_horas': tiempos, 'masa_restante': masa})
    umbral = np.random.randint(15, 25)
    
    return {"df_material": df, "umbral": umbral}