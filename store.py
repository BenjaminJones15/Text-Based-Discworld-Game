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

    wallet = 0
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
    while openStore:
        t.start()
        optioncmot = input(">")
        t.cancel()

        if optioncmot == "1":
            print("You have bought a health pie for 5 AM$")
            wallet = wallet - 5
            inventory["health pie"] += 1
            print("Do you want to buy anything else?")

        if optioncmot == "2":
            print("You have bought a mana pie for 20 AM$")
            wallet = wallet - 20
            inventory["mana pie"] += 1
            print("Do you want to buy anything else?")

        if optioncmot == "3":
            print("You have bought a strength pie for 12 AM$")
            wallet = wallet - 12
            inventory["strength pie"] += 1
            print("Do you want to buy anything else?")

        if optioncmot.lower == "x":
            openStore = False

        if optioncmot not in options:
            print("Invalid input")

        
