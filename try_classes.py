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

    def attack(self, opp):
        

aragorn = Character("Aragorn",3,2,3,2,60)
boromir = Character("Boromir",2,3,2,3,60)
gimli = Character("Gimli",2,4,1,3,60)
legolas = Character("Legolas",4,1,4,2,60)

sniper = Character("Sniper",3,2,1,2,60)
merc1 = Character("Eric",2,2,2,2,60)
merc2 = Character("Justin",2,2,2,2,60)
merc3 = Character("Sarah",2,2,2,2,60)

players = [aragorn, boromir, gimli, legolas]
enemies = [sniper, merc1, merc2, merc3]

#for i in players:
#    i.printStats()
