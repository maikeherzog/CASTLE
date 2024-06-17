import matplotlib
matplotlib.use('TkAgg') # or 'Qt5Agg'
import matplotlib.pyplot as plt


def plot_graph(x_values, y_values):
    plt.figure(figsize=(10,8))
    plt.plot(x_values, y_values)
    plt.title('Durchschnittlicher Informationsverlust zu Anzahl anonymisierter Cluster')
    plt.xlabel('Anzahl anonymisierter Cluster')
    plt.ylabel('Durchschnittlicher Informationsverlust')
    plt.grid(True)
    plt.savefig('C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/Diagrams/InfoLoss_Cluster_5000_100_1000_50.png') # Speichern Sie das Diagramm als 'output.png'
    print("gespeichert")

