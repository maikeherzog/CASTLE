import itertools

import matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.lines as mlines


matplotlib.use('TkAgg') # or 'Qt5Agg'
import matplotlib.pyplot as plt

x_values_qi = [2,4,6,8,10]
x_values_qi_all= [1,2,3,4,5,6,7,8,9,10]
x_values_k = [20,50,100,200]

# Werte für QI
y_values_qi_paper = [0.05, 0.17, 0.24, 0.3, 0.35]

# kompletter Durchschnittlicher Informationsverlust über allen Tupeln
y_values_qi_castle = [0.2483696347570108, 0.36168077146298583, 0.386061843754726, 0.5332345963435429, 0.6776610664120115]
y_values_qi_castle_all = [0.008652005994402552, 0.2483696347570108, 0.4505926221293735, 0.36168077146298583, 0.35431500937809374, 0.386061843754726, 0.482808632140979, 0.5332345963435429, 0.6593923010565717, 0.6776610664120115]
y_values_qi_castle_reverse = [0.18574208730527858, 0.5893115200393008, 0.5978387629971983, 0.4767373789968718, 0.6759415306307202]
y_values_qi_castle_reverse_all = [0.053263935906116, 0.18574208730527858, 0.28536089629188977, 0.5893115200393008, 0.6934732469074669, 0.5978387629971983, 0.5333934410701987, 0.4767373789968718, 0.6631604666649661, 0.6759415306307202]
y_values_qi_castle_mix = [0.13280631191590095, 0.6132861029855499, 0.7142842037752191, 0.7107566664508188, 0.6791720107523715]
y_values_qi_castle_mix_all = [0.00897066348130573, 0.13280631191590095, 0.4993460106896701, 0.6132861029855499, 0.6604167686642873, 0.7142842037752191, 0.6289610074723366, 0.7107566664508188, 0.668013051691473, 0.6791720107523715]
y_values_qi_castle_new_tree = [0.3005564213662934, 0.33068126556705785,  0.4083100604654541, 0.5294765968476125, 0.6560982650037115]
y_values_qi_castle_short_tree = [0.24684234758433216, 0.34666696406544867, 0.4119481337381397, 0.5288144241818867, 0.6557387029935382]
y_values_qi_castle_big_intervalls = [0.022642880811881188, 0.056397081566482085, 0.055468823802983784, 0.2385588416300357,0.4313366544344852]

# Durchschnittlicher Informationsverlust über den Cluster
y_values_qi_castle_2 = [0.2560170828163158, 0.36545147483099477, 0.38840337982738704, 0.5344581085023651, 0.6775190829833714]
y_values_qi_castle_reverse_2 = [0.18157964660555334, 0.6054078014184396, 0.5995415357838287, 0.4776019017587392, 0.6756844747502789]
y_values_qi_castle_mix_2 = [0.14035018969081534, 0.6221640814480498, 0.7203938643793676, 0.7105915009042936, 0.6790095721070815]
y_values_qi_castle_new_tree_2 = [0.3113092358692388, 0.3317592978993259, 0.4119736649050401, 0.5314159753798142, 0.6571180868632295]

# Durchschittlicher Informationsverlust der letzten Cluster
y_values_qi_castle_3 = [0.39215440661359524, 0.3829460662622452, 0.46967407398981226, 0.5562506377935414, 0.6317118556355094]
y_values_qi_castle_reverse_3 = [1.0, 0.7506666666666666, 0.6666666666666666, 0.4480442176870748, 0.7105915009042936]
y_values_qi_castle_mix_3 = [0.00684931506849315, 0.7024836031158914, 0.7972993284082428, 0.7023139964248389, 0.7072171031910277 ]
y_values_qi_castle_new_tree_3 = [0.37075224341358715, 0.694217630674972, 0.3946353543050697, 0.6055514871861386, 0.7355042453496964]

#durchschnittlicher Onformationsverlust über anonymisierten Clustern
y_values_qi_castle_4=[0.3446095758314822, 0.42485780005037055, 0.3307439062456227, 0.5163637883345459, 0.70324918582464]
y_values_qi_castle_reverse_4=[]
y_values_qi_castle_mix_4=[]


# Werte für k
y_values_k_paper = [0.19, 0.25, 0.35, 0.39]
y_values_k_castle = [ 0.5437331988926057, 0.622437165959034, 0.6790459443622361, 0.7244802133632634]
y_values_k_adult = [0.6584107973981038, 0.7225233215413919, 0.7620742521021323, 0.7991629767469173]
y_values_castle_continous = [0.28400420642181723, 0.358315431149584, 0.4344031533675682, 0.47328211964451483]
y_values_castle_categorical = [0.22756587302711406, 0.4213855557541253, 0.5543123980993804, 0.6805062959506148]
y_values_k_castle_big_intervalls = [0.37710684743060885, 0.41438218961020207, 0.4316659155793987, 0.44292611419157757]
y_values_k_castle_big_intervalls_konti = [0.03374598657066146, 0.04592127689412862, 0.055105460291424255, 0.0680692702419068]
#Werte FADS
y_values_fads_castle = [0.18, 0.25, 0.32, 0.2, 0.27]

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


import matplotlib.pyplot as plt


def plot_multiple_curves_point_labels(x_values, y_values_list, colors, labels, title, xlabel, ylabel, filename, rotation=False,
                         point_labels_list=None):
    """
    Plots multiple curves with different colors and saves the plot.

    Parameters:
    x_values (list): List of x values.
    y_values_list (list of lists): List of lists where each sublist contains y values for a curve.
    colors (list): List of colors for each curve.
    labels (list): List of labels for each curve.
    title (str): Title of the plot.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    filename (str): Name of the file to save the plot.
    rotation (bool): Whether to rotate the x-axis labels.
    point_labels_list (list of lists): List of lists where each sublist contains labels for the points of a curve.
    """
    plt.figure(figsize=(10, 6))

    for i, (y_values, color, label) in enumerate(zip(y_values_list, colors, labels)):
        plt.plot(x_values, y_values, marker='o', color=color, label=label)

        # Punkte beschriften, falls point_labels_list angegeben ist
        if point_labels_list and i < len(point_labels_list):
            point_labels = point_labels_list[i]
            for x, y, point_label in zip(x_values, y_values, point_labels):
                plt.text(x, y, point_label, fontsize=9, ha='right')

    # plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    if rotation:
        plt.xticks(x_values, rotation=-25)
    else:
        plt.xticks(x_values)

    plt.savefig(filename, format='svg')
    # plt.show()


def plot_multiple_curves_point_labels_new(x_values, y_values_list, colors, labels, title, xlabel, ylabel, filename,
                                      rotation=False,
                                      point_labels_list=None, symbols_list=None, legend_symbols=None, legend_labels=None, linestyles=None):
    """
    Plots multiple curves with different colors and saves the plot.

    Parameters:
    x_values (list): List of x values.
    y_values_list (list of lists): List of lists where each sublist contains y values for a curve.
    colors (list): List of colors for each curve.
    labels (list): List of labels for each curve.
    title (str): Title of the plot.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    filename (str): Name of the file to save the plot.
    rotation (bool): Whether to rotate the x-axis labels.
    point_labels_list (list of lists): List of lists where each sublist contains labels for the points of a curve.
    symbols_list (list of lists): List of lists where each sublist contains symbols for the points of a curve.
    """
    plt.figure(figsize=(10, 6))

    # Dictionary to store the symbol handles for the legend
    symbol_handles = {}

    for i, (y_values, color, label) in enumerate(zip(y_values_list, colors, labels)):
        linestyle = linestyles[i] if linestyles and i < len(linestyles) else '-'
        plt.plot(x_values, y_values, color=color,linestyle=linestyle, label=label)

        # Punkte beschriften, falls point_labels_list angegeben ist
        if point_labels_list and i < len(point_labels_list) and symbols_list and i < len(symbols_list):
            point_labels = point_labels_list[i]
            symbols = symbols_list[i]
            for x, y, point_label, symbol in zip(x_values, y_values, point_labels, symbols):
                plt.scatter(x, y, marker=symbol, color=color)

                # Add the symbol to the legend if not already added
                if symbol not in symbol_handles:
                    symbol_handles[symbol] = mlines.Line2D([], [], color='black', marker=symbol, linestyle='None',
                                                           markersize=8, label=point_label)

    # Plot configuration
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc='best')
    plt.grid(True)
    if rotation:
        plt.xticks(x_values, rotation=-25)
    else:
        plt.xticks(x_values)

    # Add manually specified legend entries
    if legend_symbols and legend_labels and len(legend_symbols) == len(legend_labels):
        for symbol, label in zip(legend_symbols, legend_labels):
            plt.scatter([], [], marker=symbol, color='black', label=label)
        plt.legend(loc='best')

    plt.savefig(filename, format='svg')
    # plt.show()


def plot_multiple_curves(x_values, y_values_list, colors, labels, title, xlabel, ylabel, filename, rotation=False, point_labels_list=None):
    """
    Plots multiple curves with different colors and saves the plot.

    Parameters:
    x_values (list): List of x values.
    y_values_list (list of lists): List of lists where each sublist contains y values for a curve.
    colors (list): List of colors for each curve.
    labels (list): List of labels for each curve.
    title (str): Title of the plot.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    filename (str): Name of the file to save the plot.
    """
    plt.figure(figsize=(10, 6))

    for y_values, color, label in zip(y_values_list, colors, labels):
        plt.plot(x_values, y_values, marker='o', color=color, label=label)

    #plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    if rotation:
        plt.xticks(x_values, rotation=-25)
    else:
        plt.xticks(x_values)

    plt.savefig(filename, format='svg')
    #plt.show()


def plot_multiple_curves_sns(x_values, y_values_list, colors, labels, title, xlabel, ylabel, filename, styles, rotation=False,
                         point_labels_list=None):
    """
    Plots multiple curves with different colors and saves the plot.

    Parameters:
    x_values (list): List of x values.
    y_values_list (list of lists): List of lists where each sublist contains y values for a curve.
    colors (list): List of colors for each curve.
    labels (list): List of labels for each curve.
    title (str): Title of the plot.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    filename (str): Name of the file to save the plot.
    """
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # Create combinations of line styles and markers
    for idx, (y_values, color, label) in enumerate(zip(y_values_list, colors, labels)):
        # Use unique line style and marker for each curve
        line_style, marker = styles[idx % len(styles)]
        plt.plot(x_values, y_values, linestyle=line_style, marker=marker, color=color, label=label)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)

    if rotation:
        plt.xticks(rotation=-25)
    else:
        plt.xticks(rotation=0)

    if point_labels_list:
        for i, point_labels in enumerate(point_labels_list):
            for x, y, txt in zip(x_values, y_values_list[i], point_labels):
                plt.annotate(txt, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.savefig(filename, format='svg')


# Beispielaufruf

colors = ['red', 'blue', 'green', 'purple', 'orange']
labels = ['CASTLE_original', 'adult_castle', 'castle_reverse', 'castle_mix']
title = 'Informationsverlust bei verschiedenen großen QI Mengen'
xlabel = '|QI|'
ylabel = 'Informationsverlust'
# Different line styles and marker symbols
line_styles = [(':','o'), ('-','s'), ('--','^'), ('-.','D'), (':','*')]
#markers = ['o', 's', '^', 'D', 'v', 'p', '*', 'h']

#ILoss über alle Tuple
y_values_list = [
    y_values_qi_paper, y_values_qi_castle, y_values_qi_castle_reverse, y_values_qi_castle_mix
]
title = ""
filename = 'QI_ILoss_alle_Tuple.svg'
plot_multiple_curves_sns(x_values_qi, y_values_list, colors, labels, title, xlabel, ylabel, filename, line_styles)

#ILoss über alle Cluster
y_values_list_2 = [
    y_values_qi_paper, y_values_qi_castle_2, y_values_qi_castle_reverse_2, y_values_qi_castle_mix_2
]
filename_2 = 'QI_ILoss_alle_Cluster.svg'
plot_multiple_curves_sns(x_values_qi, y_values_list_2, colors, labels, title, xlabel, ylabel, filename_2, line_styles)

#ILoss über letzte Cluster
y_values_list_3 = [
    y_values_qi_paper, y_values_qi_castle_3, y_values_qi_castle_reverse_3, y_values_qi_castle_mix_3
]
filename_3 = 'QI_ILoss_letzte_Cluster.svg'
plot_multiple_curves_sns(x_values_qi, y_values_list_3, colors, labels, title, xlabel, ylabel, filename_3, line_styles)

#ILoss über anonymisierten Cluster
"""y_values_list_ano_c = [
    y_values_qi_paper, y_values_qi_castle_4, y_values_qi_castle_reverse_4, y_values_qi_castle_mix_4
]
filename_ano_c = 'QI_ILoss_anonymisierte_Cluster.svg'
plot_multiple_curves(x_values_qi, y_values_list_ano_c, colors, labels, title, xlabel, ylabel, filename_ano_c)"""

#ILoss vergleich
y_values_list_4 = [
    y_values_qi_paper, y_values_qi_castle, y_values_qi_castle_2, y_values_qi_castle_4, y_values_qi_castle_3
]
labels_2 = ['CASTLE_original', 'ILoss über allen Tupeln', 'ILoss über allen Clustern', 'ILoss über anonymisierten Clustern', 'ILoss über letzten Clustern']
filename_4 = 'QI_ILoss_vgl.svg'
title = ""
plot_multiple_curves_sns(x_values_qi, y_values_list_4, colors, labels_2, title, xlabel, ylabel, filename_4, line_styles)

#ILoss qi big intervalls
y_values_list_4 = [
    y_values_qi_paper, y_values_qi_castle, y_values_qi_castle_big_intervalls
]
labels_2 = ['CASTLE_original', 'ILoss ursprüngliche Intervalle', 'ILoss bei großen Intervallen']
filename_4 = 'QI_ILoss_big_intervalls.svg'
title = ""
plot_multiple_curves_sns(x_values_qi, y_values_list_4, colors, labels_2, title, xlabel, ylabel, filename_4, line_styles)

#ILoss QI über Tupel verschiedene Bäume
y_values_list_trees = [
    y_values_qi_paper, y_values_qi_castle, y_values_qi_castle_new_tree, y_values_qi_castle_short_tree
]
labels_trees = ['CASTLE_original', 'adult_castle', 'castle_new_tree', 'castle_short_tree']
filename_trees = 'QI_ILoss_alle_Tuple_vers_Bäume.svg'
title = ""
plot_multiple_curves_sns(x_values_qi, y_values_list_trees, colors, labels_trees, title, xlabel, ylabel, filename_trees, line_styles)

#ILoss k über Tupel
y_values_list_5 = [
    y_values_k_paper, y_values_k_castle, y_values_k_adult
]
#title_5 = 'Informationsverlust bei verschiedenen k Werten'
title_5 = ""
labels_5 = ['CASTLE_original', 'adult_castle', 'adult']
xlabel_5 = 'k'
filename_5 = 'k_ILoss_adult.svg'
plot_multiple_curves_sns(x_values_k, y_values_list_5, colors, labels_5, title_5, xlabel_5, ylabel, filename_5, line_styles)

#ILoss k big intervalls
y_values_list_big = [
    y_values_k_paper, y_values_k_castle, y_values_k_castle_big_intervalls, y_values_k_castle_big_intervalls_konti
]
title_big = ''
labels_big = ['CASTLE_original', 'adult_castle', 'big intervalls', 'big intervalls kontinuierliche Attr.']
xlabel_big = 'k'
filename_big = 'k_ILoss_big_intervalls.svg'
plot_multiple_curves_sns(x_values_k, y_values_list_big, colors, labels_big, title_big, xlabel_big, ylabel, filename_big, line_styles)

#ILoss k über Tupel Vergleich kontinuierlich und kategorisch
y_values_list_cc = [
    y_values_k_paper, y_values_castle_continous, y_values_castle_categorical
]
#title_cc = 'Informationsverlust bei verschiedenen k Werten (Vergleich kontinuierliche und kategorische Attribute)'
title_cc = ""
labels_cc = ['CASTLE_original', 'kontinuierliche Attribute', 'kategorische Attribute']
xlabel_cc = 'k'
filename_cc = 'k_ILoss_cont_vs_cate.svg'
plot_multiple_curves_sns(x_values_k, y_values_list_cc, colors, labels_cc, title_cc, xlabel_cc, ylabel, filename_cc, line_styles)

#ILoss über alle Tuple FADS
y_values_list_fads = [
    y_values_fads_castle, y_values_qi_castle_reverse
]
filename_fads = 'QI_ILoss_FADS.svg'
labels_fads = ["castle_fads", "castle_reverse"]
colors_fads = ['blue', 'green']
plot_multiple_curves_sns(x_values_qi, y_values_list_fads, colors_fads, labels_fads, title, xlabel, ylabel, filename_fads, line_styles)

#ILoss-QI alle Abstände castle
y_values_list_all = [
    y_values_qi_castle_all, y_values_qi_castle_reverse_all, y_values_qi_castle_mix_all
]
point_labels_qi_all_castle= ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week', 'education', 'marital-status', 'occupation', 'native-country']
point_labels_qi_all_reverse = ['native-country', 'occupation', 'marital-status', 'education', 'hours-per-week', 'capital-loss', 'capital-gain', 'education-num', 'fnlwgt', 'age']
point_labels_qi_all_mix = ['age', 'native-country', 'fnlwgt', 'occupation', 'education-num', 'marital-status', 'capital-gain', 'education', 'capital-loss', 'hours-per-week']
point_labels_list_all = [
    point_labels_qi_all_castle, point_labels_qi_all_reverse, point_labels_qi_all_mix
]
filename_all = 'QI_ILoss_castle_all_qi.svg'
labels_all = ["adult_castle", "castle_reverse", "castle_mix"]
xlabel_all = 'Hinzugefügtes Attribut'

plot_multiple_curves_point_labels(x_values_qi_all, y_values_list_all, colors, labels_all, title, xlabel_all, ylabel, filename_all, rotation=True, point_labels_list=point_labels_list_all)

# Beispielaufruf
y_values_list_all = [
    y_values_qi_castle_all, y_values_qi_castle_reverse_all, y_values_qi_castle_mix_all
]
point_labels_qi_all_castle= ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week', 'education', 'marital-status', 'occupation', 'native-country']
point_labels_qi_all_reverse = ['native-country', 'occupation', 'marital-status', 'education', 'hours-per-week', 'capital-loss', 'capital-gain', 'education-num', 'fnlwgt', 'age']
point_labels_qi_all_mix = ['age', 'native-country', 'fnlwgt', 'occupation', 'education-num', 'marital-status', 'capital-gain', 'education', 'capital-loss', 'hours-per-week']
point_labels_list_all = [
    point_labels_qi_all_castle, point_labels_qi_all_reverse, point_labels_qi_all_mix
]
filename_all = 'QI_ILoss_castle_all_qi.svg'
labels_all = ["adult_castle", "castle_reverse", "castle_mix"]
xlabel_all = '|QI|'
#ylabel = 'Y-Achse Label'
title = ''

# Symbole für die Attribute (kann angepasst werden)
symbols_castle = ['o', 'v', '^', '<', '>', 's', 'p', '*', 'h', 'D']
symbols_reverse = ['D', 'h', '*', 'p', 's', '>', '<', '^', 'v', 'o']
symbols_mix = ['o', 'D', 'v', 'h', '^', '*', '<', 'p', '>', 's']
symbols_list_all = [symbols_castle, symbols_reverse, symbols_mix]

legend_symbols = ['o', 'v', '^', '<', '>', 's', 'p', '*', 'h', 'D']
legend_labels = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week', 'education', 'marital-status', 'occupation', 'native-country']

linestyles = ['-', '--', '-.']

plot_multiple_curves_point_labels_new(x_values_qi_all, y_values_list_all, colors, labels_all, title, xlabel_all, ylabel, filename_all, rotation=False, point_labels_list=point_labels_list_all, symbols_list=symbols_list_all, legend_symbols=legend_symbols, legend_labels=legend_labels, linestyles=linestyles)

# CSV-Datei einlesen
df = pd.read_csv('../data/adult_castle.csv')

# Überprüfen der Spaltennamen, um sicherzustellen, dass sie korrekt sind
print(df.columns)

# Boxplot für die Spalte 'capital-gain' (die 6. Spalte) erstellen
plt.figure(figsize=(10, 6))
#plt.boxplot(df.iloc[:, 5], vert=False)  # .iloc[:, 5] greift auf die 6. Spalte zu (0-basiert)
#sns.kdeplot(df.iloc[:, 5], fill=True)  # `fill=True` anstelle von `shade=True`
#sns.kdeplot(x=df.iloc[:, 2])
#sns.kdeplot(x=df.iloc[:, 3])
#sns.kdeplot(x=df.iloc[:, 4])
#sns.kdeplot(x=df.iloc[:, 5])
#sns.kdeplot(x=df.iloc[:, 6])
sns.kdeplot(x=df.iloc[:, 7])
#plt.hist(df.iloc[:, 5], bins=30, edgecolor='k')

#plt.title('Boxplot für age')
#plt.title('Boxplot für fnlwgt ')
#plt.title('Boxplot für education-num')
#plt.title('Boxplot für capital-gain')
#plt.title('Boxplot für  capital-loss')
plt.title('Boxplot für hours-per-week')
#plt.xlabel('age')
#plt.xlabel('fnlwgt')
#plt.xlabel('education-num')
#plt.xlabel('capital-gain')
#plt.xlabel('capital-loss')
plt.xlabel('hours-per-week')

plt.ylabel('Häufigkeit')

# Diagramm speichern
#plt.savefig('age_boxplot_final.png')
#plt.savefig('fnlwgt_boxplot_final.png')
#plt.savefig('education-num_boxplot_final.png')
#plt.savefig('capital-gain_boxplot_final.png')
#plt.savefig('capital-loss_boxplot_final.png')
plt.savefig('hours-per-week_boxplot_final.png')

# Diagramm anzeigen
#plt.show()

# Pfad zur CSV-Datei
csv_file_path = '../data/adult_castle.csv'

# CSV-Daten laden
data = pd.read_csv(csv_file_path)

# Relevante Spalten extrahieren (index 3 bis 8)
selected_columns = data.iloc[:, 3:9]

# Sicherstellen, dass alle ausgewählten Spalten numerisch sind
for col in selected_columns.columns:
    selected_columns[col] = pd.to_numeric(selected_columns[col], errors='coerce')

# Boxplots erstellen
fig = plt.figure(figsize=(10, 20))
ax = fig.add_axes([0, 0, 1, 1])
ax.boxplot([selected_columns[col].dropna() for col in selected_columns])
ax.set_xticklabels(selected_columns.columns)


# Plot anzeigen
#plt.show()

# Diagramm speichern
fig.savefig('boxplot_diagramm.png')