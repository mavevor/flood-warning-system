from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import build_station_list, fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
import datetime


def run():
    
    all_stations = build_station_list()

    N = 5
    dt = 10

    highest_stations_rel = stations_highest_rel_level(all_stations, N)

    for station in highest_stations_rel:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()