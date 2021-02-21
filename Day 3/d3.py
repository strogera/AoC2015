def move(position, direction):
    if direction == '>':
        position += 1
    elif direction == '<':
        position -= 1
    elif direction == '^':
        position += 1j
    elif direction == 'v':
        position -= 1j
    return position

def partOne():
    with open("input.txt", "r") as inputFile:
        santaPos = 0 + 0j
        visit = set()
        visit.add((santaPos.real, santaPos.imag))
        for line in inputFile:
            for direction in line.strip():
                santaPos = move(santaPos, direction)
                if (santaPos.real, santaPos.imag) in visit:
                    pass
                else:
                    visit.add((santaPos.real, santaPos.imag))
        return len(visit)


def partTwo():
    with open("input.txt", "r") as inputFile:
        santaPos = 0 + 0j
        santaRobotPos = 0 + 0j
        visit = set()
        visit.add((santaPos.real, santaPos.imag))
        visit.add((santaRobotPos.real, santaRobotPos.imag))
        for line in inputFile:
            santasTurn = True
            for direction in line.strip():
                if santasTurn:
                    santaPos = move(santaPos, direction)
                    if (santaPos.real, santaPos.imag) in visit:
                        pass
                    else:
                        visit.add((santaPos.real, santaPos.imag))
                else:
                    santaRobotPos = move(santaRobotPos, direction)
                    if (santaRobotPos.real, santaRobotPos.imag) in visit:
                        pass
                    else:
                        visit.add((santaRobotPos.real, santaRobotPos.imag))
                santasTurn = not santasTurn
        return len(visit)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
