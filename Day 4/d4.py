import hashlib

def partOne():
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            inc = 0
            while True:
                md5hash = hashlib.md5((line+str(inc)).encode('utf-8')).hexdigest()
                if md5hash.startswith('00000'):
                    return inc
                inc += 1


def partTwo():
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            inc = 0
            while True:
                md5hash = hashlib.md5((line+str(inc)).encode('utf-8')).hexdigest()
                if md5hash.startswith('000000'):
                    return inc
                inc += 1

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
