import pandas as pd
import random

# Anzahl der Einträge, die erzeugt werden sollen
num_entries = 100

# Die möglichen Werte für den Bildungsabschluss
education_levels = ["Primary School", "Secondary School", "Bachelors", "Masters", "Ph.D"]

# leere Listen für die Datensätze
time = []
pid = []
ages = []
educations = []

# Zufällige Daten generieren
for i in range(num_entries):
    time.append(i)
    pid.append(i)
    ages.append(random.randint(18, 120))
    educations.append(random.choice(education_levels))

# Daten in einen DataFrame umwandeln
data = {"Time": time, "Person Id": pid, "Age": ages, "Education": educations}
df = pd.DataFrame(data)

# DataFrame in eine CSV-Datei schreiben
df.to_csv("easy_data.csv", index=False)
