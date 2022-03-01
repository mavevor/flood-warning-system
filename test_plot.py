from floodsystem.plot import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def test_plot_water_levels():

    #create list of all stations and fetch water level data
    all_stations = build_station_list()
    update_water_levels(all_stations)

    dt = 20

    #search for River Cam and plot
    for station in all_stations:
        if station.name == "Cam":
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            assert len(dates) == len(levels) #check lenth of dates and levels lists are the same
            plot_water_levels(station, dates, levels)
            assert True #will assert true if didn't crash


def test_plot_water_levels_with_fit():

    #create list of all stations and fetch water level data
    all_stations = build_station_list()
    update_water_levels(all_stations)

    dt = 20
    p = 5
    
    #search for River Cam and plot with polynomial approximation
    for station in all_stations:
        if station.name == "Cam":
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            assert len(dates) == len(levels) #check lenth of dates and levels lists are the same
            plot_water_level_with_fit(station, dates, levels, p)
            assert True #will assert true if didn't crash
