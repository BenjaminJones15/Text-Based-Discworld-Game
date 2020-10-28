from threading import Timer
import time, sys
from inventory import *

def store():
    openStore = True  # store check for the while loop
    print("CMOT Dibbler: 'Welcome to my store'")
    print("-----------------------------------")
    print("CMOT Dibbler: 'I'll sell it for less, and that's cutting me own throat.'")
    print("1.) Health Pie 5 AM$")
    print("2.) Mana Pie 20 AM$")
    print("3.) Strength Pie 12 AM$")
    print()
    print("x.) Exit Store")

    options = ["1", "2", "3", "x"]  # prints out the options you can select

    timeframe = 60  # time frame used for easter egg

    t = Timer(
        timeframe,
        print, # custom print message appears
        [
            "\n CMOT Dibbler: '… when you sell sausages you don’t just hang around waiting for people to want sausage,"
            "\n you go out there and make them hungry. And you put mustard on ‘em.' \n \n Please choose an option..."
            "\n>"
        ],
    )
    t.start()
    while openStore:  # loop for continuing to buy things
        print("you have " + inventory["money"] + " AM$")  # prints how much money you have left each loop
        optioncmot = input(">")
        t.cancel()

        if optioncmot == "1":
            if inventory["money"] < 5:  # if you can't afford it, it throws this message
                print("you can't afford that")
            else:
                print("You have bought a health pie for 5 AM$")  # otherwise you buy it and add it to the inventory
                inventory["money"] -= 5
                inventory["health pie"] += 1
                print("Do you want to buy anything else?")

        if optioncmot == "2":
            if inventory["money"] < 20:
                print("you can't afford that")
            else:
                print("You have bought a mana pie for 20 AM$")
                inventory["money"] -= 20
                inventory["mana pie"] += 1
                print("Do you want to buy anything else?")

        if optioncmot == "3":
            if inventory["money"] < 12:
                print("you can't afford that")
            else:
                print("You have bought a strength pie for 12 AM$")
                inventory["money"] -= 12
                inventory["strength pie"] += 1
                print("Do you want to buy anything else?")

        if str(optioncmot).lower() == "x":  # means the player can then leave the shop
            openStore = False

        if optioncmot not in options:  # incase another command is entered
            print("Invalid input")

        
