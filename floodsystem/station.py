# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

        self.current_risk = None
        self.forecasted_risk = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    #TASK 1F
    def typical_range_consistent(self):
        """Check if hi/lo data is consistent and/ or available."""
        if self.typical_range == None:
            return False
        else:
            if self.typical_range[1] < self.typical_range[0]:
                return False
            else:
                return True
    #TASK 2B
    def relative_water_level(self):
        """ returns the latest water level as a fraction of the typical range """
        if (self.typical_range_consistent() and self.latest_level):
            return (self.latest_level - self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
        else: return None

    #TASK 2G
    def risk_by_water_level(self):
        water_level_rel = self.relative_water_level()
        if water_level_rel:
            if water_level_rel > 2: return 4                                    # 4 denotes very high level
            elif water_level_rel > 1: return 3                                  # 3 denotes high level
            elif water_level_rel > 0: return 2                                  # 2 denotes moderate level
            else: return 1                                                                  # 1 denotes low level
        else:
            return None

    #TASK 2G
    def relative_water_level_any(self, level):
        """ returns the latest water level as a fraction of the typical range """
        if self.typical_range_consistent():
            return (level - self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
        else: return None

#TASK 1F
def inconsistent_typical_range_stations(stations):
    """Given list of MonitoringStation objects; returns list of MonitoringStations
    with inconsistent hi/lo ranges"""

    output = []
    for station in stations:
        if not station.typical_range_consistent():
            output.append(station)
            
    return output

