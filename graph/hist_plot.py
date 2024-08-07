import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# Setzen Sie das Backend, falls erforderlich
matplotlib.use('Agg')  # Oder 'TkAgg', wenn Sie interaktive Plots benötigen

# Daten einlesen
df = pd.read_csv('../data/adult.csv')

# Überprüfen und Bereinigen der Spaltennamen
df.columns = df.columns.str.strip()  # Entfernt zusätzliche Leerzeichen in den Spaltennamen

# Liste der Spalten, für die Diagramme erstellt werden sollen
columns = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']

# Erstellen Sie eine Figur mit 2 Spalten und 3 Zeilen (6 Diagramme)
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(14, 18))

# Iterieren Sie über die Spalten und erstellen Sie die Diagramme
for i, col in enumerate(columns):
    if col not in df.columns:
        print(f"Spalte '{col}' nicht gefunden.")
        continue

    row = i // 2
    col_idx = i % 2
    ax = axes[row, col_idx]

    # Plotten der Verteilung
    sns.histplot(df[col], kde=False, stat='probability', ax=ax, bins=20)

    # Setzen der Achsenbeschriftungen
    #ax.set_title(f'Distribution of {col}')
    ax.set_xlabel(col, fontsize=18)
    ax.set_ylabel('Anteil', fontsize=18)
    ax.set_ylim(0, 1)  # Y-Achse von 0 bis 1

    if col == 'fnlwgt':
            ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

# Entfernen Sie leere Subplots, falls nötig
if len(columns) % 2 != 0:
    fig.delaxes(axes[-1, -1])

# Layout anpassen
plt.tight_layout()

# Diagramm speichern
plt.savefig('distribution_plots.svg', format='svg')


