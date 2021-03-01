from collections import defaultdict


def replaceMolecules(replacement, medicine):
    altMedicines = set()
    for r in replacement.keys():
        for m in range(len(medicine)):
            if medicine[m:m+len(r)] == r:
                for alt in replacement[r]:
                    altMedicines.add(medicine[:m]+alt+medicine[m+len(r):])
    return altMedicines


def partOne():
    with open("input.txt", "r") as inputFile:
        replacements = defaultdict(list)
        medicine = ''
        for line in inputFile:
            if '=>' in line:
                lineData = line.replace(' ', '').strip().split('=>')
                replacements[lineData[0]].append(lineData[1])
            elif line:
                medicine = line.strip()

        return len(replaceMolecules(replacements, medicine))


def greedyReplace(replacements, medicine):
    count = 0
    while medicine != 'e':
        for k in replacements.keys():
            if k in medicine:
                medicine = medicine.replace(k, replacements[k], 1)
                count += 1
    return count

def partTwo():
    with open("input.txt", "r") as inputFile:
        replacements = defaultdict(list)
        medicine = ''
        for line in inputFile:
            if '=>' in line:
                lineData = line.replace(' ', '').strip().split('=>')
                replacements[lineData[0]].append(lineData[1])
            elif line:
                medicine = line.strip()

        reverseReplacements = {} 
        for k in replacements.keys():
            for item in replacements[k]:
                reverseReplacements[item] = k

        return greedyReplace(reverseReplacements, medicine)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
