class grid:
    def __init__(self, dimx=1000, dimy=1000):
        self.dimx = dimx
        self.dimy = dimy
        self.grid = [[0 for _ in range(dimx)] for _ in range(dimy)]

    def turnOn(self, rectSE, rectNE, rectSW, rectNW):
        for x in range(rectSE, rectSW+1):
            for y in range(rectNE, rectNW+1):
                self.grid[x][y] = 1

    def turnOff(self, rectSE, rectNE, rectSW, rectNW):
        for x in range(rectSE, rectSW+1):
            for y in range(rectNE, rectNW+1):
                self.grid[x][y] = 0

    def toggle(self, rectSE, rectNE, rectSW, rectNW):
        for x in range(rectSE, rectSW+1):
            for y in range(rectNE, rectNW+1):
                if self.grid[x][y] == 0 :
                    self.grid[x][y] = 1
                else:
                    self.grid[x][y] = 0

    def countOn(self):
        count = 0
        for x in range(self.dimx):
            for y in range(self.dimy):
                if self.grid[x][y] == 1:
                    count += 1
        return count

    def incBrightness(self, rectSE, rectNE, rectSW, rectNW, increment):
        for x in range(rectSE, rectSW+1):
            for y in range(rectNE, rectNW+1):
                self.grid[x][y] += increment
                
    def decrBrighness(self, rectSE, rectNE, rectSW, rectNW, increment):
        for x in range(rectSE, rectSW+1):
            for y in range(rectNE, rectNW+1):
                if self.grid[x][y] - increment >= 0:
                    self.grid[x][y] -= increment

    def totalBrightness(self):
        count = 0
        for x in range(self.dimx):
            for y in range(self.dimy):
                count += self.grid[x][y]
        return count

    def printGrid(self):
        print(self.grid)


def partOne():
    with open("input.txt", "r") as inputFile:
        lightGrid = grid()
        for line in inputFile:
            line = line.replace(' ', ',')
            elems=line.strip().split(',')
            if "off" in line.lower():
                lightGrid.turnOff(int(elems[2]), int(elems[3]), int(elems[-2]), int(elems[-1]))
            elif "on" in line.lower():
                lightGrid.turnOn(int(elems[2]), int(elems[3]), int(elems[-2]), int(elems[-1]))
            else:
                lightGrid.toggle(int(elems[1]), int(elems[2]), int(elems[-2]), int(elems[-1]))
        return lightGrid.countOn()

def partTwo():
    with open("input.txt", "r") as inputFile:
        lightGrid = grid()
        for line in inputFile:
            line = line.replace(' ', ',')
            elems=line.strip().split(',')
            if "off" in line.lower():
                lightGrid.decrBrighness(int(elems[2]), int(elems[3]), int(elems[-2]), int(elems[-1]), 1)
            elif "on" in line.lower():
                lightGrid.incBrightness(int(elems[2]), int(elems[3]), int(elems[-2]), int(elems[-1]), 1)
            else:
                lightGrid.incBrightness(int(elems[1]), int(elems[2]), int(elems[-2]), int(elems[-1]), 2)
        return lightGrid.totalBrightness()

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
