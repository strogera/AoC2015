from itertools import combinations

def combOfContainers(containers, target):
    return [x for i in range(0, len(containers)+1) for x in combinations(containers, i) if sum(x) == target ]

def partOne(target = 150):
    with open("input.txt", "r") as inputFile:
        containers = []
        for line in inputFile:
            containers.append(int(line.strip()))
        return len(combOfContainers(containers, target))


def partTwo(target = 150):
    with open("input.txt", "r") as inputFile:
        containers = []
        for line in inputFile:
            containers.append(int(line.strip()))

        cont = combOfContainers(containers, target)
        minn = len(cont[0])
        for c in cont:
            minn = min(minn, len(c))
        return minn


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
