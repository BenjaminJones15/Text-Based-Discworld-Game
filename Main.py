from boss import *
from combat import *
from enemies import *
from Map import *
from normalise import *
import random

CurrentLocation = Pseudopolis_Yard_Inside

def main():
    print()

    #commenting

def RndEncounter(location):
    if location.name == "The Library":
        print_battle(ShadowingLemma)
    elif location.name == "The Shades":
        print_battle(Mugger)
    else:
        EnChance = random.randint(0,1)
        if EnChance == 0:
            return()
        else:
            print_battle()


