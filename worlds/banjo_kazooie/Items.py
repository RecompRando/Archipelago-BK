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
    "Jump": BKItemData(
        code=0x0400000A,
        type=ItemClassification.progression
    ),
    "Feathery Flap": BKItemData(
        code=0x04000007,
        type=ItemClassification.progression
    ),
    "Flap Flip": BKItemData(
        code=0x04000008,
        type=ItemClassification.progression
    ),
    "Swim": BKItemData(
        code=0x0400000F,
        type=ItemClassification.progression
    ),
    "Climb": BKItemData(
        code=0x04000005,
        type=ItemClassification.progression
    ),
    "Beak Barge": BKItemData(
        code=0x04000000,
        type=ItemClassification.progression
    ),
    "Claw Swipe": BKItemData(
        code=0x04000004,
        type=ItemClassification.progression
    ),
    "Roll": BKItemData(
        code=0x0400000C,
        type=ItemClassification.progression
    ),
    "Rat-A-Tat Rap": BKItemData(
        code=0x0400000B,
        type=ItemClassification.progression
    ),
    "Eggs": BKItemData(
        code=0x04000006,
        type=ItemClassification.progression
    ),
    "Talon Trot": BKItemData(
        code=0x04000010,
        type=ItemClassification.progression
    ),
    "Talon Trot Speed Upgrade": BKItemData(
        code=0x04000011,
        type=ItemClassification.progression
    ),
    "Beak Buster": BKItemData(
        code=0x04000002,
        type=ItemClassification.progression
    ),
    "Flight": BKItemData(
        code=0x04000009,
        type=ItemClassification.progression
    ),
    "Shock Spring Jump": BKItemData(
        code=0x0400000D,
        type=ItemClassification.progression
    ),
    "Wonderwing": BKItemData(
        code=0x04000012,
        type=ItemClassification.progression
    ),
    "Stilt Stride": BKItemData(
        code=0x0400000E,
        type=ItemClassification.progression
    ),
    "Beak Bomb": BKItemData(
        code=0x04000001,
        type=ItemClassification.progression
    ),
    "Turbo Talon Trot": BKItemData(
        code=0x04000011,
        type=ItemClassification.progression
    ),
    "Jiggy": BKItemData(
        code=0x0001FBE2,
        type=ItemClassification.progression,
        num_exist=100
    ),
    "Mumbo Token": BKItemData(
        code=0x0001FBE3,
        type=ItemClassification.progression,
        num_exist=116
    ),
    "Note": BKItemData(
        code=0x0001FBE4,
        type=ItemClassification.progression,
        num_exist=900
    ),
    "Empty Honeycomb Piece": BKItemData(
        code=0x0001FBE5,
        type=ItemClassification.useful,
        num_exist=24
    ),
    "Acorn": BKItemData(
        code=0x0001FBE5,
        type=ItemClassification.useful,
        num_exist=24
    ),
    "BLUEEGGS Cheato": BKItemData(
        code=0x0001FBE6,
        type=ItemClassification.useful,
        can_create=lambda options: False
    ),
    "REDFEATHERS Cheato": BKItemData(
        code=0x0001FBE7,
        type=ItemClassification.useful,
        can_create=lambda options: False
    ),
    "GOLDFEATHERS Cheato": BKItemData(
        code=0x0001FBE8,
        type=ItemClassification.useful,
        can_create=lambda options: False
    ),
    "Double Health": BKItemData(
        code=0x0001FBE9,
        type=ItemClassification.useful
    ),
    "Ice Key": BKItemData(
        code=0x0001FBEA,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    "Pink Egg": BKItemData(
        code=0x0001FBEB,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    "Blue Egg": BKItemData(
        code=0x0001FBEC,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    "Cyan Egg": BKItemData(
        code=0x0001FBED,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    "Green Egg": BKItemData(
        code=0x0001FBEE,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    "Red Egg": BKItemData(
        code=0x0001FBEF,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    "Yellow Egg": BKItemData(
        code=0x0001FBF0,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    "Honeycomb": BKItemData(
        code=0x0001FBF1,
        type=ItemClassification.filler,
        can_create=lambda options: False
    ),
    ITEM_EGG_REFILL: BKItemData(
        code=0x0001FBF2,
        type=ItemClassification.filler,
        can_create=lambda options: False
    ),
    ITEM_REDFEATHER_REFILL: BKItemData(
        code=0x0001FBF3,
        type=ItemClassification.filler,
        can_create=lambda options: False
    ),
    ITEM_GOLDFEATHER_REFILL: BKItemData(
        code=0x0001FBF4,
        type=ItemClassification.filler,
        can_create=lambda options: False
    ),
    "Extra Life": BKItemData(
        code=0x0001FBF5,
        type=ItemClassification.filler,
        can_create=lambda options: False
    ),
    ITEM_VICTORY: BKItemData(
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
code_to_item_table = {data.code: name for name, data in item_data_table.items() if data.code is not None}
