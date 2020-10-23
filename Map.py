class Location(object):
    def _init_(self, name, NPC, exits, POI, boss):
        self.name = name     #name of the location
        self.NPC = NPC       #list of all NPCs in that location
        self.exits = exits   #dictionary of exits from the location
        self.POI = POI       #list of things to do around the location
        self.boss = boss     #boolean variable, if boss battle happens = True


Pseudopolis_Yard = Location
Pseudopolis_Yard.name = "Pseudopolis Yard"
Pseudopolis_Yard.NPC = ["Fred Colon", "Nobby Nobs"]
Pseudopolis_Yard.exits = {}

