def isNiceString(string):
    string = string.lower()
    countAEIOU = 0 
    lastChar = ''
    badstring = False
    repeating = False
    for c in string:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            countAEIOU += 1
        if c == lastChar:
            repeating = True
        if lastChar + c == 'ab' or lastChar + c == 'cd' or lastChar + c == 'pq' or lastChar + c == 'xy':
            badstring = True
            break
        lastChar = c
    return countAEIOU >= 3 and repeating and not badstring
        

def partOne():
    with open("input.txt", "r") as inputFile:
        count = 0
        for line in inputFile:
            if isNiceString(line.strip()):
                count += 1
        return count

def hasRepeatingPair(string):
    for i in range(len(string)-2):
        if string[i:i+2] in string[i+2:]:
            return True
    return False

def hasRepeatingLetterWithALetterInBetween(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

def isNiceString2(string):
    string = string.lower()
    return hasRepeatingPair(string) and hasRepeatingLetterWithALetterInBetween(string)

def partTwo():
    with open("input.txt", "r") as inputFile:
        count = 0
        for line in inputFile:
            if isNiceString2(line.strip()):
                count += 1
        return count

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
