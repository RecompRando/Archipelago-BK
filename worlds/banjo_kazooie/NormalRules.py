from .Constants import *

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
            (
                state.has(ITEM_TERMITE_TRANSFORMATION, player)
            ),
        LOC_JIGGY_GL_TTC_CANNON:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_JIGGY_GL_EYE_SWITCHES:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_GL_ABOVE_FP:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JIGGY_GL_SARCOPHAGUS:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) or
                (
                    state.has(ITEM_FLAP_FLIP, player) and   #Requires somewhat specific timing
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_JIGGY_GL_GRUNTYS_EYE:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_FEATHERY_FLAP, player)
                    ) or
                    (
                        state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                        state.has(ITEM_BEAK_BUSTER, player) and
                        state.has(ITEM_TURBO_TALON_TROT, player) and
                        state.has(ITEM_FLIGHT, player)
                    )
                ) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player) or
                    state.has(ITEM_WONDERWING, player) or
                    (
                        state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                        state.has(ITEM_BEAK_BUSTER, player) and
                        state.has(ITEM_TURBO_TALON_TROT, player) and
                        state.has(ITEM_FLIGHT, player) and
                        state.has(ITEM_BEAK_BOMB, player)
                    )
                )
            ),
        LOC_JIGGY_GL_WATER_SWITCH:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_GL_BEE_TREE:
            lambda state:
            (
                state.has(ITEM_BEE_TRANSFORMATION, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or  # required to access Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                )
            ),
        LOC_JIGGY_MM_CONGA_ORANGE_THROW:
            lambda state: True,
        LOC_JIGGY_MM_CHIMPY_ORANGE:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_CLIMB, player) or
                (
                    state.has(ITEM_JUMP, player) and    #can reach orange with good timing
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_JIGGY_MM_CONGA_ATTACK:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_MM_STONEHENGE:
            lambda state: True, #you can just mash shorthop, it's not hard:P
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
                    state.has(ITEM_FLAP_FLIP, player) or    #required to get on the platform
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
                    state.has(ITEM_FLAP_FLIP, player)    #required to get on top of the huts
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
                    state.has(ITEM_RAT_A_TAT_RAP, player) #can actually hurt him with Wonderwing as well
                )
                and
                (
                    state.has(ITEM_JUMP, player) or    #required to get the Jiggy
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_JIGGY_TTC_BLUBBER:
            lambda state:
            (
                state.has(ITEM_BLUBBER_GOLD, player, 2)
            ),
        LOC_JIGGY_TTC_SANDCASTLE:
            lambda state:
            (
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    state.has(ITEM_JUMP, player) or    #required to get the Jiggy
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
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach all Xs
                    (
                        state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            (
                                state.has(ITEM_JUMP, player) and
                                state.has(ITEM_TALON_TROT, player)
                            )
                        )
                    )
                )
            )
        ),
        LOC_JIGGY_TTC_POOL:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_TTC_CLIFFSIDE:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to get the Jiggy, some of which require falling
                state.has(ITEM_BEAK_BUSTER, player) or      #onto the platform
                state.has(ITEM_FLIGHT, player) or
                state.has(ITEM_WONDERWING, player)
            ),
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
                state.has(ITEM_SWIM, player)    #required to access most of the level
            ),
        LOC_JIGGY_CC_CLANKER_TAIL:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and    #required to access most of the level
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open the gate and/or get the Jiggy
                    (
                        state.has(ITEM_EGGS, player) and
                        (
                            state.has(ITEM_FLAP_FLIP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            (
                                state.has(ITEM_JUMP, player) and
                                state.has(ITEM_TALON_TROT, player)
                            )
                        )
                    )
                )
            ),
        LOC_JIGGY_CC_CLANKER_BOLT:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and    #required to access most of the level
                (
                    state.has(ITEM_FLAP_FLIP, player) or    #required to get the Jiggy
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ),
        LOC_JIGGY_CC_CLANKER_GOLD_TEETH:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and    #required to access most of the level
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_CC_CLANKER_BLOWHOLE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)    #required to access most of the level
            ),
        LOC_JIGGY_CC_WONDERWING:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and    #required to access most of the level
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_JIGGY_CC_STOMACH_RINGS:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and    #required to access most of the level
                state.has(ITEM_FLAP_FLIP, player) and    #required to jump through all the rings
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_JIGGY_CC_SNIPPET:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and    #required to access most of the level
                (
                    state.has(ITEM_FLAP_FLIP, player) or    #required to get the Jiggy
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
                and
                (
                    state.has(ITEM_CLAW_SWIPE, player) or
                    state.has(ITEM_ROLL, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or    #required to defeat the Snippets
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_EGGS, player) or
                    state.has(ITEM_WONDERWING, player)
                )
            ),
        LOC_JIGGY_CC_UNDERWATER_TUNNEL:
            lambda state:
            (
                state.has(ITEM_SWIM, player)    #required to access most of the level
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
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or    #required to access most of the level
                    state.has(ITEM_TALON_TROT, player) or    #can fall from bridge without taking damage
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_ROLL, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_EGGS, player) or
                    state.has(ITEM_WONDERWING, player)
                )
            ),
        LOC_JIGGY_BGS_TANKTUP:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or    #required to access most of the level
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_TIPTUP:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or    #required to access most of the level
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_HUT:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or    #required to access most of the level/get on the huts
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_MUMBOS_HUT_RACE:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_JIGGY_BGS_CROCTUS:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or    #required to access most of the level
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_TALON_TROT, player) and    #required to reach all Croctus locations
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_MR_VILE:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
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
                state.has(ITEM_FLIGHT, player) or    #required to reach the snowman's scarf
                (
                    state.has(ITEM_TALON_TROT, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_JIGGY_FP_TOBOGGAN:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or    #required to reach the snowman's scarf
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
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or    #required to the Jiggy at the top of the tree
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP)
                )
            ),
        LOC_JIGGY_FP_WOZZA:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
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
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_WALRUS_TRANSFORMATION, player)
            ),
        LOC_JIGGY_FP_BOGGY_RACE_2:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull (Race 1 must be completed)
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
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
        LOC_JIGGY_GV_JINXY:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or   #required to get on top of Jinxy/jump across carpets
                    (
                        state.has(ITEM_JUMP, player) and    #some carpets have very strict jumps that need the height
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_GV_GRABBA:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_JIGGY_GV_FLIP_PANELS:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_GV_WATER_PYRAMID:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_GV_ANCIENT_ONES:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or   #required to get on top of Jinxy
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and    #fairly easy to get on top of him with these
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JIGGY_GV_RUBEE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or   #required to get on top of Jinxy
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and    #fairly easy to get on top of him with these
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_GV_SANDYBUTT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
            state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_GV_GOBI:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
            state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_GV_TRUNKER:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player) #Gobi's jiggy required first
            ) and
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    (
                        state.has(ITEM_CLIMB, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or    #to get on top of Trunker, you can either climb
                            state.has(ITEM_RAT_A_TAT_RAP, player) or    #up a nearby tree and jump across, or...
                            (
                                state.has(ITEM_JUMP, player) and
                                state.has(ITEM_TALON_TROT, player)
                            )
                        )
                    ) or
                    (
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or  #...get to the flight pad and fly over
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            (
                                state.has(ITEM_JUMP, player) and
                                state.has(ITEM_TALON_TROT, player)
                            )
                        ) and
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_FLIGHT, player)
                    )
                )
            ),
        LOC_JIGGY_GV_JINJO:
            lambda state:
            (
                state.has(ITEM_GV_BLUE_JINJO, player) and
                state.has(ITEM_GV_GREEN_JINJO, player) and
                state.has(ITEM_GV_ORANGE_JINJO, player) and
                state.has(ITEM_GV_PURPLE_JINJO, player) and
                state.has(ITEM_GV_YELLOW_JINJO, player)
            ),
        LOC_JIGGY_MMM_NAPPER:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_JUMP, player) or         #required to hop along the chairs
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or    #yes, it's possible, and not really that difficult
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_JIGGY_MMM_CELLAR:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_MMM_TUMBLAR:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_MMM_WELL:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    state.has(ITEM_PUMPKIN_TRANSFORMATION, player) and
                    state.has(ITEM_FLAP_FLIP, player) and   #required to get to Mumbo's Skull
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                        state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_JIGGY_MMM_FLOWERPOT:
            lambda state:
            (
                state.has(ITEM_EGGS, player)
            ),
        LOC_JIGGY_MMM_CLOCK_TOWER:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to open church gate
                    state.has(ITEM_BEAK_BARGE, player) or  # Wonderwing also works
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_JIGGY_MMM_MOTZAND:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to open church gate
                    state.has(ITEM_BEAK_BARGE, player) or  # Wonderwing also works
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_JIGGY_MMM_LOGGO:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or        #required to break window
                    state.has(ITEM_EGGS, player)                    #Wonderwing also works
                )
                (
                    state.has(ITEM_PUMPKIN_TRANSFORMATION, player) and
                    state.has(ITEM_FLAP_FLIP, player) and           #required to get to Mumbo's Skull
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                        state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_JIGGY_MMM_STORM_DRAIN:
            lambda state:
            (
                state.has(ITEM_PUMPKIN_TRANSFORMATION, player) and
                state.has(ITEM_FLAP_FLIP, player) and           #required to get to Mumbo's Skull
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                    state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                    state.has(ITEM_EGGS, player)
                )

            ),
        LOC_JIGGY_MMM_JINJO:
            lambda state:
            (
                state.has(ITEM_MMM_BLUE_JINJO, player) and
                state.has(ITEM_MMM_GREEN_JINJO, player) and
                state.has(ITEM_MMM_ORANGE_JINJO, player) and
                state.has(ITEM_MMM_PURPLE_JINJO, player) and
                state.has(ITEM_MMM_YELLOW_JINJO, player)
            ),
        LOC_JIGGY_RBB_SMOKESTACK:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_JIGGY_RBB_WHISTLE:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or        #to get to the platform
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_RBB_WAREHOUSE:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_EGGS, player) and    #to get to the Jiggy, you can either take the toll road...
                        state.has(ITEM_TALON_TROT, player) and
                        state.has(ITEM_BEAK_BUSTER, player)
                    )
                ) or
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or    #...or go in through the submerged door and climb up
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                state.has(ITEM_FLAP_FLIP, player)           #you need this for the last jump regardless
            ),
        LOC_JIGGY_RBB_METAL_CAGE:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_BEAK_BARGE, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or        #to get on top of the box
                    state.has(ITEM_RAT_A_TAT_RAP, player) or    #going around is never logically unique due to Trot
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_JIGGY_RBB_CAPTAINS_ROOM:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or   #to break the window and the wooden door
                    state.has(ITEM_EGGS, player)                #Wonderwing probably works?
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or        #to get the Jiggy
                    state.has(ITEM_BEAK_BUSTER, player)         #not tested but probably works?
                )
            ),
        LOC_JIGGY_RBB_BOSS_BOOM_BOX:
            lambda state:
            (
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or   #to jump on the TNT box above the boss room
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or             #to jump on the other boxes
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                (
                    state.has(ITEM_CLIMB, player) or            #to drop the TNT box
                    state.has(ITEM_BEAK_BARGE, player)          #Beak Barge is enough to beat the boss. Good luck:)
                )
            ),
        LOC_JIGGY_RBB_SNORKEL:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_RBB_ENGINE_ROOM:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and       #to hit the switch before entering the engine room
                state.has(ITEM_BEAK_BUSTER, player)     #yes, you really need no other moves to get the Jiggy
            ),
        LOC_JIGGY_RBB_PROPELLER:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and           #to hit the switch before entering the engine room
                state.has(ITEM_BEAK_BUSTER, player) and     #yes, you don't need any more moves for this one either
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_RBB_JINJO:
            lambda state:
            (
                state.has(ITEM_RBB_BLUE_JINJO, player) and
                state.has(ITEM_RBB_GREEN_JINJO, player) and
                state.has(ITEM_RBB_ORANGE_JINJO, player) and
                state.has(ITEM_RBB_PURPLE_JINJO, player) and
                state.has(ITEM_RBB_YELLOW_JINJO, player)
            ),
        LOC_JIGGY_CCW_TREETOP_ROOM:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or        #required to break the wooden door at the top
                    state.has(ITEM_BEAK_BARGE, player) or           #Wonderwing works too
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_JIGGY_CCW_TREETOP_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_BEE_TRANSFORMATION, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or       #required to access Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                )
            ),
        LOC_JIGGY_CCW_ZUBBA:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_BEAK_BUSTER, player)         #yes, you can beat the Zubbas with just Beak Buster
            ),
        LOC_JIGGY_CCW_LEAVES:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and   #either route requires this
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or        #you can either jump up the leaves from the bottom...
                    state.has(ITEM_TALON_TROT, player)          #...or climb up and fall onto the platform
                )
            ),
        LOC_JIGGY_CCW_CABIN:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_JIGGY_CCW_GNAWTY:
            lambda state:
            (
                (
                    state.has(ITEM_BEAK_BARGE, player) or           #required to break the boulder
                    state.has(ITEM_BEAK_BUSTER, player) or          #Wonderwing MIGHT work but probably not
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_CCW_PLANT:
            lambda state:
            (
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_BEAK_BUSTER, player) and         #needs all Gobi events prior done
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_JIGGY_CCW_NABNUTS:
            lambda state:
            (
                state.has(ITEM_ACORN, player, 6)
            ),
        LOC_JIGGY_CCW_EYRIE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_CATERPILLAR, player, 15)
            ),
        LOC_JIGGY_CCW_JINJO:
            lambda state:
            (
                state.has(ITEM_CCW_BLUE_JINJO, player) and
                state.has(ITEM_CCW_GREEN_JINJO, player) and
                state.has(ITEM_CCW_ORANGE_JINJO, player) and
                state.has(ITEM_CCW_PURPLE_JINJO, player) and
                state.has(ITEM_CCW_YELLOW_JINJO, player)
            ),
        LOC_DEFEAT_GRUNTILDA:
            lambda state: True,
    }
