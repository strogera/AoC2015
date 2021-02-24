varDic = {}

def getValue(var):
    global varDic
    try:
        elems = varDic[var]
    except:
        return int(var)
    if isinstance(elems, int):
        return elems
    if len(elems) == 1:
        try:
            varDic[var] = int(elems[0])
        except ValueError:
            varDic[var] = getValue(elems[0])

    elif len(elems) == 2:
        varDic[var] = ~getValue(elems[1]) & 0xffff
    elif len(elems) == 3:
        if elems[1] == 'AND':
            varDic[var] = getValue(elems[0]) & getValue(elems[2])
        elif elems[1] == 'OR':
            varDic[var] = getValue(elems[0]) | getValue(elems[2])
        elif elems[1] == 'LSHIFT':
            varDic[var] = getValue(elems[0]) << int(elems[2])
        elif elems[1] == 'RSHIFT':
            varDic[var] = getValue(elems[0]) >> int(elems[2])
    return int(varDic[var])


def partOne(searchVar='a'):
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            line = line.replace('->', '')
            elems = line.strip().split()
            varDic[elems[-1]] = elems[:-1]
        return getValue(searchVar)


def partTwo(part1Answer, searchVar = 'a'):
    with open("input.txt", "r") as inputFile:
        global varDic
        varDic = {}
        for line in inputFile:
            line = line.replace('->', '')
            elems = line.strip().split()
            varDic[elems[-1]] = elems[:-1]
        varDic['b'] = part1Answer
        return getValue(searchVar)



print("Answer for part 1: ")
p1ans = partOne()
print(p1ans)
print("Answer for part 2: ")
print(partTwo(p1ans))
