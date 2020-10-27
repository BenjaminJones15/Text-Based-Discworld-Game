from Map import *
from normalise import *
from inventory import *

def print_location(location):        
    # Display room name
    print()
    print((location.name).upper())
    print()
    # Display room description
    print(location.description)
    print()   

def exit_leads_to(exits, direction):
    #returns name of room into which exit leads.    
    return (ListLocations[exits[direction]]).name

def print_exit(direction, leads_to):
    print("Type Go " + direction.upper() + " to go to " + leads_to + ".")

def print_menu(exits, location_items, inv_items):
    print("You can:")
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for i in location_items:
        print("TAKE " + i["id"].upper() + " to take " + i["name"] + ".")

    for i in inv_items:
        print("DROP " + i.upper() + " to drop your " + i + ".")
    
    print("What do you want to do?")

def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits

def execute_go(direction,location):  
     
    if is_valid_exit(location.exits,direction) == True:
        location = move(location.exits, direction)        
        return location
    else:
        print("You cannot go there.")        

def execute_take(item_id, location):
    for i in location.Items:
        count +=1
        if item_id == i["id"]:   #change if each item becomes an object
            if item_id in inventory:
                inventory[item_id] += 1
                del location.Items[count]
                return()

def execute_drop(item_id, location):
    for i in inventory:
        count +=1
        if item_id == i["id"]:   #change if each item becomes an object
            if item_id in inventory:
                inventory[item_id] += 1
                del location.Items[count]
                return()
    print("You cannot drop that")

def execute_command(command, location):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            newlocation= execute_go(command[1], location) 
            if newlocation is None:
                newlocation = location
                return newlocation
            else:
                return newlocation          
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1], location)
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1], location)
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")

def menu(exits, room_items, inv_items):
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def move(exits, direction):
    return ListLocations[exits[direction]]