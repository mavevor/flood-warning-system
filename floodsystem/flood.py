from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    high_level = []
    for station in stations:
        if station.typical_range_consistent():
            level = station.relative_water_level()
            if (level and level > tol):
                high_level.append((station, level))
    return sorted_by_key(high_level, 1, True)

def stations_highest_rel_level(stations, N):
    highest_level = []
    x = []
    for station in stations:
         if station.typical_range_consistent():
            level = station.relative_water_level()
            if level:
                highest_level.append((station, level))
    a = sorted_by_key(highest_level, 1, True)[:N]
    for i in a:
        x.append(i[0])
    return x