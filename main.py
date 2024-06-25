
import pandas as pd

from graph.plot_graph import plot_graph, plot_graph_ILoss_k, plot_graph_ILoss_QI
from src.Castle import Castle
from src.Data import Data
from src.edit_data import process_tuple, attribute_properties, edit_data, edit_data_sorted

print("hello world")

#edit_data_sorted("C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/data/adult.data", "C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/data/adult_sorted.csv")


# Pfad zur CSV-Datei
csv_datei_pfad = 'data/adult.csv'
#csv_datei_pfad = '../data/easy_data.csv'
#csv_datei_pfad = '../data/easy_data_double.csv'

# Anzahl der Zeilen, die eingelesen werden sollen
anzahl_zeilen = 32000

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

"""# Plots für QI zu ILoss
plot_data_ILoss_QI= {}

#Plot 1
data1 = Data(data_tuples, [2,3], [])
castle1 = Castle(data1.data, 31, 3125, 16, "adult")
castle1.castle_algo(data1.data)
x_values1 = range(1, len(castle1.anonymized_clusters_InfoLoss) + 1)
y_values1 = [sum(castle1.anonymized_clusters_InfoLoss[:i])/i for i in x_values1]
plot_data_ILoss_QI["1_QI"] = x_values1, y_values1

#plot_graph(x_values1, y_values1, "InfoLoss_Cluster_1_QI_10000_100_1000_50")

#y_values = castle.anonymized_clusters_InfoLoss

#Plot 2
data2 = Data(data_tuples, [2,8], [])
castle2 = Castle(data2.data, 31, 3125, 16, "adult")
castle2.castle_algo(data2.data)
x_values2 = range(1, len(castle2.anonymized_clusters_InfoLoss) + 1)
y_values2 = [sum(castle2.anonymized_clusters_InfoLoss[:i])/i for i in x_values2]
plot_data_ILoss_QI["6_QI"] = x_values2, y_values2
#plot_graph(x_values2, y_values2, "InfoLoss_Cluster_6_QI_10000_100_1000_50")


#Plot 3
data3 = Data(data_tuples, [2,12], [])
castle3 = Castle(data3.data, 31, 3125, 16, "adult")
castle3.castle_algo(data3.data)
x_values3 = range(1, len(castle3.anonymized_clusters_InfoLoss) + 1)
y_values3 = [sum(castle3.anonymized_clusters_InfoLoss[:i])/i for i in x_values3]
plot_data_ILoss_QI["10_QI"] = x_values3, y_values3
#plot_graph(x_values3, y_values3, "InfoLoss_Cluster_10_QI_10000_100_1000_50")


#Plot 4
data4 = Data(data_tuples, [2,16], [])
castle4 = Castle(data4.data, 31, 3125, 16, "adult")
castle4.castle_algo(data4.data)
x_values4 = range(1, len(castle4.anonymized_clusters_InfoLoss) + 1)
y_values4 = [sum(castle4.anonymized_clusters_InfoLoss[:i])/i for i in x_values4]
plot_data_ILoss_QI["14_QI"] = x_values4, y_values4
#plot_graph(x_values4, y_values4, "InfoLoss_Cluster_14_QI_10000_100_1000_50")

plot_graph("InfoLoss_Cluster_num_Cluster_1000_31_3125_16__1000__", plot_data_ILoss_QI)"""

"""# Plots für k zu ILoss
data = Data(data_tuples, [2,16], [])
x_values = range(2, 100, 10)
y_values = []
for k in x_values:
    castle = Castle(data.data, k, 3125, 16, "adult")
    castle.castle_algo(data.data)
    print("len anonymized clusters", len(castle.anonymized_clusters_InfoLoss))
    y_values.append(castle.average_Loss())
    print(f"K: {k}, ILoss: {y_values}")

plot_graph_ILoss_k(x_values, y_values, "InfoLoss_Cluster_K_1-100_312_2__1000__")"""

"""# Plots für QI zu ILoss

x_values = range(2, 10, 1)
y_values = []
for n in x_values:
    data = Data(data_tuples, [2, n + 2], [])
    castle = Castle(data.data, 3, 312, 2, "adult")
    castle.castle_algo(data.data)
    print("len anonymized clusters", len(castle.anonymized_clusters_InfoLoss))
    y_values.append(castle.average_Loss())
    print(f"K: {n}, ILoss: {y_values}")

plot_graph_ILoss_QI(x_values, y_values, "InfoLoss_Cluster_QI_2-10_3_312_2__1000__")"""

# original für IL und k
data = Data(data_tuples, [2, 16], [])
"""
castle = Castle(data.data, 20, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

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
"""
castle = Castle(data.data, 150, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

"""castle = Castle(data.data, 180, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())"""

castle = Castle(data.data, 200, 10000, 50, "adult")
castle.castle_algo(data.data)
print("Average InfoLoss: ", castle.average_Loss())

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