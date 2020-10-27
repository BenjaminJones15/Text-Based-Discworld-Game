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


▀█▀ █░█ █▀▀   █▀▄ █▀█ █░█░█ █▄░█ █▀▀ ▄▀█ █░░ █░░   █▀█ █▀▀   █▄▀ █ █▀█ █ █░░ █░░
░█░ █▀█ ██▄   █▄▀ █▄█ ▀▄▀▄▀ █░▀█ █▀░ █▀█ █▄▄ █▄▄   █▄█ █▀░   █░█ █ █▀▄ █ █▄▄ █▄▄
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
        if location.boss == True:
            CurEnemy = Johnathan        
            start_battle(location, CurEnemy)        
    elif location == Library_Roof:
        if location.boss == True:
            CurEnemy = CarcerDun
            start_battle(location, CurEnemy)        
    elif location == Palace:
        if location.boss == True:
            CurEnemy = Kirill
            start_battle(location, CurEnemy)        
    elif location == Post_Office_Basement:
        if location.boss == True:
            CurEnemy = MrGryle
            start_battle(location, CurEnemy)        
    elif location == Temple_of_Anoia_Inner:
        if location.boss == True:
            CurEnemy = Gitlab
            start_battle(location, CurEnemy)        
    else:        
        if EnChance == 0:
            return()
        else:
            CurEnemy = EnemyList[random.randint(0,len(EnemyList)-1)]    #selects an enemy from the list of sprites
            start_battle(location, CurEnemy)
    global CurrentLocation
    CurrentLocation = NewLocation
            
if __name__ == "__main__":  # Sets the main to StartMenu()
    main()