from ...Options import Toggle, DefaultOnToggle, Range, Choice, DeathLink


class ShuffleMoves(Choice):
    """Shuffles moves into other molehills, or adds them to the item pool"""
    display_name = "Shuffle Moves"
    default = 1
    option_off = 0
    option_shuffle_molehills = 1
    option_movesanity = 2


class ShuffleBasicMoves(Toggle):
    """If checked, shuffles all basic moves, based on Shuffle Moves setting"""
    display_name = "Shuffle Basic Moves"


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


class LevelRandomizer(Toggle):
    """Randomizes most level entrances. Mad Monster Mansion cannot be randomized. If ShuffleMoves is disabled,
    the first level will always be Mumbo's Mountain"""
    display_name = "Level Randomizer"


class CorrectPads(DefaultOnToggle):
    """Some Shock Spring Pads and Flight Pads are always usable without learning the corresponding moves. If this is
    turned on, those pads will be replaced with regular pads that require those moves"""
    display_name = "Correct Pads"


class SkipFurnaceFun(Toggle):
    """Skips Furnace Fun entirely. When you get to it, the game will immediately behave as though you completed it"""
    display_name = "Skip Furnace Fun"


class NumberOfJiggies(Range):
    """How many jiggies exist. There will always be enough to open every level, complete the secret puzzle, and win the
    game. Level requirements will dynamically change based on the number of jiggies that exist"""
    range_start = 0
    range_end = 100
    default = 100


class NumberOfMumboTokens(Range):
    """How many Mumbo Tokens exist. There will always be enough to afford every transformation. Transformation
    requirements will dynamically change based on the number of Mumbo Tokens that exist"""
    range_start = 0
    range_end = 112
    default = 112


bk_options = {
    "shuffle_moves": ShuffleMoves,
    "shuffle_basic_moves": ShuffleBasicMoves,
    "shuffle_cheato": ShuffleCheato,
    "shuffle_secrets": ShuffleSecrets,
    "level_randomizer": LevelRandomizer,
    "correct_pads": CorrectPads,
    "number_of_jiggies": NumberOfJiggies,
    "number_of_mumbo_tokens": NumberOfMumboTokens,
    "death_link": DeathLink
}
