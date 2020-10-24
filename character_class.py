class_wizard = {
    # Low phys dmg, high mag dmg, med hp, high mana, 2 mana potions
    "name": "Wizard",
    "health": 100,
    "mana": 100,
    "strength": 15,
    "description": "The wizard  deals high magic damage, with a high amount of mana. Beware, as the wizard has a lower amount of health.\n Starts with 2 mana pies"
    
}

class_warrior = {
    # Med phys dmg, low mag dmg, med hp, med mana, 1 mana 1 hp potions
    "name": "Warrior",
    "health": 130,
    "mana": 70,
    "strength": 12,
    "description": "The warrior deals medium amounts of damage, and has a fairly high amount of health.\n Starts with 1 mana and 1 health pie."
    
}

class_undead = {
    # Med dmg, high hp, low mana, 2 strength potions (when added)
    "name": "Undead",
    "health": 150,
    "mana": 50,
    "strength": 10,
    "description": "The undead compensates for his smaller mana pool for a very amount high of health.\n Starts with 2 strength pies."

}

Classes = {
    "Wizard": class_wizard,
    "Warrior": class_warrior,
    "Undead": class_undead
}

#Change to a class instead?
'''
class Character(object):
        def _init_(self, name, health, mana, strength, description):
            self.name = name
            self.health = health
            self.mana = mana
            self.strength = strength
            self.description = description

ClassList = ["Wizard", "Warrior", "Undead"]

Wizard = Character
Wizard.name = "Wizard"
Wizard.health = 100
Wizard.strength = 15
Wizard.mana = 100
Wizard.description = "The wizard  deals high magic damage, with a high amount of mana. Beware, as the wizard has a lower amount of health.\n Starts with 2 mana pies"

Warrior = Character
Warrior.name = "Warrior"
Warrior.health = 130
Warrior.strength = 12
Warrior.mana = 70
Warrior.description = "The warrior deals medium amounts of damage, and has a fairly high amount of health.\n Starts with 1 mana and 1 health pie"

Undead = Character
Undead.name = "Undead"
Undead.health = 150
Undead.strength = 10
Undead.mana = 50
Undead.description = "The undead compensates for his smaller mana pool for a very amount high of health.\n Starts with 2 strength pies."
'''