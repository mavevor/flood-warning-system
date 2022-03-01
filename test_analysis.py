from floodsystem.analysis import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime, numpy


def test_polyfit():
    
    #create list of all stations and fetch water level data
    all_stations = build_station_list()
    update_water_levels(all_stations)

    dt = 20
    p = 6

    #search for the River Cam and obtain historic water level data
    for station in all_stations:
        if station.name == "Cam":
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

            #check that the dates and levels lists are the same length
            assert len(dates) == len(levels)
    
    #fit water level data with a polynomial approximation
    best_fit_poly, d0 = polyfit(dates, levels, p)

    #check that output is the correct datatype and the polynomial is of the desired degree
    assert isinstance(best_fit_poly, numpy.poly1d)
    assert best_fit_poly.order == p
    assert isinstance(d0, float)
