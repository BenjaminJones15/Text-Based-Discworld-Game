from combat import *
from enemies import *
from Map import *
from Player import *
import random
CurEnemy = enemy

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
        CurEnemy = ShadowingLemma
        start_battle()        #will be fixed if moving save and load to combat.
    elif location.name == "The Shades":
        CurEnemy = Mugger
        start_battle()
    else:
        EnChance = random.randint(0,1)
        if EnChance == 0:
            return()
        else:
            CurEnemy = EnemyList[random.randint(0,len(EnemyList)-1)]    #selects an enemy from the list of sprites
            start_battle()

            
if __name__ == "__main__":  # Sets the main to StartMenu()
    main()