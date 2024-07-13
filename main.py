
import pandas as pd

from graph.plot_graph import plot_graph, plot_graph_ILoss_k, plot_graph_ILoss_QI
from src.Castle import Castle
from src.Data import Data
from src.edit_data import process_tuple, attribute_properties, edit_data, edit_data_sorted, switch_cols

print("hello world")

#edit_data_sorted("C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/data/adult.data", "C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/data/adult_sorted.csv")


# Pfad zur CSV-Datei
csv_datei_pfad_castle = 'data/adult_castle.csv'
csv_datei_pfad_reverse = 'data/adult_castle_reverse_new.csv'
csv_datei_pfad_mix = 'data/adult_castle_mix.csv'
#csv_datei_pfad = 'data/easy_data.csv'
#csv_datei_pfad = 'data/easy_data_double.csv'

# Anzahl der Zeilen, die eingelesen werden sollen
anzahl_zeilen = 32000
#anzahl_zeilen = 100

# CSV-Datei mit pandas einlesen, nur die ersten 5 Zeilen
df_castle = pd.read_csv(csv_datei_pfad_castle, nrows=anzahl_zeilen)
df_reverse = pd.read_csv(csv_datei_pfad_reverse, nrows=anzahl_zeilen)
df_mix = pd.read_csv(csv_datei_pfad_mix, nrows=anzahl_zeilen)
# Setze den Index auf den ursprünglichen DataFrame zurück und füge einen neuen Index als Position hinzu
#df_reset = df.reset_index()
#input_stream = [(index,) + tuple(row) for index, row in df_reset.iterrows()]

#print(input_stream)
# print(input_stream[0][:3])
#print(CASTLE(input_stream, 3,4,4))

#tuple_data= input_stream[0]
#easy_data
#processed_data = process_tuple(tuple_data[:3], attribute_properties)  # Nur die ersten drei kontinuierlichen Attribute als Beispiel

print(df_castle)
data_tuples_castle = list(df_castle.itertuples(index=False, name=None))
print(data_tuples_castle)

print(df_reverse)
data_tuples_reverse = list(df_reverse.itertuples(index=False, name=None))
print(data_tuples_reverse)

print(df_mix)
data_tuples_mix = list(df_mix.itertuples(index=False, name=None))
print(data_tuples_mix)

#Data for adult data
#data = Data(data_tuples, [2,16], [])
#data = Data(data_tuples, [2,6], [])
# data just 1 attributes
#print (data.data[0].qi)

#Data for easy data
#data = Data(data_tuples, [2,4], [])
#print (data.data[0].qi)

#Data for easy data double
#data = Data(data_tuples, [2,4], [])
#print (data.data[0].qi)


#castle = Castle(data.data, 3, 10, 5, "easy_data")


#print(castle.castle_algo(data.data))

#iLoss und QI

data1_castle = Data(data_tuples_castle, [2,4], [])
data2_castle = Data(data_tuples_castle, [2,6], [])
data3_castle= Data(data_tuples_castle, [2, 8], [])
data4_castle = Data(data_tuples_castle, [2, 10], [])
data5_castle = Data(data_tuples_castle, [2, 12], [])

data1_reverse = Data(data_tuples_reverse, [2,4], [])
data2_reverse = Data(data_tuples_reverse, [2,6], [])
data3_reverse= Data(data_tuples_reverse, [2, 8], [])
data4_reverse = Data(data_tuples_reverse, [2, 10], [])
data5_reverse = Data(data_tuples_reverse, [2, 12], [])

data1_mix = Data(data_tuples_mix, [2,4], [])
data2_mix = Data(data_tuples_mix, [2,6], [])
data3_mix= Data(data_tuples_mix, [2, 8], [])
data4_mix = Data(data_tuples_mix, [2, 10], [])
data5_mix = Data(data_tuples_mix, [2, 12], [])

castle1 = Castle(data1_castle.data, 100, 10000, 50, "adult_castle")
castle1.castle_algo(data1_castle.data)
print("Average InfoLoss: ", castle1.average_Loss())

castle6 = Castle(data1_reverse.data, 100, 10000, 50, "adult_castle_reverse")
castle6.castle_algo(data1_reverse.data)
print("Average InfoLoss: ", castle6.average_Loss())

castle11 = Castle(data1_mix.data, 100, 10000, 50, "adult_castle_mix")
castle11.castle_algo(data1_mix.data)
print("Average InfoLoss: ", castle11.average_Loss())

castle2 = Castle(data2_castle.data, 100, 10000, 50, "adult_castle")
castle2.castle_algo(data2_castle.data)
print("Average InfoLoss: ", castle2.average_Loss())

castle7 = Castle(data2_reverse.data, 100, 10000, 50, "adult_castle_reverse")
castle7.castle_algo(data2_reverse.data)
print("Average InfoLoss: ", castle7.average_Loss())

castle12 = Castle(data2_mix.data, 100, 10000, 50, "adult_castle_mix")
castle12.castle_algo(data2_mix.data)
print("Average InfoLoss: ", castle12.average_Loss())

castle3 = Castle(data3_castle.data, 100, 10000, 50, "adult_castle")
castle3.castle_algo(data3_castle.data)
print("Average InfoLoss: ", castle3.average_Loss())

castle8 = Castle(data3_reverse.data, 100, 10000, 50, "adult_castle_reverse")
castle8.castle_algo(data3_reverse.data)
print("Average InfoLoss: ", castle8.average_Loss())

castle13 = Castle(data3_mix.data, 100, 10000, 50, "adult_castle_mix")
castle13.castle_algo(data3_mix.data)
print("Average InfoLoss: ", castle13.average_Loss())

castle4 = Castle(data4_castle.data, 100, 10000, 50, "adult_castle")
castle4.castle_algo(data4_castle.data)
print("Average InfoLoss: ", castle4.average_Loss())

castle9 = Castle(data4_reverse.data, 100, 10000, 50, "adult_castle_reverse")
castle9.castle_algo(data4_reverse.data)
print("Average InfoLoss: ", castle9.average_Loss())

castle14 = Castle(data4_mix.data, 100, 10000, 50, "adult_castle_mix")
castle14.castle_algo(data4_mix.data)
print("Average InfoLoss: ", castle14.average_Loss())

castle5 = Castle(data5_castle.data, 100, 10000, 50, "adult_castle")
castle5.castle_algo(data5_castle.data)
print("Average InfoLoss: ", castle5.average_Loss())

castle10 = Castle(data5_reverse.data, 100, 10000, 50, "adult_castle_reverse")
castle10.castle_algo(data5_reverse.data)
print("Average InfoLoss: ", castle10.average_Loss())

castle15 = Castle(data5_mix.data, 100, 10000, 50, "adult_castle_mix")
castle15.castle_algo(data5_mix.data)
print("Average InfoLoss: ", castle15.average_Loss())


# original für IL und k

#data = Data(data_tuples, [2, 12], [])

"""castle = Castle(data.data, 100, 10000, 50, "adult_castle")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss_all())"""

"""castle = Castle(data.data, 100, 10000, 50, "adult_castle")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss_all())

castle = Castle(data.data, 50, 10000, 50, "adult_castle")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss_all())

castle = Castle(data.data, 20, 10000, 50, "adult_castle")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss_all())"""

"""
castle = Castle(data.data, 40, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 60, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 80, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 100, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 120, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 140, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 160, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 180, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 200, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())"""

"""
data = Data(data_tuples, [2, 16], [])

castle = Castle(data.data, 5, 3316, 17, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 10, 3316, 17, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 20, 3316, 17, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 30, 3316, 17, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 40, 3316, 17, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 50, 3316, 17, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data.data, 60, 3316, 17, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())
"""


#plot_graph_ILoss_k([2,3,4,5,6,7,8,9,10], [0.21407179310471494, 0.28115511138381305, 0.27798231955351405, 0.2897912486438855, 0.3542408444025129, 0.3662441030354796, 0.383069064263756, 0.3594858862882107, 0.4719898992050222], 'InfoLoss_Cluster_QI_2-10_3_312_2__1000__neu')
#plot_graph_ILoss_k([5,10,20,30,40,50,60], [0.2959409214230391, 0.44510246587294616, 0.5614279403758493, 0.5236612703312591, 0.5716889908209324, 0.6156253646781726, 0.6515944861442672], 'InfoLoss_Cluster_QI_2-10_3316_17__10000__neu')
#plot_graph_ILoss_k([10, 25, 50, 75, 100, 125, 150, 175, 200, 225], [0.41444599657390613, 0.5181606848631809, 0.6030626756404411, 0.6327106052030486, 0.6862595359430634, 0.6831731826904892, 0.7029661998202513, 0.7201581698541878, 0.7174547299096078, 0.7234883877717487], 'InfoLoss_Cluster_k_50-225_10000_50__32000__')
#plot_graph_ILoss_QI([2,4,6,8,10,12], [0.17502051638154154, 0.45453992687558753, 0.7575677414294303, 0.741961010887795, 0.7668720151473093,0.715101956076992], 'InfoLoss_Cluster_QI_2-10_100_10000_50__32000__adult')

#plot_graph_ILoss_k([[20,100,150,200], [50,100,150,200]],[[0.48371763114519095,0.6712416082448087, 0.6740524066736436, 0.7386193017910867],[0.5357345877041585, 0.514159838388337, 0.6279618280759122, 0.6372683759407402 ]], ['adult', 'adult_castle'])

"""data1 = Data(data_tuples, [2,4], [])
data2 = Data(data_tuples, [2,6], [])
data3= Data(data_tuples, [2, 8], [])

castle = Castle(data1.data, 3, 40, 2, "adult_castle_reverse")
castle.castle_algo(data1.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data2.data, 3, 40, 2, "adult_castle_reverse")
castle.castle_algo(data2.data)
print("Average InfoLoss: ", castle.average_Loss())

castle = Castle(data3.data,3, 40, 2, "adult_castle_reverse")
castle.castle_algo(data3.data)
print("Average InfoLoss: ", castle.average_Loss())"""

#switch_cols("C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/data/adult_castle.csv",
 #           "C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/data/adult_castle_reverse_new.csv", [0, 1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 12, 13, 14, 15, 16])