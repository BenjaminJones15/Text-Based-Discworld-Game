# ordered enemies from weakest to strongest
class enemy(object):
    def _init_(self, name, health, strength, magic, descrption, exp):
        self.name = name  #the name of the enemy, string
        self.health = health  #how much health the enemy has, int
        self.strength = strength #how much strength the enemy has, int
        self.magic = magic  #the enemies magic stat, int
        self.description = descrption  #a description of the enemy, string
        self.exp = exp #how much experience the enemy awards you, string

#these are the common enemies
Mugger = enemy()
Mugger.name = "Mugger"
Mugger.health = 25
Mugger.strength = 8
Mugger.magic = 0
Mugger.description = ("Armed with a shiv and a licence to steal.")
Mugger.exp = 8


Gnome = enemy()
Gnome.name = "Gnome"
Gnome.health = 40
Gnome.strength = 12
Gnome.magic = 8
Gnome.description = ("Gnomes are the smallest form of humanoids")
Gnome.exp = 18


Werewolf = enemy()
Werewolf.name = "Werewolf"
Werewolf.health = 30
Werewolf.strength = 30
Werewolf.magic = 0
Werewolf.description = ("Physcially powerful and hard to kill")
Werewolf.exp = 20


SwampDragon = enemy()
SwampDragon.name = "Swamp Dragon"
SwampDragon.health = 50
SwampDragon.strength = 16
SwampDragon.magic = 20
SwampDragon.description = ("Will eat and drink anything that can be used as fuel for fire-breathing")
SwampDragon.exp = 24


ShadowingLemma = enemy()
ShadowingLemma.name = "Shadowing Lemma"
ShadowingLemma.health = 60
ShadowingLemma.strength = 8
ShadowingLemma.magic = 28
ShadowingLemma.description = ("A curious creature that exists in only two dimensions, and eats mathematicians.")
ShadowingLemma.exp = 28


Basilisk = enemy()
Basilisk.name = "Basilisk"
Basilisk.health = 80
Basilisk.strength = 16
Basilisk.magic = 24
Basilisk.description = ("Powerful and giant snake whose gaze can kill")
Basilisk.exp = 36


Chimera = enemy()
Chimera.name = "Chimera"
Chimera.health = 50
Chimera.strength = 22
Chimera.magic = 22
Chimera.description = ("Native to Klatch, incredibly rare species")
Chimera.exp = 34

EnemyList = [Mugger, Gnome, Werewolf, SwampDragon, ShadowingLemma, Basilisk, Chimera]

# these are the bosses
Johnathan = enemy()
Johnathan.name = "Jonathan"
Johnathan.health = 100
Johnathan.strength = 5
Johnathan.magic = 0
Johnathan.description = ("Most annoying in Ankh-Morpork")


CarcerDun = enemy()
CarcerDun.name = "Carcer Dun"
CarcerDun.health = 150
CarcerDun.strength = 30
CarcerDun.magic = 10
CarcerDun.description = ("Stone-cold killer")


Gitlab = enemy()
Gitlab.name = "Gitlab"
Gitlab.health = 250
Gitlab.strength = 25
Gitlab.magic = 28
Gitlab.description = ("A quasi-demonic entity from the Dungeon Dimensions")


MrGryle = enemy()
MrGryle.name = "Mr Gryle"
MrGryle.health = 200
MrGryle.strength = 20
MrGryle.magic = 40
MrGryle.description = ("Powerful Banshee")


Kirill = enemy()
Kirill.name = "Kirill"
Kirill.health = 400
Kirill.strength = 30
Kirill.magic = 49
Kirill.description = ("Biggest badass in Ankh-Morpork")