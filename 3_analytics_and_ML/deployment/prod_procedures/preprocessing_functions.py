#importamos las librerías (módulos)
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Lasso

import joblib


# Funciones individuales de procesado y entrenamiento
# ====================================================

def load_data(df_path):
    # Carga los datos
    return pd.read_csv(df_path)



def divide_train_test(df, target):
    # Divide los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(df,
                                                        df[target],
                                                        test_size=0.1,
                                                        random_state=0)
    return X_train, X_test, y_train, y_test



def impute_na(df, var, replacement='Missing'):
    # Función para reempazar los NA por valores de usuario.
    return df[var].fillna(replacement)



def elapsed_years(df, var, ref_var='YrSold'):
    # Función para calcular intervalos de tiempo
    
    df[var] = df[ref_var] - df[var]
    return df



def log_transform(df, var):
    # Función para la transformación logarítmica.
    return np.log(df[var])



def remove_rare_labels(df, var, frequent_labels):
    # Función para la agrupación de variables poco frecuentes
    return np.where(df[var].isin(frequent_labels), df[var], 'Rare')



def encode_categorical(df, var, mappings):
    # Usamos un diccionario (mapeo) para recodificar las variables categóricas
    return df[var].map(mappings)



def train_scaler(df, output_path):
    scaler = MinMaxScaler()
    scaler.fit(df)
    joblib.dump(scaler, output_path)
    return scaler
  
    

def scale_features(df, scaler):
    scaler = joblib.load(scaler) # with joblib probably
    return scaler.transform(df)



def train_model(df, target, output_path):
    # initialise the model
    lin_model = Lasso(alpha=0.005, random_state=0)
    
    # train the model
    lin_model.fit(df, target)
    
    # save the model
    joblib.dump(lin_model, output_path)
    
    return None



def predict(df, model):
    model = joblib.load(model)
    return model.predict(df)

