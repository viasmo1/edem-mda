#Necesitamos las funciones y los valores de configuración
import preprocessing_functions as pf
import config

# =========== predicción =========

# imputar valores
def predict(data):
    
    # imputar datos faltantes
    for var in config.CATEGORICAL_TO_IMPUTE:
        data[var] = pf.impute_na(data, var, replacement='Missing')
    
    data[config.NUMERICAL_TO_IMPUTE] = pf.impute_na(data,
           config.NUMERICAL_TO_IMPUTE,
           replacement=config.LOTFRONTAGE_MODE)
    
    
    # intervalos de tiempo
    data[config.YEAR_VARIABLE] = pf.elapsed_years(data,
           config.YEAR_VARIABLE, ref_var='YrSold')
    
    
    # transformación logarítmica
    for var in config.NUMERICAL_LOG:
       data[var] = pf.log_transform(data, var)
    
    
    # agrupación de etiquetas poco frecuentes
    for var in config.CATEGORICAL_ENCODE:
        data[var] = pf.remove_rare_labels(data, var, config.FREQUENT_LABELS[var])
    
    # codificación de var. categóricas
    for var in config.CATEGORICAL_ENCODE:
        data[var] = pf.encode_categorical(data, var,
               config.ENCODING_MAPPINGS[var])
    
    
    # escalar variables
    data = pf.scale_features(data[config.FEATURES],
                             config.OUTPUT_SCALER_PATH)
    
    # obtener predicciones
    predictions = pf.predict(data, config.OUTPUT_MODEL_PATH)
    
    return predictions

# ======================================
    
# Comprobación MSE RMSE y R2
    
if __name__ == '__main__':
    
    from math import sqrt
    import numpy as np
    
    from sklearn.metrics import mean_squared_error, r2_score
    
    import warnings
    warnings.simplefilter(action='ignore')
    
    # cargar los datos
    data = pf.load_data(config.PATH_TO_DATASET)
    X_train, X_test, y_train, y_test = pf.divide_train_test(data,
                                                            config.TARGET)
    
    pred = predict(X_test)
    
    # determinar mse y rmse
    print('MSE prueba: {}'.format(int(
        mean_squared_error(y_test, np.exp(pred)))))
    print('RMSE prueba: {}'.format(int(
        sqrt(mean_squared_error(y_test, np.exp(pred))))))
    print('R2 prueba: {}'.format(
        r2_score(y_test, np.exp(pred))))
    print()
        