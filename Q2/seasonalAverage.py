from tempAnalysis import is_valid_number


def calculate_seasonal_averages(rows):
    """
    Calculates average temperature for each Australian season
    across all stations and all years.
    """
    seasons = {
    "Summer": [15, 4, 5],     # Dec, Jan, Feb
    "Autumn": [6, 7, 8],      # Mar, Apr, May
    "Winter": [9, 10, 11],    # Jun, Jul, Aug
    "Spring": [12, 13, 14]    # Sep, Oct, Nov
}


    season_data = {season: [] for season in seasons}

    for row in rows:
        for season, indices in seasons.items():
            for index in indices:
                if is_valid_number(row[index]):
                    season_data[season].append(float(row[index]))

    season_avg = {}
    for season in season_data:
        season_avg[season] = sum(season_data[season]) / len(season_data[season])

    return season_avg