from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial
from Options import bk_options
from Items import BKItem, item_table
from Locations import *
from Regions import create_regions, connect_regions, initialize_locations
from Rules import set_rules


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

    option_definitions = bk_options
    game = "Banjo-Kazooie"
    topology_present = True

    data_version = 0
    required_client_version = (0, 3, 5)

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    def create_item(self, name: str):
        return BKItem(name, item_table.get(name).classification, item_table.get(name).code, self.player)

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.player)

    #    def fill_slot_data(self) -> Dict[str, Any]:

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(
            ["Honeycomb", "20 Eggs", "10 Red Feathers", "5 Gold Feathers", "Extra Life"])

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player)

    def generate_early(self) -> None:
        self.multiworld.local_early_items[self.player]["Jiggy"] = 1
        if self.multiworld.move_shuffle[self.player]:
            self.multiworld.local_early_items[self.player]["Talon Trot"] = 1

    def generate_basic(self) -> None:
        jiggy_count = self.multiworld.number_of_jiggies[self.player].value
        self.multiworld.itempool += [self.create_item("Jiggy")
                                     for amount in range(0, jiggy_count)]
        self.multiworld.itempool += [self.create_item(self.get_filler_item_name())
                                     for amount in range(jiggy_count, 100)]

        if self.multiworld.shuffle_mumbo_tokens[self.player]:
            mumbo_token_count = self.multiworld.number_of_mumbo_tokens[self.player].value
            self.multiworld.itempool += [self.create_item("Mumbo Token")
                                         for amount in range(0, mumbo_token_count)]
            self.multiworld.itempool += [self.create_item(self.get_filler_item_name())
                                         for amount in range(mumbo_token_count, 112)]
        else:
            for location in mumbo_token_location_table:
                self.multiworld.get_location(location, self.player).place_locked_item(
                    self.create_item("Mumbo Token"))

        if self.multiworld.shuffle_empty_honeycombs[self.player]:
            self.multiworld.itempool += [self.create_item("Empty Honeycomb Piece")]
        else:
            for location in empty_honeycomb_location_table:
                self.multiworld.get_location(location, self.player).place_locked_item(
                    self.create_item("Empty Honeycomb"))

        if self.multiworld.shuffle_cheato[self.player]:
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

        if self.multiworld.shuffle_secrets[self.player]:
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

        if self.multiworld.shuffle_moves[self.player]:
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
            self.multiworld.get_location("Eggs", self.player).place_locked_item(
                self.create_item("Eggs"))
            self.multiworld.get_location("Talon Trot", self.player).place_locked_item(
                self.create_item("Talon Trot"))
            self.multiworld.get_location("Beak Buster", self.player).place_locked_item(
                self.create_item("Beak Buster"))
            self.multiworld.get_location("Flight", self.player).place_locked_item(
                self.create_item("Flight"))
            self.multiworld.get_location("Shock Spring Jump", self.player).place_locked_item(
                self.create_item("Shock Spring Jump"))
            self.multiworld.get_location("Wonderwing", self.player).place_locked_item(
                self.create_item("Wonderwing"))
            self.multiworld.get_location("Stilt Stride", self.player).place_locked_item(
                self.create_item("Stilt Stride"))
            self.multiworld.get_location("Beak Bomb", self.player).place_locked_item(
                self.create_item("Beak Bomb"))
            self.multiworld.get_location("Turbo Talon Trot", self.player).place_locked_item(
                self.create_item("Turbo Talon Trot"))

        if self.multiworld.shuffle_basic_moves[self.player]:
            self.multiworld.itempool += [self.create_item("Jump"),
                                         self.create_item("Feathery Flap"),
                                         self.create_item("Flap Flip"),
                                         self.create_item("Swim"),
                                         self.create_item("Climb"),
                                         self.create_item("Beak Barge"),
                                         self.create_item("Claw Swipe"),
                                         self.create_item("Roll"),
                                         self.create_item("Rat-A-Tat Rap")]
            self.multiworld.get_location("Jump", self.player).place_locked_item(
                self.create_item("Jump"))
            self.multiworld.get_location("Feathery Flap", self.player).place_locked_item(
                self.create_item("Feathery Flap"))
            self.multiworld.get_location("Flap Flip", self.player).place_locked_item(
                self.create_item("Flap Flip"))
            self.multiworld.get_location("Swim", self.player).place_locked_item(
                self.create_item("Swim"))
            self.multiworld.get_location("Climb", self.player).place_locked_item(
                self.create_item("Climb"))
            self.multiworld.get_location("Beak Barge", self.player).place_locked_item(
                self.create_item("Beak Barge"))
            self.multiworld.get_location("Claw Swipe", self.player).place_locked_item(
                self.create_item("Claw Swipe"))
            self.multiworld.get_location("Roll", self.player).place_locked_item(
                self.create_item("Roll"))
            self.multiworld.get_location("Rat-A-Tat Rap", self.player).place_locked_item(
                self.create_item("Rat-A-Tat Rap"))
