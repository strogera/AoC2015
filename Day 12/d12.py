import re
import json


def sumObject(obj):
    if type(obj) is int:
        return obj
    if type(obj) is list:
        return sum(map(sumObject, obj))
    if type(obj) is dict:
        vals = obj.values()
        if "red" in vals:
            return 0
        return sum(map(sumObject, vals))
    else:
        return 0


def partOne():
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            return sum([int(x) for x in re.findall(r'[-+]?\d+', line.strip())])


def partTwo():
    with open("input.txt", "r") as inputFile:
        obj = json.loads(inputFile.read())
        return sumObject(obj)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
