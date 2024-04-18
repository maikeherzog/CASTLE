import pandas as pd

def edit_data(path_from, path_to):
    # Open the .data file for reading
    with open(path_from, 'r') as f:
        lines = f.readlines()

    # Create a new list for the edited lines
    cleaned_lines = []

    for line in lines:
        # Check for '?' in the line
        if '?' not in line and line.strip():
            cleaned_lines.append(line.strip())

    # Column labelling
    header = "age, workclass, fnlwgt, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country, income"

    # add header and cleaned lines
    cleaned_data = [header] + cleaned_lines

    # Write the cleaned data to a new file
    with open(path_to, 'w') as f:
        for line in cleaned_data:
            f.write(line + '\n')

    print(f"Clean-up completed and the data was written to a new file with the path {path_to}.")

