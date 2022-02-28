
from floodsystem.geo import *

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
    

from turtle import Turtle
from numpy import isin
from floodsystem.geo import *
from floodsystem.station import MonitoringStation

def test_rivers_with_station():

    #Create list of stations and set of river names
    stations = build_station_list()
    rivers = rivers_with_station(stations)

    assert isinstance(rivers, set)                                              # No duplicates possible
    assert len(rivers) > 0                                                      # Has been filled
    
    for river in rivers:
        assert isinstance(river, str)                                           # Make sure names are in the set

def test_stations_by_river():

    #Create list of stations and dictionary of rivers and stations
    stations = build_station_list()
    river_stations = stations_by_river(stations)

    assert isinstance(river_stations, dict)

    for river, station_list in river_stations.items():
        assert isinstance(river, str)                                           # Are names
        assert isinstance(station_list, list) #Is a list

        for station in station_list:
            assert isinstance(station, MonitoringStation)                       # List of the correct object
            assert station.river == river                                       # Make sure river is correct

def test_rivers_by_station_number():

    N = 12
    #Create list of stations and list of names of the most recorded rivers
    stations = build_station_list()
    popular_rivers = rivers_by_station_number(stations, N)

    assert isinstance(popular_rivers, list)                                     # Is a list?
    
    for river in popular_rivers:
        assert isinstance(river, tuple)                                         # List contains tuples only?
        assert isinstance(river[0], str)                                        # First element of each tuple is a string?
        assert isinstance(river[1], int)                                        # Second element of each tuple is an integer?
    
    if len(popular_rivers) == N:
        assert len(popular_rivers) == N
    else:
        last_river_no = popular_rivers[N-1][1]
        for river in popular_rivers[N:]:
            assert river[1] == last_river_no


