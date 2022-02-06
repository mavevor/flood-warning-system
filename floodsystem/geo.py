# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa 
from . import haversine  

def stations_by_distance(stations, p):
    list = []
    for station in stations:
        d = haversine.distance(p[0],p[1], station.coord[0], station.coord[1])
        list.append((station, d))
    return sorted_by_key(list,1)

def stations_within_radius(stations, centre, r):
    list = []
    for station in stations:
        d = haversine.distance(centre[0],centre[1], station.coord[0], station.coord[1])
        if(d < r): list.append(station)
    return list