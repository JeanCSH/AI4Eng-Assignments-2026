from sklearn.preprocessing import RobustScaler

def escalar_robusto(X):
    # 1. Instanciar el RobustScaler de scikit-learn
    # Por defecto, utiliza el rango intercuartílico (IQR) entre los percentiles 25 y 75
    scaler = RobustScaler()
    
    # 2. Ajustar el escalador con la matriz X y aplicar la transformación
    X_transformado = scaler.fit_transform(X)
    
    # 3. Retornar la matriz procesada asegurando el tipo de dato float
    return X_transformado.astype(float)
