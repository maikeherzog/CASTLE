import csv
from src.hierarchy_tree import *
"""Dictionary for defining the domains of different attributes across various datasets."""
attribute_properties = {
    "adult":{
        0: {'name': 'age', 'type': 'continuous', 'interval': (17, 90)},
        1: {'name': 'workclass', 'type': 'cathegorical', 'hierarchy_tree': workclass_tree},
        2: {'name': 'fnlwgt', 'type': 'continuous', 'interval': (13769,  1484705)},
        3: {'name': 'education', 'type': 'cathegorical', 'hierarchy_tree': education_tree},
        4: {'name': 'education_num', 'type': 'continuous', 'interval': (1, 16)},
        5: {'name': 'marital-status', 'type': 'cathegorical', 'hierarchy_tree': marital_status_tree},
        6: {'name': 'occupation', 'type': 'cathegorical', 'hierarchy_tree': occupation_tree},
        7: {'name': 'relationship', 'type': 'cathegorical', 'hierarchy_tree': relationship_tree},
        8: {'name': 'race', 'type': 'cathegorical', 'hierarchy_tree': race_tree},
        9: {'name': 'sex', 'type': 'cathegorical', 'hierarchy_tree': sex_tree},
        10: {'name': 'capital-gain', 'type': 'continuous', 'interval': (0,  99999)},
        11: {'name': 'capital-loss', 'type': 'continuous', 'interval': (0, 4356)},
        12: {'name': 'hours-per-week', 'type': 'continuous', 'interval': (1, 99)},
        13: {'name': 'native-country', 'type': 'cathegorical', 'hierarchy_tree': native_country_tree},
        14: {'name': 'income', 'type': 'class', 'attributes': [' <=50K', ' >50K']},
    },
    "easy_data":{
        0: {'name': 'age', 'type': 'continuous', 'interval': (18, 120)},
        1: {'name': 'education', 'type': 'cathegorical', 'hierarchy_tree': education_tree_easy}
    },
    "adult_castle":{
        0: {'name': 'age', 'type': 'continuous', 'interval': (17, 90)},
        1: {'name': 'fnlwgt', 'type': 'continuous', 'interval': (13769, 1484705)},
        2: {'name': 'education_num', 'type': 'continuous', 'interval': (1, 16)},
        3: {'name': 'capital-gain', 'type': 'continuous', 'interval': (0, 99999)},
        4: {'name': 'capital-loss', 'type': 'continuous', 'interval': (0, 4356)},
        5: {'name': 'hours-per-week', 'type': 'continuous', 'interval': (1, 99)},
        6: {'name': 'education', 'type': 'cathegorical', 'hierarchy_tree': education_tree},
        7: {'name': 'marital-status', 'type': 'cathegorical', 'hierarchy_tree': marital_status_tree},
        8: {'name': 'occupation', 'type': 'cathegorical', 'hierarchy_tree': occupation_tree},
        9: {'name': 'native-country', 'type': 'cathegorical', 'hierarchy_tree': native_country_tree},
        10: {'name': 'workclass', 'type': 'cathegorical', 'hierarchy_tree': workclass_tree},
        11: {'name': 'relationship', 'type': 'cathegorical', 'hierarchy_tree': relationship_tree},
        12: {'name': 'race', 'type': 'cathegorical', 'hierarchy_tree': race_tree},
        13: {'name': 'sex', 'type': 'cathegorical', 'hierarchy_tree': sex_tree},
        14: {'name': 'income', 'type': 'class', 'attributes': [' <=50K', ' >50K']},
    },
    "adult_castle_reverse":{
        0: {'name': 'native-country', 'type': 'cathegorical', 'hierarchy_tree': native_country_tree},
        1: {'name': 'occupation', 'type': 'cathegorical', 'hierarchy_tree': occupation_tree},
        2: {'name': 'marital-status', 'type': 'cathegorical', 'hierarchy_tree': marital_status_tree},
        3: {'name': 'education', 'type': 'cathegorical', 'hierarchy_tree': education_tree},
        4: {'name': 'hours-per-week', 'type': 'continuous', 'interval': (1, 99)},
        5: {'name': 'capital-loss', 'type': 'continuous', 'interval': (0, 4356)},
        6: {'name': 'capital-gain', 'type': 'continuous', 'interval': (0, 99999)},
        7: {'name': 'education_num', 'type': 'continuous', 'interval': (1, 16)},
        8: {'name': 'fnlwgt', 'type': 'continuous', 'interval': (13769, 1484705)},
        9: {'name': 'age', 'type': 'continuous', 'interval': (17, 90)},
        10: {'name': 'workclass', 'type': 'cathegorical', 'hierarchy_tree': workclass_tree},
        11: {'name': 'relationship', 'type': 'cathegorical', 'hierarchy_tree': relationship_tree},
        12: {'name': 'race', 'type': 'cathegorical', 'hierarchy_tree': race_tree},
        13: {'name': 'sex', 'type': 'cathegorical', 'hierarchy_tree': sex_tree},
        14: {'name': 'income', 'type': 'class', 'attributes': [' <=50K', ' >50K']},
    },
    "adult_castle_mix":{
        0: {'name': 'age', 'type': 'continuous', 'interval': (17, 90)},
        1: {'name': 'native-country', 'type': 'cathegorical', 'hierarchy_tree': native_country_tree},
        2: {'name': 'fnlwgt', 'type': 'continuous', 'interval': (13769, 1484705)},
        3: {'name': 'occupation', 'type': 'cathegorical', 'hierarchy_tree': occupation_tree},
        4: {'name': 'education_num', 'type': 'continuous', 'interval': (1, 16)},
        5: {'name': 'marital-status', 'type': 'cathegorical', 'hierarchy_tree': marital_status_tree},
        6: {'name': 'capital-gain', 'type': 'continuous', 'interval': (0, 99999)},
        7: {'name': 'education', 'type': 'cathegorical', 'hierarchy_tree': education_tree},
        8: {'name': 'capital-loss', 'type': 'continuous', 'interval': (0, 4356)},
        9: {'name': 'hours-per-week', 'type': 'continuous', 'interval': (1, 99)},
        10: {'name': 'workclass', 'type': 'cathegorical', 'hierarchy_tree': workclass_tree},
        11: {'name': 'relationship', 'type': 'cathegorical', 'hierarchy_tree': relationship_tree},
        12: {'name': 'race', 'type': 'cathegorical', 'hierarchy_tree': race_tree},
        13: {'name': 'sex', 'type': 'cathegorical', 'hierarchy_tree': sex_tree},
        14: {'name': 'income', 'type': 'class', 'attributes': [' <=50K', ' >50K']},
    },
    "adult_castle_binary_tree":{
            0: {'name': 'age', 'type': 'continuous', 'interval': (17, 90)},
            1: {'name': 'fnlwgt', 'type': 'continuous', 'interval': (13769, 1484705)},
            2: {'name': 'education_num', 'type': 'continuous', 'interval': (1, 16)},
            3: {'name': 'capital-gain', 'type': 'continuous', 'interval': (0, 99999)},
            4: {'name': 'capital-loss', 'type': 'continuous', 'interval': (0, 4356)},
            5: {'name': 'hours-per-week', 'type': 'continuous', 'interval': (1, 99)},
            6: {'name': 'education', 'type': 'cathegorical', 'hierarchy_tree': education_tree_binary},
            7: {'name': 'marital-status', 'type': 'cathegorical', 'hierarchy_tree': marital_status_tree_binary},
            8: {'name': 'occupation', 'type': 'cathegorical', 'hierarchy_tree': occupation_tree_binary},
            9: {'name': 'native-country', 'type': 'cathegorical', 'hierarchy_tree': native_country_tree_binary},
            10: {'name': 'workclass', 'type': 'cathegorical', 'hierarchy_tree': workclass_tree_binary},
            11: {'name': 'relationship', 'type': 'cathegorical', 'hierarchy_tree': relationship_tree_binary},
            12: {'name': 'race', 'type': 'cathegorical', 'hierarchy_tree': race_tree_binary},
            13: {'name': 'sex', 'type': 'cathegorical', 'hierarchy_tree': sex_tree},
            14: {'name': 'income', 'type': 'class', 'attributes': [' <=50K', ' >50K']},

    },
    "adult_castle_binary_tree_short":{
            0: {'name': 'age', 'type': 'continuous', 'interval': (17, 90)},
            1: {'name': 'fnlwgt', 'type': 'continuous', 'interval': (13769, 1484705)},
            2: {'name': 'education_num', 'type': 'continuous', 'interval': (1, 16)},
            3: {'name': 'capital-gain', 'type': 'continuous', 'interval': (0, 99999)},
            4: {'name': 'capital-loss', 'type': 'continuous', 'interval': (0, 4356)},
            5: {'name': 'hours-per-week', 'type': 'continuous', 'interval': (1, 99)},
            6: {'name': 'education', 'type': 'cathegorical', 'hierarchy_tree': education_tree_binary},
            7: {'name': 'marital-status', 'type': 'cathegorical', 'hierarchy_tree': marital_status_tree_binary},
            8: {'name': 'occupation', 'type': 'cathegorical', 'hierarchy_tree': occupation_tree_binary},
            9: {'name': 'native-country', 'type': 'cathegorical', 'hierarchy_tree': native_country_tree_binary_short},
            10: {'name': 'workclass', 'type': 'cathegorical', 'hierarchy_tree': workclass_tree_binary_short},
            11: {'name': 'relationship', 'type': 'cathegorical', 'hierarchy_tree': relationship_tree_binary},
            12: {'name': 'race', 'type': 'cathegorical', 'hierarchy_tree': race_tree_binary},
            13: {'name': 'sex', 'type': 'cathegorical', 'hierarchy_tree': sex_tree},
            14: {'name': 'income', 'type': 'class', 'attributes': [' <=50K', ' >50K']},

    },
    "adult_castle_big":{
        0: {'name': 'age', 'type': 'continuous', 'interval': (0, 1000)},
        1: {'name': 'fnlwgt', 'type': 'continuous', 'interval': (0, 5000000)},
        2: {'name': 'education_num', 'type': 'continuous', 'interval': (0, 100)},
        3: {'name': 'capital-gain', 'type': 'continuous', 'interval': (0, 100000)},
        4: {'name': 'capital-loss', 'type': 'continuous', 'interval': (0, 100000)},
        5: {'name': 'hours-per-week', 'type': 'continuous', 'interval': (0, 1000)},
        6: {'name': 'education', 'type': 'cathegorical', 'hierarchy_tree': education_tree},
        7: {'name': 'marital-status', 'type': 'cathegorical', 'hierarchy_tree': marital_status_tree},
        8: {'name': 'occupation', 'type': 'cathegorical', 'hierarchy_tree': occupation_tree},
        9: {'name': 'native-country', 'type': 'cathegorical', 'hierarchy_tree': native_country_tree},
        10: {'name': 'workclass', 'type': 'cathegorical', 'hierarchy_tree': workclass_tree},
        11: {'name': 'relationship', 'type': 'cathegorical', 'hierarchy_tree': relationship_tree},
        12: {'name': 'race', 'type': 'cathegorical', 'hierarchy_tree': race_tree},
        13: {'name': 'sex', 'type': 'cathegorical', 'hierarchy_tree': sex_tree},
        14: {'name': 'income', 'type': 'class', 'attributes': [' <=50K', ' >50K']},
    },
}

""" Functions for editing csv data files. """
def edit_data(path_from, path_to):
    """
    Cleans up the data in the file at path_from and writes the cleaned data to a new file at path_to.
    :param path_from (str): the path to the file to clean up (.data file)
    :param path_to (str): the path to the file to write the cleaned data to
    :return: None
    """
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

def edit_data_sorted(path_from, path_to):
    """
    Cleans up the data in the file at path_from and writes the cleaned data to a new file at path_to.
    :param path_from (str): the path to the file to clean up (.data file)
    :param path_to (str): the path to the file to write the cleaned data to
    :return: None
    """
    header = "pid, time, age, fnlwgt, education-num, capital-gain, capital-loss, hours-per-week, workclass, education, marital-status, occupation, relationship, race, sex, native-country, income"
    header_list = [x.strip() for x in header.split(",")]

    # Open the .data file for reading
    with open(path_from, 'r') as f:
        lines = f.readlines()

    # Create a new list for the edited lines
    cleaned_lines = []

    for line in lines:
        # Check for '?' in the line
        if '?' not in line and line.strip():
            line_data_dict = dict(zip(header_list, [x.strip() for x in line.split(",")]))

            # Arrange the data in the desired order
            reordered_data = [line_data_dict[column_name] for column_name in header_list]

            # Convert the list into a string and add to the output list
            cleaned_line = ",".join(reordered_data)
            cleaned_lines.append(cleaned_line)

    # add pid and time
    numbered_lines = []
    for i, line in enumerate(cleaned_lines, start=1):
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
    """
    Processes a tuple according to the attribute properties.
    :param tuple_data (list): the tuple data
    :param attribute_properties (dict): the attribute properties
    :return: the processed tuple
    """
    processed_tuple = []
    print(enumerate(tuple_data))
    for i, value in enumerate(tuple_data):
        attribute_type = attribute_properties[i]['type']

        if attribute_type == 'continuous':
            interval = attribute_properties[i]['interval']
            processed_value = interval[1] - value
        else:
            processed_value = value

        processed_tuple.append(processed_value)

    return processed_tuple

def switch_cols(csv_datei, path_for_save, new_order):
    """
    Switches the columns of a csv file according to the new order.
    :param csv_datei (str): the path to the csv file
    :param path_for_save (str): the path to save the new csv file
    :param new_order (list): the new order of the columns
    :return: None
    """
    with open(csv_datei, 'r') as file:
        daten = csv.reader(file)
        new_data = []
        for line in daten:
            new_line = [line[i] for i in new_order]
            new_data.append(new_line)

    with open(path_for_save, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_data)