from itertools import combinations


class Npc:
    def __init__(self, hp, dmg, armor):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor

    def decrHp(self, decr):
        self.hp -= decr

    def isDead(self):
        return self.hp <= 0

    def getDmg(self):
        return self.dmg

    def getArmor(self):
        return self.armor

    def getHp(self):
        return self.hp


class Item:
    def __init__(self, name, cost, dmg, armor):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.armor = armor

    def getCost(self):
        return self.cost

    def getDmg(self):
        return self.dmg

    def getArmor(self):
        return self.armor

class Shop:
    def __init__(self):
        self.weapons = [Item('d', 8, 4, 0), Item('sh', 10, 5, 0), Item('w', 25, 6, 0), Item('lo', 40, 7, 0), Item('g', 74, 8, 0)]
        self.armor = [Item('le', 13, 0, 1), Item('c', 31, 0, 2), Item('sp', 53, 0, 3), Item('b', 75, 0, 4), Item('p', 102, 0, 5)]
        self.rings = [Item('da1', 25, 1, 0), Item('da2', 50, 2, 0), Item('da3', 100, 3, 0), Item('de1', 20, 0, 1), Item('de2', 40, 0, 2), Item('de3', 80, 0, 3)]

    def getWeaponItems(self):
        return self.weapons

    def getArmorItems(self):
        return self.armor
    
    def getRingItems(self):
        return self.rings

class Game:
    def __init__(self, bossHp, bossDmg, bossArmor):
        self.bossHp = bossHp
        self.bossDmg = bossDmg
        self.bossArmor = bossArmor
        self.shop = Shop()

    def playAllItemCombinations(self):
        bestWinningCost = 1000000
        worstLosingCost = 0
        for weaponItem in self.shop.getWeaponItems():
            for armorItem in self.shop.getArmorItems() + [None]:
                for ringItems in [self.shop.getRingItems()] + [[None]] + [x for x in combinations(self.shop.getRingItems() + [None], 2)]:
                    cost = 0
                    dmg = 0
                    armor = 0
                    dmg += weaponItem.getDmg()
                    cost += weaponItem.getCost()
                    if armorItem:
                        armor += armorItem.getArmor()
                        cost += armorItem.getCost()

                    for r in ringItems:
                        if r !=None:
                            dmg += r.getDmg()
                            armor += r.getArmor() 
                            cost += r.getCost()

                    if self.playNewGame(Npc(100, dmg, armor)):
                        bestWinningCost = min(cost, bestWinningCost)
                    else:
                        worstLosingCost = max(cost, worstLosingCost)

        self.bestWinningCost = bestWinningCost
        self.worstLosingCost = worstLosingCost

    def getBestCost(self):
        try:
            return self.bestWinningCost
        except:
            self.playAllItemCombinations()
        return self.bestWinningCost
    
    def getWorstLosingCost(self):
        try:
            return self.worstLosingCost
        except:
            self.playAllItemCombinations()
        return self.worstLosingCost

    def playNewGame(self, player:Npc):
        self.boss = Npc(self.bossHp, self.bossDmg, self.bossArmor)
        while True:
            result = self.playTurn(player)
            if result == 1:
                return True
            elif result == -1:
                return False

    def playTurn(self, player:Npc):
        self.boss.decrHp(player.getDmg() - self.boss.getArmor())
        if self.boss.isDead():
            return 1
        player.decrHp(self.boss.getDmg() - player.getArmor())
        if player.isDead():
            return -1
        return 0


def partOne():
    with open("input.txt", "r") as inputFile:
        stats = []
        for line in inputFile:
            elems=line.strip().split(':')
            stats.append(int(elems[1]))
        game = Game(stats[0], stats[1], stats[2])
        return game.getBestCost()



def partTwo():
    with open("input.txt", "r") as inputFile:
        stats = []
        for line in inputFile:
            elems=line.strip().split(':')
            stats.append(int(elems[1]))
        game = Game(stats[0], stats[1], stats[2])
        return game.getWorstLosingCost()

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())