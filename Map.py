class Location(object):
    def _init_(self, name, description, NPC, exits, Items, POI, boss, sprite):
        self.name = name     #name of the location
        self.description = description    #description of the location
        self.NPC = NPC       #list of all NPCs in that location
        self.exits = exits   #dictionary of exits from the location
        self.POI = POI       #list of things to do around the location
        self.items = Items   #list of items around the location
        self.boss = boss     #boolean variable, if boss battle happens = True
        self.sprite = sprite #boolean variable, if sprite can spawn here = True


Pseudopolis_Yard_Inside = Location
Pseudopolis_Yard_Inside.name = "The Inside of Pseudopolis Yard Watch house"
Pseudopolis_Yard_Inside.description = ""  #insert roshan here
Pseudopolis_Yard_Inside.NPC = ["Fred Colon", "Nobby Nobs"]
Pseudopolis_Yard_Inside.exits = {"upstairs":"Locker Room", "outside": "Outside the watch house"}
Pseudopolis_Yard_Inside.POI = {"Talk to Fred and Nobby": '''insert dialogue var here'''}
Pseudopolis_Yard_Inside.Items = []
Pseudopolis_Yard_Inside.boss = False
Pseudopolis_Yard_Inside.sprite = False

Pseudopolis_Yard_Upstairs = Location
Pseudopolis_Yard_Upstairs.name = "The locker room of the watch house"
Pseudopolis_Yard_Upstairs.description = ""  #insert roshan here
Pseudopolis_Yard_Upstairs.NPC = []
Pseudopolis_Yard_Upstairs.exits = {"downstairs":"Watch House Reception"}
Pseudopolis_Yard_Upstairs.POI = {}
Pseudopolis_Yard_Upstairs.Items = []
Pseudopolis_Yard_Upstairs.boss = False
Pseudopolis_Yard_Upstairs.sprite = False

Pseudopolis_Yard_Outside = Location
Pseudopolis_Yard_Outside.name = "The outside of Pseudopolis Yard Watch house"
Pseudopolis_Yard_Outside.description = ""  #insert roshan here
Pseudopolis_Yard_Outside.NPC = ["Captain Carrot"]
Pseudopolis_Yard_Outside.exits = {"reception":"Watch House Reception", "tower of art": "The Tower of Art",
"palace": "The Palace", "gimlet's restaurant": "Gimlet the Dwarf's Delicatessen"}
Pseudopolis_Yard_Outside.POI = {"Talk to Captain Carrot.": '''insert dialogue here'''}
Pseudopolis_Yard_Outside.Items = []
Pseudopolis_Yard_Outside.boss = False
Pseudopolis_Yard_Outside.sprite = False

Tower_of_Art = Location
Tower_of_Art.name = "The Tower of Art"
Tower_of_Art.description = ""  #insert roshan here
Tower_of_Art.NPC = ["Mustrum Ridcully"]
Tower_of_Art.exits = {"pseudopolis yard":"Pseudopolis Yard", "library":"Library"}
Tower_of_Art.POI = {"Talk to Mustrum Ridcully": '''insert dialogue'''}
Tower_of_Art.Items = []
Tower_of_Art.boss = False
Tower_of_Art.sprite = True

Library = Location
Library.name = "The Library"
Library.description = ""  #insert roshan here
Library.NPC = ["Ponder Stibbons", "The Librarian"]
Library.exits = {"tower of art":"The Tower of Art", "library roof":"The Library Roof", "sator square":"Sator Square"}
Library.POI = {"Talk to Ponder and the Librarian": '''insert dialogue here'''}
Library.Items = []
Library.boss = False
Library.sprite = True

Library_Roof = Location
Library_Roof.name = "The roof of the Library"
Library_Roof.description = ""  #insert roshan here
Library_Roof.NPC = ["Sam Vimes"]
Library_Roof.exits = {"library":"Library"}
Library_Roof.POI = {}
Library_Roof.Items = []
Library_Roof.boss = True
Library_Roof.sprite = False

Sator_Square = Location
Sator_Square.name = "Sator Square"
Sator_Square.description = ""  #insert roshan here
Sator_Square.NPC = ["CMOT Dibbler"]
Sator_Square.exits = {"library":"Library", "palace":"Palace"}
Sator_Square.POI = {"Buy something from Dibbler": '''insert dialogue here? maybe'''}
Sator_Square.Items = []
Sator_Square.boss = False
Sator_Square.sprite = True

Palace_Entrance = Location
Palace_Entrance.name = "Palace Entrance"
Palace_Entrance.description = ""  #insert roshan here
Palace_Entrance.NPC = ["Vetinari"]
Palace_Entrance.exits = {"sator square":"Sator Square", "pseudopolis yard":"Pseudopolis Yard",
"post office":"Post Office"}
Palace_Entrance.POI = {"Enter the throne room to battle Kirill": '''insert dialogue here'''}
Palace_Entrance.Items = []
Palace_Entrance.boss = False
Palace_Entrance.sprite = False

Palace = Location
Palace.name = "Throne Room"
Palace.description = ""  #insert roshan here
Palace.NPC = []
Palace.exits = {"palace entrance":"Palace Entrance"}
Palace.POI = {}
Palace.Items = []
Palace.boss = True
Palace.sprite = False

Post_Office = Location
Post_Office.name = "Post Office"
Post_Office.description = ""  #insert roshan here
Post_Office.NPC = []
Post_Office.exits = {"palace entrance":"Palace Entrance", "mended drum":"The Mended Drum",
"post office basement":"Post Office Basement"}
Post_Office.POI = {}
Post_Office.Items = []
Post_Office.boss = False
Post_Office.sprite = False

Post_Office_Basement = Location
Post_Office_Basement.name = "Post Office Basement"
Post_Office_Basement.description = ""  #insert roshan here
Post_Office_Basement.NPC = ["Moist Von Lipwig"]
Post_Office_Basement.exits = {"post office":"Post Office"}
Post_Office_Basement.POI = {}
Post_Office_Basement.Items = []
Post_Office_Basement.boss = True
Post_Office_Basement.sprite = False

Mended_Drum = Location
Mended_Drum.name = "The Mended Drum"
Mended_Drum.description = ""  #insert roshan here
Mended_Drum.NPC = ["Librarian", "Conan the Barbarian"]
Mended_Drum.exits = {"post office":"Post Office", "hospital":"Lady Sybil Free Hospital",
"temple of anoia":"Temple of Anoia"}
Mended_Drum.POI = {}        #maybe?
Mended_Drum.Items = []
Mended_Drum.boss = False
Mended_Drum.sprite = True

Lady_Sybil_Free_Hospital = Location
Lady_Sybil_Free_Hospital.name = "Lady Sybil Free Hospital"
Lady_Sybil_Free_Hospital.description = ""  #insert roshan here
Lady_Sybil_Free_Hospital.NPC = ["Igor"]
Lady_Sybil_Free_Hospital.exits = {"mended drum":" The Mended Drum", "temple of anoia":"Temple of Anoia"}
Lady_Sybil_Free_Hospital.POI = {}    
Lady_Sybil_Free_Hospital.Items = []    
Lady_Sybil_Free_Hospital.boss = False
Lady_Sybil_Free_Hospital.sprite = True

Temple_of_Anoia = Location
Temple_of_Anoia.name = "Temple of Anoia"
Temple_of_Anoia.description = ""  #insert roshan here
Temple_of_Anoia.NPC = ["Prietess?"]
Temple_of_Anoia.exits = {"mended drum":"The Mended Drum", "hospital":"Lady Sybil Free Hospital",
"gimlet's restaurant":"Gimlet the Dwarf's Delicatessen", "inner temple":"Inner Shrine of Anoia"}
Temple_of_Anoia.POI = {}    
Temple_of_Anoia.Items = []    
Temple_of_Anoia.boss = False
Temple_of_Anoia.sprite = False

Temple_of_Anoia_Inner = Location
Temple_of_Anoia_Inner.name = "Inner Shrine of Anoia"
Temple_of_Anoia.description = ""  #insert roshan here
Temple_of_Anoia_Inner.NPC = []
Temple_of_Anoia_Inner.exits = {"temple of anoia":"Temple of Anoia"}
Temple_of_Anoia_Inner.POI = {}
Temple_of_Anoia_Inner.Items = []        
Temple_of_Anoia_Inner.boss = True
Temple_of_Anoia_Inner.sprite = False

Gimlets_Restaurant = Location
Gimlets_Restaurant.name = "Gimlet the Dwarf's Delicatessen"
Gimlets_Restaurant.description = ""  #insert roshan here
Gimlets_Restaurant.NPC = ["Gimlet", "Captain Carrot"]
Gimlets_Restaurant.exits = {"temple of anoia":"Temple of Anoia", "shades":"The Shades"}
Gimlets_Restaurant.POI = {}    
Gimlets_Restaurant.Items = []    
Gimlets_Restaurant.boss = False
Gimlets_Restaurant.sprite = True

The_Shades = Location
The_Shades.name = "The Shades"
The_Shades.description = ""  #insert roshan here
The_Shades.NPC = []
The_Shades.exits = {"pink pussycat club":"The Pink Pussycat Club", 
"gimlet's restaurant":"Gimlet the Dwarf's Delicatessen"}
The_Shades.POI = {}  
The_Shades.Items = []     
The_Shades.boss = False
The_Shades.sprite = True

The_Pink_Pussycat_Club = Location
The_Pink_Pussycat_Club.name = "The Pink Pussycat Club"
The_Pink_Pussycat_Club.description = ""  #insert roshan here
The_Pink_Pussycat_Club.NPC = ["Professor Flead"]
The_Pink_Pussycat_Club.exits = {"the shades":"The Shades", 
"dragon sanctuary":"The Sanctuary for Lost Dragons"}
The_Pink_Pussycat_Club.POI = {}        
The_Pink_Pussycat_Club.Items = []
The_Pink_Pussycat_Club.boss = False
The_Pink_Pussycat_Club.sprite = False

Dragon_Sanctuary = Location
Dragon_Sanctuary.name = "The Sanctuary for Lost Dragons"
Dragon_Sanctuary.description = ""  #insert roshan here
Dragon_Sanctuary.NPC = ["Lady Sybil Ramkin"]
Dragon_Sanctuary.exits = {"pseudopolis yard":"Pseudopolis Yard", "pink pussycat club":"The Pink Pussycat Club"} 
Dragon_Sanctuary.POI = ["Return dragons"]
Dragon_Sanctuary.Items = []        
Dragon_Sanctuary.boss = False
Dragon_Sanctuary.sprite = True