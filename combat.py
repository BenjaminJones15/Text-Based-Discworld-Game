from normalise import *
from Map import *
from Player import *
from enemies import *
import random
import time


def print_battle():  # prints your battle options each turn
    print("You can: ")
    print("Attack")
    print("Use Mana")
    print("Use Items")
    print("Inspect enemy")
    print("RUN!!!")
    print()
    print("What do you want to do?")
    choice = input("> ")
    choice = remove_punct(choice.lower()) # uses the function from normalise.py
    choice = remove_spaces(choice)
    return choice


def execute_attack(CurEnemy):  # deals damage to the enemy
    CurEnemy.health = CurEnemy.health - random.randrange(Player.strength / 2, Player.strength, 1)
    # takes a random number based on strength to attack
    print("The enemy lost " + Player.strength + " health")
    global strength_check  # used to check if a strength potion has been used
    if strength_check = True:
        Player.strength = Player.strength/3
        strength_check = False


def execute_mana(CurEnemy):  # mana is set damage and shows your mana falling
    CurEnemy.health = CurEnemy.health - 20
    Player.mana = Player.mana - 20
    print("The enemy lost 20 health")
    print("You used up 20 mana")


def execute_item():  # brings up a item selection menu
    print("What item do you want to use: ")
    for i in inventory:  # prints items in your inventory
        print(i)
    item = normalise_input(input("> "))
    if item == "health pie":
        if inventory["Health Pie"] == 0:
            print("You do not have enough Health Pies")
        else:
            Player.health = Player.health + 50            
            Player.maxHealth = Player.maxHealth            
            if Player.health > Player.maxHealth:  # checks to see health doesn't go over the max
                Player.health = Player.maxHealth
            inventory["Health Pie"] -= 1
    elif item == "mana pie":
        if inventory["Mana Pie"] == 0:
            print("You do not have enough Mana Pies")
        else:
            Player.mana = Player.mana + 50
            Player.maxMana = Player.maxMana
            if Player.mana > Player.maxMana:  # checks to see mana doesn't go over the max
                Player.mana = Player.maxMana
            inventory["Mana Pie"] -= 1
    elif item == "strength pie":
        if inventory["Strength Pie"] == 0:
            print("You do not have enough Strength Pies")
        else:
            Player.strength = Player.strength*3  # increases the players strength for one turn
            global strength_check
            strength_check = True  # check used to turn it back the next attack
            inventory["Strength Pie"] -= 1
    else:  # incase the user try's to select another item
        print("Please select a potion")


def execute_inspect(CurEnemy):  # views the enemies stats
    print(CurEnemy.description)
    print("The enemy has " + CurEnemy.health)
    print("Enemy strength " + CurEnemy.strength)
    print("Enemy magic " + CurEnemy.magic)


def execute_run(CurrentLocation, CurEnemy):  # try to run from the fight
    if CurrentLocation.boss:  # checks if the fight is a boss battle
        if CurEnemy.name == "Jonathan":  # easter egg with the first boss
            print("Really?")
            game_over(CurrentLocation)  #nice touch
        else:  # not allowed to run from a boss fight
            print("You can't run from this battle")
    else:
        run = random.randrange(1, 2, 1)  # random chance to run from the battle
        if run == 1:
            Player.health = Player.health - 10  # still take damage for running away
            health_check(CurrentLocation)
            global battle
            battle = False
            print("You ran away!")
        else:
            print("You couldn't get away")


def execute_battle_choice(choice, CurrentLocation, CurEnemy):  # used to pick which battle action should occur
    if choice == "attack":
        execute_attack(CurEnemy)
    elif choice == "mana":
        if Player.mana >= 20:  # see's if the player has enough mana to use a spell
            execute_mana(CurEnemy)
        else:
            print("Not enough mana")
    elif choice == "items":
        execute_item()
    elif choice == "inspects":
        execute_inspect(CurEnemy)
    elif choice == "run":
        execute_run(CurrentLocation, CurEnemy)
    else:
        print("Incorrect command")  # used to make sure the user knows they entered the wrong value


def enemy_health_check(CurrentLocation, CurEnemy):  # checks the enemy's health each turn to see if the battle has ended
    if CurEnemy.health <= 0:
        print("you win.")
        global battle
        battle = False
        if CurrentLocation.boss:  # if it is a boss fight it drops set items
            inventory["Money"] += 100
            inventory["Key Piece"] += 1
            Player.exp = Player.exp + 100  # level up after a fight
            save_checkpoint(CurrentLocation)  # saves the players progress after beating a boss
        else:  # otherwise a random amount of gold and exp
            drop = random.randrange(0, 5, 1)
            inventory["Money"] += drop
            ex = random.randrange(CurEnemy.exp / 2, CurEnemy.exp, 1)  # random amount of experience after regular fights
            Player.exp = Player.exp + ex


def enemy_attack(CurEnemy):
    attack = random.randrange(1, 3, 1)   # randomly decides what attack enemies should use
    if attack == 3:
        print(CurEnemy.name + " uses magic")
        print("You took " + CurEnemy.magic + " damage")
        Player.health = Player.health - CurEnemy.magic
    else:  # enemies are more likely to attack than use magic
        print(CurEnemy.name + " attacks")
        print("You took " + str(CurEnemy.strength) + " damage")
        Player.health = Player.health - CurEnemy.strength


def health_check(CurrentLocation):  # checks the player's health each turn to check they haven't died
    if Player.health <= 0:  # if they have it does the game over screen
        game_over(CurrentLocation)
 

def exp_check():  # checks to see if the player should level up    
    if Player.exp >= 100:
        Player.health = Player.maxHealth
        Player.mana = Player.maxMana
        Player. exp = 0


def game_over(CurrentLocation):  # game over screen asking if they wish to continue
    print("You lose")
    time.sleep(10)  # time to reflect on losing
    print()
    print("Do you wish to continue? yes/no")  # option to continue
    choice = normalise_input(input())
    if choice == "yes":  # if yes it loads a checkpoint otherwise the game quits
        load_checkpoint(CurrentLocation)
    else:
        quit()


def start_battle(CurrentLocation, CurEnemy):  # how the battle will be carried out each turn
    global strength_check
    global battle
    battle = True
    strength_check = False
    print(CurEnemy.name + " has appeared")  # gets enemy name from what was called in the random encounter
    while battle == True:
        print("Your turn")  # with your turn is occurring
        options = print_battle()
        execute_battle_choice(options, CurrentLocation, CurEnemy)
        enemy_health_check(CurrentLocation, CurEnemy)
        print("Enemy's turn")  # and then the enemies
        time.sleep(2)
        enemy_attack(CurEnemy)
        health_check(CurrentLocation)


def save_checkpoint(CurrentLocation):  # saves all the players stats after reaching a checkpoint
    global saveHealth, saveMana, saveExp, saveInventory, saveLocation
    # global used so that the variables can be accessed in other functions e.g. load_checkpoint
    saveHealth = Player.health
    saveMana = Player.mana
    saveExp = Player.exp
    saveInventory = Player.inventory
    saveLocation = CurrentLocation


def load_checkpoint(CurrentLocation):  # loads last saved checkpoint after loosing a game
    Player.health = saveHealth
    Player.mana = saveMana
    Player.exp = saveExp
    Player.inventory = saveInventory
    CurrentLocation = saveLocation