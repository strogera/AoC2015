def partOne(rep=40):
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            inputString = line.strip()
            for _ in range(rep):
                output = ''
                stack = []
                for c in inputString:
                    if stack and c not in stack:
                        output += str(len(stack)) + stack[-1]
                        stack = []
                    stack.append(c)
                if stack:
                    output += str(len(stack)) + stack[-1]
                inputString = output
            return len(output)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(50))
