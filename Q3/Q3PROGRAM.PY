"""
main.py
Root file for the temperature analysis program.
"""

from tempAnalysis import *
from seasonalAverage import *
from readCSVFiles import *

TEMPERATURE_FOLDER = "temperatures"


def main():
    rows = read_all_csv_files(TEMPERATURE_FOLDER)

    # ---- Seasonal Averages ----
    seasonal_avg = calculate_seasonal_averages(rows)
    with open("average_temp.txt", "w") as file:
        for season, avg in seasonal_avg.items():
            file.write(f"{season}: {avg:.1f}°C\n")

    # ---- Largest Temperature Range ----
    station_ranges = calculate_station_ranges(rows)
    max_range = max(value[0] for value in station_ranges.values())

    with open("largest_temp_range_station.txt", "w") as file:
        for station, (range_val, max_t, min_t) in station_ranges.items():
            if round(range_val, 1) == round(max_range, 1):

                file.write(
                    f"{station}: Range {range_val:.1f}°C "
                    f"(Max: {max_t:.1f}°C, Min: {min_t:.1f}°C)\n"
                )

    # ---- Temperature Stability ----
    station_std = calculate_station_stddev(rows)
    min_std = min(station_std.values())
    max_std = max(station_std.values())

    with open("temperature_stability_stations.txt", "w") as file:
        file.write("Most Stable Stations:\n")
        for station, std in station_std.items():
            if round(std, 1) == round(min_std, 1):

                file.write(f"{station}: StdDev {std:.1f}°C\n")

        file.write("\nMost Variable Stations:\n")
        for station, std in station_std.items():
            if round(std, 1) == round(max_std, 1):

                file.write(f"{station}: StdDev {std:.1f}°C\n")


if __name__ == "__main__":
    main()