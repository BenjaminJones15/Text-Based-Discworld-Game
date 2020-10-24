from player import *
from items import *
from main import *
from map import *

## This piece of code is designed to be amended to the excecute go function.
## This is currently unfinished and requires correct variable names and modules to import

keyvalue = 0  ## start this value as zero from main? Global Variable

stringinput = ()
stringinput = normalised_user_input
# string input lets us know when the player wants to go into throne room
# global variable, can be placed potentionally in main

global current_room


if stringinput == "throne room ":
    # granted user input is normalised and .lowered / else may require stringinput[1]
    for key in inventory:
        keyvalue = keyvalue + 1
    # iterate over all keys in inventory to add a int value to keyvalue variable if "throne room is entered"
    print("You have have", keyvalue, "keys")
    # let player know regardless
    if CurrentLocation == Palace.name and keyvalue < 4:
        print("You need four keys to enter the Throne Room")
    # if player is in palace AND does not have all 4 keys

    elif is_valid_exit(current_room["exits"], direction):
        updated_room = move(current_room["exits"], direction)
        current_room = updated_room
        return current_room
    # else check if valid direction and move player.
    # This can be removed and replaced with actual function if different from lab 6.

    else:
        print("You cannot go there.")

elif is_valid_exit(current_room["exits"], direction):
    updated_room = move(current_room["exits"], direction)
    current_room = updated_room
    return current_room

else:
    print("You cannot go there.")
