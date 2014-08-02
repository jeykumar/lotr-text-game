import random

class Character(object):
    hpMax = 60

    def __init__(self,name,acc,res,speed,strength,hp):
        self.name = name
        self.acc = acc
        self.res = res
        self.speed = speed
        self.strength = strength
        self.hp = Character.hpMax

    def printStats(self):
        print self.name
        print "HP " + str(self.hp)
        print "Accuracy " + str(self.acc)
        print "Resistance " + str(self.res)
        print "Speed " + str(self.speed)
        print "Strength " + str(self.strength)
        print ""

    def defend(self, opp):
        chance = self.acc - opp.speed
        if random.randint(1,10) <= (5 + chance):
            damage = 15 + 2*(self.strength - opp.res) + random.randint(-5,5)
            opp.hp -= damage
            if opp.hp <= 0:
                opp.die()
                return "Counterattack: %s killed %s." % (self.name, opp.name)
            else:
                return "Counterattack: %s dealt %s with %d damage. %s now has %d HP." % (self.name, opp.name, damage, opp.name, opp.hp)
        else:
            return "Counterattack: %s missed." % (self.name)

    def attack(self, opp):
        chance = self.acc - opp.speed
        if random.randint(1,10) <= (5 + chance):
            damage = 15 + 2*(self.strength - opp.res) + random.randint(-5,5)
            opp.hp -= damage
            if opp.hp <= 0:
                opp.die()
                print "Attack: %s killed %s." % (self.name, opp.name)
                return
            else:
                print "Attack: %s dealt %s with %d damage. %s now has %d HP." % (self.name, opp.name, damage, opp.name, opp.hp) + "\n" + opp.defend(self)
                return
        else:
            print "Attack: %s missed." % (self.name) + "\n" + opp.defend(self)
            return

    def die(self):
        if self.name in players:
            del players[self.name]
        elif self.name in enemies:
            del enemies[self.name]     
        
#Create objects and organize into dictionaries
aragorn = Character("Aragorn",3,2,3,2,60)
boromir = Character("Boromir",2,3,2,3,60)
gimli = Character("Gimli",2,4,1,3,60)
legolas = Character("Legolas",4,1,4,2,60)

sniper = Character("Sniper",3,2,1,2,60)
merc1 = Character("Eric",2,2,2,4,60)
merc2 = Character("Justin",3,2,2,3,60)
merc3 = Character("Sarah",3,2,3,2,60)

players = {"Aragorn" : aragorn, "Boromir" : boromir, "Gimli" : gimli, "Legolas" : legolas}
enemies = {"Sniper" : sniper, "Eric" : merc1, "Justin" : merc2, "Sarah" : merc3}

def choose(dic):
    n = 1
    keys = dict()
    for i in sorted(dic.keys()):
        if i != "Sniper":
            keys[n] = i
            print "%d. %s" % (n, i)
            n += 1
    print ""
    choice = int(raw_input("Enter # of choice: "))
    return keys[choice]

def playGame():
    choiceP = choose(players)
    choiceE = choose(enemies)

    players[choiceP].attack(enemies[choiceE])
