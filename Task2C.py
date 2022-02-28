from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    a = stations_highest_rel_level(stations, N)
    for i in a:
        print("{}, {}".format(i.name, i.latest_level))


if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()
