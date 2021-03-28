from copy import deepcopy

printMessages = False

class Npc:
    def __init__(self, hp, dmg, armor):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor

    def decrHp(self, decr):
        self.hp -= decr

    def incrHp(self, amount):
        self.hp += amount

    def isDead(self):
        return self.hp <= 0

    def getDmg(self):
        return self.dmg

    def getArmor(self):
        return self.armor

    def getHp(self):
        return self.hp

    def incrArmor(self, amount):
        self.armor += amount

    def decrArmor(self, amount):
        self.armor -= amount

class Wizard(Npc):
    def __init__(self, hp, mana):
        Npc.__init__(self, hp, 0, 0)
        self.mana = mana

    def getMana(self):
        return self.mana

    def spentMana(self, amount):
        self.mana -= amount

    def addMana(self, amount):
        self.mana += amount

            
class Spell:
    def __init__(self, name, manaCost, dmg, armorGain, duration, manaGain):
        self.name = name
        self.manaCost = manaCost
        self.dmg = dmg
        self.armorGain = armorGain
        self.duration = duration
        self.manaGain = manaGain
        self.remainingDuration = 0

    def __eq__(self, other):
        return isinstance(other, Spell) and self.name == other.getName()

    def cast(self, player:Wizard, boss:Npc):
        global printMessages
        player.spentMana(self.manaCost)
        if self.name == 'MM':
            if printMessages:
                print('Casts Magic Missile, dealing', self.dmg, 'damage')
            boss.decrHp(self.dmg)
        elif self.name == 'Dr':
            if printMessages:
                print('Casts Drain, drains', self.dmg,'from boss')
            boss.decrHp(self.dmg)
            player.incrHp(self.dmg)
        elif self.name == 'Sh':
            if printMessages:
                print('Shieled casted, armor increased by', self.armorGain)
            player.incrArmor(self.armorGain)
            self.remainingDuration = self.duration
        elif self.name == 'Po':
            if printMessages:
                print('Casts Poison')
            self.remainingDuration = self.duration 
        elif self.name == 'Re':
            if printMessages:
                print('Casts Recharge')
            self.remainingDuration = self.duration
        return self.manaCost

    def triggerEffect(self, player:Wizard, boss:Npc):
        global printMessages
        if self.remainingDuration <= 0:
            return
        self.remainingDuration -= 1 
        if self.name == 'Sh':
            if printMessages:
                print('Shield timer now is', self.remainingDuration)
            if self.remainingDuration == 0:
                player.decrArmor(self.armorGain)
                if printMessages:
                    print('Shield wore off')
        elif self.name == 'Po':
            if printMessages:
                print('Poison deals', self.dmg, 'damage; timer now is', self.remainingDuration)
            boss.decrHp(self.dmg)
        elif self.name == 'Re':
            if printMessages:
                print('Gained', self.manaGain, 'mana; timer now is', self.remainingDuration)
            player.addMana(self.manaGain)

    def isActive(self):
        return self.remainingDuration > 0

    def getManaCost(self):
        return self.manaCost

    def getName(self):
        return self.name

class FightState:
    def __init__(self, player:Wizard, boss:Npc, activeSpells):
        self.player = player
        self.boss = boss
        self.activeSpells = activeSpells

    def getPlayer(self):
        return self.player

    def getBoss(self):
        return self.boss

    def getActiveSpells(self):
        return self.activeSpells

    def isActive(self, spell:Spell):
        for s in self.activeSpells:
            if s == spell:
                return True
        return False

    def clearInactiveSpells(self):
        clearedList = []
        for spell in self.activeSpells:
            if spell.isActive():
                clearedList.append(spell)
        self.activeSpells = clearedList
            


class Game:
    def __init__(self, bossHp, bossDmg, bossArmor):
        self.bossHp = bossHp
        self.bossDmg = bossDmg
        self.bossArmor = bossArmor
        self.manaSpentToWin = 1000000
        self.allSpells = [Spell('MM', 53, 4, 0, 0, 0), Spell('Dr', 73, 2, 0, 0, 0), Spell('Sh', 113, 0, 7, 6, 0), Spell('Po', 173, 3, 0, 6, 0), Spell('Re', 229, 0, 0, 5, 101)]

    def getBestManaWin(self, part=1):
        self.playAll(part)
        return (self.manaSpentToWin)
    
    def playAll(self, part=1):
        player = Wizard(50, 500)
        #player = Wizard(10, 250)
        boss = Npc(self.bossHp, self.bossDmg, self.bossArmor)
        self.playNewGame(FightState(player, boss, []), 0, 'player', part)


    def playNewGame(self, state, manaSpent, turn, part = 1):
        if manaSpent >= self.manaSpentToWin:
            return

        activeSpells = state.getActiveSpells()
        player = state.getPlayer()
        boss = state.getBoss()
        
        global printMessages

        if printMessages:
            print()
            print('--', turn, 'Turn--')
            print('-Player has', player.getHp(), 'hp', player.getArmor(), 'armor', player.getMana(), 'mana')
            print('-Boss has', boss.getHp(), 'hp')

        if part == 2 and turn == 'player':
            if printMessages:
                print('Hard mode: hp decreased by 1')
            player.decrHp(1)
            if player.isDead():
                if printMessages:
                    print('PLAYER LOSES')
                return 

        for activeSpell in activeSpells:
            activeSpell.triggerEffect(player, boss)
            if boss.isDead():
                if printMessages:
                    print('####################PLAYER WINS 1', manaSpent)
                self.manaSpentToWin=min(manaSpent, self.manaSpentToWin)
                return
        state.clearInactiveSpells()


        if turn == 'player':
            for spell in self.allSpells:
                if state.isActive(spell) or player.getMana() < spell.getManaCost():
                    continue

                newPlayer = deepcopy(player)
                newBoss = deepcopy(boss) 
                newSpell = deepcopy(spell)

                manaSpentForTurn = newSpell.cast(newPlayer, newBoss)

                newActiveSpells = deepcopy(activeSpells) + [newSpell]

                if newBoss.isDead():
                    if printMessages:
                        print('####################PLAYER WINS 2', manaSpent+manaSpentForTurn)
                    self.manaSpentToWin=min(manaSpent+manaSpentForTurn, self.manaSpentToWin)
                else:
                    self.playNewGame(FightState(newPlayer, newBoss, newActiveSpells), manaSpent+manaSpentForTurn, 'boss', part)
        else:
            dmgToPlayer = boss.getDmg() - player.getArmor()
            if printMessages:
                print('Boss attacks for', dmgToPlayer, 'damage')
            player.decrHp(dmgToPlayer if dmgToPlayer >= 1 else 1)
            if player.isDead():
                if printMessages:
                        print('PLAYER LOSES')
            else:
                self.playNewGame(FightState(player, boss, activeSpells), manaSpent, 'player', part)

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
printMessages = False
print("Answer for part 2: ")
print(partTwo())
