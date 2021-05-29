import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


# 1- Imputación datos faltantes var. categóricas
class CategoricalImputer(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # we need the fit statement to accomodate the sklearn pipeline
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna('Missing')

        return X


# 2- Imputación datos faltantes var. numéricas
class NumericalImputer(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # diccionario
        self.imputer_dict_ = {}
        
        for feature in self.variables:
            self.imputer_dict_[feature] = X[feature].mode()[0]
        return self

    def transform(self, X):

        X = X.copy()
        for feature in self.variables:
            X[feature].fillna(self.imputer_dict_[feature], inplace=True)
        return X


# 3- Intervalos de tiempo
class TemporalVariableEstimator(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None, reference_variable=None):
        
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

        self.reference_variables = reference_variable

    def fit(self, X, y=None):
        # ajustarse a sklearn pipeline
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[self.reference_variables] - X[feature]

        return X


# 4- Codificador de categorías poco frecuentes
class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, tol=0.05, variables=None):
        
        self.tol = tol
        
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):

        # diccionario de etiquetas
        self.encoder_dict_ = {}

        for var in self.variables:
            # el codificador "aprende" qué etiquetas son frecuentes
            t = pd.Series(X[var].value_counts() / np.float(len(X)))
            # etiquetas frecuentes
            self.encoder_dict_[var] = list(t[t >= self.tol].index)

        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.where(X[feature].isin(self.encoder_dict_[
                    feature]), X[feature], 'Rare')

        return X


# 5- Codificación variables categóricas
class CategoricalEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y):
        temp = pd.concat([X, y], axis=1)
        temp.columns = list(X.columns) + ['target']

        # diccionario codificación
        self.encoder_dict_ = {}

        for var in self.variables:
            t = temp.groupby([var])['target'].mean().sort_values(ascending=True).index
            self.encoder_dict_[var] = {k: i for i, k in enumerate(t, 0)}

        return self

    def transform(self, X):
        # codificar etiquetas
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.encoder_dict_[feature])

        return X


# 6- transformación logarítmica
class LogTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # ajustarse  sklearn pipeline
        return self

    def transform(self, X):
        X = X.copy()

        for feature in self.variables:
            X[feature] = np.log(X[feature])

        return X

# 7- Descartar variables que no vamos a necesitar
class DropUnecessaryFeatures(BaseEstimator, TransformerMixin):

    def __init__(self, variables_to_drop=None):
        
        self.variables = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # codificar etiquetas
        X = X.copy()
        X = X.drop(self.variables, axis=1)

        return X