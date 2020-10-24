# ordered enemies from weakest to strongest
class enemy(object):
    def _init_(self, name, health, strength, magic, descrption, exp):
        self.name = name  #
        self.health = health  #
        self.strength = strength #
        self.magic = magic  #
        self.description = descrption  #
        self.exp = exp #


Mugger = enemy
Mugger.name = "Mugger"
Mugger.health = 25
Mugger.strength = 8
Mugger.magic = 0
Mugger.description = ("Armed with a shiv and a licence to steal.")
Mugger.exp = 8


Gnome = enemy
Gnome.name = "Gnome"
Gnome.health = 40
Gnome.strength = 12
Gnome.magic = 10
Gnome.description = ("Gnomes are the smallest form of humanoids")
Gnome.exp = 18


Werewolf = enemy
Werewolf.name = "Werewolf"
Werewolf.health = 30
Werewolf.strength = 30
Werewolf.magic = 0
Werewolf.description = ("Physcially powerful and hard to kill")
Werewolf.exp = 20


SwampDragon = enemy
SwampDragon.name = "Swamp Dragon"
SwampDragon.health = 100
SwampDragon.strength = 14
SwampDragon.magic = 20
SwampDragon.description = ("Will eat and drink anything that can be used as fuel for fire-breathing")
SwampDragon.exp = 25


ShadowingLemma = enemy
ShadowingLemma.name = "Shadowing Lemma"
ShadowingLemma.health = 50
ShadowingLemma.strength = 14
ShadowingLemma.magic = 28
ShadowingLemma.description = ("A curious creature that exists in only two dimensions, and eats mathematicians.")
ShadowingLemma.exp = 28


Basilisk = enemy
Basilisk.name = "Basilisk"
Basilisk.health = 80
Basilisk.strength = 24
Basilisk.magic = 28
Basilisk.description = ("Powerful and giant snake")
Basilisk.exp = 36


Chimera = enemy
Chimera.name = "Chimera"
Chimera.health = 70
Chimera.strength = 25
Chimera.magic = 25
Chimera.description = ("Native to Klatch, incredibly rare species")
Chimera.exp = 40


# these are the bosses
Johnathan = enemy
Johnathan.name = "Johnathan"
Johnathan.health = 100
Johnathan.strength = 5
Johnathan.magic = 0
Johnathan.description = ("Most annoying in Ankh-Morpork")


CarcerDun = enemy
CarcerDun.name = "Carcer Dun"
CarcerDun.health = 150
CarcerDun.strength = 40
CarcerDun.magic = 20
CarcerDun.description = ("Stone-cold killer")


Gitlab = enemy
Gitlab.name = "Gitlab"
Gitlab.health = 250
Gitlab.strength = 30
Gitlab.magic = 35
Gitlab.description = ("Why do we even use this?")


MrGryle = enemy
MrGryle.name = "Mr Gryle"
MrGryle.health = 200
MrGryle.strength = 20
MrGryle.magic = 60
MrGryle.description = ("Powerful Banshee")


Kiril = enemy
Kiril.name = "Kirill"
Kiril.health = 400
Kiril.strength = 35
Kiril.magic = 50
Kiril.description = ("Biggest badass in Ankh-Morpork")