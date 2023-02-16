import typing

from ...Options import Option, Toggle, DefaultOnToggle, Range, Choice, DeathLink


class SafetyChecks(DefaultOnToggle):
    """Prevents you from getting stuck in certain areas. If disabled, you can still get out by dying or savewarping"""
    display_name = "Safety Checks"


class AdvancedTricks(Toggle):
    """Considers some advanced tricks in logic, such as Flap Flipping midair"""
    display_name = "Advanced Tricks"


class ShuffleMumboTokens(Toggle):
    """Shuffles all Mumbo Tokens into the item pool, and includes Mumbo Token locations in randomization"""
    display_name = "Shuffle Mumbo Tokens"


class ShuffleMoves(Choice):
    """Shuffles moves to other molehills, or adds them to the item pool"""
    display_name = "Shuffle Moves"
    option_Off = 0
    option_shuffle_molehills = 1
    option_movesanity = 2


class ShuffleBasicMoves(Toggle):
    """If checked, shuffles all basic moves, based on Shuffle Moves setting"""
    display_name = "Shuffle Basic Moves"


class LevelRandomizer(Toggle):
    """Randomizes some level entrances. Due to transformation limitations, Mumbo's Mountain and Bubblegloop Swamp can
    only shuffle between each other, and Mad Monster Mansion and Click Clock Wood cannot be randomized"""
    display_name = "Level Randomizer"


class NumberOfJiggies(Range):
    """How many jiggies exist. There will always be enough to win the game"""
    range_start = 94
    range_end = 100
    default = 100


class NumberOfMumboTokens(Range):
    """How many Mumbo Tokens exist. There will always be enough to afford every transformation"""
    range_start = 75
    range_end = 113
    default = 113


class NoteDoor1Cost(Range):
    """How many notes are required to open the first Note Door"""
    range_start = 0
    range_end = 100
    default = 50


class NoteDoor2Cost(Range):
    """How many notes are required to open the second Note Door"""
    range_start = 0
    range_end = 300
    default = 180


class NoteDoor3Cost(Range):
    """How many notes are required to open the third Note Door"""
    range_start = 0
    range_end = 400
    default = 260


class NoteDoor4Cost(Range):
    """How many notes are required to open the fourth Note Door"""
    range_start = 0
    range_end = 500
    default = 350


class NoteDoor5Cost(Range):
    """How many notes are required to open the fifth Note Door"""
    range_start = 0
    range_end = 600
    default = 450


class NoteDoor6Cost(Range):
    """How many notes are required to open the sixth Note Door"""
    range_start = 0
    range_end = 800
    default = 640


class NoteDoor7Cost(Range):
    """How many notes are required to open the seventh Note Door"""
    range_start = 0
    range_end = 900
    default = 765


class NoteDoor8Cost(Range):
    """How many notes are required to open the eighth Note Door"""
    range_start = 0
    range_end = 900
    default = 810


class NoteDoor9Cost(Range):
    """How many notes are required to open the ninth Note Door"""
    range_start = 0
    range_end = 900
    default = 828


class NoteDoor10Cost(Range):
    """How many notes are required to open the tenth Note Door"""
    range_start = 0
    range_end = 900
    default = 846


class NoteDoor11Cost(Range):
    """How many notes are required to open the eleventh Note Door"""
    range_start = 0
    range_end = 900
    default = 864


class NoteDoor12Cost(Range):
    """How many notes are required to open the twelfth Note Door"""
    range_start = 0
    range_end = 900
    default = 882


bk_options: typing.Dict[str, type(Option)] = {
    "SafetyChecks": SafetyChecks,
    "AdvancedTricks": AdvancedTricks,
    "MumboShuffle": ShuffleMumboTokens,
    "MoveShuffle": ShuffleMoves,
    "BasicMoveShuffle": ShuffleBasicMoves,
    "LevelRandomizer": LevelRandomizer,
    "NumberOfJiggies": NumberOfJiggies,
    "NumberOfMumboTokens": NumberOfMumboTokens,
    "NoteDoor1Cost": NoteDoor1Cost,
    "NoteDoor2Cost": NoteDoor2Cost,
    "NoteDoor3Cost": NoteDoor3Cost,
    "NoteDoor4Cost": NoteDoor4Cost,
    "NoteDoor5Cost": NoteDoor5Cost,
    "NoteDoor6Cost": NoteDoor6Cost,
    "NoteDoor7Cost": NoteDoor7Cost,
    "NoteDoor8Cost": NoteDoor8Cost,
    "NoteDoor9Cost": NoteDoor9Cost,
    "NoteDoor10Cost": NoteDoor10Cost,
    "NoteDoor11Cost": NoteDoor11Cost,
    "NoteDoor12Cost": NoteDoor12Cost,
    "DeathLink": DeathLink
}
