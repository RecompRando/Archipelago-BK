from typing import NamedTuple, Callable, List, Dict
from BaseClasses import CollectionState

from .Constants import *


class BKRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, BKRegionData] = {
    RGN_MENU: BKRegionData([RGN_SPIRAL_MOUNTAIN]),
    RGN_SPIRAL_MOUNTAIN: BKRegionData([RGN_GRUNTILDAS_LAIR]),
    RGN_GRUNTILDAS_LAIR: BKRegionData([RGN_MUMBOS_MOUNTAIN]),
    RGN_MUMBOS_MOUNTAIN: BKRegionData([])
}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit
