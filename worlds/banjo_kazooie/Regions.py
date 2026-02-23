from typing import NamedTuple, Callable, List, Dict
from BaseClasses import CollectionState

from .Constants import *

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit

class BKRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, BKRegionData] = {

    # Core progression

    RGN_MENU: BKRegionData([RGN_SPIRAL_MOUNTAIN]),
    RGN_SPIRAL_MOUNTAIN: BKRegionData([RGN_GRUNTILDAS_LAIR_LOBBY]),

    # Gruntilda's Lair - Note Door regions (linear chain + cauldron shortcuts)

    # Lobby: MM entrance (always open), path to 50 note door
    RGN_GRUNTILDAS_LAIR_LOBBY: BKRegionData([
        RGN_MUMBOS_MOUNTAIN,
        RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR,
    ]),

    # 50 Note Door region: TTC, CC entrances
    # Cauldron shortcuts: Purple→350, Orange→640
    RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR: BKRegionData([
        RGN_TREASURE_TROVE_COVE,
        RGN_CLANKERS_CAVERN,
        RGN_GRUNTILDAS_LAIR_180_NOTE_DOOR,
        RGN_GRUNTILDAS_LAIR_350_NOTE_DOOR,       # Purple cauldron shortcut
        RGN_GRUNTILDAS_LAIR_640_NOTE_DOOR,       # Orange cauldron shortcut
    ]),

    # 180 Note Door region: BGS entrance
    RGN_GRUNTILDAS_LAIR_180_NOTE_DOOR: BKRegionData([
        RGN_BUBBLEGLOOP_SWAMP,
        RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR,
        RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR,        # Reverse (walk back)
    ]),

    # 260 Note Door region: FP, GV entrances
    # Cauldron shortcut: Green→450
    RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR: BKRegionData([
        RGN_FREEZEEZY_PEAK,
        RGN_GOBIS_VALLEY,
        RGN_GRUNTILDAS_LAIR_350_NOTE_DOOR,
        RGN_GRUNTILDAS_LAIR_450_NOTE_DOOR,       # Green cauldron shortcut
        RGN_GRUNTILDAS_LAIR_180_NOTE_DOOR,       # Reverse (walk back)
    ]),

    # 350 Note Door region: MMM entrance
    # Cauldron shortcut: Purple→50
    RGN_GRUNTILDAS_LAIR_350_NOTE_DOOR: BKRegionData([
        RGN_MAD_MONSTER_MANSION,
        RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR,        # Purple cauldron shortcut back
        RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR,       # Reverse (walk back)
    ]),

    # 450 Note Door region: RBB entrance
    # Cauldron shortcut: Green→260
    RGN_GRUNTILDAS_LAIR_450_NOTE_DOOR: BKRegionData([
        RGN_RUSTY_BUCKET_BAY,
        RGN_GRUNTILDAS_LAIR_640_NOTE_DOOR,
        RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR,       # Green cauldron shortcut back
        RGN_GRUNTILDAS_LAIR_350_NOTE_DOOR,       # Reverse (walk back)
    ]),

    # 640 Note Door region: CCW entrance
    # Cauldron shortcut: Orange→50
    RGN_GRUNTILDAS_LAIR_640_NOTE_DOOR: BKRegionData([
        RGN_CLICK_CLOCK_WOOD,
        RGN_GRUNTILDAS_LAIR_765_NOTE_DOOR,
        RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR,        # Orange cauldron shortcut back
        RGN_GRUNTILDAS_LAIR_450_NOTE_DOOR,       # Reverse (walk back)
    ]),

    # 765 Note Door region: path to Furnace Fun
    RGN_GRUNTILDAS_LAIR_765_NOTE_DOOR: BKRegionData([
        RGN_GRUNTILDAS_LAIR_FURNACE_FUN,
    ]),

    # Furnace Fun: path to 810
    # Cauldron shortcut: Yellow→810
    RGN_GRUNTILDAS_LAIR_FURNACE_FUN: BKRegionData([
        RGN_GRUNTILDAS_LAIR_810_NOTE_DOOR,
    ]),

    # 810 Note Door region: path to fight and 882
    # Cauldron shortcut: Yellow→Furnace Fun
    RGN_GRUNTILDAS_LAIR_810_NOTE_DOOR: BKRegionData([
        RGN_GRUNTILDAS_LAIR_FIGHT,
        RGN_GRUNTILDAS_LAIR_882_NOTE_DOOR,
        RGN_GRUNTILDAS_LAIR_FURNACE_FUN,         # Yellow cauldron shortcut back
    ]),

    # 882 Note Door region
    RGN_GRUNTILDAS_LAIR_882_NOTE_DOOR: BKRegionData([]),

    # Final fight
    RGN_GRUNTILDAS_LAIR_FIGHT: BKRegionData([]),

    # Worlds (no connecting regions - you exit back to the lair region)

    RGN_MUMBOS_MOUNTAIN: BKRegionData([]),
    RGN_TREASURE_TROVE_COVE: BKRegionData([]),
    RGN_CLANKERS_CAVERN: BKRegionData([]),
    RGN_BUBBLEGLOOP_SWAMP: BKRegionData([]),
    RGN_FREEZEEZY_PEAK: BKRegionData([]),
    RGN_GOBIS_VALLEY: BKRegionData([]),
    RGN_MAD_MONSTER_MANSION: BKRegionData([]),
    RGN_RUSTY_BUCKET_BAY: BKRegionData([]),

    # CCW hub connects to 4 season sub-regions
    RGN_CLICK_CLOCK_WOOD: BKRegionData([
        RGN_CCW_SPRING,
        RGN_CCW_SUMMER,
        RGN_CCW_AUTUMN,
        RGN_CCW_WINTER,
    ]),
    RGN_CCW_SPRING: BKRegionData([]),
    RGN_CCW_SUMMER: BKRegionData([]),
    RGN_CCW_AUTUMN:   BKRegionData([]),
    RGN_CCW_WINTER: BKRegionData([]),
}