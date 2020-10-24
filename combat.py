# need to know how inventory dictionary and player class are formed
# need to know what information is being sent when the random encounter occurs
# need to know python files to import from
from normalise import *
from Map import *
import random
import time


def print_battle(enemy):
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


def execute_attack(enemy):
    enemy.health = enemy.health - random.randrange(player.strength / 2, player.strength, 1)
    # takes a random number based on strength to attack
    print("the enemy lost " + player.strength + " health")
    global strength_check  # used to check if a strength potion has been used
    if strength_check:
        player.strength = player.strength/3
        strength_check = False


def execute_mana(enemy):  # mana is set damage and shows your mana falling
    enemy.health = enemy.health - 15
    player.mana = player.mana - 20
    print("the enemy lost 15 health")
    print("you used up 20 mana")


def execute_item(player):
    print("what item do you want to use: ")
    for i in inventory:  # prints items in your inventory
        print(i)
    item = normalise_input(input("> "))
    if item == "health pie":
        player.health = player.health + 50
        if player.health > player.MaxHealth:  # checks to see health doesn't go over the max
            player.health = player.MaxHealth
        inventory.remove("health pie")
    elif item == "mana pie":
        player.mana = player.mana + 50
        if player.mana > player.MaxMana:  # checks to see mana doesn't go over the max
            player.mana = player.MaxMana
        inventory.remove("mana pie")
    elif item == "strength pie":
        player.strength = player.strength*3  # increases the players strength for one turn
        global strength_check
        strength_check = True  # check used to turn it back the next attack
        inventory.remove("strength pie")


def execute_inspect(enemy):
    print(enemy.description)
    print("the enemy has " + enemy.health)
    print("enemy strength " + enemy.description)
    print("enemy magic " + enemy.description)


def execute_run():
    if Location.boss:  # checks if the fight is a boss battle
        if enemy.name == "Jonathan":  # easter egg with the first boss
            print("Really?")
            game_over()
        else:  # not allowed to run from a boss fight
            print("you can't run from this battle")
    else:
        run = random.randrange(1, 2, 1)  # random chance to run from the battle
        if run == 1:
            player.health = player.health - 10  # still take damage for running away
            health_check(player)
            global battle
            battle = False
            print("You ran away!")
        else:
            print("You couldn't get away")


def execute_battle_choice(choice):  # used to pick which battle action should occur
    if choice == "attack":
        execute_attack(enemy)
    elif choice == "mana":
        if player.mana >= 20:  # see's if the player has enough mana to use a spell
            execute_mana(enemy)
        else:
            print("not enough mana")
    elif choice == "items":
        execute_item(player)
    elif choice == "inspects":
        execute_inspect(enemy)
    elif choice == "run":
        execute_run()
    else:
        print("incorrect command")  # used to make sure the user knows they entered the wrong value


def enemy_health_check(enemy):  # checks the enemy's health each turn to see if the battle has ended
    if enemy.health <= 0:
        print("you win.")
        battle = False
        if Location.boss:  # if it is a boss fight it drops set items
            drop = enemy.drop
            player.inventory.append(drop)
            player.inventory.append("key piece")
            player.exp = player.exp + 100  # level up after a fight

        else:  # otherwise a random amount of gold
            drop = random.randrange(0, 5, 1)
            player.inventory.append(drop)
            ex = random.randrange(enemy.exp /2, enemy.exp, 1)  # random amount of experience after regular fights
            player.exp = player.exp + ex


def enemy_attack():
    attack = random.randrange(1, 3, 1)   # randomly decides what attack enemies should use
    if attack == 3:
        print(enemy.name + " uses magic")
        print("you took " + enemy.mana + " damage")
        player.health = player.health - enemy.mana
    else:  # enemies are more likely to attack than use magic
        print(enemy.name + " attacks")
        print("you took " + enemy.strength + " damage")
        player.health = player.health - enemy.strength


def health_check(player):  # checks the players health each turn to check they haven't died
    if player.health <= 0:
        game_over()


def exp_check():
    if player.exp >= 100:
        player.health = player.MaxHealth
        player.mana = player.MaxMana
        player. exp = 0


def game_over():  # game over screen asking if they wish to continue
    print("You lose")
    time.sleep(10)
    print()
    print("Do you wish to continue? yes/no")
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
        print("your turn")  # with your turn occuring
        options = print_battle(enemy)
        execute_battle_choice(options)
        enemy_health_check(enemy)
        print("enemy turn")  # and then the enemies
        time.sleep(2)
        enemy_attack()
        health_check(player)  # checks player health at the end of each turn

