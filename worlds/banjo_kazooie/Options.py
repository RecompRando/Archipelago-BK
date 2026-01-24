from dataclasses import dataclass

from typing import Dict

from Options import Choice, Option, DefaultOnToggle, Toggle, Range, OptionList, StartInventoryPool, DeathLink, PerGameCommonOptions


class LogicDifficulty(Choice):
    """Set the logic difficulty used when generating."""
    display_name = "Logic Difficulty"
    # ~ option_easy = 0
    option_normal = 1
    #option_obscure_glitchless = 2
    #option_glitched = 3
    option_no_logic = 4
    # ~ alias_baby = option_easy
    default = 1


class Notesanity(Toggle):
    """Set whether notes will be shuffled."""
    display_name = "Notesanity"

class Talonlobby(Toggle):
    """Set whether the player is able to climb the 50 note door slope without talon trot."""
    display_name = "Talonlobby"

# class Eggsanity(Toggle):
#     """Set whether blue eggs will be shuffled."""
#     display_name = "Eggsanity"

# class Feathersanity(Toggle):
#     """Set whether red feathers will be shuffled."""
#     display_name = "Feathersanity"

class ExtraLocations(Toggle):
    """Set whether extra locations will be shuffled.
    
    Prevents generation failures."""
    display_name = "Extra Locations"

@dataclass
class BKOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    logic_difficulty: LogicDifficulty
    notesanity: Notesanity
    talon_lobby: Talonlobby
    # eggsanity: Eggsanity
    # feathersanity: Feathersanity
    extra_locations: ExtraLocations
