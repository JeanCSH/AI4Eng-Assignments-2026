import numpy as np
from sklearn.decomposition import PCA

def optimizar_pca_señales(X, varianza_objetivo):
    pca = PCA().fit(X)
    cum_var = np.cumsum(pca.explained_variance_ratio_)
    n_comp = np.argmax(cum_var >= varianza_objetivo) + 1
    return (int(n_comp), cum_var)

def generar_caso_de_uso_optimizar_pca_señales():
    X = np.random.rand(100, 20)
    v_obj = 0.90
    
    entrada = {"X": X, "varianza_objetivo": v_obj}
    salida_esperada = optimizar_pca_señales(X, v_obj)
    
    return entrada, salida_esperada
