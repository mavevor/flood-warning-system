from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    a = stations_within_radius(stations, centre, r)
    x = []
    for i in a:
        x.append(i.name)
    x.sort()
    print(x)

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()