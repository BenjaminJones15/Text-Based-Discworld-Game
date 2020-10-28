from Map import *
from normalise import *
from inventory import *
from store import *
from Player import *

def print_location(location):         #prints out the location's name and description.    
    print()
    print((location.name).upper())       #displays the location's name in upper case, due to .upper
    print()    
    print(location.description)    #displays the location's description.
    print()


def exit_leads_to(exits, direction):        # returns the name of the location which the chosen direction leads to.  
    return (ListLocations[exits[direction]]).name


def print_exit(direction, leads_to):              #displays what the user will need to enter to travel to a location.
    print("Type Go " + direction.upper() + " to go to " + leads_to + ".")


def print_menu(exits, location, player):     #displays the options available to the user in a certain location.

    print("You currently have:")
    print()
    for key, value in inventory.items():            #iterates through each pair in the inventory dictionary, to display items.
        if value > 0:                #only prints if the player actually has the item. prevents the screen from clogging up with useless information.
            print(key, "- Quantity:", value)

    print()

    print("You can:")
    for direction in exits:             #iterates through each key in the dictionary,  
        print_exit(direction, exit_leads_to(exits, direction))           #prints the exit associated with the current value in the dictionary.

    if location == Mended_Drum:                     #specific condition for sidequest.
        print("TAKE ARMS to pick up the arms.")

    if location == Lady_Sybil_Free_Hospital:        #specific condition for sidequest.
        print("DROP arms")                          

    if player.class_chosen == "computer" and location == Pseudopolis_Yard_Upstairs:    #easter egg included, for use with a secret character class.
        print("INTERACT with locker")

    for i in location.POI:                        #iterates through each POI in the current location
        print("TALK to " + i.upper())            #prints out the appropriate command to interact with the POI

    print("What do you want to do?")      #ends with question, which can lead directly into user input.


def is_valid_exit(exits, chosen_exit):     #checks that the player has actually entered an exit which is available to them.
    return chosen_exit in exits

def execute_go(direction, location):           #used to move the player after they've entered the a movement command. 

    keyvalue = 0

    keyvalue = inventory.get("key piece")         #variable used to check if the player has enough keys to fight the final boss.

    if direction == "palace":                           #checks if the player is approaching the final boss
        print("You have " + str(keyvalue) + " keys")            #catches if they player doesn't have enough keys.
        if keyvalue < 4:
            print("You need four keys to enter the Throne Room")
            return location             #if not enough keys, returns the CurrentLocation.

    if is_valid_exit(location.exits, direction) == True:     #checks if the input is valid
        location = move(location.exits, direction)
        return location                 #returns the new location of the player
    else:
        print("You cannot go there.")       #catches the incorrect input, and the location stays the same.
        return location

def execute_take(item_id, location):       #used by the player to interact with items in the room.
    item_id = " ".join(item_id)     #takes the normalised list of the user's input, and converts it to a string again.
    for i in location.Items:        #iterates through each item in the location.
        if item_id == i:  
            if location.Items[item_id] > 0:     #checks that the item is present in the room.
                if item_id in inventory:
                    inventory[item_id] += 1                #adds item to the user's inventory
                    location.Items[item_id] -= 1           #removes the item from the room.
                    return ()

def execute_drop(item_id, location):         #used the the player to drop an item.
    item_id = " ".join(item_id)      #takes the normalised list of the user's input, and converts it to a string
    for i in inventory:               
        if item_id == i: 
            if item_id in inventory:                #checks that the item is presen in the user's inventory
                if inventory[item_id] > 0:
                    inventory[item_id] -= 1             #removes item from inventory
                    location.Items[item_id] +=1         #adds item to the room's list of items.
                return ()
    print("You cannot drop that")           #catches error if the user does not have the item in their inventory, or other error is thrown.


def execute_talk(command, location):        #used to interact with POI's in each room.
    command = " ".join(command)
    if command == "dibbler":        #calls the store function 
        store()
    elif location == Post_Office_Basement and location.sidequest:           #first POI after defeating boss, only shows up once.
        print("He damn near killed old Mr Groat. Thank you so much for defeating him. As a gift, take some money - the first ever 30 AM$ bill.")
        inventory["money"] += 30
        location.sidequest = False      #sets to false, so this dialogue won't repeat.
    elif location == Gimlets_Restaurant and location.sidequest:                #first POI after defeating boss, only shows up once.
        print("Thank you for getting rid of him - he was grating on everyone's nerves. Truly the most irritating customer I've ever met, and that's saying something. Have a free rat pie on me!")
        inventory["health pie"] += 1
        location.sidequest = False         #sets to false, so dialogue won't repeat.
    elif location.Items["arms"] == 5 and location == Lady_Sybil_Free_Hospital:      #dialogue used for sidequest. 
        if location.sidequest:
            print("Thank you for bringing me these arms")
            print("Here is some money for your troubles")
            inventory["money"] += 50
            location.sidequest = False              #set to false, so dialogue won't repeat.
        else:
            print("You've already helped me")       #alternate dialogue after quest completed.
    elif location == Dragon_Sanctuary and inventory["swamp dragons"] > 0:               #sidequest option, repeats everytime the user gains more swamp dragons.
        print("I can take those dragons of your hands for 10 AM$ each: yes/no")
        choice = " ".join(normalise_input(input("> ")))
        if choice == "yes":
            num = 0
            while inventory["swamp dragons"]>0:
                inventory["swamp dragons"] -=1
                num +=1
            print("here is " + str(num*10) + " AM$")
            inventory["money"] += num*10
        else:
            print("Are you sure you won't reconsider?")

    else:                   #reacts normally to the POI, using the value specified by the command
        if command in location.POI:         #checks the command is in the POI dictionary.
            print(location.POI[command])
        else:
            print("you can't talk to that")     #catch statement if user enters an incorrect input.
    time.sleep(15)

def execute_command(command, location):         #used by the user to interact with the game via text commands.
    if 0 == len(command):       #prevents an empty command from being entered. 
        return location

    if command[0] == "go":      #deals with movement
        if len(command) > 1:
            newlocation = execute_go(command[1], location)
            if newlocation is None:         #catch statement if the user has entered an incorrect location.
                newlocation = location  #simply returns the current location, so nothing has happened.
                return newlocation      
            else:
                return newlocation
        else:
            print("Go where?")      #conditional if the user has only entered go

    elif command[0] == "take":          #deals with user taking something from location.
        if len(command) > 1:
            execute_take(command[1:], location)
        else:
            print("Take what?")         #conditional if the user has only entered take

    elif command[0] == "drop":          #deals with user dropping something in a location.
        if len(command) > 1:
            execute_drop(command[1:], location)
        else:
            print("Drop what?")     #conditional if the user has only entered drop
    elif command[0] == "interact" and location == Pseudopolis_Yard_Upstairs:        #easter egg command, for a specific location and class.
        print("A picture of your computer scientist degree")

    elif command[0] == "talk":      #deals with user talking/interacting with someone in the location.
        if len(command) > 1:
            execute_talk(command[1:], location)
        else:
            print("Talk to who?")       #conditional if the user has only entered talk

    else:
        print("This makes no sense.")       #general error catch if the user has entered text, but it doesn't apply to any of the other statements.

    newlocation = location      #catch if any of the conditionals throughout the function fail.
    return newlocation


def menu(exits, location, player):    #gets and then returns the user's input.  
    print_menu(exits, location, player)     #displays the menu
    user_input = input("> ")    #waits for the user's input
    normalised_user_input = normalise_input(user_input)     #normalises the user's input
    return normalised_user_input        


def move(exits, direction):           #used to check if a player's movement is valid.
    return ListLocations[exits[direction]]      
