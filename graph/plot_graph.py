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
    plt.savefig(f'C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/Diagrams/qi_100_10000_50__32000__adult/{name}.png')
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


def plot_graph_ILoss_k(x_values_list, y_values_list, names_list):
    plt.figure(figsize=(10, 8))
    for i in range(len(x_values_list)):
        plt.plot(x_values_list[i], y_values_list[i], label=names_list[i])

    plt.title('Durchschnittlicher Informationsverlust zu Anzahl k')
    plt.xlabel('k')
    plt.ylabel('Durchschnittlicher Informationsverlust')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'C:/Users/maike/Documents/TU Dresden/Bachelorarbeit/CASTLE/Diagrams/ILoss_k__32000__/ILoss_k_20-200_adult&adult-castle__32000__10000_50.png')
    plt.show()