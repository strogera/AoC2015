def checkTicket(ticketData, auntInfo):
    count = 0
    for t in ticketData:
        if t.split(':')[0] in auntInfo:
            if t in auntInfo:
                count += 1
            else:
                return 0
    return count

def partOne():
    ticketData = []
    with open("ticket.txt", "r") as inputFile:
        for line  in inputFile:
            ticketData.append(line.strip())

    with open("input.txt", "r") as inputFile:
        aunts = []
        posibility = []
        for line in inputFile:
            r = checkTicket(ticketData, line.strip()) 
            aunts.append(line.split(':')[0].split()[1])
            posibility.append(r)

        return aunts[posibility.index(max(posibility))]


def checkTicketRanges(ticketData, auntInfo):
    count = 0
    for t in ticketData:
        if t.split(':')[0] in auntInfo:
            if 'cats' in auntInfo and 'cats' in t:
                elems = auntInfo.replace(',', ':').replace(' ', '').split(':')
                value = int(elems[elems.index('cats')+1])
                if value > int(t.split(':')[1]):
                    count += 1
                else:
                    return 0
            elif 'trees' in auntInfo and 'trees' in t:
                elems = auntInfo.replace(',', ':').replace(' ', '').split(':')
                value = int(elems[elems.index('trees')+1])
                if value > int(t.split(':')[1]):
                    count += 1
                else:
                    return 0
                
            elif 'pomeranians' in auntInfo and 'pomeranians' in t:
                elems = auntInfo.replace(',', ':').replace(' ', '').split(':')
                value = int(elems[elems.index('pomeranians')+1])
                if value < int(t.split(':')[1]):
                    count += 1
                else:
                    return 0
            elif 'goldfish' in auntInfo and 'goldfish' in t:
                elems = auntInfo.replace(',', ':').replace(' ', '').split(':')
                value = int(elems[elems.index('goldfish')+1])
                if value < int(t.split(':')[1]):
                    count += 1
                else:
                    return 0
            else:
                if t in auntInfo:
                    count += 1
                else:
                    return 0
    return count


def partTwo():
    ticketData = []
    with open("ticket.txt", "r") as inputFile:
        for line  in inputFile:
            ticketData.append(line.strip())

    with open("input.txt", "r") as inputFile:
        aunts = []
        posibility = []
        for line in inputFile:
            r = checkTicketRanges(ticketData, line.strip()) 
            aunts.append(line.split(':')[0].split()[1])
            posibility.append(r)

        return aunts[posibility.index(max(posibility))]


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
