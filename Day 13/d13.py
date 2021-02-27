from collections import defaultdict
from itertools import permutations


def calcHappiness(preferences, seatings):
    summ = 0
    for i in range(len(seatings)):
        summ += preferences[seatings[i]][seatings[(0 if i == len(seatings) - 1 else i + 1)]]
        summ += preferences[seatings[i]][seatings[(-1 if i == 0 else i - 1)]]

    return summ


def partOne():
    with open("input.txt", "r") as inputFile:

        preferences = defaultdict(dict)
        for line in inputFile:
            elems = line.replace('.', '').strip().split()
            preferences[elems[0]][elems[-1]] = int(('-' if elems[2] == 'lose' else '') + elems[3])

        happiness = [calcHappiness(preferences, h) for h in permutations(preferences.keys())]

        return max(happiness)


def partTwo():
    with open("input.txt", "r") as inputFile:

        preferences = defaultdict(dict)
        for line in inputFile:
            elems = line.replace('.', '').strip().split()
            preferences[elems[0]][elems[-1]] = int(('-' if elems[2] == 'lose' else '') + elems[3])

        templist = list(preferences.keys()).copy()
        for person in templist:
            preferences[person]['me'] = 0
            preferences['me'][person] = 0

        happiness = [calcHappiness(preferences, h)
                     for h in permutations(preferences.keys())]

        return max(happiness)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
