from combat import *
from enemies import *
from Map import *
from Player import *
import random

CurrentLocation = Pseudopolis_Yard_Inside
saveHealth = 0
saveMana = 0
saveExp = 0
saveInventory = ""
saveLocation = ""

def main():
    print()
 
    #commenting

def RndEncounter(location):
    if location.name == "The Library":
        print_battle(ShadowingLemma)
    elif location.name == "The Shades":
        print_battle(Mugger)
    else:
        EnChance = random.randint(0,1)
        if EnChance == 0:
            return()
        else:
            CurEnemy = EnemyList[random.randint(0,len(EnemyList)-1)]    #selects an enemy from the list of sprites
            print_battle(CurEnemy)


def save_checkpoint():  # saves all the players stats after reaching a checkpoint
    global saveHealth, saveMana, saveExp, saveInventory, saveLocation
    # global used so that the variables can be accessed in other functions e.g. load_checkpoint
    saveHealth = Player.health
    saveMana = Player.mana
    saveExp = Player.exp
    saveInventory = Player.inventory
    saveLocation = Location


def load_checkpoint():  # loads last saved checkpoint after loosing a game
    Player.health = saveHealth
    Player.mana = saveMana
    Player.exp = saveExp
    Player.inventory = saveInventory
    Location = saveLocation