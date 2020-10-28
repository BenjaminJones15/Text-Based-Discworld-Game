class_wizard = {            #dictionary of the wizard class's statistics.
    #Low physical damage, high magical damage, medium health points, high mana, inventory contains 2 mana potions
    "name": "wizard",
    "health": 100,
    "mana": 100,
    "strength": 14,
    "description": "The wizard  deals high magic damage, with a high amount of mana. Beware, as the wizard has a lower amount of health.\n Starts with 2 mana pies"
    
}

class_warrior = {           #dictionary of the warrior class's statistics 
    #Medium physical damage, low magical damage, medium health points, medium mana, inventory contains 1 mana 1 hp potions
    "name": "warrior",
    "health": 130,
    "mana": 70,
    "strength": 20,
    "description": "The warrior deals medium amounts of damage, and has a fairly high amount of health.\n Starts with 1 mana and 1 health pie."
    
}

class_undead = {           #dictionary of the warrior class's statistics.
    #Medium physical damage, high health points, low mana, inventory contains 2 strength potions
    "name": "undead",
    "health": 150,
    "mana": 50,
    "strength": 16,
    "description": "The undead compensates for his smaller mana pool for a very amount high of health.\n Starts with 2 strength pies."

}

class_computer = {      #easter egg character class. will make it fairly challenging to defeat the game. dictionary of the computer scientist's class's statistics.
    #medium physical damage, low health points, low mana, no potions
    "name": "computer",
    "health": 80,
    "mana": 20,
    "strength": 10,
    "description": ""       #no description to prevent it from showing up in the list of classes.
}

Classes = {             #dictionary of the different character classes.
    "wizard": class_wizard,
    "warrior": class_warrior,
    "undead": class_undead,
    "computer": class_computer
}