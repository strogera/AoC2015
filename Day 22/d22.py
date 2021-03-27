from itertools import combinations
from copy import deepcopy

printMessages = False

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

class Wizard(Npc):
    def __init__(self, hp, mana):
        Npc.__init__(self, hp, 0, 0)
        self.mana = mana
        self.allSpells = [['MM', 53, 4, 0, 1, 0], ['Dr', 73, 2, 0, 1, 0], ['Sh', 113, 0, 7, 6, 0], ['Po', 173, 3, 0, 6, 0], ['Re', 229, 0, 0, 5, 101]]
        self.activeSpells = []
        self.activeSpellsDurationRemaining = []

    def incrHp(self, amount):
        self.hp += amount

    def getMana(self):
        return self.mana

    def spentMana(self, amountSpent):
        self.mana -= amountSpent

    def addMana(self, amount):
        self.mana += amount

    def useSpell(self, spell):
        self.activeSpells.append(spell)
        self.activeSpellsDurationRemaining.append(spell[4])
        self.mana -= spell[1]
        return spell[1]

    def getAvailableSpells(self):
        return [x for x in self.allSpells if x not in self.activeSpells]

    def endTurn(self, effectCastedThisTurn = []):
        global printMessages
        dmgToBoss = 0
        ended = []
        endedDur = []
        for i in range(len(self.activeSpellsDurationRemaining)):
            if (self.activeSpells[i][0] == 'Po' or self.activeSpells[i][0] == 'Sh' or self.activeSpells[i][0] == 'Re') and effectCastedThisTurn == self.activeSpells[i]:
                if self.activeSpells[i][0] == 'Sh':
                    #Armor
                    self.armor += self.activeSpells[i][3]
                    if printMessages:
                        if self.activeSpells[i][0] == 'Sh':
                            print('Armor increased by', self.activeSpells[i][3], ', timer now is ', self.activeSpellsDurationRemaining[i]-1)

            else:
                #Damage
                if self.activeSpells[i][2] != 0:
                    if printMessages:
                        print(self.activeSpells[i][0], 'deals', self.activeSpells[i][2], 'damage, timer now is:', self.activeSpellsDurationRemaining[i]-1)
                dmgToBoss += self.activeSpells[i][2]
                if self.activeSpells[i][0] == 'Dr':
                    if printMessages:
                        print('Drain heals', self.activeSpells[i][2], 'hp')
                    self.incrHp(self.activeSpells[i][2])

                #Mana
                self.addMana(self.activeSpells[i][-1])
                if printMessages:
                    if self.activeSpells[i][0] == 'Re':
                        print('Recharge provides', self.activeSpells[i][-1], 'mana, timer now is ', self.activeSpellsDurationRemaining[i]-1)
                #Duration
                self.activeSpellsDurationRemaining[i] -= 1
                if self.activeSpellsDurationRemaining[i] == 0:
                    if self.activeSpells[i][0] == 'Sh':
                        if printMessages:
                            print('Shield wore off')
                        self.armor -= self.activeSpells[i][3]
                    ended.append(self.activeSpells[i])
                    endedDur.append(i)
        self.activeSpells = [x for x in self.activeSpells if x not in ended]
        self.activeSpellsDurationRemaining = [self.activeSpellsDurationRemaining[i] for i in range(len(self.activeSpellsDurationRemaining)) if i not in endedDur]
        return dmgToBoss
            

class Game:
    def __init__(self, bossHp, bossDmg, bossArmor):
        self.bossHp = bossHp
        self.bossDmg = bossDmg
        self.bossArmor = bossArmor
        self.manaSpentToWin = 1000000

    def getBestManaWin(self, part=1):
        self.playAll(part)
        return (self.manaSpentToWin)
    
    def playAll(self, part=1):
        player = Wizard(50, 500)
        #player = Wizard(10, 250)
        boss = Npc(self.bossHp, self.bossDmg, self.bossArmor)
        self.playNewGame(player, boss, 0, part)


    def playNewGame(self, player:Wizard, boss:Npc, manaSpent, part = 1):
        global printMessages
        if manaSpent >= self.manaSpentToWin:
            if printMessages:
                print('###Too costy')
            return
        #Player's Turn
        for spell in player.getAvailableSpells():
            if player.getMana() < spell[1]:
                continue
            newPlayer = deepcopy(player)
            newBoss = deepcopy(boss) 
            if printMessages:
                print()
                print('--Player Turn--')
            if part == 2:
                if printMessages:
                    print('Hard mode: hp decreased by 1')
                newPlayer.decrHp(1)
                if newPlayer.isDead():
                    if printMessages:
                            print('PLAYER LOSES')
                    return 
            if printMessages:
                print('-Player has', newPlayer.getHp(), 'hp', newPlayer.getArmor(), 'armor', newPlayer.getMana(), 'mana')
                print('-Boss has', newBoss.getHp(), 'hp')
            manaSpentForTurn = newPlayer.useSpell(spell)
            if printMessages:
                print('Player casts', spell[0])

            dmgToBoss = newPlayer.endTurn(spell) 
            newBoss.decrHp(dmgToBoss)
            if newBoss.isDead():
                if printMessages:
                    print('####################PLAYER WINS 1', manaSpent+manaSpentForTurn)
                self.manaSpentToWin=min(manaSpent+manaSpentForTurn, self.manaSpentToWin)
            else:
                #Boss' turn
                if printMessages:
                    print('--Boss Turn--')
                    print('-Player has', newPlayer.getHp(), 'hp', newPlayer.getArmor(), 'armor', newPlayer.getMana(), 'mana')
                    print('-Boss has', newBoss.getHp(), 'hp')
                dmgToBoss = newPlayer.endTurn() 
                newBoss.decrHp(dmgToBoss)
                if newBoss.isDead():
                    if printMessages:
                        print('####################PLAYER WINS 2', manaSpent+manaSpentForTurn)
                    self.manaSpentToWin=min(manaSpent+manaSpentForTurn, self.manaSpentToWin)
                    continue
                dmgToPlayer = newBoss.getDmg() - newPlayer.getArmor()
                if printMessages:
                    print('Boss attacks for', dmgToPlayer, 'damage')
                newPlayer.decrHp(dmgToPlayer if dmgToPlayer>=1 else 1)
                if newPlayer.isDead():
                    if printMessages:
                            print('PLAYER LOSES')
                    continue
                self.playNewGame(newPlayer, newBoss, manaSpent+manaSpentForTurn, part)

def partOne():
    global printMessages
    #printMessages = True
    with open("input.txt", "r") as inputFile:
        stats = []
        for line in inputFile:
            elems=line.strip().split(':')
            stats.append(int(elems[1]))
        game = Game(stats[0], stats[1], 0)
        return game.getBestManaWin(part = 1)

def partTwo():
    global printMessages
    #printMessages = True
    with open("input.txt", "r") as inputFile:
        stats = []
        for line in inputFile:
            elems=line.strip().split(':')
            stats.append(int(elems[1]))
        game = Game(stats[0], stats[1], 0)
        return game.getBestManaWin(part = 2)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
