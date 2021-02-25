from itertools import permutations
from collections import defaultdict


def totalDistance(cities, curCities):
    return sum(cities[src][dest] for src, dest in zip(curCities, curCities[1:]))


def partOne():
    with open("input.txt", "r") as inputFile:
        cities = defaultdict(dict)
        for line in inputFile:
            line = line.strip().replace('to', '').replace('=', '')
            src, dest, distance = line.split()
            cities[src][dest] = int(distance)
            cities[dest][src] = int(distance)
        distances = [totalDistance(cities, curCities)
                     for curCities in permutations(cities.keys())]
        return min(distances)


def partTwo():
    with open("input.txt", "r") as inputFile:
        cities = defaultdict(dict)
        for line in inputFile:
            line = line.strip().replace('to', '').replace('=', '')
            src, dest, distance = line.split()
            cities[src][dest] = int(distance)
            cities[dest][src] = int(distance)
        distances = [totalDistance(cities, curCities)
                     for curCities in permutations(cities.keys())]
        return max(distances)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
