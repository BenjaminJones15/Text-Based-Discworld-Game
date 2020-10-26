from combat import *
from enemies import *
from Map import *
from Player import *
from Move import *
import random
CurEnemy = enemy
CurrentLocation = Pseudopolis_Yard_Reception

def main():
    StartMenu()

    while True:
        print("You must free the city and defeat Kirill!")
        print_location(CurrentLocation)

        command = menu(CurrentLocation.exits, CurrentLocation.Items, inventory)
        execute_command(command)
        

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