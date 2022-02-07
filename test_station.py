# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent_method():
    
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445) #Valid range
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert s.typical_range_consistent() == True
    
    s.typical_range = None
    assert s.typical_range_consistent() == False

    s.typical_range = (76.004, -12.3)
    assert s.typical_range_consistent() == False


def test_inconsistent_typical_range_stations():
    s0 = MonitoringStation("s_id_0", "m_id_0", "some station", (-2.0, 4.0), (-2.3, 3.4445), "River X", "My Town") #Valid
    s1 = MonitoringStation("s_id_1", "m_id_1", "some station", (2.0, 4.0), None, "River X", "My Town") #Invalid
    s2 = MonitoringStation("s_id_2", "m_id_2", "some station", (-2.0, -4.0), (76.004, -12.3), "River X", "My Town") #Invalid
    s3 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0, 1), "River X", "My Town") #Valid

    stations = [s0, s1, s2, s3]
    invalid_stations = inconsistent_typical_range_stations(stations)

    assert s1 in invalid_stations and s2 in invalid_stations