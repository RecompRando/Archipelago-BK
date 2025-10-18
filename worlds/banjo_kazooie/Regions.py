from typing import NamedTuple, Callable, List, Dict
from BaseClasses import CollectionState

from .Constants import *


class BKRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, BKRegionData] = {
    RGN_MENU: BKRegionData([RGN_SPIRAL_MOUNTAIN]),
    RGN_SPIRAL_MOUNTAIN: BKRegionData([RGN_GRUNTILDAS_LAIR]),
    RGN_GRUNTILDAS_LAIR: BKRegionData([RGN_MUMBOS_MOUNTAIN, RGN_TREASURE_TROVE_COVE, RGN_CLANKERS_CAVERN, RGN_BUBBLEGLOOP_SWAMP, RGN_FREEZEEZY_PEAK, RGN_GOBIS_VALLEY, RGN_MAD_MONSTER_MANSION, RGN_RUSTY_BUCKET_BAY, RGN_CLICK_CLOCK_WOOD]),
    RGN_MUMBOS_MOUNTAIN: BKRegionData([]),
    RGN_TREASURE_TROVE_COVE: BKRegionData([]),
    RGN_CLANKERS_CAVERN: BKRegionData([]),
    RGN_BUBBLEGLOOP_SWAMP: BKRegionData([]),
    RGN_FREEZEEZY_PEAK: BKRegionData([]),
    RGN_GOBIS_VALLEY: BKRegionData([]),
    RGN_MAD_MONSTER_MANSION: BKRegionData([]),
    RGN_RUSTY_BUCKET_BAY: BKRegionData([]),
    RGN_CLICK_CLOCK_WOOD: BKRegionData([])
}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit
