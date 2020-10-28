class Location(object):
    def _init_(self, name, description, exits, Items, POI, boss, sprite):
        self.name = name     #name of the location
        self.description = description    #description of the location
        self.exits = exits   #dictionary of exits from the location
        self.POI = POI       #list of things to do around the location
        self.items = Items   #list of items around the location
        self.boss = boss     #boolean variable, if boss battle happens = True
        self.sprite = sprite #boolean variable, if sprite can spawn here = True


Pseudopolis_Yard_Reception = Location()
Pseudopolis_Yard_Reception.name = "The reception of Pseudopolis Yard Watch house"
Pseudopolis_Yard_Reception.description = "You find yourself inside the cold stone walls of the Pseudopolis Yard Watch House, standing in the bustling centre of the building – the Reception. In front of you, sitting at his desk, is a pudgy Sergeant, named Fred Colon, and lounging nearby is his friend Nobby Nobs – a man of dwarf-like proportions with an uncanny ability to attract nearby small objects and loose change into his pockets."
Pseudopolis_Yard_Reception.exits = {"locker":"Locker Room", "outside": "Outside"}
Pseudopolis_Yard_Reception.POI = {"fred and nobby": '''insert dialogue var here'''}
Pseudopolis_Yard_Reception.Items = {}
Pseudopolis_Yard_Reception.boss = False
Pseudopolis_Yard_Reception.sprite = False

Pseudopolis_Yard_Upstairs = Location()
Pseudopolis_Yard_Upstairs.name = "The locker room of the watch house"
Pseudopolis_Yard_Upstairs.description = "The locker room of the Watch House contains tall standing storage cupboards – once a gleaming bronze, but now dull and dented by the grime of life. They are filled with the possessions of all the Watchmen.        *grime of life sounds wrong."
Pseudopolis_Yard_Upstairs.exits = {"reception":"Reception"}
Pseudopolis_Yard_Upstairs.POI = {}
Pseudopolis_Yard_Upstairs.Items = {}
Pseudopolis_Yard_Upstairs.boss = False
Pseudopolis_Yard_Upstairs.sprite = False

Pseudopolis_Yard_Outside = Location()
Pseudopolis_Yard_Outside.name = "The outside of Pseudopolis Yard Watch house"
Pseudopolis_Yard_Outside.description = "Following a cobbled path leads you to the headquarters of the Ankh-Morpork City Watch. The Watch primarily deal with crimes committed in front of a watch officer or otherwise reported. Hulking over you is Captain Carrot with his bulging muscles in his glistening bronze armour – you can see your own warped image peering back at you." 
Pseudopolis_Yard_Outside.exits = {"reception":"Reception", "tower": "Tower","entrance": "Entrance",
"restaurant": "Restaurant"}
Pseudopolis_Yard_Outside.POI = {"Talk to Captain Carrot.": '''insert dialogue here'''}
Pseudopolis_Yard_Outside.Items = {}
Pseudopolis_Yard_Outside.boss = False
Pseudopolis_Yard_Outside.sprite = False

Tower_of_Art = Location()
Tower_of_Art.name = "The Tower of Art"
Tower_of_Art.description = "Standing over 800 feet tall, it is completely without windows and, due to several repairs over the centuries, it has a gnarled appearance, much like an ancient tree. Wearing a jogging suit talking at a consistent shout is the current Archchancellor of Unseen Univeristy, Mustrum Ridcully, standing at the entrance of the Tower."
Tower_of_Art.exits = {"outside":"Outside", "library":"Library"}
Tower_of_Art.POI = {"Talk to Mustrum Ridcully": '''insert dialogue'''}
Tower_of_Art.Items = {}
Tower_of_Art.boss = False
Tower_of_Art.sprite = True

Library = Location()
Library.name = "The Library"
Library.description = "The endless shelves stretch into the darkness, and above, a clear glass dome provides illumination. The ancient stone building houses far more rooms and corridors than it’s outer dimensions should have allowed. You see the Librarian, once a human, and now – through an unfortunate magical accident – an orangutan, tending to his duties and a young man called Ponder Stibbons in a pointed hat and round glasses, engrossed in a dusty old tome.  *ask ponder what he’s reading?"
Library.exits = {"tower":"Tower", "roof":"Roof", "square":"Square"}
Library.POI = {"Talk to Ponder and the Librarian": '''insert dialogue here'''}
Library.Items = {}
Library.boss = False
Library.sprite = True

Library_Roof = Location()
Library_Roof.name = "The roof of the Library"
Library_Roof.description = "As you ascend to the roof, you see a dark and looming figure with a stone-cold face - Carcer Dun. He stands near the dome of the library of with a cynical grin plastered on his face, holding two knives – dried bloodstains on both."
Library_Roof.exits = {"library":"Library"}
Library_Roof.POI = {}
Library_Roof.Items = {}
Library_Roof.boss = True
Library_Roof.sprite = False

Sator_Square = Location()
Sator_Square.name = "Sator Square"
Sator_Square.description = "Walking through the rowdy marketplace, you see a wide-open public space with four fountains – each displaying a hippopotamus, the patron animal of Ankh-Morpork – spurting water. The entire scene is overlooked by the clock-tower, and all around, you see pop-up stores selling anything and everything that could be desired." 
Sator_Square.exits = {"library":"Library", "palace":"Palace"}
Sator_Square.POI = {"Buy something from Dibbler": '''insert dialogue here? maybe'''}
Sator_Square.Items = {}
Sator_Square.boss = False
Sator_Square.sprite = True

Palace_Entrance = Location()
Palace_Entrance.name = "Palace Entrance"
Palace_Entrance.description = "Standing in front of the palace entrance, you feel dwarf-like. Its architecture is like no other in the city – having been extended by multiple patricians and kings throughout the centuries. This all combines to present a building which is both staggeringly beautiful, while also providing an aura of impregnability which seems to dare you to assault it. "
Palace_Entrance.exits = {"square":"Square", "outside":"Outside", "post":"Post Office", "palace":"Palace"}
Palace_Entrance.POI = {"Enter the throne room to battle Kirill": '''insert dialogue here'''}
Palace_Entrance.Items = {"dibbler": "Oi officer, I've got everything you want and more. Come are buy some of my products. My pies are the cheapest in the market!"}
Palace_Entrance.boss = False
Palace_Entrance.sprite = False

Palace = Location()
Palace.name = "Throne Room"
Palace.description = "Entering the throne room, you see the gilded chair sitting at the end of a long room, flanked by portraits of former rulers throughout the ages. The short flight of steps leading up the throne are presently home to Lord Vetinari, the Patrician of the city – who has now found himself in chains. Standing above him is Kirill – an ambitious man who wishes to become the Patrician and thus extend his rule over the entire city."
Palace.exits = {"entrance":"Entrance"}
Palace.POI = {}
Palace.Items = {}
Palace.boss = True
Palace.sprite = False

Post_Office = Location()
Post_Office.name = "Post Office"
Post_Office.description = "Once a forgotten relic of the past, the post office has been dragged into the century of the fruit-bat by Moist von Lipwig – once a criminal and confidence trickster, now a government employee, not that there are many differences between the two. The counters gleam, and a steady buzz of activity fills the air."
Post_Office.exits = {"entrance":"Entrance", "mended":"Mended Drum", "basement":"Basement"}
Post_Office.POI = {}
Post_Office.Items = {}
Post_Office.boss = False
Post_Office.sprite = False

Post_Office_Basement = Location()
Post_Office_Basement.name = "Post Office Basement"
Post_Office_Basement.description = "The basement contains a rather notorious machine, which sorts mail. It is a creation of BS (Bloody Stupid) Johnson, the man who disapproved of pi, instead setting it equal to 3. This has led to the machine producing letters not only from the future, but indeed from alternate realities as well. A small grimy window produces the only source of illumination – spotlighting a hunched figure, the banshee Mr Gryle, who is tightly wrapped in a thick, leathery cape. "
Post_Office_Basement.exits = {"post":"Post Office"}
Post_Office_Basement.POI = {}
Post_Office_Basement.Items = {}
Post_Office_Basement.boss = True
Post_Office_Basement.sprite = False

Mended_Drum = Location()
Mended_Drum.name = "The Mended Drum"
Mended_Drum.description = "Entering the bar, you pass a lichen covered troll acting as a bouncer, and walk almost immediately into an on-going bar fight, between a wiry old man and various other patrons of the bar. After observing the carnage for a few minutes, you notice a distinct decrease in the amount of combat, mainly due to the old man’s canny ability to convince the other participants it is best to stay down rather than face him again.     #talk to cohen the barbarian, npc."
Mended_Drum.exits = {"post":"Post Office", "hospital":"Hospital",
"temple":"Temple"}
Mended_Drum.POI = {}        #maybe?
Mended_Drum.Items = {}
Mended_Drum.boss = False
Mended_Drum.sprite = True

Lady_Sybil_Free_Hospital = Location()
Lady_Sybil_Free_Hospital.name = "Lady Sybil Free Hospital"
Lady_Sybil_Free_Hospital.description = "Upon entering the reception of the hospital you are greeted by a maze of rambling hallways, with multiple signs pointing to assorted wings. The faint background of noise is provided by the sound of coughing, mixed in with the occasional scream. In one corner of the room, an Igor stands, slowly and carefully sewing his hand back onto his wrist."
Lady_Sybil_Free_Hospital.exits = {"mended":"Mended Drum", "temple":"Temple"}
Lady_Sybil_Free_Hospital.POI = {}    
Lady_Sybil_Free_Hospital.Items = {"Arms":0}    
Lady_Sybil_Free_Hospital.boss = False
Lady_Sybil_Free_Hospital.sprite = True

Temple_of_Anoia = Location()
Temple_of_Anoia.name = "Temple of Anoia"
Temple_of_Anoia.description = "Once just a table covered with a linen tablecloth, the fortunes of Anoia, and her priestess, have increased dramatically, and now in place of the table stands an altar, hung with ladles. The goddess of stuck cutlery is invoked through the rattle of drawers, combined with a frustrated cry.	 A small collection plate to one side holds a few coins, along with a corkscrew – which Anoia is said to eat. *possibly drop money into collection plate?"
Temple_of_Anoia.exits = {"mended":"Mended Drum", "hospital":"Hospital","restaurant":"Restaurant",
"inner":"Inner"}
Temple_of_Anoia.POI = {}    
Temple_of_Anoia.Items = {}   
Temple_of_Anoia.boss = False
Temple_of_Anoia.sprite = False

Temple_of_Anoia_Inner = Location()
Temple_of_Anoia_Inner.name = "Inner Shrine of Anoia"
Temple_of_Anoia_Inner.description = "Venturing into the inner shrine of Anoia’s temple, GitLabs can be seen – a quasi-demonic entity from the Dungeon Dimensions. Brought forth to this world by a funny man in a hat with no understanding of what he was doing, for now it lurks here, gaining strength and preparing to destroy this reality."
Temple_of_Anoia_Inner.exits = {"temple":"Temple"}
Temple_of_Anoia_Inner.POI = {}
Temple_of_Anoia_Inner.Items = {}       
Temple_of_Anoia_Inner.boss = True
Temple_of_Anoia_Inner.sprite = False

Gimlets_Restaurant = Location()
Gimlets_Restaurant.name = "Gimlet the Dwarf's Delicatessen"
Gimlets_Restaurant.description = "Following Captain Carrot, you enter the dwarven restaurant, and greet the proprietor, a bearded dwarf named Gimlet. He points you in the direction of a particularly troublesome customer – a feeble dwarf by the name of Jonathan. He is refusing to leave, creating a ruckus and generally annoying the other customers.        #gimlet gives you health pie/rat pie for killing jonathan."
Gimlets_Restaurant.exits = {"temple":"Temple", "shades":"Shades"}
Gimlets_Restaurant.POI = {}    
Gimlets_Restaurant.Items = {}   
Gimlets_Restaurant.boss = True
Gimlets_Restaurant.sprite = False

The_Shades = Location()
The_Shades.name = "The Shades"
The_Shades.description = "Being both the oldest and the most “colourful” area in the city, letting your guard down in the Shades is not a wise idea. The use of troll officers has convinced the locals that assaulting a watch officer is not the brightest idea, but there will always be some bright sparks who are unable to get the message. With caution and luck, one is able to pass through the Shades unscathed. "
The_Shades.exits = {"club":"Club", "restaurant":"Restaurant"}
The_Shades.POI = {}  
The_Shades.Items = {}     
The_Shades.boss = False
The_Shades.sprite = True

The_Pink_Pussycat_Club = Location()
The_Pink_Pussycat_Club.name = "The Pink Pussycat Club"
The_Pink_Pussycat_Club.description = "Located at the edge of the Shades, the Pink Pussycat Club caters to all tastes, with a multitude of talented performers – including Broccoli, the girl who can the back of her head with her foot. Originally named Candi, she recently heard that Broccoli is better for you – hence the name change. Seat 7 in the front row is currently occupied by the ghost of Professor Flead, a long-dead professor from Unseen University.     #talk to flead?"
The_Pink_Pussycat_Club.exits = {"shades":"Shades", "sanctuary":"Sanctuary"}
The_Pink_Pussycat_Club.POI = {}        
The_Pink_Pussycat_Club.Items = {}
The_Pink_Pussycat_Club.boss = False
The_Pink_Pussycat_Club.sprite = False

Dragon_Sanctuary = Location()
Dragon_Sanctuary.name = "The Sanctuary for Lost Dragons"
Dragon_Sanctuary.description = "A building with similar design principles to that of a firework factory – mainly thick walls and a light roof – it houses abandoned and mistreated swamp dragons that have been rescued from across the city. A large lady, clad in slightly charred leather armour, approaches, in one hand holding a small swamp dragon, and in the other a lump of coal which she is currently feeding to the animal. #talk to sybil. "
Dragon_Sanctuary.exits = {"outside":"Outside", "club":"Club"} 
Dragon_Sanctuary.POI = ["Return dragons"]
Dragon_Sanctuary.Items = {"swamp dragons":0}        
Dragon_Sanctuary.boss = False
Dragon_Sanctuary.sprite = True

ListLocations = {"Reception":Pseudopolis_Yard_Reception,
"Locker Room":Pseudopolis_Yard_Upstairs, 
"Outside":Pseudopolis_Yard_Outside, 
"Tower":Tower_of_Art, 
"Library":Library, 
"Roof":Library_Roof, 
"Square":Sator_Square,
"Entrance":Palace_Entrance, 
"Palace":Palace, 
"Post Office":Post_Office, 
"Basement":Post_Office_Basement, 
"Mended Drum":Mended_Drum,
"Hospital":Lady_Sybil_Free_Hospital, 
"Temple":Temple_of_Anoia, 
"Inner":Temple_of_Anoia_Inner,
"Restaurant":Gimlets_Restaurant, 
"Shades":The_Shades, 
"Club":The_Pink_Pussycat_Club, 
"Sanctuary":Dragon_Sanctuary}