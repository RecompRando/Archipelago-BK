import typing

from BaseClasses import Item, ItemClassification


class ItemData(typing.NamedTuple):
    name: str
    classification: ItemClassification
    quantity: int


class BKItem(Item):
    game: str = "Banjo-Kazooie"


basic_ability_table = {
    "Jump": ItemData(13000)
}