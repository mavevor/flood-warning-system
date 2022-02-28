import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit

"""Module containing functions creating plots related to level data"""


def plot_water_levels(station, dates, levels):
    """Displays a plot of station level against time"""

    plt.plot(dates, levels, label="Water Level")

    if station.typical_range_consistent():
        typical_range = station.typical_range
        plt.plot(dates, [typical_range[1]]*len(dates), "--", color="r", label="Typical High")
        plt.plot(dates, [typical_range[0]]*len(dates), "-.", color="r", label="Typical Low")
        plt.legend()
    else:
        print("Typical level range is not available for {}".format(station.name))

    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """Displays a plot of a station water level and the best-fit polynimial"""

    try:
        best_fit_poly, d0 = polyfit(dates, levels, p)
    except:
        pass
    else:
        t = matplotlib.dates.date2num(dates) - d0
        plt.plot(dates, best_fit_poly(t), "--", label="Best-fit Polynomial", c="r")

    plt.plot(dates, levels, label="Water Level")
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()

    plt.tight_layout()
    plt.show()
