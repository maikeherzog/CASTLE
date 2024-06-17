
import pandas as pd

from src.Castle import Castle
from src.Data import Data
from src.edit_data import process_tuple, attribute_properties, edit_data

print("hello world")

#edit_data("C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/data/adult.data", "C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/data/adult.csv")


# Pfad zur CSV-Datei
csv_datei_pfad = '../data/adult.csv'
#csv_datei_pfad = '../data/easy_data.csv'
#csv_datei_pfad = '../data/easy_data_double.csv'

# Anzahl der Zeilen, die eingelesen werden sollen
anzahl_zeilen = 500

# CSV-Datei mit pandas einlesen, nur die ersten 5 Zeilen
df = pd.read_csv(csv_datei_pfad, nrows=anzahl_zeilen)
# Setze den Index auf den ursprünglichen DataFrame zurück und füge einen neuen Index als Position hinzu
#df_reset = df.reset_index()
#input_stream = [(index,) + tuple(row) for index, row in df_reset.iterrows()]

#print(input_stream)
# print(input_stream[0][:3])
#print(CASTLE(input_stream, 3,4,4))

#tuple_data= input_stream[0]
#easy_data
#processed_data = process_tuple(tuple_data[:3], attribute_properties)  # Nur die ersten drei kontinuierlichen Attribute als Beispiel

print(df)
data_tuples = list(df.itertuples(index=False, name=None))
print(data_tuples)

#Data for adult data
data = Data(data_tuples, [2,16], [])
#data = Data(data_tuples, [2,6], [])
print (data.data[0].qi)

#Data for easy data
#data = Data(data_tuples, [2,4], [])
#print (data.data[0].qi)

#Data for easy data double
#data = Data(data_tuples, [2,4], [])
#print (data.data[0].qi)

castle = Castle(data.data, 10, 8, 5, "adult")
print(castle.castle_algo(data.data))




