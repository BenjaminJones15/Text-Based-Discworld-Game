from combat import *
from enemies import *
from Map import *
from Player import *
from Move import *
import copy
import random
CurEnemy = Mugger
CurrentLocation = Pseudopolis_Yard_Reception
MyPlayer = Player

def main(): 
    global MyPlayer   
    MyPlayer = StartMenu()
    global CurrentLocation    
    save_checkpoint(CurrentLocation, MyPlayer)
    print("""
 ____  _                             _     _ 
|  _ \(_)___  _____      _____  _ __| | __| |
| | | | / __|/ __\ \ /\ / / _ \| '__| |/ _` |
| |_| | \__ \ (__ \ V  V / (_) | |  | | (_| |
|____/|_|___/\___| \_/\_/ \___/|_|  |_|\__,_|


▀█▀ █ █ █▀▀   █▀▄ █▀█ █ █ █ █▄ █ █▀▀ ▄▀█ █   █     █▀█ █▀▀   █▄▀ █ █▀█ █ █   █  
 █  █▀█ ██▄   █▄▀ █▄█ ▀▄▀▄▀ █ ▀█ █▀  █▀█ █▄▄ █▄▄   █▄█ █▀    █ █ █ █▀▄ █ █▄▄ █▄▄
""")

    print("You must free the city and defeat Kirill!")
    time.sleep(2.5)
    while True:
        print_location(CurrentLocation)
        RndEncounter(CurrentLocation)
        command = menu(CurrentLocation.exits, CurrentLocation.Items, inventory, CurrentLocation)
        CurrentLocation = execute_command(command, CurrentLocation)
                

def RndEncounter(location):    
    global CurEnemy   
    global CurrentLocation
    global MyPlayer
    EnChance = random.randint(0,1)

    if location == Library:              
        CurEnemy = copy.deepcopy(ShadowingLemma)
        if EnChance == 0:
            return()
        else:
            CurrentLocation = start_battle(location, CurEnemy, MyPlayer)        
    elif location == The_Shades:
        CurEnemy = copy.deepcopy(Mugger)
        if EnChance == 0:
            return()
        else:
            CurrentLocation = start_battle(location, CurEnemy, MyPlayer)
    elif location == Gimlets_Restaurant:
        if location.boss == True:
            CurEnemy = copy.deepcopy(Johnathan)        
            CurrentLocation = start_battle(location, CurEnemy, MyPlayer)        
    elif location == Library_Roof:
        if location.boss == True:
            CurEnemy = copy.deepcopy(CarcerDun)
            CurrentLocation = start_battle(location, CurEnemy, MyPlayer)        
    elif location == Palace:
        if location.boss == True:
            CurEnemy = copy.deepcopy(Kirill)
            CurrentLocation = start_battle(location, CurEnemy, MyPlayer)        
    elif location == Post_Office_Basement:
        if location.boss == True:
            CurEnemy = copy.deepcopy(MrGryle)
            CurrentLocation = start_battle(location, CurEnemy, MyPlayer)        
    elif location == Temple_of_Anoia_Inner:
        if location.boss == True:
            CurEnemy = copy.deepcopy(Gitlab)
            CurrentLocation = start_battle(location, CurEnemy, MyPlayer)        
    else:            
        if EnChance == 0 or location.sprite == False:            
            return()
        else:
            CurEnemy = copy.deepcopy(EnemyList[random.randint(0,len(EnemyList)-1)])    #selects an enemy from the list of sprites
            CurrentLocation = start_battle(location, CurEnemy, MyPlayer) 
            if CurEnemy == SwampDragon:
                   inventory["swamp dragons"] += 1
            
if __name__ == "__main__":  # Sets the main to StartMenu()
    main()