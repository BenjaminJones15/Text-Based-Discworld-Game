# Contain items and amount of them
# This dictionary is not currently being used
health_pie = {
    "name": "health pie",
    "amount": 0,
    "Description": "A pie that refills part of your health bar"}

mana_pie = {
    "name": "Mana Pie",
    "amount": 0,
    "description": "A pie that refills part of your mana bar"}

strength_pie = {
    "name": "Strength Pie",
    "amount": 0,
    "description": "A pie that temporarily increases your strength"}


inventory = {  # User inventory. Starts empty
    "health pie": 0,
    "mana pie": 0,
    "strength pie": 0,
    "money": 0,
    "key piece": 0,
    "arms": 0,
    "swamp dragons": 0
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



