###################
##### IMPORTS #####
###################

from ..generic.Rules import set_rule
from BaseClasses import MultiWorld, CollectionState
from .Locations import location_table
from .Regions import connect_regions

from .BK_Enums import BK_Str_Enums
from .BK_Requirement_Dict import JIGGY_REQUIREMENT_DICT, NOTE_REQUIREMENT_DICT

#####################
##### FUNCTIONS #####
#####################

def can_access_location(world: MultiWorld, state: "CollectionState", player: int, location: str, locations):
    '''
    Checks whether the player has access to a specific location.
    For that location, it checks whether the number of Mumbo Tokens,
    Jiggies, Notes, and other requirements are met.

    Returns a boolean whether the player can access the location.
    '''
    for requirements in locations[location].requirements:
        fulfills_requirements:bool = True
        for requirement in requirements:
            if requirement.startswith(BK_Str_Enums.MUMBO_TOKEN_AMOUNT):
                if not state.has(BK_Str_Enums.MUMBO_TOKEN, player, int(world.number_of_mumbo_tokens[player].value * 0.66)):
                    fulfills_requirements:bool = False
            elif requirement in JIGGY_REQUIREMENT_DICT:
                if not state.has(BK_Str_Enums.JIGGY, player, JIGGY_REQUIREMENT_DICT[requirement]):
                    fulfills_requirements:bool = False
            elif requirement in NOTE_REQUIREMENT_DICT:
                if not state.has(BK_Str_Enums.NOTE, player, NOTE_REQUIREMENT_DICT[requirement]):
                    fulfills_requirements:bool = False
            elif not state.has(requirement, player):
                fulfills_requirements:bool = False
        if fulfills_requirements:
            return True
    return False

def set_location_rules(world: MultiWorld, player: int):
    '''
    Sets the criteria(s) needed to access a location.
    '''
    for location, data in location_table.items():
        if data.requirements:
            set_rule(world.get_location(location, player),
                     lambda state: can_access_location(world, state, player, location, location_table))

def set_rules(world: MultiWorld, player: int, level_entrances: list[list[str, int]]):
    '''
    Connects each location of the world by their access requirements.
    '''
    connect_regions(world, player, BK_Str_Enums.MENU, BK_Str_Enums.GRUNTYS_LAIR_1F)
    # ~ connect_regions(world, player, BK_Str_Enums.MENU, BK_Str_Enums.SPIRAL_MOUNTAIN)
    # ~ connect_regions(world, player, BK_Str_Enums.SPIRAL_MOUNTAIN, BK_Str_Enums.GRUNTYS_LAIR_1F)
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_1F, level_entrances[0][0], lambda state: state.has(
        # ~ BK_Str_Enums.MM_JIGGY_PUZZLE, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_1F, BK_Str_Enums.GRUNTYS_LAIR_2F, lambda state: state.has(
        # ~ BK_Str_Enums.TALON_TROT, player) and state.has(BK_Str_Enums.NOTE_DOOR_1, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_2F, level_entrances[1][0], lambda state: state.has(
        # ~ BK_Str_Enums.TTC_JIGGY_PUZZLE, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_2F, BK_Str_Enums.GRUNTYS_LAIR_3F, lambda state: state.has(
        # ~ BK_Str_Enums.FLAP_FLIP, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_3F, level_entrances[2][0], lambda state: state.has(
        # ~ BK_Str_Enums.CC_JIGGY_PUZZLE, player) and state.has(BK_Str_Enums.BEAK_BUSTER, player) and (state.has(BK_Str_Enums.FEATHERY_FLAP, player) or
                                                                                                   # ~ state.has(BK_Str_Enums.RAT_A_TAP_RAP, player) or
                                                                                                   # ~ state.has(BK_Str_Enums.TALON_TROT, player)))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_2F, BK_Str_Enums.GRUNTYS_LAIR_4F, lambda state: state.has(
        # ~ BK_Str_Enums.TALON_TROT, player) and state.has(BK_Str_Enums.NOTE_DOOR_2, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_4F, level_entrances[3][0], lambda state: state.has(
        # ~ BK_Str_Enums.BS_JIGGY_PUZZLE, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_4F, BK_Str_Enums.GRUNTYS_LAIR_5F, lambda state: state.has(
        # ~ BK_Str_Enums.SHOCK_SPRING_JUMP, player) and state.has(BK_Str_Enums.NOTE_DOOR_3, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_5F, level_entrances[4][0], lambda state: state.has(
        # ~ BK_Str_Enums.FP_JIGGY_PUZZLE, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_5F, level_entrances[5][0], lambda state: state.has(
        # ~ BK_Str_Enums.GV_JIGGY_PUZZLE, player) and state.has(BK_Str_Enums.STILT_STRIDE, player) and (state.has(BK_Str_Enums.BEAK_BARGE, player) or
                                                                                                    # ~ state.has(BK_Str_Enums.RAT_A_TAP_RAP, player) or
                                                                                                    # ~ state.has(BK_Str_Enums.EGGS, player)))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_5F, BK_Str_Enums.GRUNTYS_LAIR_6F, lambda state: state.has(
        # ~ BK_Str_Enums.NOTE_DOOR_4, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_6F, level_entrances[6][0], lambda state: state.has(
        # ~ BK_Str_Enums.MMM_JIGGY_PUZZLE, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_5F, BK_Str_Enums.GRUNTYS_LAIR_7F, lambda state: state.has(
        # ~ BK_Str_Enums.NOTE_DOOR_5, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_7F, level_entrances[7][0], lambda state: state.has(
        # ~ BK_Str_Enums.RBB_JIGGY_PUZZLE, player) and state.has(BK_Str_Enums.WATER_LEVEL_SWITCH_1, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_7F, BK_Str_Enums.GRUNTYS_LAIR_8F, lambda state: state.has(
        # ~ BK_Str_Enums.NOTE_DOOR_6, player) and state.has(BK_Str_Enums.WATER_LEVEL_SWITCH_1, player) and state.has(
        # ~ BK_Str_Enums.WATER_LEVEL_SWITCH_2, player) and (state.has(BK_Str_Enums.FLAP_FLIP, player) or (state.has(BK_Str_Enums.RAT_A_TAP_RAP, player) and
                                                                                                      # ~ state.has(BK_Str_Enums.BEAK_BUSTER, player)) or
                                                       # ~ (state.has(BK_Str_Enums.EGGS, player) and
                                                        # ~ state.has(BK_Str_Enums.BEAK_BUSTER, player))))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_8F, level_entrances[8][0], lambda state: state.has(
        # ~ BK_Str_Enums.CCW_JIGGY_PUZZLE, player) and state.has(BK_Str_Enums.TALON_TROT, player))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_8F, BK_Str_Enums.GRUNTYS_LAIR_FURNACE_FUN, lambda state: state.has(
        # ~ BK_Str_Enums.NOTE_DOOR_7, player) and (state.has(BK_Str_Enums.FLAP_FLIP, player) or state.has(BK_Str_Enums.BEE_TRANSFORMATION, player) or
                                              # ~ (state.has(BK_Str_Enums.TALON_TROT, player) and state.has(BK_Str_Enums.FLIGHT, player))))
    # ~ connect_regions(world, player, BK_Str_Enums.GRUNTYS_LAIR_FURNACE_FUN, BK_Str_Enums.GRUNTYS_LAIR_TOP_FLOOR, lambda state: state.has(
        # ~ BK_Str_Enums.NOTE_DOOR_8, player))

    set_location_rules(world, player)