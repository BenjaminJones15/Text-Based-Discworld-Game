from combat import *
from enemies import *
from Map import *
from Player import *
import random

CurrentLocation = Pseudopolis_Yard_Inside       #would need to move to combat.py if also moving save and load 
saveHealth = 0
saveMana = 0
saveExp = 0
saveInventory = ""
saveLocation = ""

def main():
    StartMenu()
    
 
    #commenting

def RndEncounter(location):
    if location.name == "The Library":
        CurEnemy = "ShadowingLemma"
        start_battle()
    elif location.name == "The Shades":
        CurEnemy = "Mugger"
        start_battle()
    else:
        EnChance = random.randint(0,1)
        if EnChance == 0:
            return()
        else:
            CurEnemy = EnemyList[random.randint(0,len(EnemyList)-1)]    #selects an enemy from the list of sprites
            start_battle()

#to solve errors need to move both functions into combat.py, and then call them from here.


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