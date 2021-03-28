class Computer:
    def __init__(self, program):
        self.index = 0
        self.program = program
        self.registers = {}

    def step(self):
        if self.program[self.index][0] != 'jmp':
            if self.program[self.index][1] not in self.registers:
                self.registers[self.program[self.index][1]] = 0

        if self.program[self.index][0] == 'hlf':
            self.registers[self.program[self.index][1]] //= 2
            self.index += 1
        elif self.program[self.index][0] == 'tpl':
            self.registers[self.program[self.index][1]] *= 3
            self.index += 1
        elif self.program[self.index][0] == 'inc':
            self.registers[self.program[self.index][1]] += 1
            self.index += 1
        elif self.program[self.index][0] == 'jmp':
            self.index += int(self.program[self.index][1])
        elif self.program[self.index][0] == 'jie':
            if self.registers[self.program[self.index][1]] % 2 == 0:
                self.index += int(self.program[self.index][2])
            else:
                self.index += 1
        elif self.program[self.index][0] == 'jio':
            if self.registers[self.program[self.index][1]] == 1:
                self.index += int(self.program[self.index][2])
            else:
                self.index += 1
        return len(self.program) > self.index

    def executeProgram(self, part = 1):
        self.index = 0
        if part == 2:
            self.registers['a'] = 1
        while self.step():
            pass
        return self.registers

def partOne():
    with open("input.txt", "r") as inputFile:
        program = []
        for line in inputFile:
            elems=line.strip().replace(',', '').split()
            program.append((elems[0], elems[1], None if len(elems) < 3 else elems[2]))
        return Computer(program).executeProgram()['b']


def partTwo():
    with open("input.txt", "r") as inputFile:
        program = []
        for line in inputFile:
            elems=line.strip().replace(',', '').split()
            program.append((elems[0], elems[1], None if len(elems) < 3 else elems[2]))
        return Computer(program).executeProgram(part = 2)['b']

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
