import pandas as pd

from src.Castle import Castle
from src.Data import Data

# Sortieren der Daten
#edit_data_sorted("C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/data/adult.data", "C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/data/adult_sorted.csv")


# Pfad zur CSV-Datei
csv_datei_pfad_castle = 'data/adult_castle.csv'
csv_datei_pfad_reverse = 'data/adult_castle_reverse.csv'
csv_datei_pfad_mix = 'data/adult_castle_mix.csv'


# Anzahl der Zeilen, die eingelesen werden sollen
anzahl_zeilen = 32000

# CSV-Datei mit pandas einlesen
df_castle = pd.read_csv(csv_datei_pfad_castle, nrows=anzahl_zeilen)
df_reverse = pd.read_csv(csv_datei_pfad_reverse, nrows=anzahl_zeilen)
df_mix = pd.read_csv(csv_datei_pfad_mix, nrows=anzahl_zeilen)

# Dataframe in Liste von Tupeln umwandeln
print(df_castle)
data_tuples_castle = list(df_castle.itertuples(index=False, name=None))
print(data_tuples_castle)

print(df_reverse)
data_tuples_reverse = list(df_reverse.itertuples(index=False, name=None))
print(data_tuples_reverse)

print(df_mix)
data_tuples_mix = list(df_mix.itertuples(index=False, name=None))
print(data_tuples_mix)

# original für IL und k

#Bestimmen der QIs und der sensiblen Attribute
data = Data(data_tuples_castle, [2, 12], [])

#erstellen der CASTLE Instanzen mit den Parametern
castle = Castle(data.data, 200, 10000, 50, "adult_castle")
#ausführen des CASTLE Algorithmus
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss_all())

#wiederholen mit anderen Parametern
castle = Castle(data.data, 100, 10000, 50, "adult_castle")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss_all())

castle = Castle(data.data, 50, 10000, 50, "adult_castle")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss_all())

castle = Castle(data.data, 20, 10000, 50, "adult_castle")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss_all())

#iLoss und QI
#Bestimmen der QIs und der sensiblen Attribute
data1_castle = Data(data_tuples_castle, [2,4], [])
data2_castle = Data(data_tuples_castle, [2,6], [])
data3_castle= Data(data_tuples_castle, [2, 8], [])
data4_castle = Data(data_tuples_castle, [2, 10], [])
data5_castle = Data(data_tuples_castle, [2, 12], [])

#erstellen der CASTLE Instanzen mit den Parametern
castle1 = Castle(data1_castle.data, 100, 10000, 50, "adult_castle")
#ausführen des CASTLE Algorithmus
castle1.castle_algo(data1_castle.data)
print("Average InfoLoss: ", castle1.average_Loss())

#wiederholen mit anderen QI-Mengen
castle2 = Castle(data2_castle.data, 100, 10000, 50, "adult_castle")
castle2.castle_algo(data2_castle.data)
print("Average InfoLoss: ", castle2.average_Loss())

castle3 = Castle(data3_castle.data, 100, 10000, 50, "adult_castle")
castle3.castle_algo(data3_castle.data)
print("Average InfoLoss: ", castle3.average_Loss())

castle4 = Castle(data4_castle.data, 100, 10000, 50, "adult_castle")
castle4.castle_algo(data4_castle.data)
print("Average InfoLoss: ", castle4.average_Loss())

castle5 = Castle(data5_castle.data, 100, 10000, 50, "adult_castle")
castle5.castle_algo(data5_castle.data)
print("Average InfoLoss: ", castle5.average_Loss())
