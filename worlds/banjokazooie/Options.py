import typing
from ...Options import Option, Toggle, DefaultOnToggle, Range, Choice, DeathLink


class ShuffleMumboTokens(DefaultOnToggle):
    """Shuffles all Mumbo Tokens into the item pool, and includes Mumbo Token locations in randomization"""
    display_name = "Shuffle Mumbo Tokens"


class ShuffleEmptyHoneycombs(DefaultOnToggle):
    """Shuffles all Empty Honeycombs into the item pool, and includes Empty Honeycomb locations in randomization"""
    display_name = "Shuffle Empty Honeycombs"


class ShuffleCheato(Toggle):
    """Shuffles the three Cheato checks into the item pool, and includes Cheato locations in randomization"""
    display_name = "Shuffle Cheato"


class ShuffleSecrets(Choice):
    """Shuffles the six Giant Eggs and Ice Key into the pool, and includes Cheato locations in randomization. Open
    Locations has all of them available by default, while Closed Locations requires entering the appropriate codes in
    the Treasure Trove Cove Sandcastle Room"""
    display_name = "Shuffle Secrets"
    option_off = 0
    option_open_locations = 1
    option_closed_locations = 2


class ShuffleMoves(Choice):
    """Shuffles moves into other molehills, or adds them to the item pool"""
    display_name = "Shuffle Moves"
    option_off = 0
    option_shuffle_molehills = 1
    option_movesanity = 2


class ShuffleBasicMoves(Toggle):
    """If checked, shuffles all basic moves, based on Shuffle Moves setting"""
    display_name = "Shuffle Basic Moves"


class LevelRandomizer(Toggle):
    """Randomizes most level entrances. Mad Monster Mansion cannot be randomized. If ShuffleMoves is disabled,
    the first level will always be Mumbo's Mountain"""
    display_name = "Level Randomizer"


class NumberOfJiggies(Range):
    """How many jiggies exist. There will always be enough to win the game"""
    range_start = 94
    range_end = 100
    default = 100


class NumberOfMumboTokens(Range):
    """How many Mumbo Tokens exist. There will always be enough to afford every transformation. This only applies if
    Shuffle Mumbo Tokens is turned on"""
    range_start = 75
    range_end = 112
    default = 112


bk_options = {
    "shuffle_mumbo_tokens": ShuffleMumboTokens,
    "shuffle_empty_honeycombs": ShuffleEmptyHoneycombs,
    "shuffle_cheato": ShuffleCheato,
    "shuffle_secrets": ShuffleSecrets,
    "shuffle_moves": ShuffleMoves,
    "shuffle_basic_moves": ShuffleBasicMoves,
    "level_randomizer": LevelRandomizer,
    "number_of_jiggies": NumberOfJiggies,
    "number_of_mumbo_tokens": NumberOfMumboTokens,
    "death_link": DeathLink
}
