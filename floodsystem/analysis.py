import numpy as np
import matplotlib.dates


"""Module containing functions regarding analysis of level data"""

def polyfit(dates, levels, p):
    """Returns tuple of polynomial object and any date shift that represents the
    water level of a station over time."""

    t = matplotlib.dates.date2num(dates) #time

    p_coeff = np.polyfit(t - t[0], levels, p)
    poly = np.poly1d(p_coeff)

    return poly, t[0]

