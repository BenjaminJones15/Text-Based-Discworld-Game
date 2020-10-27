from pies import *
from threading import Timer
import time, sys


def store():
    print("CMOT Dibbler: 'Welcome to my store'")
    print("-----------------------------------")
    print("CMOT Dibbler: 'I'll sell it for less, and that's cutting me own throat.'")
    print("1.) Health Pie 5 AM$")
    print("2.) Mana Pie 20 AM$")
    print("3.) Strength Pie 12 AM$")
    print()
    print("X.) Exit Store")

    inventory = ""
    wallet = 0
    global pies

    timeframe = 500

    t = Timer(
        timeframe,
        print,
        [
            "\n CMOT Dibbler: '… when you sell sausages you don’t just hang around waiting for people to want sausage,"
            "\n you go out there and make them hungry. And you put mustard on ‘em.' \nPress ENTER to display menu..."
        ],
    )
    t.start()
    optioncmot = input(">")
    t.cancel()
    ## if no input after 500 seconds
    if optioncmot == "1":
        print("You have bought a health pie for 5 AM$")
        wallet = wallet - 5
        for items in inventory:
            Health_Pie = inventory["Health_Pie"]
            inventory.append(Health_Pie)

    if optioncmot == "2":
        print("You have bought a mana pie for 20 AM$")
        wallet = wallet - 20
        for items in inventory:
            Mana_Pie = inventory["Mana_Pie"]
            inventory.append(Mana_Pie)

    if optioncmot == "3":
        print("You have bought a strength pie for 12 AM$")
        wallet = wallet - 12
        for items in inventory:
            Strength_Pie = inventory["Strength_Pie"]
            inventory.append(Strength_Pie)

    if optioncmot == "":
        store()

    else:
        print("That item does not exist")


store()
