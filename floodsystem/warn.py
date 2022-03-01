import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np


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

    if change_speed == 0:
        change_speed = -1
    if change_acceleration == 0:
        change_acceleration = -1

                                                               #Derivative First  Second  Risk    
    if change_speed > 0 and change_acceleration > 0: return 4           #   +       +      4 (SEVERE)
    if change_speed > 0 and change_acceleration < 0: return 2           #   +       -      2 (MODERATE)
    if change_speed < 0 and change_acceleration > 0: return 3           #   -       +      3 (HIGH)
    if change_speed < 0 and change_acceleration < 0: return 1           #   -       -      1 (LOW)


def flood_risk(station):
    """Determines the flood risk of a given station.
       Returns integer 1-4 dependent on risk"""
    
    station.current_risk = station.risk_by_water_level()
    station.forecasted_risk = flood_risk_by_level_change(station)

    # Return greatest risk
    if station.current_risk and station.forecasted_risk:
        
        if station.forecasted_risk >= station.forecasted_risk:
            return station.forecasted_risk
        else:
            return station.current_risk

    elif station.forecasted_risk and not station.current_risk:
        return station.forecasted_risk

    elif not station.forecasted_risk and station.current_risk:
        return station.current_risk

    else:
        return None
