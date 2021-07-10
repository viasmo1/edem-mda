#cargamos las librerías
import numpy as np

#cargamos las funciones de preprocesamiento y los datos de configuración: rutas, valores y grupos de variables.
import preprocessing_functions as pf
import config

#Silenciar los mensajes "warning"
import warnings
warnings.simplefilter(action='ignore')

# ================================================
# ENTRENAMIENTO

# cargar los daots
data = pf.load_data(config.PATH_TO_DATASET)

# dividir el set
X_train, X_test, y_train, y_test = pf.divide_train_test(data, config.TARGET)

# imputar variables categóricas
for var in config.CATEGORICAL_TO_IMPUTE:
    X_train[var] = pf.impute_na(X_train, var, replacement='Missing')


# imputar variables numéricas
X_train[config.NUMERICAL_TO_IMPUTE] = pf.impute_na(X_train,
       config.NUMERICAL_TO_IMPUTE,
       replacement=config.LOTFRONTAGE_MODE)


# intervalos de tiempo
X_train[config.YEAR_VARIABLE] = pf.elapsed_years(X_train,
       config.YEAR_VARIABLE, ref_var='YrSold')


# transformación logarítmica
for var in config.NUMERICAL_LOG:
    X_train[var] = pf.log_transform(X_train, var)


# agrupación de categorías poco frecuentes
for var in config.CATEGORICAL_ENCODE:
    X_train[var] = pf.remove_rare_labels(X_train, var, config.FREQUENT_LABELS[var])


# codificación de variables categóricas
for var in config.CATEGORICAL_ENCODE:
    X_train[var] = pf.encode_categorical(X_train, var,
           config.ENCODING_MAPPINGS[var])


# entrenear y guardar el escalador
scaler = pf.train_scaler(X_train[config.FEATURES],
                         config.OUTPUT_SCALER_PATH)

# escalar variables
X_train = scaler.transform(X_train[config.FEATURES])

# entrenar y guardar el modelo
pf.train_model(X_train,
               np.log(y_train),
               config.OUTPUT_MODEL_PATH)

print('Enterenamiento terminado')