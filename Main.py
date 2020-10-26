from combat import *
from enemies import *
from Map import *
from Player import *
from Move import *
import random
CurEnemy = enemy
CurrentLocation = Pseudopolis_Yard_Reception

saveHealth = 0
saveMana = 0
saveExp = 0
saveInventory = ""
saveLocation = ""

def main():
    StartMenu()

    while True:   #main game loop.        
        display_location(CurrentLocation)    #displays current location

        # What are the possible exits from the current room?
        exits = current_room["exits"]

        # Show the menu with exits and ask the player
        direction = menu(exits)

        # Move the protagonist, i.e. update the current room
        current_room = move(exits, direction)

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