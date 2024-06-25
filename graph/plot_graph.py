import matplotlib
matplotlib.use('TkAgg') # or 'Qt5Agg'
import matplotlib.pyplot as plt


def plot_graph_ILoss_QI(x_values, y_values, name):
    plt.figure(figsize=(10,8))
    plt.plot(x_values, y_values)
    plt.title('Durchschnittlicher Informationsverlust zu Anzahl von QI')
    plt.xlabel('QI')
    plt.ylabel('Durchschnittlicher Informationsverlust')
    plt.grid(True)
    plt.savefig(f'C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/Diagrams/3_312_2__1000__/{name}.png')
    print("gespeichert")

def plot_graph(name, plot_data):
    plt.figure(figsize=(10, 8))
    for label, (x_values, y_values) in plot_data.items():
        plt.plot(x_values, y_values, label=label)
    plt.title('Durchschnittlicher Informationsverlust zu Anzahl anonymisierter Cluster')
    plt.xlabel('Anzahl anonymisierter Cluster')
    plt.ylabel('Durchschnittlicher Informationsverlust')
    plt.grid(True)
    plt.legend()  # Fügt eine Legene hinzu
    plt.savefig(f'C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/Diagrams/3_312_2__10000__/{name}.png')
    print("gespeichert")

def plot_graph_ILoss_k(x_values, y_values, name):
    plt.figure(figsize=(10,8))
    plt.plot(x_values, y_values)
    plt.title('Durchschnittlicher Informationsverlust zu Anzahl k')
    plt.xlabel('k')
    plt.ylabel('Durchschnittlicher Informationsverlust')
    plt.grid(True)
    plt.savefig(f'C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/Diagrams/k_3316_17__10000__/{name}.png')
    print("gespeichert")