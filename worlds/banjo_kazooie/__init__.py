from typing import List
from typing import Dict

from BaseClasses import Region, Tutorial, CollectionState
from worlds.AutoWorld import WebWorld, World
from .Items import BKItem, item_data_table, item_table, code_to_item_table
from .Locations import BKLocation, BKLocationData, num_total_extra_locs, location_data_table, extra_location_table, extra_location_table_old_names, location_table, code_to_location_table, locked_locations
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
        player = self.player

        item_pool: List[BKItem] = []
        item_pool_count: Dict[str, int] = {}
        for name, item in item_data_table.items():
            item_pool_count[name] = 0
            if item.code and item.can_create(self.options):
                while item_pool_count[name] < item.num_exist:
                    item_pool.append(self.create_item(name))
                    item_pool_count[name] += 1

        mw.itempool += item_pool

        # Add filler items for jinjo locations
        self.create_and_add_filler_items(45)

        # Balance: ensure total items >= total unfilled locations
        # This must be here (in create_items) not in create_regions,
        # because create_regions runs BEFORE create_items in AP's generation order.
        total_unfilled = sum(
            1 for loc in mw.get_locations(player)
            if not loc.item
        )
        total_items = sum(1 for item in mw.itempool if item.player == player)
        if total_items < total_unfilled:
            self.create_and_add_filler_items(total_unfilled - total_items)

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

        if self.options.extra_locations.value:
            self.create_and_add_filler_items(num_total_extra_locs)

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

    def pre_fill(self) -> None:
        from BaseClasses import CollectionState

        player = self.player
        mw = self.multiworld

        # Place 1 Jiggy in sphere 0 to unlock MM and prevent deadlocks
        state = CollectionState(mw)
        sphere0_locations = [
            loc for region in mw.regions if region.player == player
            for loc in region.locations if not loc.item and loc.can_reach(state)
        ]

        if not sphere0_locations:
            return

        jiggy = next((i for i in mw.itempool if i.player == player and i.name == ITEM_JIGGY), None)
        if not jiggy:
            return

        loc = self.random.choice(sphere0_locations)
        loc.place_locked_item(jiggy)
        mw.itempool.remove(jiggy)

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
            elif name in extra_location_table and location_data_table[name].can_create(self.options):
                old_name = extra_location_table_old_names[name]
                if old_name in location_rules:
                    location.access_rule = location_rules[old_name]

    def fill_slot_data(self):
        return {
            "talon_lobby": self.options.talon_lobby.value
        }