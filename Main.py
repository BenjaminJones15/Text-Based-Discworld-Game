from combat import *
from enemies import *
from Map import *
from Player import *
from Move import *
import copy          #used to prevent enemy health being 0 if you encounter them twice.
import random        #used to randomise the chance of an enemy appearing.
CurEnemy = Mugger          #creates the variable, using an object to make sure the data type of the variable is the class enemy.
CurrentLocation = Pseudopolis_Yard_Reception   #creates the variable, using the same principle as above.
MyPlayer = Player        #creates the variable, using the same principle as above.

def main(): 
    global MyPlayer           #imports the global variable, to allow it to be changed inside the function.
    global CurrentLocation    #same principle as above.
    MyPlayer = StartMenu()    
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
    while True:         #game will be in a loop until an exit command is called, upon completion of the game.
        print_location(CurrentLocation)
        RndEncounter(CurrentLocation)
        command = menu(CurrentLocation.exits, CurrentLocation, MyPlayer)
        CurrentLocation = execute_command(command, CurrentLocation)
                

def RndEncounter(location):           #Used to control random encounters around the map, and to pick which enemies you will face at a certain location.
    global CurEnemy                #imports global variables so they can be changed in the function
    global CurrentLocation         #as above
    global MyPlayer                #as above

    EnChance = random.randint(0,1)      #uses the equivalent of a coin flip to decide if a player will face a random enemy.

    if location == Library:              
        CurEnemy = copy.deepcopy(ShadowingLemma)      #specifies a magical enemy due to magical location. Deepcopy used to prevent updated statistics from overwriting the original object.
        if EnChance == 0:
            return()
        else:
            CurrentLocation = start_battle(location, CurEnemy, MyPlayer)        
    elif location == The_Shades:                #specifies a certain enemy due to the particular nature of the location. Uses lore to inform this decision.
        CurEnemy = copy.deepcopy(Mugger)
        if EnChance == 0:
            return()
        else:
            CurrentLocation = start_battle(location, CurEnemy, MyPlayer)
    elif location == Gimlets_Restaurant:                 
        if location.boss == True:                   #checks if the boss will appear - prevents you from having to battle him multiple times.
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
        if EnChance == 0 or location.sprite == False:            #catches either condition, so certain locations, e.g. boss battles or safe spaces won't have a chance of sprites spawning.
            return()
        else:
            CurEnemy = copy.deepcopy(EnemyList[random.randint(0,len(EnemyList)-1)])    #selects an enemy from the list of sprites, and puts it into the var. CurEnemy.
            CurrentLocation = start_battle(location, CurEnemy, MyPlayer) 
            if CurEnemy == SwampDragon:                    #after beating the specific enemy, it is added to your inventory to facilitate a sidequest.
                   inventory["swamp dragons"] += 1
            
if __name__ == "__main__":  # Sets the main to call the main module
    main()