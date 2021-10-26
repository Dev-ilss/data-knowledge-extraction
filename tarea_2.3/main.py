import pandas as pd

pd.set_option('display.max_columns', None)

data = pd.read_csv('./international-migration-March-2021-citizenship-by-visa-by-country-of-last-permanent-residence.csv')

# Podemos mostrar las columnas con
# data.columns

# Y las podemos seleccionar o crear un subset
data_subset = data[['year_month','month_of_release','citizenship','visa', 'country_of_residence', 'estimate']]

#print(len(data_subset))

# Removemos los valores TOTAL en la columna visa
data_subset = data_subset[data_subset['visa'] != 'TOTAL']
# Removemos los valores TOTAL en la columna country_of_residence
data_subset = data_subset[data_subset['country_of_residence'] != 'TOTAL']
# Removemos los valores TOTAL en la columna citizenship
data_subset = data_subset[data_subset['citizenship'] != 'TOTAL']

#print(len(data_subset))
print(data_subset.head(6))

#Exportamos csv limpio
data_subset.to_csv('limpio.csv', encoding='utf-8')
