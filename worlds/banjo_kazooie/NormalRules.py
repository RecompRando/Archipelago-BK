from .Constants import *
from ..stardew_valley.data.villagers_data import andy_loves


# ~ def can_play_song(song, state, player):
    # ~ return state.has(song, player) and state.has("Ocarina of Time", player)

def rgn_connection_string(rgn1, rgn2):
    return str(rgn1) + " -> " + str(rgn2)

def get_region_rules(player, options):
    return {
        rgn_connection_string(RGN_SPIRAL_MOUNTAIN, RGN_GRUNTILDAS_LAIR):
            lambda state: True,
        rgn_connection_string(RGN_GRUNTILDAS_LAIR, RGN_MUMBOS_MOUNTAIN):
            lambda state: state.has(ITEM_JIGGY, player),
    }

def get_location_rules(player, options):
    return {
        LOC_JIGGY_GL_ENTRYWAY:
            lambda state: True,
        LOC_JIGGY_GL_ATOP_MUMBOS_MOUNTAIN:
            lambda state:
                state.has(ITEM_TERMITE_TRANSFORMATION, player),
        LOC_JIGGY_GL_TTC_CANNON:
            lambda state:
                state.has(ITEM_FLAP_FLIP, player),
        LOC_JIGGY_GL_EYE_SWITCHES:
            lambda state:
                state.has(ITEM_BEAK_BUSTER, player),
        LOC_JIGGY_MM_CONGA_ORANGE_THROW:
            lambda state: True,
        LOC_JIGGY_MM_CHIMPY_ORANGE:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_MM_CONGA_ATTACK:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_MM_STONEHENGE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_TERMITE_TRANSFORMATION, player)
            ),
        LOC_JIGGY_MM_HILLSIDE:
            lambda state: True,
        LOC_JIGGY_MM_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_JIGGY_MM_TOTEM_POLE:
            lambda state:
            (
                state.has(ITEM_EGGS, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_JIGGY_MM_HUT:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_JIGGY_MM_MOUNTAINTOP:
            lambda state:
            (
                state.has(ITEM_TERMITE_TRANSFORMATION, player)
            ),
        LOC_JIGGY_MM_JINJO:
            lambda state:
            (
                state.has(ITEM_MM_BLUE_JINJO, player) and
                state.has(ITEM_MM_GREEN_JINJO, player) and
                state.has(ITEM_MM_ORANGE_JINJO, player) and
                state.has(ITEM_MM_PURPLE_JINJO, player) and
                state.has(ITEM_MM_YELLOW_JINJO, player)
            ),
        LOC_JIGGY_TTC_NIPPER:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_WONDERWING, player)
                )
                and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_JIGGY_TTC_BLUBBER:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_TTC_SANDCASTLE:
            lambda state:
            (
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_JIGGY_TTC_SHOCK_SPRING: (
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) or
                state.has(ITEM_FLIGHT, player)
            )
        ),
        LOC_JIGGY_TTC_X_MARK: (
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_FLIGHT, player)
            )
        ),
        LOC_JIGGY_TTC_POOL:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_TTC_CLIFFSIDE:
            lambda state: True, #requires taking damage with no moves
        LOC_JIGGY_TTC_LOCKUP:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JIGGY_TTC_LIGHTHOUSE:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JIGGY_TTC_JINJO:
            lambda state:
            (
                state.has(ITEM_TTC_BLUE_JINJO, player) and
                state.has(ITEM_TTC_GREEN_JINJO, player) and
                state.has(ITEM_TTC_ORANGE_JINJO, player) and
                state.has(ITEM_TTC_PURPLE_JINJO, player) and
                state.has(ITEM_TTC_YELLOW_JINJO, player)
            ),
        LOC_JIGGY_CC_CLANKER_RAISE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_CC_CLANKER_TAIL:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_EGGS, player) and
                        (
                            state.has(ITEM_FLAP_FLIP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player)
                        )
                    )
                )
            ),
        LOC_JIGGY_CC_CLANKER_BOLT:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    )
                )
            ),
        LOC_JIGGY_CC_CLANKER_GOLD_TEETH:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_CC_CLANKER_BLOWHOLE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_CC_WONDERWING:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_JIGGY_CC_STOMACH_RINGS:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_JIGGY_CC_SNIPPET:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    )
                )
                and
                (
                    state.has(ITEM_CLAW_SWIPE, player) or
                    state.has(ITEM_ROLL, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_EGGS, player) or
                    state.has(ITEM_WONDERWING, player)
                )
            ),
        LOC_JIGGY_CC_UNDERWATER_TUNNEL:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_CC_JINJO:
            lambda state:
            (
                state.has(ITEM_CC_BLUE_JINJO, player) and
                state.has(ITEM_CC_GREEN_JINJO, player) and
                state.has(ITEM_CC_ORANGE_JINJO, player) and
                state.has(ITEM_CC_PURPLE_JINJO, player) and
                state.has(ITEM_CC_YELLOW_JINJO, player)
            ),
        LOC_JIGGY_BGS_EGG:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_RAT_A_TAT_RAP, player) and
                state.has(ITEM_BEAK_BARGE, player)
            ),
        LOC_JIGGY_BGS_CENTER_RACE:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_JIGGY_BGS_FLIBBET:
            lambda state:
            (
                state.has(ITEM_CLAW_SWIPE, player) or
                state.has(ITEM_ROLL, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or
                state.has(ITEM_BEAK_BUSTER, player) or
                state.has(ITEM_EGGS, player) or
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_JIGGY_BGS_TANKTUP:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_TIPTUP:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_HUT:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_MUMBOS_HUT_RACE:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    state.has(ITEM_STILT_STRIDE, player) or
                    state.has(ITEM_WONDERWING, player)
                )
            ),
        LOC_JIGGY_BGS_CROCTUS:
            lambda state:
            (
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player),
            ),
        LOC_JIGGY_BGS_MR_VILE:
            lambda state:
            (
                state.has(ITEM_CROCODILE_TRANSFORMATION, player)
            ),
        LOC_JIGGY_BGS_JINJO:
            lambda state:
            (
                    state.has(ITEM_BGS_BLUE_JINJO, player) and
                    state.has(ITEM_BGS_GREEN_JINJO, player) and
                    state.has(ITEM_BGS_ORANGE_JINJO, player) and
                    state.has(ITEM_BGS_PURPLE_JINJO, player) and
                    state.has(ITEM_BGS_YELLOW_JINJO, player)
            ),
        LOC_JIGGY_FP_SIR_SLUSH:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_JIGGY_FP_SNOWMAN_PIPE:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_TALON_TROT, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_JIGGY_FP_TOBOGGAN:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_JIGGY_FP_SNOWMAN_BUTTONS:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_JIGGY_FP_CHRISTMAS_TREE:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_CLIMB, player) and #tree behavior when climb isn't unlocked?
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP)
                )
            ),
        LOC_JIGGY_FP_WOZZA:
            lambda state:
            (
                state.has(ITEM_WALRUS_TRANSFORMATION, player)
            ),
        LOC_JIGGY_FP_PRESENTS:
            lambda state:
            (
                state.has(ITEM_RED_PRESENT, player) and
                state.has(ITEM_BLUE_PRESENT, player) and
                state.has(ITEM_GREEN_PRESENT, player)
            ),
        LOC_JIGGY_FP_BOGGY_RACE_1:
            lambda state:
            (
                state.has(ITEM_WALRUS_TRANSFORMATION, player)
            ),
        LOC_JIGGY_FP_BOGGY_RACE_2:
            lambda state:
            (
                state.has(ITEM_WALRUS_TRANSFORMATION, player) and
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_JIGGY_FP_JINJO:
            lambda state:
            (
                    state.has(ITEM_FP_BLUE_JINJO, player) and
                    state.has(ITEM_FP_GREEN_JINJO, player) and
                    state.has(ITEM_FP_ORANGE_JINJO, player) and
                    state.has(ITEM_FP_PURPLE_JINJO, player) and
                    state.has(ITEM_FP_YELLOW_JINJO, player)
            ),
        LOC_DEFEAT_GRUNTILDA:
            lambda state: True,
    }
