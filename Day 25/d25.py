import re

def partOne():
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            coords = [int(x) for x in re.findall(r'\d+', line)]
            x , y = 1, 1
            num = 20151125
            while True:
                if (x, y) == (coords[0], coords[1]):
                    return num
                num = (num*252533)%33554393
                if x ==  1:
                    x = y + 1
                    y = 1
                else:
                    x -= 1
                    y += 1


def partTwo():
    return 'Submit the answer for every question in the year'

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
