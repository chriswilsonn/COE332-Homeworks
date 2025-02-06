import math

def great_circle_distance(lat1: float, long1: float, lat2: float, long2: float) -> float:
    longitude1 = math.radians(long1)
    latitude1 = math.radians(lat1)
    longitude2 = math.radians(long2)
    latitude2 = math.radians(lat2)

    delta_lambda = longitude2 - longitude1

    inside = (math.sin(latitude1) * math.sin(latitude2)) + (math.cos(latitude1) * math.cos(latitude2) * math.cos(delta_lambda))
    distance = 6378 * (math.acos(inside)) # in km

    return distance

