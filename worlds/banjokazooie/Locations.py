import typing
from BaseClasses import Location


class BKLocation(Location):
    game = "Banjo-Kazooie"


class LocationData(typing.NamedTuple):
    address: int
    requirements: typing.Optional[typing.List[typing.List[str]]] = None


glf1_location_table = {
    "GLF1 Entryway Jiggy": LocationData(120013, [["Jump"], ["Feathery Flap"], ["Flap Flip"], ["Rat-A-Tat Rap"]]),
    "GLF1 Atop Mumbo's Mountain Jiggy": LocationData(120014, [["Jump", "Beak Buster"]]), #Needs Transformation
}

glf2_location_table = {
    "GLF2 Treasure Trove Cove Cannon Jiggy": LocationData(120015, [["Flap Flip", "Beak Buster", "Flight"]]),
    "GLF2 Clanker's Cavern Eye Switch Jiggy": LocationData(120016, [["Swim", "Beak Buster"]]),
}

glf3_location_table = {
    "GLF3 Bubblegloop Swamp Witch's Hat Jiggy": LocationData(120017, [["Rat-A-Tat Rap", "Beak Buster", "Shock Spring Jump"], ["Beak Barge", "Beak Buster", "Shock Spring Jump"], ["Eggs", "Beak Buster", "Shock Spring Jump"]]),
}

glf4_location_table = {
    "GLF4 Above Freezeezy Peak Jiggy": LocationData(120018, [["Flap Flip", "Eggs", "Beak Buster" "Flight", "Turbo Talon Trot"]]),
    "GLF4 Gobi's Valley Sarcophagus Jiggy": LocationData(120019, [["Feathery Flap", "Eggs", "Beak Buster", "Flight"], ["Rat-A-Tat Rap", "Eggs", "Beak Buster",  "Flight"], ["Swim", "Eggs", "Beak Buster", "Turbo Talon Trot"]]),
    "GLF4 Mad Monster Mansion Grunty's Eye Jiggy": LocationData(99999[["Flap Flip", "Rat-A-Tat Rap", "Beak Buster", "Turbo Talon Trot", "Shock Spring Jump", "Flight"]]),
}

glf5_location_table = {
    "GLF5 Rusty Bucket Bay Area Jiggy": LocationData(99999, [["Jump", "Feathery Flap", "Beak Buster"], [["Jump", "Rat-A-Tat Rap", "Beak Buster"]]]),
}

glf6_location_table = {
    "GLF6 Click Clock Wood Bee Jiggy": LocationData(99999, [["Feathery Flap", "Talon Trot", "Shock Spring Jump"], ["Rat-A-Tat Rap", "Talon Trot", "Shock Spring Jump"]]), #Requires Transformation
}

mm_location_table = {
    "MM Conga Orange Throw Jiggy": LocationData(120014),
    "MM Chimpy Orange Jiggy": LocationData(120015, [["Climb"]]),
    "MM Conga Attack Jiggy": LocationData(120016, [["Flap Flip", "Eggs"]]),
    "MM Stonehenge Jiggy": LocationData(120017),
    "MM Hillside Jiggy": LocationData(120018),
    "MM Mumbo's Hut Jiggy": LocationData(120019, [["Flap Flip"]]),
    "MM Totem Pole Jiggy": LocationData(120020, [["Jump", "Egg"], ["Flap Flip, Egg"]]),
    "MM Hut Jiggy": LocationData(120021, [["Jump", "Beak Buster"], ["Flap Flip, Beak Buster"]]),
    "MM Top of Termite Mountain Jiggy": LocationData(120022), #Needs Transformation
    "MM Jinjo Jiggy": LocationData(12028, [["Jump", "Beak Buster", "Talon Trot", "Flap Flip"], ["Feathery Flap", "Beak Buster", "Talon Trot", "Flap Flip"]]),
#    "MM Blue Jinjo": LocationData(120023, [["Jump"], ["Feathery Flap"]]),
#    "MM Green Jinjo": LocationData(12024, [["Jump", "Beak Buster"], ["Flap Flip", "Beak Buster"]]),
#    "MM Orange Jinjo": LocationData(12025, [["Talon Trot"]]),
#    "MM Pink Jinjo": LocationData(120026, [["Flap Flip"]]),
#    "MM Yellow Jinjo": LocationData(12027),
}

ttc_location_table = {
    "TTC Nipper Jiggy": LocationData(99999, [["Jump", "Rat-A-Tat Rap"], ["Flap Flip", "Rat-A-Tat Rap"], ["Jump", "Wonderwing"], ["Flap Flip", "Wonderwing"]]),
    "TTC Blubber's Jiggy": LocationData(99999, [["Flap Flip", "Swim", "Beak Buster"]]),
    "TTC Sandcastle Jiggy": LocationData(99999, [["Flap Flip", "Eggs", "Beak Buster"]]),
    "TTC Shock Spring Jump Jiggy": LocationData(99999, [["Shock Spring Jump"], ["Flight"]]),
    "TTC X Marks the Spot Jiggy": LocationData(99999 [["Beak Buster", "Flight"], ["Beak Buster", "Shock Spring Jump"]]),
    "TTC Underwater Pool Jiggy": LocationData(99999, [["Swim"]]),
    "TTC Cliffside Jiggy": LocationData(99999),
    "TTC Lockup Jiggy": LocationData(99999, [["Flap Flip", "Flight"]]),
    "TTC Lighthouse Jiggy": LocationData(99999, [["Flight"]]),
    "TTC Jinjo Jiggy": LocationData(99999, [["Swim, Flight"]]),
#    "TTC Blue Jinjo": LocationData(99999, [["Swim"]]),
#    "TTC Green Jinjo": LocationData(99999, [["Climb"], ["Flight"]]),
#    "TTC Orange Jinjo": LocationData(99999),
#    "TTC Pink Jinjo": LocationData(99999, [["Shock Spring Jump"], ["Jump", "Feathery Flap"], ["Flight"]]),
#    "TTC Yellow Jinjo": LocationData(99999, [["Flight"]]),
}

cc_location_table = {
    "CC Raising Clanker Jiggy": LocationData(99999),
    "CC Above Clanker's Tail Jiggy": LocationData(99999, [["Rat-A-Tat Rap"]]),
    "CC Above Clanker's Bolt Jiggy": LocationData(99999, [["Flap Flip"]]),
    "CC Clanker's Second Gold Tooth Jiggy": LocationData(99999, [["Eggs"]]),
    "CC Inside Clanker's Blowhole Jiggy": LocationData(99999),
    "CC Wonderwing Jiggy": LocationData(99999, [["Flight", "Wonderwing"]]),
    "CC Clanker's Rings Jiggy": LocationData(99999, [["Jump", "Feathery Flap"], ["Jump", "Rat-A-Tat Rap"]]),
    "CC Snippet Jiggy": LocationData(99999, [["Flap Flip", "Claw Swipe"], ["Flap Flip", "Roll"], ["Flap Flip", "Rat-A-Tat Rap"], ["Flap Flip", "Eggs"], ["Flap Flip", "Beak Barge"], ["Flap Flip", "Beak Buster"]]),
    "CC Underwater Tunnel Jiggy": LocationData(99999),
    "CC Jinjo Jiggy": LocationData(99999, [["Climb", "Feathery Flap", "Beak Buster", "Shock Spring Jump"], ["Climb", "Rat-A-Tat Rap", "Beak Buster", "Shock Spring Jump"]]),
#    "CC Blue Jinjo": LocationData(99999),
#    "CC GreenJinjo": LocationData(99999),
#    "CC Orange Jinjo": LocationData(99999, [["Climb", "Feathery Flap", "Beak Buster", "Shock Spring Jump"], ["Climb", "Rat-A-Tat Rap", "Beak Buster", "Shock Spring Jump"]]),
#    "CC Pink Jinjo": LocationData(99999),
#    "CC Yellow Jinjo": LocationData(99999, [["Feathery Flap", "Climb"], ["Rat-A-Tat Rap", "Climb"]]),
}

bs_location_table = {
    "BS Egg Jiggy": LocationData(99999, [["Rat-A-Tat Rap", "Beak Barge", "Beak Buster", "Shock Spring Jump"]]),
    "BS Central Switch Jiggy": LocationData(99999, [["Talon Trot", "Beak Buster"]]),
    "BS Flibbet Jiggy": LocationData(99999, [["Claw Swipe"], ["Roll"], ["Rat-A-Tat Rap"], ["Beak Barge"], ["Beak Buster"]]), #OR Transformation
    "BS Tanktup Jiggy": LocationData(99999, [["Beak Buster"]]),
    "BS Tiptup Jiggy": LocationData(99999, [["Beak Buster"]]),
    "BS Hut Jiggy": LocationData (99999, [["Beak Buster", "Shock Spring Jump"]]),
    "BS Platform Near Mumbo's Hut Jiggy": LocationData(99999, [["Beak Buster", "Stilt Stride"]]),
    "BS Croctus Jiggy": LocationData(99999, [["Eggs", "Talon Trot", "Beak Buster", "Shock Spring Jump"]]),
    "BS Mr. Vile Jiggy": LocationData(99999, [["Stilt Stride"]]), #AND Transformation
    "BS Jinjo Jiggy": LocationData(99999, [["Climb", "Feathery Flap", "Talon Trot", "Stilt Stride"], ["Climb", "Rat-A-Tat Rap", "Talon Trot", "Stilt Stride"]]), #AND Transformation
#    "BS Blue Jinjo": LocationData (99999, [["Climb"]]),
#    "BS Green Jinjo": LocationData(99999, [["Talon Trot"], ["Stilt Stride"]]), #OR Transformation
#    "BS Orange Jinjo": LocationData(99999),
#    "BS Pink Jinjo": LocationData(99999 [["Stilt Stride"]]), AND Transformation
#    "BS Yellow Jinjo": LocationData(99999, [["Feathery Flap"], ["Rat-A-Tat Rap"]]),
}

fp_location_table = {
    "FP Snowman Jiggy": LocationData(99999, [["Flight", "Beak Bomb"]]),
    "FP Snowman's Pipe Jiggy": LocationData(99999, [["Talon Trot", "Shock Spring Jump"], ["Flight"]]),
    "FP Boggy's Toboggan Jiggy": LocationData(99999, [["Talon Trot"], ["Flight"]]),
    "FP Snowman's Buttons Jiggy": LocationData(99999, [["Flight", "Beak Bomb"]]),
    "FP Top of the Christmas Tree Jiggy": LocationData(99999, [["Climb", "Eggs", "Beak Buster", "Flight"]]),
    "FP Wozza's Jiggy": LocationData(99999), #AND Transformation
    "FP Boggy's Presents Jiggy": LocationData(99999, [["Climb", "Eggs", "Beak Buster", "Flight"]]),
    "FP Boggy's First Race Jiggy": LocationData(99999), #AND Transformation
    "FP Boggy's Second Race Jiggy": LocationData(99999, [["Turbo Talon Trot"]]), #AND Transformation
    "FP Jinjo Jiggy": LocationData(99999, [["Flap Flip", "Feathery Flap"], ["Flap Flip", "Rat-A-Tat Rap"], ["Flap Flip", "Flight"]]), #AND Transformation
#    "FP Blue Jinjo": LocationData(99999, [["Feathery Flap"], ["Rat-A-Tat Rap"], ["Flight"]]),
#    "FP Green Jinjo": LocationData(99999),
#    "FP Orange Jinjo": LocationData(99999, [["Flap Flip"]]), #AND Transformation
#    "FP Pink Jinjo": LocationData(99999, [["Jump"], ["Flap Flip"]]),
#    "FP Purple Jinjo": LocationData(99999, [["Flap Flip"], ["Flight"]]),
}

gv_location_table = {
    "GV Jinxy's Jiggy": LocationData(99999, [["Feathery Flap", "Flap Flip", "Eggs"], ["Rat-A-Tat Rap", "Flap Flip", "Eggs"]]),
    "GV Grabba's Jiggy": LocationData(99999, [["Turbo Talon Trot"]]),
    "GV Flip Puzzle Jiggy": LocationData(99999, [["Beak Buster"]]),
    "GV Water Pyramid Jiggy": LocationData(99999, [["Swim", "Turbo Talon Trot"]]),
    "GV Ancient Ones' Jiggy": LocationData(99999, [["Feathery Flap", "Flap Flip", "Flight"], ["Rat-A-Tat Rap", "Flap Flip", "Flight"]]),
    "GV Rubee's Jiggy": LocationData(99999, [["Feathery Flap", "Flap Flip", "Eggs", "Flight", "Beak Bomb"], ["Rat-A-Tat Rap", "Flap Flip", "Eggs", "Flight", "Beak Bomb"]]),
    "GV Sandybutt's Jiggy": LocationData(99999, [["Feathery Flap", "Flight", "Eggs"], ["Rat-A-Tat Rap", "Flight", "Eggs"], ["Swim", "Eggs", "Turbo Talon Trot"]]),
    "GV Gobi's Jiggy": LocationData(99999, [["Beak Buster"]]),
    "GV Trunker's Jiggy": LocationData(99999, [["Climb", "Feathery Flap", "Beak Buster"], ["Climb", "Rat-A-Tat Rap", "Beak Buster"], ["Flight, Beak Buster"]]),
    "GV Jinjo Jiggy": LocationData(99999, [["Feathery Flap", "Flap Flip", "Eggs", "Flight", "Stilt Stride"], ["Swim", "Rat-A-Tat Rap", "Flap Flip", "Eggs", "Stilt Stride", "Turbo Talon Trot"]]),
#    "GV Blue Jinjo": LocationData(99999, [["Flight"], ["Swim", "Turbo Talon Trot"]]),
#    "GV Yellow Jinjo": LocationData(99999),
#    "GV Green Jinjo": LocationData(99999),
#    "GV Pink Jinjo": LocationData(99999), [["Eggs", "Flight"], ["Swim", "Eggs", "Turbo Talon Trot"]]),
#    "GV Orange Jinjo": LocationData(99999, [["Feathery Flap", "Flap Flip", "Eggs", "Stilt Stride"], ["Rat-A-Tat Rap", "Flap Flip", "Eggs", "Stilt Stride"]]),
}

mmm_location_table = {
    "MMM Napper's Jiggy": LocationData(99999, [["Jump", "Climb", "Shock Spring Jump"], ["Flap Flip", "Feathery Flap", "Climb", "Talon Trot", "Shock Spring Jump"], ["Flap Flip", "Climb", "Rat-A-Tat Rap", "Talon Trot", "Shock Spring Jump"]]),
    "MMM Cellar Jiggy": LocationData(99999, [["Rat-A-Tat Rap"], ["Beak Barge"], ["Eggs"]]),
    "MMM Tumblar's Jiggy": LocationData(99999, [["Rat-A-Tat Rap"], ["Beak Barge"], ["Eggs"]]),
    "MMM Jiggy in the Well": LocationData(99999, [["Climb", "Swim"]]), #Transformation works too
    "MMM Flowerpot Jiggy": LocationData(99999, [["Beak Barge", "Eggs"], ["Rat-A-Tat Rap", "Eggs"]]),
    "MMM Top of the Clock Tower Jiggy": LocationData(99999, [["Jump", "Climb", "Talon Trot"]]),
    "MMM Motzand's Jiggy": LocationData(99999, [["Flap Flip", "Beak Barge", "Beak Buster", "Turbo Talon Trot", "Shock Spring Jump"], ["Flap Flip", "Rat-A-Tat Rap", "Beak Buster", "Turbo Talon Trot", "Shock Spring Jump"]]),
    "MMM Jiggy in the Toilet": LocationData(99999, [["Flap Flip", "Jump", "Climb", "Rat-A-Tat Rap"], ["Flap Flip", "Jump", "Climb", "Eggs"], ["Flap Flip", "Climb", "Talon Trot", "Rat-A-Tat Rap"], ["Flap Flip", "Climb", "Talon Trot", "Eggs"]]),
    "MMM Jiggy in the Gutter": LocationData(99999, [["Flap Flip", "Climb"], ["Flap Flip", "Beak Barge"], ["Flap Flip", "Rat-A-Tat Rap"]]),
    "MMM Jinjo Jiggy": LocationData(99999, [["Jump", "Climb", "Rat-A-Tat Rap", "Shock Spring Jump"], ["Jump", "Climb", "Eggs", "Shock Spring Jump"], ["Climb", "Rat-A-Tat Rap", "Talon Trot", "Shock Spring Jump"], ["Climb", "Talon Trot", "Eggs", "Shock Spring Jump"]]),
#    "MMM Blue Jinjo": LocationData(99999, [["Shock Spring Jump"]]),
#    "MMM Green Jinjo": LocationData(99999, [["Jump", "Climb", "Shock Spring Jump"], ["Climb", "Talon Trot", "Shock Spring Jump"]]),
#    "MMM Orange Jinjo": LocationData(99999),
#    "MMM Pink Jinjo": LocationData(99999, [["Rat-A-Tat Rap"], ["Beak Barge"], ["Eggs"]]),
#    "MMM Yellow Jinjo": LocationData(99999, [["Jump", "Climb", "Rat-A-Tat Rap", "Shock Spring Jump"], ["Jump", "Climb", "Eggs", "Shock Spring Jump"], ["Climb", "Rat-A-Tat Rap", "Talon Trot", "Shock Spring Jump"], ["Climb", "Talon Trot", "Eggs", "Shock Spring Jump"]]),
}

rbb_location_table = {
    #RBB Entry REQUIRES Climb
    "RBB Smokestack Jiggy": LocationData(99999),
    "RBB Whistle Jiggy": LocationData(99999, [["Beak Buster"]]),
    "RBB Warehouse Jiggy": LocationData(99999, [["Flap Flip", "Eggs", "Talon Trot", "Beak Buster"], ["Flap Flip", "Feathery Flap"], ["Flap Flip", "Rat-A-Tat Rap"]]),
    "RBB Metal Cage Jiggy": LocationData(99999, [["Flap Flip", "Beak Barge"], ["Beak Barge", "Eggs", "Talon Trot"]]),
    "RBB Captain's Room Jiggy": LocationData(99999, [["Rat-A-Tat Rap"]]),
    "RBB Boss Boom Box's Jiggy": LocationData(99999, [["Feathery Flap", "Beak Barge"], ["Rat-A-Tat Rap", "Beak Barge"]]),
    "RBB Dolphin Jiggy": LocationData(99999, [["Swim", "Beak Buster"]]),
    "RBB Engine Room Jiggy": LocationData(99999),
    "RBB Propeller Jiggy": LocationData(99999, [["Swim", "Beak Buster"]]),
    "RBB Jinjo Jiggy": LocationData(99999, [["Feathery Flap", "Eggs", "Talon Trot"], ["Rat-A-Tat Rap", "Eggs", "Talon Trot"]]),
#    "RBB Blue Jinjo": LocationData(99999),
#    "RBB Green Jinjo": LocationData(99999, [["Feathery Flap", "Eggs", "Talon Trot"], ["Rat-A-Tat Rap", "Eggs", "Talon Trot"]]),
#    "RBB Orange Jinjo": LocationData(99999, [["Feathery Flap", "Eggs"], ["Rat-A-Tat Rap", "Eggs"]]),
#    "RBB Pink Jinjo": LocationData(99999, [["Swim"]]),
#    "RBB Yellow Jinjo": LocationData(99999),
}

ccw_location_table = {
    "CCW Treetop Room Jiggy": LocationData(99999, [["Beak Barge"], ["Rat-A-Tat Rap"], ["Eggs"]]),
    "CCW Top of the Tree Jiggy": LocationData(99999), #Requires Transformation
    "CCW Summer Zubbas' Jiggy": LocationData(99999),
    "CCW Summer Leaf Jiggy": LocationData(99999),
    "CCW Summer Construction Site Jiggy": LocationData(99999),
    "CCW Fall Gnawty's Jiggy": LocationData(99999),
    "CCW Fall Plant Jiggy": LocationData(99999, [["Eggs"]]), #Requires obtaining Gobi's Valley Gobi Jiggies and Honeycomb Piece
    "CCW Fall Nabnut's Jiggy": LocationData(99999, [["Rat-A-Tat Rap"]]),
    "CCW Winter Eyrie's Jiggy": LocationData(99999),
    "CCW Jinjo Jiggy": LocationData(99999), #Requires Transformation
#    "CCW Green Jinjo": LocationData(99999, [["Wonderwing"]]), #Transformation works too
#    "CCW Orange Jinjo": LocationData(99999),
#    "CCW Pink Jinjo": LocationData(99999), #Requires Transformation
#    "CCW Yellow Jinjo": LocationData(99999),
}

molehill_location_table = {
    "MM Egg Molehill": LocationData(12029, [["Flap Flip", "Climb"]]),
    "MM Talon Trot Molehill": LocationData(12030),
    "MM Beak Buster Molehill": LocationData(12031),
    "TTC Flight Molehill": LocationData(99999, [["Talon Trot"], ["Flight"]]),
    "TTC Shock Spring Jump Molehill": LocationData(99999),
    "CC Wonderwing Molehill": LocationData(99999, [["Flight"]]),
    "BS Stilt Stride Molehill": LocationData(99999),
    "FP Beak Bomb Molehill": LocationData(99999),
    "GV Turbo Talon Trot Molehill": LocationData(99999),
}

basic_molehill_location_table = {
    "SM Jump Molehill": LocationData(120000),
    "SM Swim Molehill": LocationData(120001),
    "SM Climb Molehill": LocationData(120002),
    "SM Beak Barge Molehill": LocationData(120003),
    "SM Attack Molehill": LocationData(120004),
}

empty_honeycomb_location_table = {
    "SM Jump Honeycomb Piece": LocationData(120005, [["Jump", "Feathery Flap"], ["Flap Flip"]]),
    "SM Waterfall Honeycomb Piece": LocationData(120006, [["Jump", "Feathery Flap"], ["Jump", "Rat-A-Tat Rap"]]),
    "SM Tree Honeycomb Piece": LocationData(120007, [["Climb"]]),
    "SM Underwater Honeycomb Piece": LocationData(120008, [["Swim"]]),
    "SM Beak Barge Honeycomb Piece": LocationData(120009, [["Beak Barge"]]),
    "SM Combat Honeycomb Piece": LocationData(120010, [["Rat-A-Tat Rap"]]),
    "MM Hillside Honeycomb Piece": LocationData(12032),
    "MM Totem Pole Honeycomb Piece": LocationData(12033, [["Flap Flip", "Eggs"]]),
    "TTC Underwater Honeycomb Piece": LocationData(99999, [["Swim"]]),
    "TTC Floating Crate Honeycomb Piece": LocationData(99999),
    "CC Inside Pipe Honeycomb Piece": LocationData(99999),
    "CC Inside Wall Grate Honeycomb Piece": LocationData(99999, [["Climb", "Feathery Flap", "Talon Trot", "Beak Buster", "Shock Spring Jump"], ["Climb", "Rat-A-Tat Rap", "Talon Trot", "Beak Buster", "Shock Spring Jump"]]),
    "BS Above Tiptup Honeycomb Piece": LocationData(99999, [["Flap Flip", "Beak Buster"]]),
    "BS Mumbo's Hut Honeycomb Piece": LocationData(99999, [["Flap Flip", "Stilt Stride"]]),
    "FP Snowman Honeycomb Piece": LocationData(99999, [["Flight", "Beak Bomb"]]),
    "FP Wozza's Cave Honeycomb Piece": LocationData(99999), #AND Transformation
    "GV Cactus Honeycomb Piece": LocationData(99999, [["Feathery Flap", "Flap Flip", "Beak Buster", "Flight"], ["Rat-A-Tat Rap", "Flap Flip", "Beak Buster", "Flight"]]),
    "GV Gobi's Honeycomb Piece": LocationData(99999, [["Beak Buster"]]),
    "MMM Church Rafters Honeycomb Piece": LocationData(99999[["Flap Flip", "Feathery Flap", "Beak Buster", "Turbo Talon Trot", "Shock Spring Jump", "Flight"], ["Flap Flip", "Rat-A-Tat Rap", "Beak Buster", "Turbo Talon Trot", "Shock Spring Jump", "Flight"]]),
    "MMM Honeycomb Piece Under the Floorboards": LocationData(99999, [["Flap Flip", "Jump", "Climb", "Rat-A-Tat Rap"], ["Flap Flip", "Jump", "Climb", "Eggs"], ["Flap Flip", "Climb", "Talon Trot", "Rat-A-Tat Rap"], ["Flap Flip", "Climb", "Talon Trot", "Eggs"]]),
    "RBB Engine Room Honeycomb Piece": LocationData(99999, [["Beak Barge"], ["Eggs"]]),
    "RBB Hidden Warehouse Honeycomb Piece": LocationData(99999, [["Swim", "Beak Buster", "Flight"]]),
    "CCW Winter Honeycomb Piece Above Nabnut's House": LocationData(99999, [["Rat-A-Tat Rap", "Flight"], ["Flight", "Beak Bomb"]]),
    "CCW Winter Honeycomb Piece in Gnawty's House": LocationData(99999, [["Swim"]]),
}

cheato_location_table = {
    "BLUEEGGS Cheato": LocationData(99999, [["Beak Barge"], ["Rat-A-Tat Rap"], ["Eggs"], ["Beak Buster"]]), #Requires Transformation
    "REDFEATHERS Cheato": LocationData(99999), #Requires Transformation
    "GOLDFEATHERS Cheato": LocationData(99999, [["Swim", "Rat-A-Tat Rap", "Beak Buster"], ["Swim", "Eggs", "Beak Buster"]])
}

secrets_location_table = {
    "Ice Key": LocationData(99999, [["Flap Flip"]]),
    "Pink Egg": LocationData(99999, [["Feathery Flap", "Shock Spring Jump"], ["Rat-A-Tat Rap", ["Shock Spring Jump"]]]),
    "Blue Egg": LocationData(99999),
    "Cyan Egg": LocationData(99999),
    "Green Egg": LocationData(99999, [["Jump", "Climb", "Rat-A-Tat Rap"], ["Jump", "Climb", "Eggs"], ["Climb", "Talon Trot", "Rat-A-Tat Rap"], ["Climb", "Talon Trot", "Eggs"]]),
    "Red Egg": LocationData(99999, [["Rat-A-Tat Rap"]]),
    "Yellow Egg": LocationData(99999, [["Rat-A-Tat Rap"]]),
}

mumbo_token_location_table = {
    "GLF2 Mumbo Token Behind Red Magic Cauldron": LocationData(999999),
    "GLF2 Mumbo Token Above Drain Pipe": LocationData(999999),
    "GLF2 Mumbo Token Above Clanker's Cavern": LocationData(999999, [["Flap Flip", "Feathery Flap", "Beak Buster"], ["Flap Flip", "Rat-A-Tat Rap", "Beak Buster"]]),
    "GLF2 Mumbo Token Near Click Clock Wood Podium": LocationData(999999, [["Swim"]]),
    "GLF4 Mumbo Token Behind Sarcophagus": LocationData(99999),
    "GLF4 Mumbo Token Above Freezeezy Peak": LocationData(99999, [["Flap Flip"]]),
    "GLF5 Mumbo Token Under Rusty Bucket Bay": LocationData(99999, [["Swim"]]),
    "GLF5 Mumbo Token By Mad Monster Mansion Podium": LocationData(99999, [["Swim", "Feathery Flap"], ["Swim", "Rar-A-Tat Rap"]]),
    "GLF5 Mumbo Token Behind Mumbo": LocationData(99999, [["Flap Flip", "Beak Barge"], [["Flap Flip", "Rat-A-Tat Rap"]]]), # Needs Transformation
    "GLF6 Tunnel from Click Clock Wood Mumbo Token": LocationData(99999),
    "MM Mumbo Token Behind Pink Jinjo": LocationData(12034),
    "MM Mumbo Token By Conga": LocationData(12035, [["Flap Flip", "Climb"]]),
    "MM Mumbo Token Behind Stonehenge": LocationData(99999),
    "MM Mumbo Token in Termite Mountain": LocationData(99999, [["Talon Trot"]]),  # OR Transformation
    "MM Mumbo Token by Mumbo's Hut": LocationData(99999),
    "TTC Mumbo Token Behind Nipper": LocationData(99999),
    "TTC Mumbo Token in Blubber's Mast": LocationData(99999, [["Climb"]]),
    "TTC Mumbo Token in Blubber's Hold": LocationData(99999, [["Flap Flip", "Swim", "Beak Buster"]]),
    "TTC Mumbo Token near Shock Spring Jump Molehill": LocationData(99999, [["Shock Spring Jump"], ["Flight"]]),
    "TTC Mumbo Token by Treasure Box Island": LocationData(99999),
    "TTC Left Mumbo Token inside Lockup": LocationData(99999, [["Flap Flip"]]),
    "TTC Right Mumbo Token inside Lockup": LocationData(99999, [["Flap Flip"]]),
    "TTC Mumbo Token in Underwater Pool": LocationData(99999, [["Swim"]]),
    "TTC Mumbo Token Above Floating Crate": LocationData(99999),
    "TTC Mumbo Token in Lighthouse": LocationData(99999, [["Flight"]]),
    "CC Mumbo Token Above Entrance": LocationData(99999, [["Jump", "Feathery Flap", "Climb"], ["Jump", "Rat-A-Tat Rap", "Climb"]]),
    "CC Mumbo Token Above Clanker's Tail": LocationData(99999),
    "CC Mumbo Token in Clanker's First Gold Tooth":  LocationData(99999, [["Eggs"]]),
    "CC Mumbo Token in High Grate": LocationData(99999, [["Climb", "Shock Spring Jump"]]),
    "CC Mumbo Token in Underwater Tunnel": LocationData(99999),
    "BS Mumbo Token Behind Yellow Jinjo": LocationData(99999),
    "BS Mumbo Token Above Cat Tail": LocationData(99999, [["Climb"]]),
    "BS Mumbo Token on Central Platform": LocationData(99999, [["Talon Trot"]]), #OR Transformation
    "BS Mumbo Token Inside Tanktup": LocationData(99999, [["Beak Buster"]]),
    "BS Mumbo Token Near Huts": LocationData(99999, [["Beak Buster", "Shock Spring Jump"]]),
    "BS Mumbo Token Behind Mumbo's Hut": LocationData(99999, [["Stilt Stride"]]),
    "BS Mumbo Token Behind Mumbo": LocationData(99999, [["Stilt Stride"]]),
    "BS Left Mumbo Token Under Huts": LocationData(99999, [["Stilt Stride"]]), #AND Transformation
    "BS Right Mumbo Token Under Huts": LocationData(99999, [["Stilt Stride"]]), #AND Transformation
    "BS Mumbo Token Near Mr. Vile": LocationData(99999, [["Stilt Stride"]]), #AND Transformation
    "FP Mumbo Token in Boggy's Igloo": LocationData(99999),
    "FP Mumbo Token By Molehill": LocationData(99999),
    "FP Mumbo Token Above House Flight Pad": LocationData(99999, [["Flight"]]),
    "FP Mumbo Token Under Wozza Snowman": LocationData(99999, [["Flight", "Beak Bomb"]]),
    "FP Mumbo Token Under Island Snowman": LocationData(99999, [["Flight", "Beak Bomb"]]),
    "FP Mumbo Token After Boggy's Toboggan": LocationData(99999, [["Talon Trot"], ["Flight"]]),
    "FP Left Mumbo Token Under Large Snowman": LocationData(99999),
    "FP Right Mumbo Token Under Large Snowman": LocationData(99999),
    "FP Mumbo Token Under Christmas Tree": LocationData(99999, [["Jump", "Feathery Flap"], ["Jump", "Rat-A-Tat Rap"], ["Flap Flip"], ["Flight"]]),
    "FP Underwater Mumbo Token": LocationData(99999),
    "GV Mumbo Token Behind Jinxy": LocationData(99999, [["Feathery Flap", "Flap Flip", "Stilt Stride"], ["Rat-A-Tat Rap", "Flap Flip", "Stilt Stride"]]),
    "GV Mumbo Token On Jinxy's Nose": LocationData(99999, [["Feathery Flap", "Flap Flip"], ["Rat-A-Tat Rap", "Flap Flip"]]),
    "GV Mumbo Token Inside Jinxy": LocationData(99999, [["Feathery Flap", "Flap Flip", "Eggs"], ["Rat-A-Tat Rap", "Flap Flip", "Eggs"]]),
    "GV Mumbo Token Outside Water Pyramid": LocationData(99999),
    "GV Mumbo Token in Flip Puzzle Pyramid": LocationData(99999, [["Beak Buster"]]),
    "GV Mumbo Token in Central Moat": LocationData(99999, [["Flight"], ["Swim", "Turbo Talon Trot"]]),
    "GV Mumbo Token in Rubee's Pyramid": LocationData(99999, [["Feathery Flap", "Flap Flip", "Beak Buster", "Flight", "Beak Bomb"], ["Rat-A-Tat Rap", "Flap Flip", "Beak Buster", "Flight", "Beak Bomb"]]),
    "GV Mumbo Token Atop Central Pyramid": LocationData(99999, [["Flight"], ["Swim", "Eggs", "Turbo Talon Trot"]]),
    "GV Mumbo Token in Sandybutt's Pot": LocationData(99999, [["Eggs", "Flight"], ["Swim", "Eggs", "Turbo Talon Trot"]]),
#   "GV Mumbo Token Inside Water Pyramid": LocationData(XXXXXX, [["Swim", "Turbo Talon Trot"]]), #MISSABLE, DO NOT RANDOMIZE OR FACTOR IN LOGIC
    "MMM Mumbo Token in Fireplace": LocationData(99999, [["Rat-A-Tat Rap"], ["Eggs"], ["Jump", "Climb", "Shock Spring Jump"], ["Climb", "Talon Trot", "Shock Spring Jump"]]),
    "MMM Mumbo Token in Toilet/Cellar": LocationData(99999, [["Rat-A-Tat Rap"], ["Beak Barge"], ["Eggs"]]), # Shared Item ID, collecting one collects the other
    "MMM Mumbo Token in Bathroom": LocationData(99999, [["Jump", "Climb", "Rat-A-Tat Rap"], ["Jump", "Climb", "Eggs"], ["Climb", "Talon Trot", "Rat-A-Tat Rap"], ["Climb", "Talon Trot", "Eggs"]]),
    "MMM Mumbo Token in Maze": LocationData(99999),
    "MMM Mumbo Token in Maze Corner from Roof": LocationData(99999, [["Climb"]]),  # Transformation works too
    "MMM Mumbo Token Atop Tumblar's Shack": LocationData(99999, [["Shock Spring Jump"]]),
    "MMM Mumbo Token in the Well": LocationData(99999, [["Climb", "Swim"]]),  # Transformation works too
    "MMM Mumbo Token Behind a Grave": LocationData(99999, [["Climb"], ["Beak Barge"], ["Rat-A-Tat Rap"]]), # Transformation works too
    "MMM Mumbo Token in the Clock Tower": LocationData(99999, [["Jump", "Rat-A-Tat Rap", "Talon Trot"], ["Jump", "Beak Barge", "Talon Trot"], ["Jump", "Climb", "Talon Trot"]]),
    "MMM Mumbo Token in Church Chair": LocationData(99999, [["Flap Flip", "Beak Barge", "Beak Buster", "Turbo Talon Trot"], ["Flap Flip", "Rat-A-Tat Rap", "Beak Buster", "Turbo Talon Trot"]]),
    "MMM Mumbo Token in Church Rafters": LocationData(99999[["Flap Flip", "Feathery Flap", "Beak Buster", "Turbo Talon Trot", "Shock Spring Jump", "Flight"], ["Flap Flip", "Rat-A-Tat Rap", "Beak Buster", "Turbo Talon Trot", "Shock Spring Jump", "Flight"]]),
    "MMM Mumbo Token Near Tumblar's Shack": LocationData(99999),
    "MMM Mumbo Token in Yellow Jinjo Room": LocationData(99999, [["Jump", "Climb", "Rat-A-Tat Rap", "Shock Spring Jump"], ["Jump", "Climb", "Eggs", "Shock Spring Jump"], ["Climb", "Rat-A-Tat Rap", "Talon Trot", "Shock Spring Jump"], ["Climb", "Talon Trot", "Eggs", "Shock Spring Jump"]]),
    "MMM Mumbo Token Near Blue Jinjo": LocationData(99999, [["Eggs"]]),
    "RBB Toll Bridge Mumbo Token": LocationData(99999, [["Flap Flip", "Eggs"]]),
    "RBB Lifeboat Mumbo Token": LocationData(99999),
    "RBB Mumbo Token Near Boss Boom Box": LocationData(99999),
    "RBB Barracks Mumbo Token": LocationData(99999),
    "RBB Engine Control Room Mumbo Token": LocationData(99999),
    "RBB Engine Room Left Mumbo Token": LocationData(99999, [["Beak Barge", "Beak Buster"], ["Eggs", "Beak Buster"]]),
    "RBB Engine Room Right Mumbo Token": LocationData(99999, [["Beak Barge", "Beak Buster"], ["Eggs", "Beak Buster"]]),
    "RBB Mumbo Token in Store Room": LocationData(99999),
    "RBB Navigation Room Mumbo Token": LocationData(99999, [["Rat-A-Tat Rap"]]),
    "RBB Oven Mumbo Token": LocationData(99999, [["Wonderwing"]]),
    "RBB Smokestack Mumbo Token": LocationData(99999, [["Shock Spring Jump"]]),
    "RBB Toxic Waste Mumbo Token": LocationData(99999, [["Feathery Flap", "Eggs", "Talon Trot"], ["Rat-A-Tat Rap", "Eggs", "Talon Trot"]]),
    "RBB Mumbo Token Ship's Bow": LocationData(99999),
    "RBB Warehouse Crate 1 Mumbo Token": LocationData(99999),
    "RBB Warehouse Crate 2 Mumbo Token": LocationData(99999),
    "CCW Spring Snapper Plant Mumbo Token Near Entrance": LocationData(99999, [["Wonderwing"]]), #Transformation works too
    "CCW Spring Snapper Plant Mumbo Token Near Garden": LocationData(99999, [["Wonderwing"]]), #Transformation works too
    "CCW Spring Mumbo Token in Treetop Above Mumbo's Hut": LocationData(99999), #Transformation works too
    "CCW Spring Mumbo Token on Beehive": LocationData(99999), #Transformation works too
    "CCW Spring Mumbo Token in Construction Site": LocationData(99999), #Transformation works too
    "CCW Spring Mumbo Token on Nabnut's Dresser": LocationData(99999), #Transformation works too
    "CCW Spring Mumbo Token outside Mumbo's Hut/Nabnut's House": LocationData(99999), #Shared Item ID, collecting one collects the other
    "CCW Summer Snapper Plant Mumbo Token Near Mumbo's Hut": LocationData(99999, [["Wonderwing"]]),
    "CCW Summer Mumbo Token in Gnawty's House": LocationData(99999),
    "CCW Summer Mumbo Token in Field by Garden": LocationData(99999),
    "CCW Summer Mumbo Token in Mumbo's Hut": LocationData(99999, [["Wonderwing"], ["Stilt Stride"]]),
    "CCW Summer Mumbo Token in Treetop Above Mumbo's Hut": LocationData(99999),
    "CCW Summer Mumbo Token Above Leaf Jiggy": LocationData(99999),
    "CCW Summer Mumbo Token after Nabnut's House": LocationData(99999),
    "CCW Fall Snapper Plant Mumbo Token Near Entrance": LocationData(99999, [["Wonderwing"]]),
    "CCW Fall Mumbo Token in Treetop Above Mumbo's Hut": LocationData(99999),
    "CCW Fall Mumbo Token on Leaves": LocationData(99999),
    "CCW Fall Mumbo Token Near Construction Site": LocationData(99999),
    "CCW Fall Snapper Plant Mumbo Token in Treetop": LocationData(99999),
    "CCW Winter Garden Mumbo Token": LocationData(99999),
    "CCW Winter Snowman  Mumbo Token Near Garden": LocationData(99999, [["Flight"]]),
    "CCW Winter Beehive": LocationData(99999),
    "CCW Winter Mumbo Token Near Nabnut's House": LocationData(99999),
    "CCW Winter Mumbo Token Behind Lake Platform": LocationData(99999),
}

location_table = {
    **glf1_location_table,
    **mm_location_table,
    **glf2_location_table,
    **ttc_location_table,
    **cc_location_table,
    **glf3_location_table,
    **bs_location_table,
    **glf4_location_table,
    **fp_location_table,
    **gv_location_table,
    **mmm_location_table,
    **glf5_location_table,
    **rbb_location_table,
    **glf6_location_table,
    **ccw_location_table,
}


def setup_locations(world, player: int):
    if world.ShuffleMoves[player].value:
        location_table.update(**molehill_location_table)

    if world.ShuffleBasicMoves[player].value:
        location_table.update(**basic_molehill_location_table)

    if world.ShuffleEmptyHoneycombs[player].value:
        location_table.update(**empty_honeycomb_location_table)

    if world.ShuffleCheato[player].value:
        location_table.update(**cheato_location_table)

    if world.ShuffleSecrets[player].value:
        location_table.update(**secrets_location_table)

    if world.ShuffleMumboTokens[player].value:
        location_table.update(**mumbo_token_location_table)

    return location_table
