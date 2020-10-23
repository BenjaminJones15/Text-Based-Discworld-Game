import random

def print_battle(enemy):
    print(enemy["name"] + " has appeared")
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
    return choice


def execute_attack(enemy):
    enemy.health = enemy.health - random.randrange((player.strength)/2, player.strength, 1)
    print("the enemy lost " + player.strength + " health")
    global strength_check
    if strength_check:
        player.strength = player.strength/3
        strength_check = False


def execute_mana(enemy):
    enemy.health = enemy.health - 15
    player.mana = player.mana - 20
    print("the enemy lost 15 health")
    print("you used up 20 mana")


def execute_item(player):
    print("what item do you want to use: ")
    for i in inventory:
        print(i["name"])
    item = normalise_input(input("> "))
    if item == "health potion":
        player.health = player.health + 50
        if player.health > player.MaxHealth:
            player.health = player.MaxHealth
    elif item == "mana potion":
        player.mana = player.mana + 50
        if player.mana > player.MaxMana:
            player.mana = player.MaxMana
    elif item == "strength potion":
        player.strength = player.strength*3
        global strength_check
        strength_check = True


def execute_inspect(enemy):
    print(enemy.description)
    print("the enemy has " + enemy.health)
    print("enemy strength " + enemy.description)
    print("enemy magic " + enemy.description)

def execute_run():
    run = random.randrange(1,2,1)
    if run == 1:
        global battle
        battle = False
        print("You ran away!")
    else:
        print("You couldn't get away")


def execute_battle_choice(choice):
    if choice == "attack":
        execute_attack(enemy)
    elif choice == "mana":
        if player.mana >= 20:
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
        print("incorrect command")


def health_check(enemy):
    if enemy.health <= 0:
        print("you win.")
        battle = False
        if Boss == True:
            drop = enemy.drop
            player["inventory"].append(drop)
            player["inventory"].append("key piece")
        else:
            drop = random.randrange(0,5,1)
            player["inventory"].append(drop)


def enemy_attack():
    attack = random.randrange(1, 3, 1)
    if attack == 3:
        print(enemy.name + " uses magic")
        player.health = player.health - enemy.mana
    else:
        print(enemy.name + " attacks")
        player.health = player.health - enemy.strength


def start_battle():
    global strength_check
    strength_check = False
    while battle:
        print("your turn")
        options = print_battle(enemy)
        execute_battle_choice(options)
        health_check(enemy)
        print("enemy turn")
        enemy_attack()