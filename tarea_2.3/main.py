import pandas as pd
from mongo import get_database

pd.set_option('display.max_columns', None)

data = pd.read_csv(
    './international-migration-March-2021-citizenship-by-visa-by-country-of-last-permanent-residence.csv')

# Podemos mostrar las columnas con
# data.columns

# Y las podemos seleccionar o crear un subset
data_subset = data[['year_month', 'month_of_release', 'citizenship', 'visa', 'country_of_residence', 'estimate']]

# print(len(data_subset))

# Removemos los valores TOTAL en la columna visa
data_subset = data_subset[data_subset['visa'] != 'TOTAL']
# Removemos los valores TOTAL en la columna country_of_residence
data_subset = data_subset[data_subset['country_of_residence'] != 'TOTAL']
# Removemos los valores TOTAL en la columna citizenship
data_subset = data_subset[data_subset['citizenship'] != 'TOTAL']

# print(len(data_subset))
# print(data_subset.head(6))

# Exportamos csv limpio
data_subset.to_csv('limpio.csv', encoding='utf-8')

datalist = data_subset.values.tolist()
# print(len(datalist))
dbname = get_database()

dbname.migration_items.drop()
data_collection = dbname["migration_items"]

data_to_save = []
count = 0
for row in datalist:
    count = count + 1
    item = {
        "year_month": row[0],
        "month_of_release": row[1],
        "citizenship": row[2],
        "visa": row[3],
        "country_of_residence": row[4],
        "estimate": row[5]
    }
    data_to_save.append(item)
    print(item)
    print("Registro agregado: ", count)
    if count == 10:
        data_collection.insert_many(data_to_save)
        print(data_to_save)
        print("Agregados",  count, "registros")
        break

# Consultamos la coleccion de mongoDB
collection_items = data_collection.find()
print("Datos desde MongoDB")
for item in collection_items:
    print(item)

# Creamos un data frame para visualizar los datos de mejor manera
items_df = pd.DataFrame(data_collection.find())
print(items_df)
