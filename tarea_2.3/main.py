import pandas as pd

pd.set_option('display.max_columns', None)

data = pd.read_csv('./international-migration-March-2021-citizenship-by-visa-by-country-of-last-permanent-residence.csv');

# Podemos mostrar las columnas con
# data.columns

# Y las podemos seleccionar o crear un subset
# data_subset = data[...columnas]

print(data.isna().sum());
