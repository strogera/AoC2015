
def checkPassword(password):
    bannedLetters = ['i', 'o', 'l']
    pairOfLetters = set()
    incresLetters = False
    hasBannedLetter = False
    i = 0
    while i < len(password):
        if password[i] in bannedLetters:
            hasBannedLetter = True
            break
        if i+2 < len(password):
            if ord(password[i]) == ord(password[i+1]) - 1 and ord(password[i+1]) == ord(password[i+2]) - 1:
                incresLetters = True
        i += 1
    i = 0
    while i < len(password):
        if i+1 < len(password):
            if password[i] == password[i+1]:
                pairOfLetters.add(password[i])
                i += 1
        i += 1
    return (len(pairOfLetters) >= 2) and incresLetters and not hasBannedLetter

def incrementStr(string):
    if string == '':
        return ''
    if string[-1] == 'z':
            return incrementStr(string[:-1]) + 'a'
    else:
        return string[:-1] + chr(ord(string[-1]) + 1)

def generatePassword(startingString):
    while True:
        startingString= incrementStr(startingString)
        if checkPassword(startingString):
            return startingString



def partOne():
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            return  generatePassword(line.strip()) 


def partTwo(password):
    return  generatePassword(password) 


print("Answer for part 1: ")
p1ans = partOne()
print(p1ans)
print("Answer for part 2: ")
print(partTwo(p1ans))
