from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
    s0 = MonitoringStation("s_id_0", "m_id_0", "some station", (-2.0, 4.0), (0.1, 3), "River X", "My Town" )
    s0.latest_level = None                                                                                      #invalid
    s1 = MonitoringStation("s_id_1", "m_id_1", "some station", (2.0, 4.0), None, "River X", "My Town")
    s1.latest_level = 3                                                                                         #Invalid
    s2 = MonitoringStation("s_id_2", "m_id_2", "some station", (-2.0, -4.0), (3, 0.1), "River X", "My Town")
    s2.latest_level  = 3                                                                                        #Invalid
    s3 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0.1, 3), "River X", "My Town")
    s3.latest_level = 1                                                                                         # < tol
    s4 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0.1, 3), "River X", "My Town")
    s4.latest_level = 1.7                                                                                       # > tol
    s5 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0.1, 3), "River X", "My Town")
    s5.latest_level = 2                                                                                         # > tol
    s6 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0.1, 3), "River X", "My Town")
    s6.latest_level = 2.5                                                                                       # > tol

    stations = [s0, s1, s2, s3, s4, s5, s6]
    tol = 0.50
    results = stations_level_over_threshold(stations, tol)
    assert len(results) == 3
    for i in range(len(results)-1):
        assert results[i+1][1] <= results[i][1]

def test_stations_highest_rel_level():
    s0 = MonitoringStation("s_id_0", "m_id_0", "some station", (-2.0, 4.0), (0.1, 3), "River X", "My Town" )
    s0.latest_level = None                                                                                      #invalid
    s1 = MonitoringStation("s_id_1", "m_id_1", "some station", (2.0, 4.0), None, "River X", "My Town")
    s1.latest_level = 3                                                                                         #Invalid
    s2 = MonitoringStation("s_id_2", "m_id_2", "some station", (-2.0, -4.0), (3, 0.1), "River X", "My Town")
    s2.latest_level  = 3                                                                                        #Invalid
    s3 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0.1, 3), "River X", "My Town")
    s3.latest_level = 1                                                                                         
    s4 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0.1, 3), "River X", "My Town")
    s4.latest_level = 1.7                                                                                       
    s5 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0.1, 3), "River X", "My Town")
    s5.latest_level = 2                                                                                         
    s6 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0.1, 3), "River X", "My Town")
    s6.latest_level = 2.5  
    s7 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0.1, 3), "River X", "My Town")
    s7.latest_level = 3.5                                                                                         
    s8 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0.1, 3), "River X", "My Town")
    s8.latest_level = 5                                                                                       
    s9 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0.1, 3), "River X", "My Town")
    s9.latest_level = 9                                                                                         
    s10 = MonitoringStation("s_id_3", "m_id_3", "some station", (2.0, -4.0), (0.1, 3), "River X", "My Town")
    s10.latest_level = 25 

    stations = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
    N = 5
    results = stations_highest_rel_level(stations, N)
    assert len(results) == N
    for i in range(N - 1):
        assert results[i].relative_water_level() > results[i+1].relative_water_level()