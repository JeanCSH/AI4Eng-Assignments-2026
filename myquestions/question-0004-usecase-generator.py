import numpy as np

def generar_caso_de_uso_optimizar_pca_señales():
    n_canales = np.random.randint(20, 40)
    n_tiempos = 500
    # Generar datos con correlación estructural
    base = np.random.randn(n_tiempos, 5)
    X = np.dot(base, np.random.rand(5, n_canales)) + np.random.normal(0, 0.1, (n_tiempos, n_canales))
    
    varianza_objetivo = np.random.uniform(0.85, 0.95)
    
    return {"X": X, "varianza_objetivo": varianza_objetivo}