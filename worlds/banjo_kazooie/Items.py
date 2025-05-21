from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld

from .Constants import *


class BKItem(Item):
    game = "Banjo-Kazooie"


class BKItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable = lambda options: True


item_data_table: Dict[str, BKItemData] = {
    # ~ "Stray Fairy (Clock Town)": BKItemData(
        # ~ code=0x346942001007F,
        # ~ type=ItemClassification.progression,
        # ~ can_create=lambda options: options.fairysanity.value
    # ~ ),
    ITEM_VICTORY: BKItemData(
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
code_to_item_table = {data.code: name for name, data in item_data_table.items() if data.code is not None}
