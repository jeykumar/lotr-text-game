import random
import pygame, sys, time
from pygame.locals import *

#Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)

maxt = 1.5
    
class Character(object):

    def __init__(self,name,acc,res,speed,strength,hp):
        self.name = name
        self.acc = acc
        self.res = res
        self.speed = speed
        self.strength = strength
        self.hp = hp

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
                print "Counterattack: %s killed %s." % (self.name, opp.name) + "\n"
                return "-------" + "\n"
            else:
                print "Counterattack: %s dealt %s with %d damage. %s now has %d HP." % (self.name, opp.name, damage, opp.name, opp.hp) + "\n"
                return "-------" + "\n"
        else:
            print "Counterattack: %s missed." % (self.name) + "\n"
            return "-------" + "\n"

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
                print "Attack: %s dealt %s %d damage. %s now has %d HP." % (self.name, opp.name, damage, opp.name, opp.hp)
                print opp.defend(self)
                return
        else:
            print "Attack: %s missed." % (self.name)
            print opp.defend(self)
            return

    def snipe(self, opp):
        chance = self.acc - opp.speed
        if random.randint(1,10) <= (5 + chance):
            damage = 15 + 2*(self.strength - opp.res) + random.randint(-5,5)
            opp.hp -= damage
            if opp.hp <= 0:
                opp.die()
                print "Attack: %s killed %s." % (self.name, opp.name)
                return
            else:
                print "Attack: %s dealt %s %d damage. %s now has %d HP." % (self.name, opp.name, damage, opp.name, opp.hp)
                return
        else:
            print "Attack: %s missed." % (self.name)
            return

    def arrow(self,opp):
        damage = 15 + 2*(self.strength - opp.res) + random.randint(-5,5)
        opp.hp -= damage
        if opp.hp <= 0:
            opp.die()
            print "Counterattack: %s killed %s." % (self.name, opp.name)
            return
        else:
            print "Counterattack: %s dealt %s %d damage. %s now has %d HP." % (self.name, opp.name, damage, opp.name, opp.hp)
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

def init():
    pygame.init()

    #Set up window
    pygame.event.set_grab(0)
    pygame.mouse.set_visible(1)
    global screen
    screen = pygame.display.set_mode((300,200))
    shape = screen.convert_alpha()
    pygame.display.set_caption("Sniper Alert")

    #Draw on surface object
    screen.fill(BLACK)

def alert():
    init()
    #Create a font
    font = pygame.font.Font(None,50)

    #Render the text
    text = font.render("Sniper Alert", True, RED)

    #Create a rectangle
    textRect = text.get_rect()

    #Center the rectangle
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    #Blit the text
    screen.blit(text, textRect)
    pygame.display.update()

    return press()

def press():
    t0 = time.clock()
    dt = 0

    while time.clock() - t0 < maxt: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                dt = time.clock()- t0
                return dt

def snipe():
    dt = alert()
    pygame.quit()
    return dt
    
def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

def choose(listC):
    n = 1
    listN = []
    keys = dict()
    for i in sorted(listC):
        if i != "Sniper":
            keys[n] = i
            print "%d. %s" % (n, i)
            listN.append(n)
            n += 1
    print ""
    while True:
        choice = int(raw_input("Enter # of choice: "))
        if choice in listN:
            break
        else:
            print "Invalid input."
    print ""
    return keys[choice]

def player():
    print "PLAYER PHASE\n"
    listP = players.keys()
    listE = enemies.keys()
    repeat = True
    while len(listP) > 0 and repeat:
        print "Choose a player to attack with"
        choiceP = choose(listP)
        listP.remove(choiceP)
        print "Choose an enemy to attack"
        choiceE = choose(listE)
        players[choiceP].attack(enemies[choiceE])
        listP = intersect(listP, players.keys())
        listE = intersect(listE, enemies.keys())
        if len(listP) > 0:
            while True:
                repeat = raw_input("Attack again (y/n)? ")
                if repeat.lower() == "y":
                    repeat = True
                    break
                elif repeat.lower() == "n":
                    repeat = False
                    break
                else:
                    print "Invalid input."

def enemy():
    print "ENEMY PHASE\n"
    listP = players.keys()
    listE = enemies.keys()
    while len(listE) > 0:
        choiceP = random.choice(listP)
        choiceE = random.choice(listE)
        listE.remove(choiceE)
        if choiceE == "Sniper":
            dt = snipe()
            print dt # remove
            sniper.snipe(players[choiceP])
            if (0.05 <= dt <= maxt) and ("Legolas" in players.keys()):
                legolas.arrow(sniper)
                print ""
            else:
                print "Legolas was too slow. He missed the shot.\n"
        else:
            enemies[choiceE].attack(players[choiceP])
        listP = intersect(listP, players.keys())
        listE = intersect(listE, enemies.keys())
        if len(listE) > 1:
            raw_input("...")

def end():
    if enemies.keys() == []:
        print "\nCongratulations! You've defeated the evil mercenaries. Frodo is saved and the Ring is safe from Sauron for now..."
    elif players.keys() == []:
        print "\nYou've been defeated! The Ring will soon be in Sauron's hands and Middle Earth will be doomed. Thanks a lot... :("
