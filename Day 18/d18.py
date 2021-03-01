class lightGrid:
    def __init__(self, initial):
        self.grid = initial

    def printCurrentState(self):
        for x in self.grid:
            print(x)

    def simulate(self, gens = 1, cornersOn = False):
        if cornersOn :
            self.grid[0][0] = '#'
            self.grid[0][-1] = '#'
            self.grid[-1][0] = '#'
            self.grid[-1][-1] = '#'

        for _ in range(gens):
            tempGrid = []
            for row in self.grid:
                tempGrid.append(row.copy())
            for x in range(len(self.grid)):
                for y in range(len(self.grid[x])):
                    if cornersOn:
                        if (x == 0 and y == 0 ) or \
                        (x == 0 and y == len(self.grid[x])-1) or \
                         (y == 0 and x == len(self.grid)-1) or \
                          (y == len(self.grid[x])-1 and x == len(self.grid)-1):
                                continue
                    onAdjLights = self.countAdjOn(x, y)
                    if self.grid[x][y] == '#':
                        if onAdjLights != 2 and onAdjLights != 3:
                            tempGrid[x][y] = '.'
                    else:
                        if onAdjLights == 3:
                            tempGrid[x][y] = '#'
            self.grid = tempGrid


    def countAdjOn(self, x, y):
        count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if j>=0 and i >=0 and i<len(self.grid) and j<len(self.grid[i]):
                    if i == x and j == y:
                        continue
                    if self.grid[i][j] == '#':
                        count += 1
        return count

    def countOn(self):
        count = 0
        for row in self.grid:
            for light in row:
                if light == '#':
                    count +=1
        return count


def partOne(steps = 100):
    with open("input.txt", "r") as inputFile:
        initialLights = []
        for line in inputFile:
            initialLights.append([x for x in line.strip()])
        lights = lightGrid(initialLights)
        lights.simulate(steps)
        return lights.countOn()


def partTwo(steps = 100):
    with open("input.txt", "r") as inputFile:
        initialLights = []
        for line in inputFile:
            initialLights.append([x for x in line.strip()])
        lights = lightGrid(initialLights)
        lights.simulate(steps, True)
        return lights.countOn()


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
