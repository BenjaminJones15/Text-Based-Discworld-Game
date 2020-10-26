# Contain items and amount of them
# This dictionary is not currently being used
Health_Pie = {
    "name": "Health Pie",
    "amount": 0,
    "Description": "A pie that refills part of your health bar"}

Mana_Pie = {
    "name": "Mana Pie",
    "amount": 0,
    "description": "A pie that refills part of your mana bar"}

Strength_Pie = {
    "name": "Strength Pie",
    "amount": 0,
    "description": "A pie that temporarily increases your strength"}


inventory = {  # User inventory. Starts empty
    "Health Pie": 0,
    "Mana Pie": 0,
    "Strength Pie": 0,
    "Money": 0,
    "Key Piece": 0,
    "Arms": 0,
    "Swamp Dragons": 0
}

'''    #possible use if each item became an object.
class Item(object):
    def _init_(self, id, name, description, amount):
        self.id = id
        self.name = name
        self.description = description
        self.amount = amount

Strength_Pie = Item
Strength_Pie.id = "strength"
Strength_Pie.name = "Strength Pie"
Strength_Pie.description = "A pie that refills part of your health bar"
Strength_Pie.amount = 0  '''



