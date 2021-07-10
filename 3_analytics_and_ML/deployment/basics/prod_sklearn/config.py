
# Datos:
TRAINING_DATA_FILE = "houseprice.csv"
PIPELINE_NAME = 'lasso_regression'

TARGET = 'SalePrice'

# Variables: 
FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood',
            'OverallQual', 'OverallCond', 'YearRemodAdd',
            'RoofStyle', 'MasVnrType', 'BsmtQual', 'BsmtExposure',
            'HeatingQC', 'CentralAir', '1stFlrSF', 'GrLivArea',
            'BsmtFullBath', 'KitchenQual', 'Fireplaces', 'FireplaceQu',
            'GarageType', 'GarageFinish', 'GarageCars', 'PavedDrive',
            'LotFrontage',
            # esta última sólo la utilizamos para calcular los intervalos de tiempo...
            'YrSold']

# por lo que debe descartarse ANTES del entrenamiento.
DROP_FEATURES = 'YrSold'

# Variables numéricas con NAs en el set de entrenamiento.
NUMERICAL_VARS_WITH_NA = ['LotFrontage']

# Variables categóricas con NAs en el set de entrenamiento.
CATEGORICAL_VARS_WITH_NA = ['MasVnrType', 'BsmtQual', 'BsmtExposure',
                            'FireplaceQu', 'GarageType', 'GarageFinish']

TEMPORAL_VARS = 'YearRemodAdd'

# Variables continuas a las que aplicar la transformación logarítmica.
NUMERICALS_LOG_VARS = ['LotFrontage', '1stFlrSF', 'GrLivArea']

# Variables categóricas a codificar: etiquetas poco frecuentes e imputación de entero.
CATEGORICAL_VARS = ['MSZoning', 'Neighborhood', 'RoofStyle', 'MasVnrType',
                    'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
                    'KitchenQual', 'FireplaceQu', 'GarageType', 'GarageFinish',
                    'PavedDrive']
