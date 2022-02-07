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