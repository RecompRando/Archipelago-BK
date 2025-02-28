from dataclasses import dataclass

from typing import Dict

from Options import Toggle, DefaultOnToggle, Range, DeathLink, PerGameCommonOptions


class ShuffleMoves(DefaultOnToggle):
    """Shuffles moves into the item pool"""
    display_name = "Shuffle Moves"


class ShuffleBasicMoves(Toggle):
    """Shuffles basic moves into the item pool"""
    display_name = "Shuffle Basic Moves"


class ShuffleCheato(Toggle):
    """Shuffles the three Cheato checks into the item pool, and includes Cheato locations in randomization"""
    display_name = "Shuffle Cheato"


class ShuffleSecrets(Toggle):
    """Shuffles the six Giant Eggs and Ice Key into the pool, and includes Cheato locations in randomization. If
    enabled, all secret locations are available by default"""
    display_name = "Shuffle Secrets"


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


class RemoveNoteDoors(Toggle):
    """Removes all Note Doors from the game"""
    display_name = "Remove Note Doors"


class NumberOfJiggies(Range):
    """How many Jiggies exist. There will always be enough to open every level, complete the secret puzzle, and win the
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

@dataclass
class BKOptions(PerGameCommonOptions):
    shuffle_moves: ShuffleMoves
    shuffle_basic_moves: ShuffleBasicMoves
    shuffle_cheato: ShuffleCheato
    shuffle_secrets: ShuffleSecrets
    level_randomizer: LevelRandomizer
    correct_pads: CorrectPads
    skip_furnace_fun: SkipFurnaceFun
    remove_note_doors: RemoveNoteDoors
    number_of_jiggies: NumberOfJiggies
    number_of_mumbo_tokens: NumberOfMumboTokens
    death_link: DeathLink
