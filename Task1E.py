from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    all_stations = build_station_list()
    print(rivers_by_station_number(all_stations, 9))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()