import typing
from BaseClasses import Item, ItemClassification


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: ItemClassification
    quantity: int = 1


class BKItem(Item):
    game: str = "Banjo-Kazooie"


basic_ability_table = {
    "Jump": ItemData(130000, ItemClassification.progression),
    "Feathery Flap": ItemData(130001, ItemClassification.progression),
    "Flap Flip": ItemData(130002, ItemClassification.progression),
    "Swim": ItemData(130003, ItemClassification.progression),
    "Climb": ItemData(130004, ItemClassification.progression),
    "Beak Barge": ItemData(130005, ItemClassification.progression),
    "Claw Swipe": ItemData(130006, ItemClassification.progression),
    "Roll": ItemData(130007, ItemClassification.progression),
    "Rat-A-Tat Rap": ItemData(130008, ItemClassification.progression),
}

learned_ability_table = {
    "Eggs": ItemData(130009, ItemClassification.progression),
    "Talon Trot": ItemData(130010, ItemClassification.progression),
    "Beak Buster": ItemData(130011, ItemClassification.progression),
    "Flight": ItemData(130012, ItemClassification.progression),
    "Shock Spring Jump": ItemData(130013, ItemClassification.progression),
    "Wonderwing": ItemData(130014, ItemClassification.progression),
    "Stilt Stride": ItemData(130015, ItemClassification.progression),
    "Beak Bomb": ItemData(130016, ItemClassification.progression),
    "Turbo Talon Trot": ItemData(130016, ItemClassification.progression)
}

progression_item_table = {
    "Jiggy": ItemData(130017, ItemClassification.progression_skip_balancing),
    "Mumbo Token": ItemData(130018, ItemClassification.progression_skip_balancing),
}

useful_item_table = {
    "Honeycomb Piece": ItemData(130019, ItemClassification.useful),
}

junk_item_table = {
    "Honeycomb": ItemData(130020, ItemClassification.filler),
    "20 Eggs": ItemData(130021, ItemClassification.filler),
    "10 Red Feathers": ItemData(130022, ItemClassification.filler),
    "5 Gold Feathers": ItemData(130023, ItemClassification.filler),
    "Extra Life": ItemData(130024, ItemClassification.filler)
}

item_table = {
    **basic_ability_table,
    **learned_ability_table,
    **progression_item_table,
    **useful_item_table,
    **junk_item_table
}
