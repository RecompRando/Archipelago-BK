from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location, MultiWorld

from .Constants import *


class BKLocation(Location):
    game = "Banjo-Kazooie"


class BKLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable = lambda options: True
    locked_item: Optional[str] = None

location_data_table: Dict[str, BKLocationData] = {
    # ~ "Link's Inventory (Kokiri Sword)": BKLocationData(
        # ~ region="Gruntilda's Lair",
        # ~ address=0x3469420000037
    # ~ ),
    LOC_DEFEAT_GRUNTILDA: BKLocationData(
        region="Gruntilda's Lair",
        locked_item="Victory"
    ),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
code_to_location_table = {data.address: name for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}