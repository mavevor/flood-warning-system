from floodsystem.warn import *
from floodsystem.stationdata import build_station_list, update_water_levels

def test_flood_risk():

    # Create list of first 10 stations and fetch water level data
    all_stations = build_station_list()[:10]
    update_water_levels(all_stations)

    for station in all_stations:
        risk = flood_risk(station)
        assert risk == station.current_risk or risk == station.forecasted_risk
        if risk:
            assert isinstance(risk, int)
            assert risk >=1 and risk <= 4   # Chenck that risk is an integer in correct range


def test_flood_risk_by_level_change():

    # Create list of first 10 stations and fetch water level data
    all_stations = build_station_list()[:5]
    update_water_levels(all_stations)

    for station in all_stations:
        risk = flood_risk_by_level_change(station)
        if risk:
            assert isinstance(risk, int)
            assert risk >=1 and risk <= 4   # Chenck that risk is an integer in correct range