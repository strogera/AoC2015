import re 
import numpy as np
from math import prod
from itertools import product

class Ingredient:
    def __init__(self, name, propertyList):
        self.name = name
        self.properties = propertyList

    def getProperties(self):
        return self.properties[:-1]

    def getCalories(self):
        return self.properties[-1]

def getPairs(numOfIngred, numOfSpoons):
    return [list(x) for x in product([y for y in range( numOfSpoons + 1)], repeat = numOfIngred) if sum(x) == numOfSpoons ]

def calcTotalScore(ingredients, spoons = 100):
    pairs = getPairs(len(ingredients), spoons)

    values = []
    for ingr in ingredients:
        values.append(ingr.getProperties())
    values = [list(x) for x in list(np.array(values).T)]

    scores = []
    for i in range(len(pairs)):
        toMult = []
        for v in values:
            summ = sum([a*b for a, b in zip(v, pairs[i])])
            if summ <= 0:
                break
            toMult.append(summ)
        if toMult:
            scores.append(prod(toMult)) 
    return max(scores)


def partOne():
    with open("input.txt", "r") as inputFile:
        ingredients = []
        for line in inputFile:
            curProperties= [int(x) for x in re.findall(r'-?\d+', line.strip())]
            ingredients.append(Ingredient(line.split(':')[0], curProperties))
        return calcTotalScore(ingredients)


def calcTotalScoreWithCalories(ingredients, spoons = 100, caloryTarget = 500):
    pairs = getPairs(len(ingredients), spoons)
    values = []
    for ingr in ingredients:
        values.append(ingr.getProperties())
    values = [list(x) for x in list(np.array(values).T)]
    scores = []
    for i in range(len(pairs)):
        #calories
        cal = 0
        for j in range(len(ingredients)):
            cal += ingredients[j].getCalories()*pairs[i][j]
        if cal != 500:
            continue

        toMult = []
        for v in values:
            summ = sum([a*b for a, b in zip(v, pairs[i])])
            if summ <= 0:
                break
            toMult.append(summ)
        if toMult:
            scores.append(prod(toMult)) 
    return max(scores)


def partTwo():
    with open("input.txt", "r") as inputFile:
        ingredients = []
        for line in inputFile:
            curProperties= [int(x) for x in re.findall(r'-?\d+', line.strip())]
            ingredients.append(Ingredient(line.split(':')[0], curProperties))
        return calcTotalScoreWithCalories(ingredients)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
