from Map import *
from normalise import *
from inventory import *
from store import *


def print_location(location):
    # Display room name
    print()
    print((location.name).upper())
    print()
    # Display room description
    print(location.description)
    print()


def exit_leads_to(exits, direction):
    # returns name of room into which exit leads.
    return (ListLocations[exits[direction]]).name


def print_exit(direction, leads_to):
    print("Type Go " + direction.upper() + " to go to " + leads_to + ".")


def print_menu(exits, location_items, inv_items, location):

    print("You currently have:")
    print()
    for key, value in inventory.items():
        if value > 0:
            print(key, "- Quantity:", value)

    print()

    print("You can:")
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    if location == Lady_Sybil_Free_Hospital or location == Dragon_Sanctuary:
        None
    else:
        for i in location_items:
            print("TAKE " + i.upper() + " to take " + i + ".")

    if location == Lady_Sybil_Free_Hospital:
        print("DROP arms")
    elif location == Dragon_Sanctuary:
        print("DROP swamp dragons")

    for i in location.POI:
        print("TALK to " + i.upper())

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits

def execute_go(direction, location):

    keyvalue = 0

    keyvalue = inventory.get("key piece")

    if direction == "palace":
        print("You have " + str(keyvalue) + " keys")
        if keyvalue < 4:
            print("You need four keys to enter the Throne Room")
            return location

    if is_valid_exit(location.exits, direction) == True:
        location = move(location.exits, direction)
        return location
    else:
        print("You cannot go there.")


def execute_take(item_id, location):    
    item_id = " ".join(item_id)
    for i in location.Items:        
        if item_id == i:  # change if each item becomes an object
            if location.Items[item_id] > 0:
                if item_id in inventory:
                    inventory[item_id] += 1                
                    location.Items[item_id] -= 1
                    return ()

def execute_drop(item_id, location):    
    item_id = " ".join(item_id)
    for i in inventory:               
        if item_id == i:  # change if each item becomes an object
            if item_id in inventory:
                if inventory[item_id] > 0:
                    inventory[item_id] -= 1
                    location.items[item_id] +=1                
                return ()
    print("You cannot drop that")


def execute_talk(command, location):
    command = " ".join(command)
    if command == "dibbler":
        store()
    else:
        if command in location.POI:
            print(location.POI[command])
        else:
            print("you can't talk to that")


def execute_command(command, location):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            newlocation = execute_go(command[1], location)
            if newlocation is None:
                newlocation = location
                return newlocation
            else:
                return newlocation
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1:], location)
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1:], location)
        else:
            print("Drop what?")

    elif command[0] == "talk":
        if len(command) > 1:
            execute_talk(command[1:], location)
        else:
            print("Talk to who?")

    else:
        print("This makes no sense.")
    newlocation = location
    return newlocation


def menu(exits, room_items, inv_items, location):
    # Display menu
    print_menu(exits, room_items, inv_items, location)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    return ListLocations[exits[direction]]
