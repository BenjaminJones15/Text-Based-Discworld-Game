import time

from character_class import *
from inventory import *

class Player:  # Player Class
    def __init__(self, player_name, class_chosen):  # player_name and class_chosen use user inputs so 'self' is used
        self.player_name = player_name
        self.class_chosen = class_chosen
        self.exp = 0  # player's exp, initially set to 0
        self.health = Classes[self.class_chosen]["health"]  # health, mana, strength added from Classes dictionary
        self.mana = Classes[self.class_chosen]["mana"]
        self.strength = Classes[self.class_chosen]["strength"]
        self.maxHealth = Classes[self.class_chosen]["health"]
        self.maxMana = Classes[self.class_chosen]["mana"]
        self.inventory = inventory  # Inventory added from inventory dictionary


def print_descriptions():  # Prints the descriptions of each class
    for key in Classes:  # Loops for the number of classes
        print(Classes[key]["description"])  # Prints each description
        time.sleep(2.5)  # 2.5 second delay between each description output
        print()  # Adds a blank line between each description


def is_valid_class(picked_class):  # Checks if the class inputted by the user is in the dictionary
    for key in Classes:  # Loops for the number of keys in dictionary 'Classes' (Currently 3: Wizard, Warrior, Undead)
        if picked_class == key:  # If user input matches one of the keys, return True
            return True
    return False  # If user input doesn't match any of the keys, return False


def choose_class():  # Takes user's class input and checks if it is valid. It will continue to loop till a valid class is entered
    print("Choose your class")
    picked_class = input("> ")  # User inputs class name
    #  <-- Insert normalise_input function here
    valid_class = is_valid_class(picked_class)  # Calls is_valid_class function to check if the class entered by user is in the character class dictionary
    while valid_class == False:  # Loops while return value from is_valid_class is False
        print("Invalid class inputted")
        print("Choose your class: ")
        picked_class = input("> ")  # User inputs class name
        #  <-- Insert normalise_input function here
        valid_class = is_valid_class(picked_class)  # Calls check_input function to check if the class entered is in the character class dictionary
    return picked_class


def starting_inventory(player):  # Gives the player starting items depending on their chosen class
    if player.class_chosen == "Wizard":  # If wizard was chosen, add 2 mana pies to inventory
        player.inventory["Mana Pie"] += 2
    elif player.class_chosen == "Warrior":  # If warrior was chosen, add 1 hp, 1 mana pie to inventory
        player.inventory["Mana Pie"] += 1
        player.inventory["HP Pie"] += 1
    else:
        player.inventory["Strength Pie"] += 2  # If undead was chosen, add 2 strength pie to inventory

    return player.inventory  # Return updated player inventory


def StartMenu():  # Where the program begins. Can change when everything is implemented
    print("Enter your name")
    user_name = input("> ")  # Prompts user to enter a name for the character
    print_descriptions()  # Calls print_descriptions function, which prints each class description
    user_class = choose_class()  # Calls function choose_class
    player = Player(user_name, user_class)  # Creating the player using an instance of the Player class
    player.inventory = starting_inventory(player)  # Gives the player starting items depending on their class

if __name__ == "__main__":  # Sets the main to StartMenu()
    StartMenu()



# inventory as a dictionary
