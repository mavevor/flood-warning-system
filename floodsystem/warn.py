import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np
import matplotlib.dates


def flood_risk_by_level_change(station):
    """Return a ranking (string) based on the rate of change of water level.
       Will return None if no historic level data is available"""

    dt = 2
    p = 10

    # Fetch level data for the past day and convert to relative water levels
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    rel_levels = [station.relative_water_level_any(level) for level in levels]

    # print("dates, levels, rel_levels")
    # print(dates, levels, rel_levels)

    if not dates or not rel_levels:
        return None
    
    try:
        best_polyfit, t0 = polyfit(dates, rel_levels, p)
    except:
        return None
    
    best_polyfit_der = np.polyder(best_polyfit) # First derivative of polynomial approximation
    best_polyfit_der2 = np.polyder(best_polyfit, m=2) # Second derivative of polynomial approximation

    change_speed = best_polyfit_der(0) # Most recent data at t=0, since dates list is in reverse chronological order
    change_acceleration = best_polyfit_der2(0)

    return change_speed, change_acceleration




    