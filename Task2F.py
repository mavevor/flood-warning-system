from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels, build_station_list
import datetime


def run():

    all_stations = build_station_list()
    update_water_levels(all_stations)

    N = 5
    dt = 2
    p = 4

    highest_stations_rel = stations_highest_rel_level(all_stations, N)

    for station in highest_stations_rel:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, p)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()