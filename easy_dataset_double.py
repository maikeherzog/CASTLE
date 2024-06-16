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
    age = random.randint(18, 120)  # generate a random age
    education = random.choice(education_levels)  # generate a random education level

    # add this set of data twice
    for j in range(2):
        time.append(i*2 + j)  # count time consecutively
        pid.append(i)
        ages.append(age)  # use the previously generated age
        educations.append(education)  # use the previously generated education level

# Daten in einen DataFrame umwandeln
data = {"Time": time, "Person Id": pid, "Age": ages, "Education": educations}
df = pd.DataFrame(data)

# DataFrame in eine CSV-Datei schreiben
df.to_csv("easy_data_double.csv", index=False)
