from floodsystem.plot import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def test_plot_water_levels():
    all_stations = build_station_list()
    update_water_levels(all_stations)

    dt = 20
    for station in all_stations:
        if station.name == "Cam":
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            plot_water_levels(station, dates, levels)
            assert True #will assert true if doesn't already crash


def test_plot_water_levels_with_fit():
    all_stations = build_station_list()
    update_water_levels(all_stations)

    dt = 20
    p = 5
    for station in all_stations:
        if station.name == "Cam":
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            plot_water_level_with_fit(station, dates, levels, p)
            assert True #will assert true if doesn't already crash