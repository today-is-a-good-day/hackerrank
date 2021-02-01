#!/bin/python3

import os
from bisect import bisect_left


# https://stackoverflow.com/a/12141511/7742211
def find_closest_station(stations, city):
    # Assumes stations is sorted
    position = bisect_left(stations, city)
    if position == 0:
        return stations[0]
    if position == len(stations):
        return stations[-1]
    station_before = stations[position - 1]
    station_after = stations[position]
    # If two numbers are equally close, return the smallest number.
    if station_after - city < city - station_before:
        return station_after
    else:
        return station_before


def flatland_space_stations(n, c):
    c.sort()
    distances = []
    for city in range(0, n):
        closest_station = find_closest_station(c, city)
        distance = abs(city - closest_station)
        distances.append(distance)
    return max(distances)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatland_space_stations(n, c)

    fptr.write(str(result) + '\n')
    fptr.close()
