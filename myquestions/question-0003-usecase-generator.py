import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression

def generar_caso_de_uso_entrenar_pipeline_diagnostico():
    """
    Genera un caso de prueba aleatorio (input y output esperado)
    para la función entrenar_pipeline_diagnostico.
    
    CRÍTICO: Esta función debe ir de primera en el archivo para que el
    validador de la materia la ejecute correctamente sin argumentos.
    """
    # 1. Configuración aleatoria de dimensiones
    n_samples = np.random.randint(40, 100)
    n_features = np.random.randint(8, 15)  # Debe ser mayor a 5 para que SelectKBest(k=5) funcione
    
    # 2. Generar datos aleatorios simulando rasgos de imágenes médicas
    X_random = np.random.randn(n_samples, n_features) * 10.0  # Escalas variadas
    y_random = np.random.randint(0, 2, size=n_samples)        # Etiquetas binarias (0 o 1)
    
    # 3. Construir el objeto INPUT (Diccionario de argumentos)
    input_data = {
        'X': X_random.copy(),
        'y': y_random.copy()
    }
    
    # 4. Calcular el OUTPUT esperado (Ground Truth)
    # Ejecuta la función interna para obtener el pipeline entrenado con estos datos concretos
    output_data = entrenar_pipeline_diagnostico(X_random.copy(), y_random.copy())
    
    return input_data, output_data

def entrenar_pipeline_diagnostico(X, y):
    """
    Lógica de solución para la pregunta 3. Recrea el pipeline requerido
    y lo entrena con los datos provistos.
    """
    # Crear el Pipeline con los pasos e hiperparámetros estipulados
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('selector', SelectKBest(score_func=f_classif, k=5)),
        ('classifier', LogisticRegression(C=0.1))
    ])
    
    # Entrenar el pipeline con las características y etiquetas recibidas
    pipeline.fit(X, y)
    
    # Devolver el objeto del pipeline entrenado
    return pipeline

# --- Ejemplo de ejecución y validación local ---
if __name__ == "__main__":
    # Generar un caso de uso de prueba
    entrada, salida_esperada = generar_caso_de_uso_entrenar_pipeline_diagnostico()
    
    print("=== INPUT GENERADO ===")
    print(f"Matriz X (Shape): {entrada['X'].shape}")
    print(f"Vector y (Shape): {entrada['y'].shape}")
    
    print("\n=== OUTPUT ESPERADO (Ground Truth) ===")
    print(f"Objeto devuelto: {salida_esperada}")
    print(f"Pasos del pipeline configurados: {list(salida_esperada.named_steps.keys())}")
    print(f"¿El modelo está entrenado?: {hasattr(salida_esperada.named_steps['classifier'], 'classes_')}")
