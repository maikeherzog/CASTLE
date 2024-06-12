import pandas as pd

from src.hierarchy_tree import *

# Definition der Attributeigenschaften
attribute_properties = {
    0: {'name': 'age', 'type': 'continuous', 'interval': (17, 90)},
    1: {'name': 'workclass', 'type': 'cathegorical', 'hierarchy_tree': workclass_tree},
    2: {'name': 'fnlwgt', 'type': 'continuous', 'interval': (13769,  1484705)},
    3: {'name': 'education', 'type': 'cathegorical', 'hierarchy_tree': education_tree},
    4: {'name': 'education_num', 'type': 'continuous', 'interval': (1, 16)},
    5: {'name': 'marital-status', 'type': 'cathegorical', 'hierarchy_tree': marital_status_tree},
    6: {'name': 'occupation', 'type': 'cathegorical', 'hierarchy_tree': occupation_tree},
    7: {'name': 'relationship', 'type': 'cathegorical', 'hierarchy_tree': relationship_tree},
    8: {'name': 'race', 'type': 'cathegorical', 'hierarchy_tree': race_tree},
    9: {'name': 'capital-gain', 'type': 'continuous', 'interval': (0,  99999)},
    10: {'name': 'capital-loss', 'type': 'continuous', 'interval': (0, 4356)},
    11: {'name': 'hours-per-week', 'type': 'continuous', 'interval': (1, 99)},
    12: {'name': 'native-country', 'type': 'cathegorical', 'hierarchy_tree': native_country_tree},
    13: {'name': 'income', 'type': 'class', 'attributes': [' <=50K', ' >50K']},
}

attribute_properties_test = {
    0: {'name': 'age', 'type': 'continuous', 'interval': (18, 120)},
    1: {'name': 'education', 'type': 'cathegorical', 'hierarchy_tree': education_tree_test}
}
def edit_data(path_from, path_to):
    # Open the .data file for reading
    with open(path_from, 'r') as f:
        lines = f.readlines()

    # Create a new list for the edited lines
    cleaned_lines = []

    for line in lines:
        # Check for '?' in the line
        if '?' not in line and line.strip():
            cleaned_line = ",".join(component.strip() for component in line.split(','))
            cleaned_lines.append(cleaned_line)

    # Column labelling
    header = "pid, time, age, workclass, fnlwgt, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country, income"

    # add pid and time
    numbered_lines = []
    for i, line in enumerate(cleaned_lines):
        numbered_line = f"{i}, {i}, " + line
        numbered_lines.append(numbered_line)

    # add header and cleaned lines
    cleaned_data = [header] + numbered_lines

    # Write the cleaned data to a new file
    with open(path_to, 'w') as f:
        for line in cleaned_data:
            f.write(line + '\n')

    print(f"Clean-up completed and the data was written to a new file with the path {path_to}.")

def process_tuple(tuple_data, attribute_properties):
    processed_tuple = []
    print(enumerate(tuple_data))
    for i, value in enumerate(tuple_data):
        attribute_type = attribute_properties[i]['type']

        if attribute_type == 'continuous':
            interval = attribute_properties[i]['interval']
            # Berechne den Unterschied zwischen dem Maximalwert des Intervalls und dem Wert aus dem Tupel
            processed_value = interval[1] - value  # Hier wird das Intervall verwendet
        else:
            processed_value = value  # Für kategoriale Attribute, mache hier deine spezifische Verarbeitung

        processed_tuple.append(processed_value)

    return processed_tuple