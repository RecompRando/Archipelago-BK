import typing
from BaseClasses import Item, ItemClassification


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: ItemClassification
    quantity: int = 1


class BKItem(Item):
    game: str = "Banjo-Kazooie"


basic_moves_table = {
    "Jump": ItemData(0x0400000A, ItemClassification.progression),
    "Feathery Flap": ItemData(0x04000007, ItemClassification.progression),
    "Flap Flip": ItemData(0x04000008, ItemClassification.progression),
    "Swim": ItemData(0x0400000F, ItemClassification.progression),
    "Climb": ItemData(0x04000005, ItemClassification.progression),
    "Beak Barge": ItemData(0x04000000, ItemClassification.progression),
    "Claw Swipe": ItemData(0x04000004, ItemClassification.progression),
    "Roll": ItemData(0x0400000C, ItemClassification.progression),
    "Rat-A-Tat Rap": ItemData(0x0400000B, ItemClassification.progression)
}

learned_moves_table = {
    "Eggs": ItemData(0x04000006, ItemClassification.progression),
    "Talon Trot": ItemData(0x04000010, ItemClassification.progression),
    "Beak Buster": ItemData(0x04000002, ItemClassification.progression),
    "Flight": ItemData(0x04000009, ItemClassification.progression),
    "Shock Spring Jump": ItemData(0x0400000D, ItemClassification.progression),
    "Wonderwing": ItemData(0x04000012, ItemClassification.progression),
    "Stilt Stride": ItemData(0x0400000E, ItemClassification.progression),
    "Beak Bomb": ItemData(0x04000001, ItemClassification.progression),
    "Turbo Talon Trot": ItemData(0x04000011, ItemClassification.progression)
}

progression_item_table = {
    "Jiggy": ItemData(130018, ItemClassification.progression),
    "Mumbo Token": ItemData(130019, ItemClassification.progression_skip_balancing),
    "Note": ItemData(130020, ItemClassification.progression_skip_balancing)
}

useful_item_table = {
    "Empty Honeycomb Piece": ItemData(130021, ItemClassification.useful),
    "BLUEEGGS Cheato": ItemData(130022, ItemClassification.useful),
    "REDFEATHERS Cheato": ItemData(130023, ItemClassification.useful),
    "GOLDFEATHERS Cheato": ItemData(130024, ItemClassification.useful),
    "Double Health": ItemData(130025, ItemClassification.useful)
}

useless_item_table = {
    "Ice Key": ItemData(130026, ItemClassification.trap),
    "Pink Egg": ItemData(130027, ItemClassification.trap),
    "Blue Egg": ItemData(130028, ItemClassification.trap),
    "Cyan Egg": ItemData(130029, ItemClassification.trap),
    "Green Egg": ItemData(130030, ItemClassification.trap),
    "Red Egg": ItemData(130031, ItemClassification.trap),
    "Yellow Egg": ItemData(130032, ItemClassification.trap)
}

junk_item_table = {
    "Honeycomb": ItemData(130033, ItemClassification.filler),
    "Egg Refill": ItemData(130034, ItemClassification.filler),
    "Red Feathers Refill": ItemData(130035, ItemClassification.filler),
    "Gold Feathers Refill": ItemData(130036, ItemClassification.filler),
    "Extra Life": ItemData(130037, ItemClassification.filler)
}

jiggy_puzzle_table = {
    "MM Jiggy Puzzle": ItemData(None, ItemClassification.progression),
    "TTC Jiggy Puzzle": ItemData(None, ItemClassification.progression),
    "CC Jiggy Puzzle": ItemData(None, ItemClassification.progression),
    "BS Jiggy Puzzle": ItemData(None, ItemClassification.progression),
    "FP Jiggy Puzzle": ItemData(None, ItemClassification.progression),
    "GV Jiggy Puzzle": ItemData(None, ItemClassification.progression),
    "MMM Jiggy Puzzle": ItemData(None, ItemClassification.progression),
    "RBB Jiggy Puzzle": ItemData(None, ItemClassification.progression),
    "CCW Jiggy Puzzle": ItemData(None, ItemClassification.progression),
    "Final Boss Jiggy Puzzle": ItemData(None, ItemClassification.progression)
}

note_door_table = {
    "Note Door 1": ItemData(None, ItemClassification.progression),
    "Note Door 2": ItemData(None, ItemClassification.progression),
    "Note Door 3": ItemData(None, ItemClassification.progression),
    "Note Door 4": ItemData(None, ItemClassification.progression),
    "Note Door 5": ItemData(None, ItemClassification.progression),
    "Note Door 6": ItemData(None, ItemClassification.progression),
    "Note Door 7": ItemData(None, ItemClassification.progression),
    "Note Door 8": ItemData(None, ItemClassification.progression),
    "Note Door 9": ItemData(None, ItemClassification.progression)
}

witch_switch_table = {
    "MM Witch Switch": ItemData(None, ItemClassification.progression_skip_balancing),
    "TTC Witch Switch": ItemData(None, ItemClassification.progression_skip_balancing),
    "CC Witch Switch": ItemData(None, ItemClassification.progression_skip_balancing),
    "BS Witch Switch": ItemData(None, ItemClassification.progression_skip_balancing),
    "FP Witch Switch": ItemData(None, ItemClassification.progression_skip_balancing),
    "GV Witch Switch": ItemData(None, ItemClassification.progression_skip_balancing),
    "MMM Witch Switch": ItemData(None, ItemClassification.progression_skip_balancing),
    "RBB Witch Switch": ItemData(None, ItemClassification.progression_skip_balancing),
    "CCW Witch Switch": ItemData(None, ItemClassification.progression_skip_balancing)
}

transformation_table = {
    "Termite Transformation": ItemData(None, ItemClassification.progression),
    "Crocodile Transformation": ItemData(None, ItemClassification.progression),
    "Walrus Transformation": ItemData(None, ItemClassification.progression),
    "Pumpkin Transformation": ItemData(None, ItemClassification.progression),
    "Bee Transformation": ItemData(None, ItemClassification.progression)
}

misc_event_table = {
    "BLUEEGGS Cheato Rock Cleared": ItemData(None, ItemClassification.progression),
    "Toboggan Jiggy Flag": ItemData(None, ItemClassification.progression),
    "Boggy's First Race Jiggy Flag": ItemData(None, ItemClassification.progression),
    "Gobi's Jiggy Flag": ItemData(None, ItemClassification.progression),
    "Trunker's Jiggy Flag": ItemData(None, ItemClassification.progression),
    "Gobi's Honeycomb Flag": ItemData(None, ItemClassification.progression),
    "Water Level Switch 1": ItemData(None, ItemClassification.progression),
    "Water Level Switch 2": ItemData(None, ItemClassification.progression),
    "CCW Jiggy Podium Switch": ItemData(None, ItemClassification.progression),
    "Victory": ItemData(None, ItemClassification.progression)
}

item_table = {
    **basic_moves_table,
    **learned_moves_table,
    **progression_item_table,
    **useful_item_table,
    **useless_item_table,
    **junk_item_table,
    **jiggy_puzzle_table,
    **note_door_table,
    **witch_switch_table,
    **transformation_table,
    **misc_event_table
}
