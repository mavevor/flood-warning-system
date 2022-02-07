from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list



def test_stations_by_distance():
    stations = build_station_list()
    p = (0,0)
    a = stations_by_distance(stations, p)
    assert len(a) == len(stations)                                              # each station should be a member of a
    for i in range(len(a)-1):
        assert a[i][1] <= a[i+1][1]                                             # a is listed in numerical order

def test_stations_within_radius():
    stations = build_station_list()
    centre = (0,0)
    r = stations_by_distance(stations, centre)[len(stations)//2 - 1][1]         # r as the midpoint distance
    a = stations_within_radius(stations, centre, r)
    assert len(a) == len(stations)//2                                           # number of stations within r should be the same as the midpoint
    