from floodsystem.analysis import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime, numpy


def test_polyfit():
    all_stations = build_station_list()
    update_water_levels(all_stations)

    dt = 20
    p = 6
    for station in all_stations:
        if station.name == "Cam":
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    
    best_fit_poly, d0 = polyfit(dates, levels, p)
    assert isinstance(best_fit_poly, numpy.poly1d)
    assert best_fit_poly.order == p
    assert isinstance(d0, float)
