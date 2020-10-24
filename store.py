from pies import *

def store():
    print("CMOT Dibbler: 'Welcome to my store'")
    print("-----------------------------------")
    print("CMOT Dibbler: 'I'll sell it for less, and that's cutting me own throat.'")
    print("1.) Health Pie 5 AM$")
    print("2.) Mana Pie 20 AM$")
    print("3.) Strength Pie 12 AM$")
    print()
    print("X.) Exit Store")
    
    inventory=""
    wallet=0
    global pies
    
    optioncmot = input('>')
    
    if optioncmot == "1":
            print("You have bought a health pie for 5 AM$")
            wallet = wallet-5
            for items in inventory:
                healthpie=inventory["healthpie"]
                inventory.append(healthpie)

    if optioncmot == "2":
            print("You have bought a mana pie for 20 AM$")
            wallet = wallet-20
            for items in inventory:
                manapie=inventory["manapie"]
                inventory.append(manapie)

    if optioncmot == "3":
            print("You have bought a strength pie for 12 AM$")
            wallet = wallet-12
            for items in inventory:
                manapie=inventory["strengthpie"]
                inventory.append(strenthpie)

    else:
            print("That item does not exist")
        
    

store()
