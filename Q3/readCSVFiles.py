import os
import csv

def read_all_csv_files(folder_path):
    """
    This reads all CSV files from the given folder 
    and it returns a list of rows from all files combined.
    """
    all_rows = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)  # skip header

                for row in reader:
                    all_rows.append(row)

    return all_rows