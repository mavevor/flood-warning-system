# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

##TASK 1B
def stations_by_distance(stations, p):
    pass


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
    
    n_last = rivers[0][1]

    for river in rivers:
        if N <= 1:
            return output

        output.append(river)

        if river[1] < n_last:
            N -= 1
            n_last = river[1]


