# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa 
import math

def hav(x):
    y = x*math.pi/180
    return math.sin(y/2)**2
def archav(x):
    return 2*math.asin(x**(1/2))
def distance(lat1,long1, lat2, long2):
    h = hav(lat2-lat1) + (1-hav(lat1-lat2)-hav(lat1+lat2))*hav(long2-long1)     #hav(distance/r)
    r = 6371                                                                    #Radius of Earth
    return r*archav(h)


def stations_by_distance(stations, p):
    list = []
    for station in stations:
        d = distance(p[0],p[1], station.coord[0], station.coord[1])
        list.append((station, d))
    return sorted_by_key(list,1)

def stations_within_radius(stations, centre, r):
    list = []
    for station in stations:
        d = distance(centre[0],centre[1], station.coord[0], station.coord[1])
        if(d <= r): list.append(station)
    return list

#TASK 1D
def rivers_with_station(stations):
    """Given list of MonitoringStation objects; returns a set of names of rivers
    with a monitoring station given in the original list."""

    output = set()

    for station in stations:
        output.add(station.river)

    return output


#TASK 1D
def stations_by_river(stations):
    """Given list of MonitoringStation objects; returns dictionary mapping river
    names to a list of MonitoringStation objects, which lie on that river."""

    output = {}
    for station in stations:
        if station.river not in output:
            output[station.river] = [station]
        else:
            output[station.river].append(station)
    
    return output


#TASK E
def rivers_by_station_number(stations, N):
    """Given a list of MonitoringStation objects and integer N; returs list of N tupples containing
    river name and number of stations on tat river. If there are multiple rivers with same
    number of stations, they are added regardless."""

    output = []
    rivers = []
    river_stations = stations_by_river(stations)

    for name, stations_on_river in river_stations.items():
        rivers.append((name, len(stations_on_river)))

    rivers = sorted(rivers, key=lambda x: x[1], reverse=True)
    
    output = rivers[:N]
    boundary_no = output[N-1][1]
    for i in range(N, len(rivers)):
        if rivers[i][1] == boundary_no:
            output.append(rivers[i])
        else:
            break
    return output


