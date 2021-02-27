import re

def calculateDistance(data, targetSec):
    baseDistance = data[0] * data[1]
    multiplier = targetSec // (data[1] + data[2])  
    reminder = targetSec % (data[1] + data[2])  
    if reminder >= data[1]:
        return baseDistance * (multiplier + 1) 
    else:
        return baseDistance * multiplier + data[0] * reminder
        
def partOne(goalSec=2503):
    with open("input.txt", "r") as inputFile:

        dist = []
        for line in inputFile:
            elems =[int(x) for x in re.findall(r'\d+', line)]
            dist.append(calculateDistance(elems, goalSec))

        return max(dist)

def winnerPoints(data, targetSec):
    points = {}
    for i in range(len(data)):
        points[i] = 0

    for i in range(1, targetSec+1):
        distance = {}
        for j in range(len(data)):
            distance[j] = calculateDistance(data[j], i)

        reindeerDistPairsorted = [(k, v) for k, v in sorted(distance.items(), key=lambda item: item[1])]

        top = reindeerDistPairsorted[-1]
        k = -1
        while k >= (-1) * len(reindeerDistPairsorted) and top[1] == (reindeerDistPairsorted[k])[1] :
            points[reindeerDistPairsorted[k][0]] += 1
            k -= 1

    return [v for _, v in sorted(points.items(), key=lambda item: item[1])][-1]


def partTwo(goalSec=2503):
    with open("input.txt", "r") as inputFile:

        data = []
        for line in inputFile:
            elems =[int(x) for x in re.findall(r'\d+', line)]
            data.append(elems)
        return winnerPoints(data, goalSec)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
