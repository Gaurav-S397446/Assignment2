"""
temp_reader.py

This file contains functions related to reading temperature CSV files
and organising the data in a usable format.
"""

import csv
import os


def read_temperature_data(folder_path):
    """
    Reads all CSV files from the given folder and stores temperature values.

    Parameters:
        folder_path (str): Path to the folder containing CSV files

    Returns:
        station_temps (dict): Dictionary containing station-wise temperatures
        seasonal_temps (dict): Dictionary containing temperatures grouped by season
    """

    station_temps = {}

    seasonal_temps = {
        "Summer": [],
        "Autumn": [],
        "Winter": [],
        "Spring": []
    }

    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, "r") as file:
                reader = csv.reader(file)
                header = next(reader)

                # Months start from index 4 in the given CSV format
                months = header[4:]

                for row in reader:
                    station_name = row[0]
                    temperatures = row[4:]

                    # Create station entry if not present
                    if station_name not in station_temps:
                        station_temps[station_name] = []

                    # Read monthly temperatures
                    for i in range(len(temperatures)):
                        value = temperatures[i]

                        # Ignore missing values
                        if value == "" or value.lower() == "nan":
                            continue

                        temp = float(value)
                        station_temps[station_name].append(temp)

                        month = months[i]

                        # Assign temperature to correct Australian season
                        if month in ["December", "January", "February"]:
                            seasonal_temps["Summer"].append(temp)
                        elif month in ["March", "April", "May"]:
                            seasonal_temps["Autumn"].append(temp)
                        elif month in ["June", "July", "August"]:
                            seasonal_temps["Winter"].append(temp)
                        elif month in ["September", "October", "November"]:
                            seasonal_temps["Spring"].append(temp)

    return station_temps, seasonal_temps