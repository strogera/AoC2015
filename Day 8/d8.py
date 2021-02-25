def partOne():
    with open("input.txt", "r") as inputFile:
        count = 0
        for line in inputFile:
            line = line.strip()
            count += len(line) - len(eval(line))
        return count

def partTwo():
    with open("input.txt", "r") as inputFile:
        count = 0
        for line in inputFile:
            line = line.strip()
            count +=  2 + line.count('\\') + line.count('\"') 
        return count


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
