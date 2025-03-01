from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial
from .Options import *
from .Items import BKItem, item_table
from .Locations import *
from .Regions import create_regions
from .Rules import set_rules
from typing import Any, Dict


class BanjoKazooieWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Banjo-Kazooie randomizer connected to an Archipelago multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["JadeCurtiss90"]
    )]


class BanjoKazooieWorld(World):
    """
    Banjo-Kazooie is a 3D platforming game. You control Banjo the bear and Kazooie the bird on their quest to save
    Banjo's sister Tooty from the evil witch Gruntilda. Climb Grunty's Lair, explore 9 unique worlds, and defeat
    the evil witch!
    """
    web = BanjoKazooieWeb()

    options_dataclass = BKOptions
    options = BKOptions
    game = "Banjo-Kazooie"
    topology_present = True

    data_version = 0
    required_client_version = (0, 2, 6)

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    level_entrances = [
        ["Mumbo's Mountain", 1],
        ["Treasure Trove Cove", 2],
        ["Clanker's Cavern", 3],
        ["Bubblegloop Swamp", 4],
        ["Freezeezy Peak", 5],
        ["Gobi's Valley", 6],
        ["Mad Monster Mansion", 7],
        ["Rusty Bucket Bay", 8],
        ["Click Clock Wood", 9],
    ]

    def create_item(self, name: str):
        return BKItem(name, item_table.get(name).classification, item_table.get(name).code, self.player)

    def create_items(self) -> None:
        jiggy_count = self.multiworld.number_of_jiggies[self.player].value
        self.multiworld.itempool += [self.create_item("Jiggy")
                                     for amount in range(0, jiggy_count)]
        self.multiworld.itempool += [self.create_item(self.get_filler_item_name())
                                     for amount in range(jiggy_count, 100)]

        self.multiworld.itempool += [self.create_item("Empty Honeycomb Piece") for amount in range(0, 24)]

        mumbo_token_count = self.multiworld.number_of_mumbo_tokens[self.player].value
        self.multiworld.itempool += [self.create_item("Mumbo Token") for amount in range(0, mumbo_token_count)]
        self.multiworld.itempool += [self.create_item(self.get_filler_item_name())
                                     for amount in range(mumbo_token_count, 112)]

        self.multiworld.itempool += [self.create_item("Double Health")]

        self.initialize_events()
        self.initialize_options()
        self.initialize_notes()

        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = {
            "shuffle_moves": self.options.shuffle_moves.value,
            "shuffle_basic_moves": self.options.shuffle_basic_moves.value,
            "shuffle_cheato": self.options.shuffle_cheato.value,
            "shuffle_secrets": self.options.shuffle_secrets.value,
            # ~ "level_randomizer": self.level_entrances,
            "correct_pads": self.options.correct_pads.value,
            "skip_furnace_fun": self.options.skip_furnace_fun.value,
            "remove_note_doors": self.options.remove_note_doors.value,
            "number_of_jiggies": self.options.number_of_jiggies.value,
            "number_of_mumbo_tokens": self.options.number_of_mumbo_tokens.value,
            "death_link": self.options.death_link.value,
        }
        return slot_data

    def generate_early(self) -> None:
        if self.multiworld.level_randomizer[self.player].value != 0:
            self.multiworld.random.shuffle(self.level_entrances)
            if self.multiworld.shuffle_moves[self.player].value == 0:
                while True:
                    if self.level_entrances[0][0] == "Mumbo's Mountain":
                        if (self.level_entrances[3][0] == "Mumbo's Mountain" or
                                self.level_entrances[3][0] == "Bubblegloop Swamp" or
                                self.level_entrances[3][0] == "Freezeezy Peak" or
                                self.level_entrances[3][0] == "Mad Monster Mansion" or
                                self.level_entrances[3][0] == "Click Clock Wood"):
                            if (self.level_entrances[6][0] == "Mumbo's Mountain" or
                                    self.level_entrances[6][0] == "Bubblegloop Swamp" or
                                    self.level_entrances[6][0] == "Freezeezy Peak" or
                                    self.level_entrances[6][0] == "Mad Monster Mansion" or
                                    self.level_entrances[6][0] == "Click Clock Wood"):
                                break
                    self.multiworld.random.shuffle(self.level_entrances)
            else:
                while True:
                    if (self.level_entrances[0][0] == "Mumbo's Mountain" or
                            self.level_entrances[0][0] == "Bubblegloop Swamp" or
                            self.level_entrances[0][0] == "Freezeezy Peak" or
                            self.level_entrances[0][0] == "Mad Monster Mansion" or
                            self.level_entrances[0][0] == "Click Clock Wood"):
                        if (self.level_entrances[3][0] == "Mumbo's Mountain" or
                                self.level_entrances[3][0] == "Bubblegloop Swamp" or
                                self.level_entrances[3][0] == "Freezeezy Peak" or
                                self.level_entrances[3][0] == "Mad Monster Mansion" or
                                self.level_entrances[3][0] == "Click Clock Wood"):
                            if (self.level_entrances[6][0] == "Mumbo's Mountain" or
                                    self.level_entrances[6][0] == "Bubblegloop Swamp" or
                                    self.level_entrances[6][0] == "Freezeezy Peak" or
                                    self.level_entrances[6][0] == "Mad Monster Mansion" or
                                    self.level_entrances[6][0] == "Click Clock Wood"):
                                break
                    self.multiworld.random.shuffle(self.level_entrances)

#        if self.multiworld.number_of_jiggies[self.player].value == 100:
#            self.multiworld.local_early_items[self.player]["Jiggy"] = 1
        if self.multiworld.shuffle_moves[self.player].value != 0:
            self.multiworld.local_early_items[self.player]["Talon Trot"] = 1

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(
            ["Honeycomb", "Egg Refill", "Red Feathers Refill", "Gold Feathers Refill", "Extra Life"])

    def initialize_events(self) -> None:
        for location, data in location_table_without_notes.items():
            if data.code is None:
                if "Jiggy Puzzle" in location:
                    if "MM" in location and "MMM" not in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("MM Jiggy Puzzle"))
                    elif "TTC" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("TTC Jiggy Puzzle"))
                    elif "CC" in location and "CCW" not in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("CC Jiggy Puzzle"))
                    elif "BS" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("BS Jiggy Puzzle"))
                    elif "FP" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("FP Jiggy Puzzle"))
                    elif "GV" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("GV Jiggy Puzzle"))
                    elif "MMM" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("MMM Jiggy Puzzle"))
                    elif "RBB" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("RBB Jiggy Puzzle"))
                    elif "CCW" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("CCW Jiggy Puzzle"))
                    elif "Final Boss" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Final Boss Jiggy Puzzle"))
                elif "Note Door" in location:
                    if "1" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Note Door 1"))
                    elif "2" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Note Door 2"))
                    elif "3" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Note Door 3"))
                    elif "4" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Note Door 4"))
                    elif "5" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Note Door 5"))
                    elif "6" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Note Door 6"))
                    elif "7" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Note Door 7"))
                    elif "8" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Note Door 8"))
                    elif "9" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Note Door 9"))
                elif "Witch Switch" in location:
                    if "MM" in location and "MMM" not in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("MM Witch Switch"))
                    elif "TTC" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("TTC Witch Switch"))
                    elif "CC" in location and "CCW" not in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("CC Witch Switch"))
                    elif "BS" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("BS Witch Switch"))
                    elif "FP" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("FP Witch Switch"))
                    elif "GV" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("GV Witch Switch"))
                    elif "MMM" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("MMM Witch Switch"))
                    elif "RBB" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("RBB Witch Switch"))
                    elif "CCW" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("CCW Witch Switch"))
                elif "Transformation" in location:
                    if "Termite" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Termite Transformation"))
                    elif "Crocodile" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Crocodile Transformation"))
                    elif "Walrus" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Walrus Transformation"))
                    elif "Pumpkin" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Pumpkin Transformation"))
                    elif "Bee" in location:
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Bee Transformation"))
                else:
                    if location == "GLF6 Water Level Switch 1":
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Water Level Switch 1"))
                    elif location == "GLF6 Water Level Switch 2":
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Water Level Switch 2"))
                    elif location == "FP Toboggan Jiggy Flag":
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Toboggan Jiggy Flag"))
                    elif location == "FP Boggy's First Race Jiggy Flag":
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Boggy's First Race Jiggy Flag"))
                    elif location == "GV Gobi's Jiggy Flag":
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Gobi's Jiggy Flag"))
                    elif location == "GV Trunker's Jiggy Flag":
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Trunker's Jiggy Flag"))
                    elif location == "GV Gobi's Honeycomb Flag":
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Gobi's Honeycomb Flag"))
                    elif location == "BLUEEGGS Cheato Rock Cleared Flag":
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("BLUEEGGS Cheato Rock Cleared"))
                    elif location == "GLF8 Click Clock Wood Jiggy Podium Switch":
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("CCW Jiggy Podium Switch"))
                    elif location == "Victory":
                        self.multiworld.get_location(location, self.player).place_locked_item(
                            self.create_item("Victory"))

    def initialize_notes(self) -> None:
        for note in mm_notes_location_table:
            self.multiworld.get_location(note, self.player).place_locked_item(self.create_item("Note (Real)"))
        for note in ttc_notes_location_table:
            self.multiworld.get_location(note, self.player).place_locked_item(self.create_item("Note"))
        for note in cc_notes_location_table:
            self.multiworld.get_location(note, self.player).place_locked_item(self.create_item("Note"))
        for note in bs_notes_location_table:
            self.multiworld.get_location(note, self.player).place_locked_item(self.create_item("Note"))
        for note in fp_notes_location_table:
            self.multiworld.get_location(note, self.player).place_locked_item(self.create_item("Note"))
        for note in gv_notes_location_table:
            self.multiworld.get_location(note, self.player).place_locked_item(self.create_item("Note"))
        for note in mmm_notes_location_table:
            self.multiworld.get_location(note, self.player).place_locked_item(self.create_item("Note"))
        for note in rbb_notes_location_table:
            self.multiworld.get_location(note, self.player).place_locked_item(self.create_item("Note"))
        for note in ccw_notes_location_table:
            self.multiworld.get_location(note, self.player).place_locked_item(self.create_item("Note"))

    def initialize_options(self) -> None:
        if self.multiworld.shuffle_moves[self.player].value != 0:
            self.multiworld.itempool += [self.create_item("Eggs"),
                                         self.create_item("Talon Trot"),
                                         self.create_item("Beak Buster"),
                                         self.create_item("Flight"),
                                         self.create_item("Shock Spring Jump"),
                                         self.create_item("Wonderwing"),
                                         self.create_item("Stilt Stride"),
                                         self.create_item("Beak Bomb"),
                                         self.create_item("Turbo Talon Trot")]
        else:
            self.multiworld.get_location("MM Eggs Molehill", self.player).place_locked_item(
                self.create_item("Eggs"))
            self.multiworld.get_location("MM Talon Trot Molehill", self.player).place_locked_item(
                self.create_item("Talon Trot"))
            self.multiworld.get_location("MM Beak Buster Molehill", self.player).place_locked_item(
                self.create_item("Beak Buster"))
            self.multiworld.get_location("TTC Flight Molehill", self.player).place_locked_item(
                self.create_item("Flight"))
            self.multiworld.get_location("TTC Shock Spring Jump Molehill", self.player).place_locked_item(
                self.create_item("Shock Spring Jump"))
            self.multiworld.get_location("CC Wonderwing Molehill", self.player).place_locked_item(
                self.create_item("Wonderwing"))
            self.multiworld.get_location("BS Stilt Stride Molehill", self.player).place_locked_item(
                self.create_item("Stilt Stride"))
            self.multiworld.get_location("FP Beak Bomb Molehill", self.player).place_locked_item(
                self.create_item("Beak Bomb"))
            self.multiworld.get_location("GV Turbo Talon Trot Molehill", self.player).place_locked_item(
                self.create_item("Turbo Talon Trot"))
        if self.multiworld.shuffle_basic_moves[self.player].value != 0:
            self.multiworld.itempool += [self.create_item("Jump"),
                                         self.create_item("Feathery Flap"),
                                         self.create_item("Flap Flip"),
                                         self.create_item("Swim"),
                                         self.create_item("Climb"),
                                         self.create_item("Beak Barge"),
                                         self.create_item("Claw Swipe"),
                                         self.create_item("Roll"),
                                         self.create_item("Rat-A-Tat Rap")]
        else:
            self.multiworld.get_location("SM Jump Molehill 1", self.player).place_locked_item(
                self.create_item("Jump"))
            self.multiworld.get_location("SM Jump Molehill 2", self.player).place_locked_item(
                self.create_item("Feathery Flap"))
            self.multiworld.get_location("SM Jump Molehill 3", self.player).place_locked_item(
                self.create_item("Flap Flip"))
            self.multiworld.get_location("SM Swim Molehill", self.player).place_locked_item(
                self.create_item("Swim"))
            self.multiworld.get_location("SM Climb Molehill", self.player).place_locked_item(
                self.create_item("Climb"))
            self.multiworld.get_location("SM Beak Barge Molehill", self.player).place_locked_item(
                self.create_item("Beak Barge"))
            self.multiworld.get_location("SM Attack Molehill 1", self.player).place_locked_item(
                self.create_item("Claw Swipe"))
            self.multiworld.get_location("SM Attack Molehill 2", self.player).place_locked_item(
                self.create_item("Roll"))
            self.multiworld.get_location("SM Attack Molehill 3", self.player).place_locked_item(
                self.create_item("Rat-A-Tat Rap"))
        if self.multiworld.shuffle_cheato[self.player].value != 0:
            self.multiworld.itempool += [self.create_item("BLUEEGGS Cheato"),
                                         self.create_item("REDFEATHERS Cheato"),
                                         self.create_item("GOLDFEATHERS Cheato")]
        else:
            self.multiworld.get_location("BLUEEGGS Cheato", self.player).place_locked_item(
                self.create_item("BLUEEGGS Cheato"))
            self.multiworld.get_location("REDFEATHERS Cheato", self.player).place_locked_item(
                self.create_item("REDFEATHERS Cheato"))
            self.multiworld.get_location("GOLDFEATHERS Cheato", self.player).place_locked_item(
                self.create_item("GOLDFEATHERS Cheato"))
        if self.multiworld.shuffle_secrets[self.player].value != 0:
            self.multiworld.itempool += [self.create_item("Ice Key"),
                                         self.create_item("Pink Egg"),
                                         self.create_item("Blue Egg"),
                                         self.create_item("Cyan Egg"),
                                         self.create_item("Green Egg"),
                                         self.create_item("Red Egg"),
                                         self.create_item("Yellow Egg")]
        else:
            self.multiworld.get_location("Ice Key", self.player).place_locked_item(
                self.create_item("Ice Key"))
            self.multiworld.get_location("Pink Egg", self.player).place_locked_item(
                self.create_item("Pink Egg"))
            self.multiworld.get_location("Blue Egg", self.player).place_locked_item(
                self.create_item("Blue Egg"))
            self.multiworld.get_location("Cyan Egg", self.player).place_locked_item(
                self.create_item("Cyan Egg"))
            self.multiworld.get_location("Green Egg", self.player).place_locked_item(
                self.create_item("Green Egg"))
            self.multiworld.get_location("Red Egg", self.player).place_locked_item(
                self.create_item("Red Egg"))
            self.multiworld.get_location("Yellow Egg", self.player).place_locked_item(
                self.create_item("Yellow Egg"))

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player, self.level_entrances)
