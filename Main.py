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
    global CurrentLocation
    save_checkpoint(CurrentLocation)
    print("""
 ____  _                             _     _ 
|  _ \(_)___  _____      _____  _ __| | __| |
| | | | / __|/ __\ \ /\ / / _ \| '__| |/ _` |
| |_| | \__ \ (__ \ V  V / (_) | |  | | (_| |
|____/|_|___/\___| \_/\_/ \___/|_|  |_|\__,_|

        88                                  88                                              ad88            88 88                   ad88     88      a8P  88              88 88 88  
  ,d    88                                  88                                             d8"              88 88                  d8"       88    ,88'   ""              "" 88 88  
  88    88                                  88                                             88               88 88                 88         88  ,88"                        88 88  
MM88MMM 88,dPPYba,   ,adPPYba,      ,adPPYb,88  ,adPPYba,  8b      db      d8 8b,dPPYba, MM88MMM ,adPPYYba, 88 88      ,adPPYba, MM88MMM     88,d88'      88  8b,dPPYba,  88 88 88  
  88    88P'    "8a a8P_____88     a8"    `Y88 a8"     "8a `8b    d88b    d8' 88P'   `"8a  88    ""     `Y8 88 88     a8"     "8a  88        8888"88,     88  88P'   "Y8  88 88 88  
  88    88       88 8PP"""""""     8b       88 8b       d8  `8b  d8'`8b  d8'  88       88  88    ,adPPPPP88 88 88     8b       d8  88        88P   Y8b    88  88          88 88 88  
  88,   88       88 "8b,   ,aa     "8a,   ,d88 "8a,   ,a8"   `8bd8'  `8bd8'   88       88  88    88,    ,88 88 88     "8a,   ,a8"  88        88     "88,  88  88          88 88 88  
  "Y888 88       88  `"Ybbd8"'      `"8bbdP"Y8  `"YbbdP"'      YP      YP     88       88  88    `"8bbdP"Y8 88 88      `"YbbdP"'   88        88       Y8b 88 8 8          88 88 88

  """)


    print("You must free the city and defeat Kirill!")
    while True:
        print_location(CurrentLocation)
        RndEncounter(CurrentLocation)
        command = menu(CurrentLocation.exits, CurrentLocation.Items, inventory)
        CurrentLocation = execute_command(command, CurrentLocation)        

def RndEncounter(location):
    global CurEnemy
    EnChance = random.randint(0,1)
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
    elif location == Gimlets_Restaurant:
        CurEnemy = Johnathan        
        start_battle(location, CurEnemy)
    elif location == Library_Roof:
        CurEnemy = CarcerDun
        start_battle(location, CurEnemy)
    elif location == Palace:
        CurEnemy = Kirill
        start_battle(location, CurEnemy)
    elif location == Post_Office_Basement:
        CurEnemy = MrGryle
        start_battle(location, CurEnemy)
    elif location == Temple_of_Anoia_Inner:
        CurEnemy = Gitlab
        start_battle(location, CurEnemy)
    else:        
        if EnChance == 0:
            return()
        else:
            CurEnemy = EnemyList[random.randint(0,len(EnemyList)-1)]    #selects an enemy from the list of sprites
            start_battle(location, CurEnemy)

            
if __name__ == "__main__":  # Sets the main to StartMenu()
    main()