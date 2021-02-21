def estimateDirection(paren):
    if paren == '(':
        return 1
    elif paren == ')':
        return -1
    else:
        return 0

def estimateFloor(instructions):
    floor = 0
    for paren in instructions:
        floor += estimateDirection(paren)
    return floor


def partOne():
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            return estimateFloor(line.strip())


def partTwo():
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            count = 0
            pos = 1
            for paren in line:
                count += estimateDirection(paren)
                if count == -1:
                    return pos
                pos += 1
    return -1

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
