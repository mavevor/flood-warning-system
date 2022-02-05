from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    
    all_stations = build_station_list()
    rivers = sorted(list(rivers_with_station(all_stations)))
    print("{} stations. First 10 - {}\n".format(len(rivers), rivers[:10]))

    river_stations = stations_by_river(all_stations)
    river_names = ["River Aire", "River Cam", "River Thames"]
    for river in river_names:
        print(sorted([station.name for station in river_stations[river]]))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
