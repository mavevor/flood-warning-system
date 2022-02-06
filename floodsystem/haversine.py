import math
def hav(x):
    y = x*math.pi/180
    return math.sin(y/2)**2
def archav(x):
    return 2*math.asin(x**(1/2))
def distance(lat1,long1, lat2, long2):
    h = hav(lat2-lat1) + (1-hav(lat1-lat2)-hav(lat1+lat2))*hav(long2-long1)     #hav(distance/r)
    r = 6371                                                                    #Radius of Earrth
    return r*archav(h)

