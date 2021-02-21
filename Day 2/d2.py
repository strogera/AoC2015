from itertools import combinations
from math import prod

def expandSides(dimension):
    return list(combinations(dimension, 2))

def calculateArea(sides):
    areas = []
    for s in sides:
        areas.append(prod(s))
    return areas

def calculateWrapPapper(areas):
    return 2*sum(areas) + min(areas)

def partOne():
    with open("input.txt", "r") as inputFile:
        totalWrap = 0
        for line in inputFile:
            dim = line.strip().split('x')
            dim = [int(x) for x in dim]
            sides = expandSides(dim) 
            areas = calculateArea(sides)
            totalWrap += calculateWrapPapper(areas) 
        return totalWrap

def calculateRibbonPresent(sides):
    halfperimeter = [sum(sidePair) for sidePair in sides]
    return min(halfperimeter) * 2

def partTwo():
    with open("input.txt", "r") as inputFile:
        totalRibbon = 0
        for line in inputFile:
            dim = line.strip().split('x')
            dim = [int(x) for x in dim]
            sides = expandSides(dim) 
            totalRibbon += calculateRibbonPresent(sides) + prod(dim)
        return totalRibbon

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())