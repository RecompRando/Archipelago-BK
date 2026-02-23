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
        early_items = [ITEM_TALON_TROT]

        for item in early_items:
            self.multiworld.local_early_items[self.player][item] = 1
    
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

        total_unfilled = sum(
            1 for loc in mw.get_locations(player)
            if not loc.item
        )
        total_items = sum(1 for item in mw.itempool if item.player == player)
        
        filler_needed = total_unfilled - total_items
        if filler_needed > 0:
            self.create_and_add_filler_items(filler_needed)

    def create_regions(self) -> None:
        player = self.player
        mw = self.multiworld

        for region_name in region_data_table.keys():
            region = Region(region_name, player, mw)
            mw.regions.append(region)

        for region_name, region_data in region_data_table.items():
            region = mw.get_region(region_name, player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self.options)
            }, BKLocation)
            region.add_exits(region_data.connecting_regions)

        for location_name, location_data in locked_locations.items():
            if not location_data.can_create(self.options):
                continue

            self.place(location_name, location_data_table[location_name].locked_item)

        if not self.options.notesanity.value:
            for location_name, location_data in location_data_table.items():
                if location_data.address is not None and (location_data.address & 0xFF000000) == 0x01000000:
                    self.place(location_name, ITEM_NOTE)

    def pre_fill(self) -> None:
        from BaseClasses import CollectionState
        from Fill import fill_restrictive

        player = self.player
        mw = self.multiworld

        # In threshold mode, lock the 9 unlock items to the 9 threshold locations
        # so every jiggy threshold guarantees a world unlock
        if self.options.level_unlock_mode.value == 0:
            world_items = [
                ITEM_OPEN_TTC, ITEM_OPEN_CC, ITEM_OPEN_BGS,
                ITEM_OPEN_FP, ITEM_OPEN_GV, ITEM_OPEN_MMM,
                ITEM_OPEN_RBB, ITEM_OPEN_CCW,
            ]
            world_locations = [
                LOC_LEVEL_UNLOCK_1, LOC_LEVEL_UNLOCK_2, LOC_LEVEL_UNLOCK_3,
                LOC_LEVEL_UNLOCK_4, LOC_LEVEL_UNLOCK_5, LOC_LEVEL_UNLOCK_6,
                LOC_LEVEL_UNLOCK_7, LOC_LEVEL_UNLOCK_8,
            ]
            self.random.shuffle(world_items)
            for loc_name, item_name in zip(world_locations, world_items):
                loc = mw.get_location(loc_name, player)
                item = next((i for i in mw.itempool if i.player == player and i.name == item_name), None)
                if item:
                    loc.place_locked_item(item)
                    mw.itempool.remove(item)

            # Final boss always last threshold
            loc = mw.get_location(LOC_LEVEL_UNLOCK_9, player)
            item = next((i for i in mw.itempool if i.player == player and i.name == ITEM_OPEN_FIGHT), None)
            if item:
                loc.place_locked_item(item)
                mw.itempool.remove(item)

        # Place a jiggy in sphere 0 to kickstart progression
        state = CollectionState(mw)
        sphere0_locations = [
            loc for region in mw.regions if region.player == player
            for loc in region.locations if not loc.item and loc.can_reach(state)
        ]

        if sphere0_locations:
            jiggy = next((i for i in mw.itempool if i.player == player and i.name == ITEM_JIGGY), None)
            if jiggy:
                loc = self.random.choice(sphere0_locations)
                loc.place_locked_item(jiggy)
                mw.itempool.remove(jiggy)

        # ============================================================
        # Pre-fill all notes when notesanity is enabled.
        #
        # With 750 progression notes in the main fill, fill_restrictive
        # deadlocks because notes + movement abilities compete for the
        # same early-sphere slots. By placing notes here in isolation,
        # the main fill only handles ~40 items and never fails.
        #
        # Notes are interchangeable (any Note is identical to any other),
        # so fill_restrictive only needs to ensure enough notes are
        # reachable before each door threshold — no item-specific logic.
        # ============================================================
        if self.options.notesanity.value:
            note_items = [i for i in list(mw.itempool)
                          if i.player == player and i.name == ITEM_NOTE]
            for item in note_items:
                mw.itempool.remove(item)

            available_locations = [
                loc for loc in mw.get_unfilled_locations(player)
                if not loc.progress_type == loc.progress_type.EXCLUDED
            ]
            self.random.shuffle(available_locations)
            self.random.shuffle(note_items)

            # Pre-collect all non-note progression items into the state
            # so fill_restrictive knows which locations are reachable.
            # Without this, only sphere 0 locations are available and
            # there aren't enough for 750 notes.
            fill_state = CollectionState(mw)
            for item in mw.itempool:
                if item.player == player and item.advancement:
                    fill_state.collect(item, prevent_sweep=True)
            fill_state.sweep_for_advancements()

            fill_restrictive(mw, fill_state, available_locations, note_items,
                             single_player_placement=True, name="BK Notes")

    def create_and_add_filler_items(self, count: int = 1):
        for i in range(count):
            self.multiworld.itempool.append(self.create_item(self.get_filler_item_name()))

    def get_filler_item_name(self) -> str:
        filler_items = [ITEM_EGG_REFILL, ITEM_REDFEATHER_REFILL, ITEM_GOLDFEATHER_REFILL]
        return self.random.choice(filler_items)

    def set_rules(self) -> None:
        player = self.player
        mw = self.multiworld
        options = self.options

        mw.completion_condition[player] = lambda state: state.has("Victory", player)

        if (self.options.logic_difficulty.value == 4):
            return

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
            "talon_lobby": self.options.talon_lobby.value,
            "extra_locations": self.options.extra_locations.value,
            "level_unlock_mode": self.options.level_unlock_mode.value,
        }