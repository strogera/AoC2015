from collections import defaultdict


def partOne(upperBound = 1000000):
    with open("input.txt", "r") as inputFile:
        houses = defaultdict(int)
        for line in inputFile:
            target = int(line.strip())
            for i in range(1, target+1):
                for j in range(i, upperBound, i):
                    houses[j] += i*10
                if houses[i] >= target:
                    return i


def partTwo():
    with open("input.txt", "r") as inputFile:
        houses = defaultdict(int)
        for line in inputFile:
            target = int(line.strip())
            for i in range(1, target+1):
                for j in range(i, i*50+1, i):
                    houses[j] += i*11
                if houses[i] >= target:
                    return i


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
