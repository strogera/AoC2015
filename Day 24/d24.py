from math import prod

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, nums, summ):
        args = tuple(nums + [summ])
        if args not in self.memo:
            self.memo[args] = self.fn(nums, summ)
        return self.memo[args]

@Memoize
def findAllSetsOfSum(nums:list, summ:int):
    if not nums:
        return []
    setsOfSum = []
    for i in range(len(nums)):
        s = nums[i]
        if s == summ:
            setsOfSum.append([s]) 
            continue
        for z in findAllSetsOfSum(nums[i+1:], summ-s):
                setsOfSum.append([s] + z)
    return setsOfSum


def findMinLengthPackage(packages):
    optionsSorted = sorted(packages, key = lambda x: len(x))
    qe = []
    i = 0
    while len(optionsSorted[i]) == len(optionsSorted[0]):
        qe.append(prod(optionsSorted[i]))
        i += 1
    return min(qe)


def partOne():
    with open("input.txt", "r") as inputFile:
        weights = []
        for line in inputFile:
            weights.append(int(line.strip()))
        return findMinLengthPackage(findAllSetsOfSum(weights, sum(weights)//3))


def partTwo():
    with open("input.txt", "r") as inputFile:
        weights = []
        for line in inputFile:
            weights.append(int(line.strip()))
        return findMinLengthPackage(findAllSetsOfSum(weights, sum(weights)//4))

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
