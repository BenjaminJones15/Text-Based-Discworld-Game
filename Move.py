from Map import *

def normalise_input(user_input):
    user_input = remove_punct(user_input)#here we are calling previous functions we made earlier
    user_input = remove_spaces(user_input)
    user_input = user_input.lower() # here we use the method .lower() to make the user_input lower case
    return user_input

def display_room(room):
    print("")
    print(room["name"].upper())#here we call from the dictionary to display the name of the room we are in and also capitlise it
    print("")
    print(room["description"])#now we call the value from room to display the description of the room
    print("")

def exit_leads_to(exits, direction):
    exit_room = exits[direction]
    return str(rooms[exit_room]["name"]) # we are calling the key name from the dictionary rooms and showing where the exits lead to

def print_menu_line(direction, leads_to):
    print("Go "+direction.upper()+" to",leads_to+".")

def print_menu(exits):

    print("You can:")
    
    #direction is the key and the nextroom is the value
    for key, value in exits.items():
        print_menu_line(key, exit_leads_to(exits, key)) # here we are printing the avaliable exits from the dictionary exits
        
    print("Where do you want to go?")

def is_valid_exit(exits, user_input):
    for direction in exits:
        if user_input == direction:
            return True
    return False

def menu(exits):
    # Repeat until the player enter a valid choice
    while True:
        print_menu(exits)
        room_input = input()
        room_input = normalise_input(room_input)
        if is_valid_exit(exits, room_input) ==True:
            return room_input
        else:
            print("Invalid input, Try Again")

def move(exits, direction):
    next_room_name = exits[direction]
    next_room = rooms[next_room_name]
    return next_room

def main():
    # Start game at the reception
    current_room = rooms["Outside of Pseudopolis Yard"]

    # Main game loop
    while True:
        # Display game status (room description etc.)
        display_room(current_room)

        # What are the possible exits from the current room?
        exits = current_room["exits"]

        # Show the menu with exits and ask the player
        direction = menu(exits)

        # Move the protagonist, i.e. update the current room
        current_room = move(exits, direction)