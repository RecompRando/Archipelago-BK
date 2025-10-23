from typing import List
from typing import Dict

from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import BKItem, item_data_table, item_table, code_to_item_table
from .Locations import BKLocation, location_data_table, location_table, code_to_location_table, locked_locations
from .Options import BKOptions
from .Regions import region_data_table, get_exit
from .NormalRules import *
from .Constants import *

class BKWebWorld(WebWorld):
    # ~ theme = "partyTime"
    
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Banjo-Kazooie randomizer connected to an Archipelago multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["JadeCurtiss90", "Spicy Wolf", "LittleCube", "ThatHypedPerson", "PixelShake92", "Muervo_"]
    )
    
    tutorials = [setup_en]


class BKWorld(World):
    """
    Banjo-Kazooie is a 3D platforming game. You control Banjo the bear and Kazooie the bird on their quest to save
    Banjo's sister Tooty from the evil witch Gruntilda. Climb Grunty's Lair, explore 9 unique worlds, and defeat
    the evil witch!
    """

    game = "Banjo-Kazooie"
    data_version = 1
    web = BKWebWorld()
    options_dataclass = BKOptions
    options = BKOptions
    location_name_to_id = location_table
    item_name_to_id = item_table

    def generate_early(self):
        pass
    
    def create_item(self, name: str) -> BKItem:
        return BKItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def place(self, location, item):
        player = self.player
        mw = self.multiworld

        mw.get_location(location, player).place_locked_item(self.create_item(item))

    def create_items(self) -> None:
        mw = self.multiworld

        item_pool: List[BKItem] = []
        item_pool_count: Dict[str, int] = {}
        for name, item in item_data_table.items():
            item_pool_count[name] = 0
            if item.code and item.can_create(self.options):
                while item_pool_count[name] < item.num_exist:
                    item_pool.append(self.create_item(name))
                    item_pool_count[name] += 1

        mw.itempool += item_pool

    def create_regions(self) -> None:
        player = self.player
        mw = self.multiworld

        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, player, mw)
            mw.regions.append(region)

        # Create locations.
        for region_name, region_data in region_data_table.items():
            region = mw.get_region(region_name, player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self.options)
            }, BKLocation)
            region.add_exits(region_data.connecting_regions)

        num_extra_jiggies = 4
        num_extra_honeycombs = 9
        num_extra_molehills = 9
        num_extra_sns = 29

        for location_name, location_data in location_data_table.items():
            region = mw.get_region(location_data.region, player)
            if location_data.address is not None and location_data.can_create(self.options) and (location_data.address & 0xFF000000) == 0x00000000:
                for i in range(2, num_extra_jiggies + 2):
                    name = location_name + " (" + str(i) + ")"
                    address = (0x10000000 + 0x01000000*(i - 2)) | (location_data.address & 0x00FFFFFF)
                    region.add_locations({
                        name: address,
                    }, BKLocation)
            if location_data.address is not None and location_data.can_create(self.options) and (location_data.address & 0xFF000000) == 0x02000000:
                for i in range(2, num_extra_honeycombs + 2):
                    name = location_name + " (" + str(i) + ")"
                    address = (0x30000000 + 0x01000000*(i - 2)) | (location_data.address & 0x00FFFFFF)
                    region.add_locations({
                        name: address,
                    }, BKLocation)
            if location_data.address is not None and location_data.can_create(self.options) and (location_data.address & 0xFF000000) == 0x04000000:
                for i in range(2, num_extra_molehills + 2):
                    name = location_name + " (" + str(i) + ")"
                    address = (0x50000000 + 0x01000000*(i - 2)) | (location_data.address & 0x00FFFFFF)
                    region.add_locations({
                        name: address,
                    }, BKLocation)
            if location_data.address is not None and location_data.can_create(self.options) and (location_data.address & 0xFF000000) == 0x05000000:
                for i in range(2, num_extra_sns + 2):
                    name = location_name + " (" + str(i) + ")"
                    address = (0x70000000 + 0x01000000*(i - 2)) | (location_data.address & 0x00FFFFFF)
                    region.add_locations({
                        name: address,
                    }, BKLocation)

        self.create_and_add_filler_items(100*num_extra_jiggies)
        self.create_and_add_filler_items(24*num_extra_honeycombs)
        self.create_and_add_filler_items(18*num_extra_molehills)
        self.create_and_add_filler_items(7*num_extra_sns)

        # Place locked locations.
        for location_name, location_data in locked_locations.items():
            # Ignore locations we never created.
            if not location_data.can_create(self.options):
                continue

            self.place(location_name, location_data_table[location_name].locked_item)

        if not self.options.notesanity.value:
            for location_name, location_data in location_data_table.items():
                if location_data.address is not None and (location_data.address & 0xFF000000) == 0x01000000:
                    self.place(location_name, ITEM_NOTE)

    def create_and_add_filler_items(self, count: int = 1):
        for i in range(count):
            self.multiworld.itempool.append(self.create_item(self.get_filler_item_name()))

    def get_filler_item_name(self) -> str:
        filler_items = [ITEM_EGG_REFILL, ITEM_REDFEATHER_REFILL, ITEM_GOLDFEATHER_REFILL]
        return self.random.choice(filler_items)
        # filler_weights = (50, 25, 10, 5, 1)
        # return self.random.choices(filler_items, weights=filler_weights)[0]

    def set_rules(self) -> None:
        player = self.player
        mw = self.multiworld
        options = self.options

        # Completion condition.
        mw.completion_condition[player] = lambda state: state.has("Victory", player)

        if (self.options.logic_difficulty.value == 4):
            return

        # ~ if (self.options.logic_difficulty.value == 0):
            # ~ region_rules = get_baby_region_rules(player, options)
            # ~ location_rules = get_baby_location_rules(player, options)
        if (self.options.logic_difficulty.value == 1):
            region_rules = get_region_rules(player, options)
            location_rules = get_location_rules(player, options)

        for entrance_name, rule in region_rules.items():
            entrance = mw.get_entrance(entrance_name, player)
            entrance.access_rule = rule

        for location in mw.get_locations(player):
            name = location.name
            if name in location_rules and location_data_table[name].can_create(self.options):
                location.access_rule = location_rules[name]

    def fill_slot_data(self):
        return {
        }
