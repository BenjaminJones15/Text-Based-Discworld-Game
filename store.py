from threading import Timer
import time, sys
from inventory import *

def store():
    openStore = True
    print("CMOT Dibbler: 'Welcome to my store'")
    print("-----------------------------------")
    print("CMOT Dibbler: 'I'll sell it for less, and that's cutting me own throat.'")
    print("1.) Health Pie 5 AM$")
    print("2.) Mana Pie 20 AM$")
    print("3.) Strength Pie 12 AM$")
    print()
    print("x.) Exit Store")

    options = ["1", "2", "3", "x"]

    timeframe = 500

    t = Timer(
        timeframe,
        print,
        [
            "\n CMOT Dibbler: '… when you sell sausages you don’t just hang around waiting for people to want sausage,"
            "\n you go out there and make them hungry. And you put mustard on ‘em.' \n \n Please choose an option..."
            "\n>"
        ],
    )
    t.start()
    while openStore:
        optioncmot = input(">")
        t.cancel()

        if optioncmot == "1":
            if inventory["money"] < 5:
                print("you can't afford that")
            else:
                print("You have bought a health pie for 5 AM$")
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

        if str(optioncmot).lower() == "x":
            openStore = False

        if optioncmot not in options:
            print("Invalid input")

        
