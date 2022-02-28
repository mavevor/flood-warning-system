from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    a = stations_level_over_threshold(stations, tol)
    for i in a:
        print("{}, {}".format(i[0].name, i[1]))


if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()
