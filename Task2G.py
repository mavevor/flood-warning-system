from floodsystem.warn import flood_risk_by_level_change
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

all_stations = build_station_list()
update_water_levels(all_stations)

for station in all_stations:
    if station.name == "Leighton Buzzard":
        print(flood_risk_by_level_change(station))
