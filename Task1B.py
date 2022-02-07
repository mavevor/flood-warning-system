from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance



def run():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    a = stations_by_distance(stations, p)
    x = []
    for i in a:
        x.append((i[0].name, i[0].town,i[1]))
    print(x[:10])
    print(x[-10:])

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()