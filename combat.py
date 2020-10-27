from normalise import *
from Map import *
from Player import *
from enemies import *
import random
import time

NewLocation = Pseudopolis_Yard_Reception
Restart = False

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
    choice = normalise_input(choice)
    choice = "".join(choice)
    return choice


def execute_attack(CurEnemy, player):  # deals damage to the enemy
    ran = random.randint(player.strength / 2, player.strength)
    CurEnemy.health = CurEnemy.health - ran
    # takes a random number based on strength to attack
    print("The enemy lost " + str(ran) + " health")
    global strength_check  # used to check if a strength potion has been used
    if strength_check:
        player.strength = player.strength/3
        strength_check = False


def execute_mana(CurEnemy, player):  # mana is set damage and shows your mana falling
    CurEnemy.health = CurEnemy.health - 20
    player.mana = player.mana - 20
    print("The enemy lost 20 health")
    print("You used up 20 mana")


def execute_item(player):  # brings up a item selection menu
    print("What item do you want to use: ")
    for i in player.inventory:  # prints items in your inventory
        print(i, inventory[i])
    item = " ".join(normalise_input(input("> ")))
    if item == "health pie":
        if inventory["health pie"] == 0:
            print("You do not have enough Health Pies")
        else:
            player.health = player.health + 50            
            player.maxHealth = player.maxHealth            
            if player.health > player.maxHealth:  # checks to see health doesn't go over the max
                player.health = player.maxHealth
            inventory["health pie"] -= 1
    elif item == "mana pie":
        if inventory["mana pie"] == 0:
            print("You do not have enough Mana Pies")
        else:
            player.mana = player.mana + 50
            player.maxMana = player.maxMana
            if player.mana > player.maxMana:  # checks to see mana doesn't go over the max
                player.mana = player.maxMana
            inventory["mana pie"] -= 1
    elif item == "strength pie":
        if inventory["strength pie"] == 0:
            print("You do not have enough Strength Pies")
        else:
            global strength_check
            if strength_check:
                print("You've already taken a strength pie")
            else:
                player.strength = player.strength*3  # increases the players strength for one turn
                strength_check = True  # check used to turn it back the next attack
                inventory["strength pie"] -= 1
    else:  # incase the user try's to select another item
        print("Please select a pie")


def execute_inspect(CurEnemy):  # views the enemies stats
    print(CurEnemy.description)
    print("The enemy has " + str(CurEnemy.health) + " health")
    print("Enemy strength " + str(CurEnemy.strength))
    print("Enemy magic " + str(CurEnemy.magic))


def execute_run(CurrentLocation, CurEnemy, player):  # try to run from the fight
    if CurrentLocation.boss:  # checks if the fight is a boss battle
        if CurEnemy.name == "Jonathan":  # easter egg with the first boss
            print("Really?")
            time.sleep(1)
            game_over(player)  #nice touch
        else:  # not allowed to run from a boss fight
            print("You can't run from this battle")
    else:
        run = random.randint(1, 2)  # random chance to run from the battle
        if run == 1:
            player.health = player.health - 10  # still take damage for running away
            health_check(player)
            global battle
            battle = False
            print("You ran away!")               #######################################################
        else:
            print("You couldn't get away")


def execute_battle_choice(choice, CurrentLocation, CurEnemy, player):  # used to pick which battle action should occur
    if choice == "attack":
        execute_attack(CurEnemy, player)
    elif choice == "mana":
        if player.mana >= 20:  # see's if the player has enough mana to use a spell
            player
            execute_mana(CurEnemy, player)
        else:
            print("Not enough mana")
    elif choice == "items":
        execute_item(player)
    elif choice == "inspect":
        execute_inspect(CurEnemy)
    elif choice == "run":
        execute_run(CurrentLocation, CurEnemy, player)
    else:
        print("Incorrect command")  # used to make sure the user knows they entered the wrong value


def enemy_health_check(CurrentLocation, CurEnemy, player):  # checks the enemy's health each turn to see if the battle has ended
    if CurEnemy.health <= 0:
        print("you win.")
        global battle
        battle = False
        if CurrentLocation.boss:  # if it is a boss fight it drops set items
            if CurEnemy.name == "Kirill":
                you_win()
            else:
                inventory["Money"] += 100
                inventory["Key Piece"] += 1
                print("You picked up a key piece")
                player.exp = player.exp + 100  # level up after a fight
                CurrentLocation.boss = False
                save_checkpoint(CurrentLocation, player)  # saves the players progress after beating a boss
        else:  # otherwise a random amount of gold and exp
            drop = random.randint(0, 5)
            inventory["Money"] += drop
            ex = random.randint(CurEnemy.exp / 2, CurEnemy.exp)  # random amount of experience after regular fights
            player.exp = player.exp + ex
    print()


def you_win():
    print("""
▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄  
█       █  █ █  █       █  █       █  █  █ █      █ 
█▄     ▄█  █▄█  █    ▄▄▄█  █    ▄▄▄█   █▄█ █  ▄    █
  █   █ █       █   █▄▄▄   █   █▄▄▄█       █ █ █   █
  █   █ █   ▄   █    ▄▄▄█  █    ▄▄▄█  ▄    █ █▄█   █
  █   █ █  █ █  █   █▄▄▄   █   █▄▄▄█ █ █   █       █
  █▄▄▄█ █▄▄█ █▄▄█▄▄▄▄▄▄▄█  █▄▄▄▄▄▄▄█▄█  █▄▄█▄▄▄▄▄▄█ 

Made By:
----------------
Benjamin Jones
Cameron Bethell
Jamie Groom
Roshan Roy
Will Simkins
Will Shepherd
    """)
    time.sleep(20)
    quit()

def enemy_attack(CurEnemy, player):
    attack = random.randint(1, 3)   # randomly decides what attack enemies should use
    if attack == 3:
        print(CurEnemy.name + " uses magic")
        print("You took " + str(CurEnemy.magic) + " damage")
        player.health = player.health - CurEnemy.magic
    else:  # enemies are more likely to attack than use magic
        print(CurEnemy.name + " attacks")
        print("You took " + str(CurEnemy.strength) + " damage")
        player.health = player.health - CurEnemy.strength
    print()


def health_check(player):  # checks the player's health each turn to check they haven't died
    if player.health <= 0:  # if they have it does the game over screen
        game_over(player)
 

def exp_check():  # checks to see if the player should level up    
    if player.exp >= 100:
        player.health = player.maxHealth
        player.mana = player.maxMana
        player. exp = 0

def game_over(player):  # game over screen asking if they wish to continue
    global battle
    global Restart
    battle = False
    print("You lose")
    time.sleep(3)  # time to reflect on losing
    print()
    print("Do you wish to continue? yes/no")  # option to continue
    choice = "".join(normalise_input(input()))
    if choice == "no":  # if yes it loads a checkpoint otherwise the game quits
        quit()
    else:
        load_checkpoint(player) 
        Restart = True

def start_battle(CurrentLocation, CurEnemy, player):  # how the battle will be carried out each turn
    global strength_check
    global battle
    global Restart 
    battle = True
    strength_check = False
    print(CurEnemy.name + " has appeared")  # gets enemy name from what was called in the random encounter
    while battle == True:               
        print("Your turn")  # with your turn is occurring
        print()
        options = print_battle()
        execute_battle_choice(options, CurrentLocation, CurEnemy, player)
        enemy_health_check(CurrentLocation, CurEnemy, player)
        if Restart == True:
            Restart = False
            battle = False
            return NewLocation
        if battle == False:            
            return CurrentLocation
        print("Enemy's turn")  # and then the enemies
        print()
        time.sleep(2)
        enemy_attack(CurEnemy, player)
        health_check(player)
        if Restart == True:
            Restart = False
            battle = False
            return NewLocation
    return CurrentLocation

def save_checkpoint(CurrentLocation, player):  # saves all the players stats after reaching a checkpoint
    global saveHealth, saveMana, saveExp, saveInventory, saveLocation
    # global used so that the variables can be accessed in other functions e.g. load_checkpoint
    saveHealth = player.health
    saveMana = player.mana
    saveExp = player.exp
    saveInventory = player.inventory
    saveLocation = CurrentLocation

def load_checkpoint(player):  # loads last saved checkpoint after losing a game    
    player.health = saveHealth
    player.mana = saveMana
    player.exp = saveExp
    player.inventory = saveInventory   
    global NewLocation
    NewLocation = saveLocation