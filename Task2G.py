from floodsystem.warn import flood_risk
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    all_stations = build_station_list()[:50] # More than 50 takes a while
    update_water_levels(all_stations)

    stations_risk = [[], [], [], []] # First list is low; last is severe

    for station in all_stations:
            risk = flood_risk(station)
            if risk:
                stations_risk[risk - 1].append(station)
    
    print("\nLOW RISK\n", set([station.town for station in stations_risk[0]]), "\n")
    print("MODERATE RISK\n", set([station.town for station in stations_risk[1]]), "\n")
    print("HIGH RISK\n", set([station.town for station in stations_risk[2]]), "\n")
    print("SEVERE RISK\n", set([station.town for station in stations_risk[3]]), "\n")


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
