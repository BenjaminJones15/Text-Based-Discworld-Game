# just need to connect the checkpoints to finish
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
    choice = normalise_input(choice)  # uses the function from normalise.py
    return choice


def execute_attack():  # deals damage to the enemy
    enemy.health = enemy.health - random.randrange(Player.strength / 2, Player.strength, 1)
    # takes a random number based on strength to attack
    print("The enemy lost " + Player.strength + " health")
    global strength_check  # used to check if a strength potion has been used
    if strength_check:
        Player.strength = Player.strength/3
        strength_check = False


def execute_mana():  # mana is set damage and shows your mana falling
    enemy.health = enemy.health - 20
    Player.mana = Player.mana - 20
    print("The enemy lost 20 health")
    print("You used up 20 mana")


def execute_item():  # brings up a item selection menu
    print("What item do you want to use: ")
    for i in inventory:  # prints items in your inventory
        print(i)
    item = normalise_input(input("> "))
    if item == "hp pie":
        if inventory["HP Pie"] == 0:
            print("You do not have enough HP Pies")
        else:
            Player.health = Player.health + 50
            if Player.health > Player.maxHealth:  # checks to see health doesn't go over the max
                Player.health = Player.maxHealth
            inventory["HP Pie"] -= 1
    elif item == "mana pie":
        if inventory["Mana Pie"] == 0:
            print("You do not have enough Mana Pies")
        else:
            Player.mana = Player.mana + 50
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


def execute_inspect():  # views the enemies stats
    print(enemy.description)
    print("The enemy has " + enemy.health)
    print("Enemy strength " + enemy.strength)
    print("Enemy magic " + enemy.magic)


def execute_run():  # try to run from the fight
    if Location.boss:  # checks if the fight is a boss battle
        if enemy.name == "Jonathan":  # easter egg with the first boss
            print("Really?")
            game_over()
        else:  # not allowed to run from a boss fight
            print("You can't run from this battle")
    else:
        run = random.randrange(1, 2, 1)  # random chance to run from the battle
        if run == 1:
            Player.health = Player.health - 10  # still take damage for running away
            health_check()
            global battle
            battle = False
            print("You ran away!")
        else:
            print("You couldn't get away")


def execute_battle_choice(choice):  # used to pick which battle action should occur
    if choice == "attack":
        execute_attack()
    elif choice == "mana":
        if Player.mana >= 20:  # see's if the player has enough mana to use a spell
            execute_mana()
        else:
            print("Not enough mana")
    elif choice == "items":
        execute_item()
    elif choice == "inspects":
        execute_inspect()
    elif choice == "run":
        execute_run()
    else:
        print("Incorrect command")  # used to make sure the user knows they entered the wrong value


def enemy_health_check():  # checks the enemy's health each turn to see if the battle has ended
    if enemy.health <= 0:
        print("you win.")
        battle = False
        if Location.boss:  # if it is a boss fight it drops set items
            inventory["Money"] += 100
            inventory["Key Piece"] += 1
            Player.exp = Player.exp + 100  # level up after a fight
            save_checkpoint()  # saves the players progress after beating a boss
        else:  # otherwise a random amount of gold and exp
            drop = random.randrange(0, 5, 1)
            inventory["Money"] += drop
            ex = random.randrange(enemy.exp / 2, enemy.exp, 1)  # random amount of experience after regular fights
            Player.exp = Player.exp + ex


def enemy_attack():
    attack = random.randrange(1, 3, 1)   # randomly decides what attack enemies should use
    if attack == 3:
        print(enemy.name + " uses magic")
        print("You took " + enemy.magic + " damage")
        Player.health = Player.health - enemy.magic
    else:  # enemies are more likely to attack than use magic
        print(enemy.name + " attacks")
        print("You took " + enemy.strength + " damage")
        Player.health = Player.health - enemy.strength


def health_check():  # checks the players health each turn to check they haven't died
    if Player.health <= 0:  # if they have it does the game over screen
        game_over()
 

def exp_check():  # checks to see if the player should level up
    if Player.exp >= 100:
        Player.health = Player.maxHealth
        Player.mana = Player.maxMana
        Player. exp = 0


def game_over():  # game over screen asking if they wish to continue
    print("You lose")
    time.sleep(10)  # time to reflect on loosing
    print()
    print("Do you wish to continue? yes/no")  # option to continue
    choice = normalise_input(input())
    if choice == "yes":  # if yes it loads a checkpoint otherwise the game quits
        load_checkpoint()
    else:
        quit()


def start_battle():  # how the battle will be carried out each turn
    global strength_check
    strength_check = False
    print(enemy.name + " has appeared")  # gets enemy name from what was called in the random encounter
    while battle:
        print("Your turn")  # with your turn is occurring
        options = print_battle()
        execute_battle_choice(options)
        enemy_health_check()
        print("Enemy's turn")  # and then the enemies
        time.sleep(2)
        enemy_attack()
        health_check()

