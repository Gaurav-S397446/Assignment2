"""
temp_utils.py
This file contains all helper functions used for temperature analysis.
Only user-defined functions are used.
"""

import csv
import math
import os


def is_valid_number(value):
    """
    Checks if a value is a valid float number and not NaN.
    """
    try:
        num = float(value)
        return not math.isnan(num)
    except:
        return False

def calculate_station_ranges(rows):
    """
    Finds temperature range (max - min) for each station.
    Returns dictionary of station data.
    """
    station_data = {}

    for row in rows:
        station = row[0]
        temps = []

        for value in row[4:]:
            if is_valid_number(value):
                temps.append(float(value))

        if station not in station_data:
            station_data[station] = []

        station_data[station].extend(temps)

    station_ranges = {}
    for station in station_data:
        max_temp = max(station_data[station])
        min_temp = min(station_data[station])
        station_ranges[station] = (max_temp - min_temp, max_temp, min_temp)

    return station_ranges


def calculate_station_stddev(rows):
    """
    This function calculates standard deviation for each station.
    """
    station_data = {}

    for row in rows:
        station = row[0]
        temps = []

        for value in row[4:]:
            if is_valid_number(value):
                temps.append(float(value))

        if station not in station_data:
            station_data[station] = []

        station_data[station].extend(temps)

    station_std = {}

    for station, temps in station_data.items():
        mean = sum(temps) / len(temps)
        variance = sum((t - mean) ** 2 for t in temps) / len(temps)
        station_std[station] = math.sqrt(variance)

    return station_std