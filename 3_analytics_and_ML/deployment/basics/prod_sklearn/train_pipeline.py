#importar librerías y métodos
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
import joblib

#importamos la definición de nuestro pipeline y los valores de configuración.
import pipeline
import config


#ejecutamos la estimación
def run_training():
    """Entrena el modelo."""

    # leer los datos del set de entrenamiento
    data = pd.read_csv(config.TRAINING_DATA_FILE)

    # divide el set en entrenamiento y prueba.
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.1,
        random_state=0)  # fijamos la semilla

    # transformamos la variable target a logaritmos
    y_train = np.log(y_train)
    y_test = np.log(y_test)

    pipeline.price_pipe.fit(X_train[config.FEATURES], y_train)
    joblib.dump(pipeline.price_pipe, config.PIPELINE_NAME)


if __name__ == '__main__':
    run_training()
