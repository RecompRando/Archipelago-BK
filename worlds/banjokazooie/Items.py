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
    "Flight": ItemData(99999, ItemClassification.progression),
    "Shock Spring Jump": ItemData(99999, ItemClassification.progression),

}

progression_item_table = {
    "Jiggy": ItemData(140000, ItemClassification.progression),
    "Note": ItemData(140001, ItemClassification.progression),
    "Mumbo Token": ItemData(140002, ItemClassification.progression),
}

useful_item_table = {
    "Honeycomb Piece": ItemData(150000, ItemClassification.useful),
}