from combat import *
from enemies import *
from Map import *
from Player import *
from Move import *
import random
CurEnemy = Mugger
CurrentLocation = Pseudopolis_Yard_Reception

def main():    
    StartMenu()              
    print("You must free the city and defeat Kirill!")
    while True:
        global CurrentLocation
        print_location(CurrentLocation)
        RndEncounter(CurrentLocation)
        command = menu(CurrentLocation.exits, CurrentLocation.Items, inventory)
        CurrentLocation = execute_command(command, CurrentLocation)        

def RndEncounter(location):
    global CurEnemy
    #EnChance = random.randint(0,1)
    EnChance = 1
    if location == Library:
        CurEnemy = ShadowingLemma
        if EnChance == 0:
            return()
        else:
            start_battle(location, CurEnemy)        
    elif location == The_Shades:
        CurEnemy = Mugger
        if EnChance == 0:
            return()
        else:
            start_battle(location, CurEnemy)
    elif location == Pseudopolis_Yard_Reception or location == Pseudopolis_Yard_Outside or location == Pseudopolis_Yard_Upstairs:
        return()
    else:        
        if EnChance == 0:
            return()
        else:
            CurEnemy = EnemyList[random.randint(0,len(EnemyList)-1)]    #selects an enemy from the list of sprites
            start_battle(location, CurEnemy)

            
if __name__ == "__main__":  # Sets the main to StartMenu()
    main()