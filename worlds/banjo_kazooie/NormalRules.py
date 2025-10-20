from .Constants import *

def rgn_connection_string(rgn1, rgn2):
    return str(rgn1) + " -> " + str(rgn2)

def has_tokens_for_all_transforms(state, player):
    return state.has(ITEM_MUMBO_TOKEN, player, 75)

def can_smash_mm_huts(state, player):
    return (
        state.has(ITEM_BEAK_BUSTER, player) and
        (
            state.has(ITEM_JUMP, player) or
            state.has(ITEM_FLAP_FLIP, player)    #required to get on top of the huts
        )
    )

def can_reach_ttc_upper_ledge(state, player):
    return (
        state.has(ITEM_JUMP, player) or
        state.has(ITEM_FEATHERY_FLAP, player) or        #required to reasonably get to and climb ladders without getting
        state.has(ITEM_RAT_A_TAT_RAP, player) or        #snack attacked
        (
            state.has(ITEM_TALON_TROT, player) and    #or you can go up from Nipper
            state.has(ITEM_SHOCK_SPRING_JUMP, player)
        ) or
        (
            state.has(ITEM_FLIGHT, player) and
            (
                state.has(ITEM_FLAP_FLIP, player) or    #you can also fly up there
                state.has(ITEM_TALON_TROT, player)
            )
        )
    )

def can_reach_ttc_middle_ledge(state, player):
    return (
        can_reach_ttc_upper_ledge(state, player) or  #one of these are required to get to the middle ledge
        state.has(ITEM_FLAP_FLIP, player)           #this, however, can access ONLY the middle ledge
    )

def can_reach_ttc_flight_pad(state, player):
    return (
        can_reach_ttc_middle_ledge(state, player) or
        state.has(ITEM_TALON_TROT, player)

def can_reach_bgs_puzzle_from_world_room(state, player):
    return (
        state.has(ITEM_FLAP_FLIP, player) and
        state.has(ITEM_SWIM, player)
    )

def can_reach_fp_puzzle_from_world_room(state, player):
    return (
        state.has(ITEM_TALON_TROT, player) and
        (
            state.has(ITEM_STILT_STRIDE, player) or
            state.has(ITEM_TRANSFORMATION_CROCODILE, player)
        )
    )

def can_reach_gv_puzzle_from_world_room(state, player):
    return (
        state.has(ITEM_NOTE, player, 350)
    )

def can_reach_mmm_puzzle_from_world_room(state, player):
    return (
        state.has(ITEM_NOTE, player, 450) and
        state.has(ITEM_SWIM, player) and
        state.has(ITEM_JUMP, player) and
        (
            state.has(ITEM_FEATHERY_FLAP, player) or
            state.has(ITEM_RAT_A_TAT_RAP, player)
        )
    )

def can_hit_one_water_switch(state, player):
    return (
        # break gate outside MMM
        can_break_mmm_gates(state, player) and
        # get to the switch
        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
        # hit the switch
        state.has(ITEM_BEAK_BUSTER, player)
    )

def can_hit_two_water_switches(state, player):
    return (
        can_hit_one_water_switch(state, player) and
        # get to the switch itself
        state.has(ITEM_SWIM, player) and
        # break box
        (
            state.has(ITEM_RAT_A_TAT_RAP, player) or
            state.has(ITEM_BEAK_BARGE, player)
        )
    )

def can_hit_three_water_switches(state, player):
    return (
        can_hit_two_water_switches(state, player) and
        # get to the switch itself
        state.has(ITEM_SWIM, player) and
        # break grate
        state.has(ITEM_RAT_A_TAT_RAP, player)
    )

def can_reach_rbb_puzzle_from_world_room(state, player):
    return (
        can_hit_two_water_switches(state, player)
    )

def can_reach_ccw_puzzle_from_world_room(state, player):
    return (
        state.has(ITEM_SWIM, player)
    )

def can_traverse_bgs(state, player):
    return (
        state.has(ITEM_JUMP, player) or
        state.has(ITEM_FEATHERY_FLAP, player) or  # required to access most of the level
        state.has(ITEM_FLAP_FLIP, player)
    )

def can_break_mmm_gates(state, player):
    return (
        state.has(ITEM_RAT_A_TAT_RAP, player) or
        state.has(ITEM_BEAK_BARGE, player)
    )

def can_reach_eyrie(state, player):
    return (
        state.has(ITEM_TALON_TROT, player) and
        state.has(ITEM_JUMP, player) and
        state.has(ITEM_FEATHERY_FLAP, player) and
        state.has(ITEM_SHOCK_SPRING_JUMP, player)
    )

def get_region_rules(player, options):
    return {
        rgn_connection_string(RGN_SPIRAL_MOUNTAIN, RGN_GRUNTILDAS_LAIR_LOBBY):
            lambda state: True,
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_LOBBY, RGN_MUMBOS_MOUNTAIN):
            lambda state:
            (
                state.has(ITEM_JIGGY, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_LOBBY, RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_NOTE, player, 50)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR, RGN_TREASURE_TROVE_COVE):
            lambda state:
            (
                state.has(ITEM_JIGGY, player, 3)  # 1+2+5+7
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR, RGN_CLANKERS_CAVERN):
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_JIGGY, player, 8)  # 1+2+5+7
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_180_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 180) and
                state.has(ITEM_TALON_TROT, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_180_NOTE_DOOR, RGN_BUBBLEGLOOP_SWAMP):
            lambda state:
            (
                can_reach_bgs_puzzle_from_world_room(state, player) and
                state.has(ITEM_JIGGY, player, 15) and
                state.has(ITEM_TALON_TROT, player)  # 1+2+5+7+8
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_180_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 260) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR, RGN_FREEZEEZY_PEAK):
            lambda state:
            (
                can_reach_fp_puzzle_from_world_room(state, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_JIGGY, player, 23)  # 1+2+5+7+8+9
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR, RGN_GOBIS_VALLEY):
            lambda state:
            (
                can_reach_gv_puzzle_from_world_room(state, player) and
                state.has(ITEM_JIGGY, player, 32) and  # 1+2+5+7+8+9
                state.has(ITEM_STILT_STRIDE, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_350_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 350)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_350_NOTE_DOOR, RGN_MAD_MONSTER_MANSION):
            lambda state:
            (
                can_reach_mmm_puzzle_from_world_room(state, player) and
                state.has(ITEM_JIGGY, player, 42)  # 1+2+5+7+8+9+10+12
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_260_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_450_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 450)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_450_NOTE_DOOR, RGN_RUSTY_BUCKET_BAY):
            lambda state:
            (
                can_reach_rbb_puzzle_from_world_room(state, player) and
                state.has(ITEM_JIGGY, player, 54)  # 1+2+5+7+8+9+10+12
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_450_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_640_NOTE_DOOR):
            lambda state:
            (
                can_hit_three_water_switches(state, player) and
                state.has(ITEM_NOTE, player, 640)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_640_NOTE_DOOR, RGN_CLICK_CLOCK_WOOD):
            lambda state:
            (
                can_reach_ccw_puzzle_from_world_room(state, player) and
                state.has(ITEM_JIGGY, player, 69) and  # 1+2+5+7+8+9+10+12+15
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_640_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_765_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 765) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_765_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_FURNACE_FUN):
            lambda state: True,
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_FURNACE_FUN, RGN_GRUNTILDAS_LAIR_810_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 810) and
                state.has(ITEM_JIGGY, player, 94)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_810_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_882_NOTE_DOOR):
            lambda state:
            (
                state.has(ITEM_NOTE, player, 882)
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_882_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_FIGHT):
            lambda state: True,
    }

def get_location_rules(player, options):
    return {
        # Blubbers Gold
        LOC_BLUBBER_GOLD_TTC_POOP_DECK:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_BLUBBER_GOLD_TTC_HOLD_UNDERWATER:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        # Presents
        LOC_RED_PRESENT_FP_TREE:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_FLAP_FLIP, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_GREEN_PRESENT_FP_NEAR_RAMP:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_BLUE_PRESENT_FP_GIANT_SNOWMAN_NOSE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player) or
                (
                    state.has(ITEM_FLIGHT, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        # Worms
        LOC_WORM_SUMMER_CCW_ENTRY_PATH:
            lambda state: True,
        LOC_WORM_SUMMER_CCW_SNAPPER_NEAR_BULL:
            lambda state:
            (
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player)
            ),
        LOC_WORM_SUMMER_CCW_LEDGE_NEAR_MUMBO:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_WORM_SUMMER_CCW_OUTSIDE_MUMBO:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_WORM_SUMMER_CCW_IN_DRIED_LAKE:
            lambda state: True,
        LOC_WORM_SUMMER_CCW_LEDGE_ABOVE_BRAMBLES:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_SUMMER_CCW_NEAR_CABIN:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player)
            ),
        LOC_WORM_SUMMER_CCW_NEAR_CABIN:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_WORM_SUMMER_CCW_NEAR_NABNUTS_HOME:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        # NOTE! The worms for Autumn will not spawn without feeding Eyrie in Summer (5 worms needed). ALSO! if you suck and die the worms respawn but Eyrie state is saved so you can get more worms than normally possible.
        LOC_WORM_AUTUMN_CCW_ENTRY_LEAF_PILE:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_AUTUMN_CCW_RAMP_NEAR_LAKE:
            lambda state:
            (
                can_reach_eyrie(state, player)
            ),
        LOC_WORM_AUTUMN_CCW_NEAR_STILT_BOOTS:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_AUTUMN_CCW_INSIDE_MUMBO_HUT:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_WORM_AUTUMN_CCW_LEAF_PILE_NEAR_BRAMBLES:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_AUTUMN_CCW_LEAF_PILE_NEAR_FLOWER:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_AUTUMN_CCW_LEDGE_ABOVE_BRAMBLES:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_AUTUMN_CCW_ATOP_BEEHIVE:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_WORM_AUTUMN_CCW_INSIDE_BEEHIVE:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_WORM_AUTUMN_CCW_BELOW_CABIN:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_WORM_AUTUMN_CCW_INSIDE_NABNUTS_HOUSE:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_WORM_AUTUMN_CCW_BEHIND_EYRIE:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_WORM_AUTUMN_CCW_TREETOP_PAST_NEST:
            lambda state:
            (
                can_reach_eyrie(state, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        # Acorns
        LOC_ACORN_AUTUMN_CCW_BEHIND_UPPER_WINDOW:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_RAT_A_TAT_RAP, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_ACORN_AUTUMN_CCW_EDGE_OF_CIRCULAR_GAP_PATH:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_ACORN_AUTUMN_CCW_MIDDLE_OF_CIRCULAR_GAP_PATH:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_ACORN_AUTUMN_CCW_LEDGE_BELOW_CIRCULAR_GAP_PATH:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_ACORN_AUTUMN_CCW_LOWER_SLOPED_PATH:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_ACORN_AUTUMN_CCW_INSIDE_NABNUTS_HOUSE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_FEATHERY_FLAP, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_TRANSFORMATION_TERMITE:
            lambda state:
            (
                has_tokens_for_all_transforms(state, player)
            ),
        LOC_TRANSFORMATION_CROCODILE:
            lambda state:
            (
                has_tokens_for_all_transforms(state, player) and
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_TRANSFORMATION_WALRUS:
            lambda state:
            (
                has_tokens_for_all_transforms(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_TRANSFORMATION_PUMPKIN:
            lambda state:
            (
                has_tokens_for_all_transforms(state, player) and
                can_break_mmm_gates(state, player)
            ),
        LOC_TRANSFORMATION_BEE:
            lambda state:
            (
                has_tokens_for_all_transforms(state, player) and
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MOLEHILL_SM_COMBAT_VEGGIE_PATCH_1:
            lambda state: True,
        LOC_MOLEHILL_SM_COMBAT_VEGGIE_PATCH_2:
            lambda state: True,
        LOC_MOLEHILL_SM_COMBAT_VEGGIE_PATCH_3:
            lambda state: True,
        LOC_MOLEHILL_SM_ROCKS:
            lambda state: True,
        LOC_MOLEHILL_SM_NEAR_MOUNTAIN_BRIDGE:
            lambda state: True,
        LOC_MOLEHILL_SM_NEAR_RIVER:
            lambda state: True,
        LOC_MOLEHILL_SM_IN_FRONT_OF_STUMP_1:
            lambda state: True,
        LOC_MOLEHILL_SM_IN_FRONT_OF_STUMP_2:
            lambda state: True,
        LOC_MOLEHILL_SM_IN_FRONT_OF_STUMP_3:
            lambda state: True,
        LOC_EMPTY_HONEYCOMB_SM_LOG:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        state.has(ITEM_FEATHERY_FLAP, player)
                    )
                )
            ),
        LOC_EMPTY_HONEYCOMB_SM_WATERFALL:
            lambda state:
            (
                state.has(ITEM_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_EMPTY_HONEYCOMB_SM_TREE:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_EMPTY_HONEYCOMB_SM_UNDERWATER:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_EMPTY_HONEYCOMB_SM_ROCKS:
            lambda state:
            (
                state.has(ITEM_BEAK_BARGE, player)
            ),
        LOC_EMPTY_HONEYCOMB_SM_COLLIWOBBLE:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_JIGGY_GL_ENTRYWAY:
            lambda state: True,
        LOC_JIGGY_GL_ATOP_MUMBOS_MOUNTAIN:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
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
                state.has(ITEM_TRANSFORMATION_BEE, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or  # required to access Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                )
            ),
        LOC_MUMBO_TOKEN_GL_RED_CAULDRON:
            lambda state: True,
        LOC_MUMBO_TOKEN_GL_DRAIN_PIPE:
            lambda state: True,
        LOC_MUMBO_TOKEN_GL_CCW_PODIUM:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_MUMBO_TOKEN_GL_ABOVE_CC_ENTRANCE:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_MUMBO_TOKEN_GL_BEHIND_SARCOPHAGUS:
            lambda state: True,
        LOC_MUMBO_TOKEN_GL_ABOVE_FP_ENTRANCE:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_MUMBO_TOKEN_GL_BEHIND_MUMBO:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player)  #TODO: figure out semantics regarding levels
            ),
        LOC_MUMBO_TOKEN_GL_BELOW_RBB_ENTRANCE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_MUMBO_TOKEN_GL_BY_MMM_PODIUM:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_GL_NEAR_CCW_PODIUM_SWITCH:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MOLEHILL_MM_AFTER_CHIMPYS_STUMP:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MOLEHILL_MM_STONEHENGE:
            lambda state: True,
        LOC_MOLEHILL_MM_HUTS:
            lambda state: True,
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
                can_smash_mm_huts(state, player)
            ),
        LOC_JIGGY_MM_MOUNTAINTOP:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_JIGGY_MM_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_MM_BLUE, player) and
                state.has(ITEM_JINJO_MM_GREEN, player) and
                state.has(ITEM_JINJO_MM_ORANGE, player) and
                state.has(ITEM_JINJO_MM_PURPLE, player) and
                state.has(ITEM_JINJO_MM_YELLOW, player)
            ),
        LOC_JINJO_MM_BLUE:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_JINJO_MM_GREEN:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_JUMP, player)
                ) and
                (
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_JINJO_MM_ORANGE:
            lambda state: True,
        LOC_JINJO_MM_PURPLE:
            lambda state:
            (
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_JUMP, player)
                ) and
                (
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_JINJO_MM_YELLOW:
            lambda state: True,
        LOC_EMPTY_HONEYCOMB_MM_HILLSIDE:
            lambda state: True,
        LOC_EMPTY_HONEYCOMB_MM_TOTEM:
            lambda state:
            (
                state.has(ITEM_EGGS, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    (
                        state.has(ITEM_BEAK_BUSTER, player) and
                        (
                            state.has(ITEM_JUMP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or # required to get on the platform
                            state.has(ITEM_FEATHERY_FLAP, player)
                        )
                    )
                 )
            ),
        LOC_MUMBO_TOKEN_MM_BEHIND_PINK_JINJO:
            lambda state: True,
        LOC_MUMBO_TOKEN_MM_CHIMPY:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_MM_STONEHENGE:
            lambda state: True,
        LOC_MUMBO_TOKEN_MM_MUMBOS_HUT:
            lambda state: True,
        LOC_MUMBO_TOKEN_MM_TERMITE_MOUND:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player) or
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_MM_BRIDGE_1:
            lambda state: True,
        LOC_NOTE_MM_BRIDGE_2:
            lambda state: True,
        LOC_NOTE_MM_BRIDGE_3:
            lambda state: True,
        LOC_NOTE_MM_BRIDGE_4:
            lambda state: True,
        LOC_NOTE_MM_BRIDGE_5:
            lambda state: True,
        LOC_NOTE_MM_BRIDGE_6:
            lambda state: True,
        LOC_NOTE_MM_BRIDGE_7:
            lambda state: True,
        LOC_NOTE_MM_TOWER_SLOPE_1:
            lambda state: True,
        LOC_NOTE_MM_TOWER_SLOPE_2:
            lambda state: True,
        LOC_NOTE_MM_TOWER_SLOPE_3:
            lambda state: True,
        LOC_NOTE_MM_TOWER_SLOPE_4:
            lambda state: True,
        LOC_NOTE_MM_TOWER_SLOPE_5:
            lambda state: True,
        LOC_NOTE_MM_TOWER_SLOPE_6:
            lambda state: True,
        LOC_NOTE_MM_TOWER_SLOPE_7:
            lambda state: True,
        LOC_NOTE_MM_TOWER_SLOPE_8:
            lambda state: True,
        LOC_NOTE_MM_TOWER_SLOPE_9:
            lambda state: True,
        LOC_NOTE_MM_HENGE_SLOPE_1:
            lambda state: True,
        LOC_NOTE_MM_HENGE_SLOPE_2:
            lambda state: True,
        LOC_NOTE_MM_HENGE_SLOPE_3:
            lambda state: True,
        LOC_NOTE_MM_HENGE_SLOPE_4:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_1:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_2:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_3:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_4:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_5:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_6:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_7:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_8:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_9:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_10:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_11:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_12:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_13:
            lambda state: True,
        LOC_NOTE_MM_STONEHENGE_14:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_UR_1:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_UR_2:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_UR_3:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_UL_1:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_UL_2:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_UL_3:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_MR_1:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_MR_2:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_MR_3:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_ML_1:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_ML_2:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_ML_3:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_BR_1:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_BR_2:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_BR_3:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_BL_1:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_BL_2:
            lambda state: True,
        LOC_NOTE_MM_CONGA_SLOPE_BL_3:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_TR_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_TR_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_TR_3:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_MR_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_MR_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_MR_3:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_ML_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_ML_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_ML_3:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_LL_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_LL_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_LL_3:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_BM_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_BM_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_BM_3:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_BR_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_BR_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SLOPE_BR_3:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SKULL_1:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SKULL_2:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SKULL_3:
            lambda state: True,
        LOC_NOTE_MM_MUMBO_SKULL_4:
            lambda state: True,
        LOC_NOTE_MM_TOTEM_HUT_1:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MM_TOTEM_HUT_2:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MM_TOTEM_HUT_3:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MM_TOTEM_HUT_4:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MM_TOTEM_HUT_5:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MM_TOTEM_HUT_6:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MM_DESTROY_TOTEM_HUT_1:
            lambda state:
            (
                can_smash_mm_huts(state, player)
            ),
        LOC_NOTE_MM_DESTROY_TOTEM_HUT_2:
            lambda state:
            (
                can_smash_mm_huts(state, player)
            ),
        LOC_NOTE_MM_DESTROY_TOTEM_HUT_3:
            lambda state:
            (
                can_smash_mm_huts(state, player)
            ),
        LOC_NOTE_MM_DESTROY_TOTEM_HUT_4:
            lambda state:
            (
                can_smash_mm_huts(state, player)
            ),
        LOC_NOTE_MM_DESTROY_TOTEM_HUT_5:
            lambda state:
            (
                can_smash_mm_huts(state, player)
            ),
        LOC_NOTE_MM_UNDERWATER_LEFT_CAVE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_MM_UNDERWATER_LEFT_CAVE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_UNDERWATER_LEFT_CAVE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_UNDERWATER_RIGHT_CAVE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_UNDERWATER_RIGHT_CAVE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_UNDERWATER_RIGHT_CAVE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_TERMITE_MOUND_1:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_TERMITE_MOUND_2:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_TERMITE_MOUND_3:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_TERMITE_MOUND_4:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_TERMITE_MOUND_5:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_NOTE_MM_TERMITE_MOUND_6:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_MOLEHILL_TTC_MAST:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_MOLEHILL_TTC_NEAR_SANDCASTLE:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
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
            lambda state: True,
            # ~ (
                # ~ state.has(ITEM_BLUBBER_GOLD, player, 2)
            # ~ ),
        LOC_JIGGY_TTC_SANDCASTLE:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    state.has(ITEM_JUMP, player) or    #required to get the Jiggy
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_JIGGY_TTC_SHOCK_SPRING:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                (
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) or
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_JIGGY_TTC_X_MARK:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        (
                            state.has(ITEM_TALON_TROT, player) and
                            state.has(ITEM_FLIGHT, player)
                        )
                    ) and
                    (
                        state.has(ITEM_FLIGHT, player) or
                        state.has(ITEM_SHOCK_SPRING_JUMP, player)
                    )
                )
            ),
        LOC_JIGGY_TTC_POOL:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_TTC_CLIFFSIDE:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or    #required to get the Jiggy, some of which require falling
                state.has(ITEM_RAT_A_TAT_RAP, player) or    #onto the platform
                (
                    (
                        state.has(ITEM_JUMP, player) or
                        state.has(ITEM_SHOCK_SPRING_JUMP, player)
                    ) and
                    (
                        state.has(ITEM_BEAK_BUSTER, player) or
                        state.has(ITEM_FLIGHT, player) or
                        state.has(ITEM_WONDERWING, player)
                    )
                ) or
                (
                    state.has(ITEM_FLIGHT, player) and
                    (
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_JIGGY_TTC_LOCKUP:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JIGGY_TTC_LIGHTHOUSE:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JIGGY_TTC_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_TTC_BLUE, player) and
                state.has(ITEM_JINJO_TTC_GREEN, player) and
                state.has(ITEM_JINJO_TTC_ORANGE, player) and
                state.has(ITEM_JINJO_TTC_PURPLE, player) and
                state.has(ITEM_JINJO_TTC_YELLOW, player)
            ),
        LOC_JINJO_TTC_BLUE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JINJO_TTC_GREEN:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) and
                    state.has(ITEM_CLIMB, player)
                ) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_JINJO_TTC_ORANGE:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_JINJO_TTC_PURPLE:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                (
                    state.has(ITEM_FLIGHT, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_JINJO_TTC_YELLOW:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_EMPTY_HONEYCOMB_TTC_UNDERWATER:
            lambda state:
            (
             state.has(ITEM_SWIM, player)
            ),
        LOC_EMPTY_HONEYCOMB_TTC_CRATE:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_MUMBO_TOKEN_TTC_NIPPER:
            lambda state: True,
        LOC_MUMBO_TOKEN_TTC_MAST:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_MUMBO_TOKEN_TTC_HOLD:
            lambda state:
            (
             state.has(ITEM_BEAK_BUSTER, player) and
             state.has(ITEM_SWIM, player)
            ),
        LOC_MUMBO_TOKEN_TTC_SHOCK_SPRING:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                (
                    state.has(ITEM_FLIGHT, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_MUMBO_TOKEN_TTC_X_MARK:
            lambda state: True,
        LOC_MUMBO_TOKEN_TTC_LOCKUP_LEFT:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_MUMBO_TOKEN_TTC_LOCKUP_RIGHT:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_MUMBO_TOKEN_TTC_POOL:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_MUMBO_TOKEN_TTC_CRATE:
            lambda state: True,
        LOC_MUMBO_TOKEN_TTC_LIGHTHOUSE:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_ARRIVAL_1:
            lambda state: True,
        LOC_NOTE_TTC_ARRIVAL_2:
            lambda state: True,
        LOC_NOTE_TTC_ARRIVAL_3:
            lambda state: True,
        LOC_NOTE_TTC_ARRIVAL_4:
            lambda state: True,
        LOC_NOTE_TTC_SHIP_FRONT_NET_1:
            lambda state: True,
        LOC_NOTE_TTC_SHIP_FRONT_NET_2:
            lambda state: True,
        LOC_NOTE_TTC_SHIP_FRONT_NET_3:
            lambda state: True,
        LOC_NOTE_TTC_SANDCASTLE_TOP_1:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player) or
                (
                    can_reach_ttc_middle_ledge(state, player) and
                    state.has(ITEM_EGGS, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
                )
            ),
        LOC_NOTE_TTC_SANDCASTLE_TOP_2:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player) or
                (
                    can_reach_ttc_middle_ledge(state, player) and
                    state.has(ITEM_EGGS, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
                )
            ),
        LOC_NOTE_TTC_SANDCASTLE_TOP_3:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player) or
                (
                    can_reach_ttc_middle_ledge(state, player) and
                    state.has(ITEM_EGGS, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
                )
            ),
        LOC_NOTE_TTC_SANDCASTLE_TOP_4:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player) or
                (
                    can_reach_ttc_middle_ledge(state, player) and
                    state.has(ITEM_EGGS, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
                )
            ),
        LOC_NOTE_TTC_SANDCASTLE_TOP_5:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player) or
                (
                    can_reach_ttc_middle_ledge(state, player) and
                    state.has(ITEM_EGGS, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_FLAP_FLIP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
                )
            ),
        LOC_NOTE_TTC_SANDCASTLE_INSIDE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    can_reach_ttc_middle_ledge(state, player) and
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_TTC_SANDCASTLE_INSIDE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    can_reach_ttc_middle_ledge(state, player) and
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_TTC_SANDCASTLE_INSIDE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    can_reach_ttc_middle_ledge(state, player) and
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_TTC_SANDCASTLE_INSIDE_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    can_reach_ttc_middle_ledge(state, player) and
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_TTC_SHELL_INSIDE_1:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_TTC_SHELL_INSIDE_2:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_TTC_SHELL_INSIDE_3:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_TTC_SHELL_INSIDE_4:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_TTC_SHELL_INSIDE_5:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_TTC_SHELL_INSIDE_6:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_TTC_UPPER_POOL_STAIRS_1:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_UPPER_POOL_STAIRS_2:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_UPPER_POOL_STAIRS_3:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_UPPER_POOL_STAIRS_4:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_MIDDLE_POOL_STAIRS_1:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_MIDDLE_POOL_STAIRS_2:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_MIDDLE_POOL_STAIRS_3:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_MIDDLE_POOL_STAIRS_4:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_LOWER_POOL_STAIRS_1:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_LOWER_POOL_STAIRS_2:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_LOWER_POOL_STAIRS_3:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_LOWER_POOL_STAIRS_4:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_CRAB_POOL_1:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_CRAB_POOL_2:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_CRAB_POOL_3:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player)
            ),
        LOC_NOTE_TTC_CHEST_BRIDGE_1:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
            ),
        LOC_NOTE_TTC_CHEST_BRIDGE_2:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
            ),
        LOC_NOTE_TTC_CHEST_BRIDGE_3:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
            ),
        LOC_NOTE_TTC_NIPPER_BRIDGE_1:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
            ),
        LOC_NOTE_TTC_NIPPER_BRIDGE_2:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
            ),
        LOC_NOTE_TTC_NIPPER_BRIDGE_3:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
            ),
        LOC_NOTE_TTC_BLUBBER_BRIDGE_1:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
            ),
        LOC_NOTE_TTC_BLUBBER_BRIDGE_2:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
            ),
        LOC_NOTE_TTC_BLUBBER_BRIDGE_3:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
            ),
        LOC_NOTE_TTC_SANDCASTLE_BRIDGE_1:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
            ),
        LOC_NOTE_TTC_SANDCASTLE_BRIDGE_2:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
            ),
        LOC_NOTE_TTC_SANDCASTLE_BRIDGE_3:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player)
            ),
        LOC_NOTE_TTC_SSS_PILLAR_1:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                (
                    state.has(ITEM_FLIGHT, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_NOTE_TTC_SSS_PILLAR_2:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                (
                    state.has(ITEM_FLIGHT, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_NOTE_TTC_SSS_PILLAR_3:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                (
                    state.has(ITEM_FLIGHT, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_NOTE_TTC_ISLAND_PLATFORM_1:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                (
                    state.has(ITEM_FLIGHT, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_NOTE_TTC_ISLAND_PLATFORM_2:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                (
                    state.has(ITEM_FLIGHT, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_NOTE_TTC_ISLAND_PLATFORM_3:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                (
                    state.has(ITEM_FLIGHT, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_NOTE_TTC_ISLAND_PLATFORM_4:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                (
                    state.has(ITEM_FLIGHT, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_NOTE_TTC_ISLAND_PLATFORM_5:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                (
                    state.has(ITEM_FLIGHT, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_NOTE_TTC_ISLAND_PLATFORM_6:
            lambda state:
            (
                can_reach_ttc_middle_ledge(state, player) and
                (
                    state.has(ITEM_FLIGHT, player) or
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                )
            ),
        LOC_NOTE_TTC_TREE_STERN_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_TTC_TREE_STERN_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_TTC_TREE_STERN_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_TTC_TREE_STERN_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_TTC_TREE_BOW_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_TTC_TREE_BOW_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_TTC_TREE_BOW_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_TTC_TREE_BOW_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_TTC_SHIP_FRONT_NET_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_TTC_SHIP_FRONT_NET_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_TTC_SHIP_FRONT_NET_6:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_TTC_SHIP_AFT_NET_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_TTC_SHIP_AFT_NET_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_TTC_SHIP_AFT_NET_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_TTC_SHIP_AFT_NET_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_TTC_SHIP_AFT_NET_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_TTC_SHIP_AFT_HOLD_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_TTC_SHIP_AFT_HOLD_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_TTC_SHIP_AFT_HOLD_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_TTC_SHIP_AFT_HOLD_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_TTC_SHIP_BOW_HOLD_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_TTC_SHIP_BOW_HOLD_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_TTC_SHIP_BOW_HOLD_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_TTC_SHIP_BOW_HOLD_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_TTC_SSS_CHEST_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_TTC_SSS_CHEST_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_TTC_SSS_CHEST_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_TTC_SSS_CHEST_4:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_TTC_SSS_CHEST_5:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_TTC_MAP_PILLAR_PATH_1:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_TTC_MAP_PILLAR_PATH_2:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_TTC_MAP_PILLAR_PATH_3:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_TTC_MAP_PILLAR_PATH_4:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_CAVE_1:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_PATH_1:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_PATH_2:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_PATH_3:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_1:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_2:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_3:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_4:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_TTC_LIGHTHOUSE_BALCONY_5:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_MOLEHILL_CC_NEAR_SPINNING_BLADES:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLAP_FLIP, player)
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
                state.has(ITEM_JINJO_CC_BLUE, player) and
                state.has(ITEM_JINJO_CC_GREEN, player) and
                state.has(ITEM_JINJO_CC_ORANGE, player) and
                state.has(ITEM_JINJO_CC_PURPLE, player) and
                state.has(ITEM_JINJO_CC_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_CC_PIPE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_EMPTY_HONEYCOMB_CC_GRATE:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_MUMBO_TOKEN_CC_ENTRANCE:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player)
                        )
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CC_CLANKER_TAIL:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_MUMBO_TOKEN_CC_CLANKER_GOLD_TEETH:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_CC_GRATE:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                )
            ),
        LOC_MUMBO_TOKEN_CC_UNDERWATER_TUNNEL:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_MOLEHILL_BGS_BEHIND_WORLD_ENTRY:
            lambda state: True,
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
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                )
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
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_JIGGY_BGS_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_BGS_BLUE, player) and
                state.has(ITEM_JINJO_BGS_GREEN, player) and
                state.has(ITEM_JINJO_BGS_ORANGE, player) and
                state.has(ITEM_JINJO_BGS_PURPLE, player) and
                state.has(ITEM_JINJO_BGS_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_BGS_TIPTUP_STAND:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_EMPTY_HONEYCOMB_BGS_INSIDE_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
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
        LOC_MUMBO_TOKEN_BGS_BEHIND_YELLOW_JINJO:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_ATOP_CATTAIL:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or  # required to access most of the level
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_MUMBO_TOKEN_BGS_CENTRAL_PLATFORM:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_INSIDE_TANKTUP:
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
        LOC_MUMBO_TOKEN_BGS_INSIDE_HUT:
            lambda state:
            (
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or  # required to access most of the level/get on the huts
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_MUMBO_TOKEN_BGS_BEHIND_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_BEHIND_MUMBO:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_UNDER_HUTS_LEFT:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_UNDER_HUTS_RIGHT:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_INSIDE_MR_VILE:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_MOLEHILL_FP_NEXT_TO_STACK_OF_PRESENTS:
            lambda state: True,
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
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or    #required to the Jiggy at the top of the tree
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_JIGGY_FP_WOZZA:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
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
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_JIGGY_FP_BOGGY_RACE_2:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull (Race 1 must be completed)
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TRANSFORMATION_WALRUS, player) and
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_JIGGY_FP_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_FP_BLUE, player) and
                state.has(ITEM_JINJO_FP_GREEN, player) and
                state.has(ITEM_JINJO_FP_ORANGE, player) and
                state.has(ITEM_JINJO_FP_PURPLE, player) and
                state.has(ITEM_JINJO_FP_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_FP_SIR_SLUSH:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_EMPTY_HONEYCOMB_FP_WOZZA:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_MUMBO_TOKEN_FP_INSIDE_IGLOO:
            lambda state: True,
        LOC_MUMBO_TOKEN_FP_BEHIND_PRESENTS:
            lambda state: True,
        LOC_MUMBO_TOKEN_FP_ABOVE_HOUSE_FLIGHT_PAD:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_MUMBO_TOKEN_FP_SIR_SLUSH_WOZZA:
            lambda state:
            (
                    state.has(ITEM_FLIGHT, player) and
                    state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_MUMBO_TOKEN_FP_SIR_SLUSH_ISLAND:
            lambda state:
            (
                    state.has(ITEM_FLIGHT, player) and
                    state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_MUMBO_TOKEN_FP_TOBOGGAN:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or    #required to reach the snowman's scarf
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_MUMBO_TOKEN_FP_LARGE_SNOWMAN_LEFT:
            lambda state: True,
        LOC_MUMBO_TOKEN_FP_LARGE_SNOWMAN_RIGHT:
            lambda state: True,
        LOC_MUMBO_TOKEN_FP_UNDER_CHRISTMAS_TREE:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_MUMBO_TOKEN_FP_UNDERWATER:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TRANSFORMATION_WALRUS, player)
            ),
        LOC_MOLEHILL_GV_NEAR_KAZOOIE_PYRAMID:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_JIGGY_GV_JINXY:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or   #required to jump across carpets
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
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) # required to get on top of Jinxy
                        )
                    ) or
                (
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ) and
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
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) # required to get on top of Jinxy
                        )
                    ) or
                (
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player) and
                state.has(ITEM_EGGS, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or    #required to get the Jiggy
                    state.has(ITEM_BEAK_BUSTER, player)
                )
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
                state.has(ITEM_JINJO_GV_BLUE, player) and
                state.has(ITEM_JINJO_GV_GREEN, player) and
                state.has(ITEM_JINJO_GV_ORANGE, player) and
                state.has(ITEM_JINJO_GV_PURPLE, player) and
                state.has(ITEM_JINJO_GV_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_GV_CACTUS:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) # required to get on top of Jinxy
                        )
                    ) or
                (
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_EMPTY_HONEYCOMB_GV_GOBI:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                state.has(ITEM_BEAK_BUSTER, player)
            ) and
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to get to carpet
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_TALON_TROT, player)
                ) #TODO: require Gobi & Trunker Jiggies
            ),
        LOC_MUMBO_TOKEN_GV_BEHIND_JINXY:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_GV_ABOVE_JINXYS_NOSE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    state.has(ITEM_FLAP_FLIP, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player) # required to get on top of Jinxy
                    )
                ) or
                (
                    state.has(ITEM_JUMP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                        state.has(ITEM_TALON_TROT, player)
                    ) and
                    (
                        state.has(ITEM_FLAP_FLIP, player) or        #required to actually get the token
                        state.has(ITEM_FLIGHT, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_GV_INSIDE_JINXY:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    state.has(ITEM_FLAP_FLIP, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player) # required to get on top of Jinxy
                    )
                ) or
                (
                    state.has(ITEM_JUMP, player) and
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_GV_OUTSIDE_WATER_PYRAMID_FRONT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or  # required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_MUMBO_TOKEN_GV_FLIP_PANEL_PYRAMID:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or  # required to access most of the level
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_MUMBO_TOKEN_GV_MOAT:
            lambda state:
            (
                (
                    state.has(ITEM_TALON_TROT, player) or  # required to access most of the level
                    state.has(ITEM_TURBO_TALON_TROT, player)
                ) #TODO: require water pyramid Jiggy or other solution
            ),
        LOC_MUMBO_TOKEN_GV_RUBEE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) # required to get on top of Jinxy
                        )
                    ) or
                (
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_MUMBO_TOKEN_GV_ATOP_CENTRAL_PYRAMID:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                (
                    state.has(ITEM_EGGS, player) or #you can either raise the pyramid normally, or...
                    (
                        ( #climb up Jinxy and fly to the token directly
                            state.has(ITEM_FLAP_FLIP, player) and
                            (
                                state.has(ITEM_FEATHERY_FLAP, player) or
                                state.has(ITEM_RAT_A_TAT_RAP, player)  # required to get on top of Jinxy
                            )
                        ) or
                        (
                            state.has(ITEM_JUMP, player) and
                            (
                                state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to get on top of Jinxy
                                state.has(ITEM_TALON_TROT, player)
                            )
                        ) and
                        state.has(ITEM_FLIGHT, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_GV_CENTRAL_PYRAMID_POT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or    #required to access most of the level
                state.has(ITEM_TURBO_TALON_TROT, player)
            ) and
            (
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_GV_INSIDE_WATER_PYRAMID:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
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
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
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
                ) and
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
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
                state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
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
                state.has(ITEM_JINJO_MMM_BLUE, player) and
                state.has(ITEM_JINJO_MMM_GREEN, player) and
                state.has(ITEM_JINJO_MMM_ORANGE, player) and
                state.has(ITEM_JINJO_MMM_PURPLE, player) and
                state.has(ITEM_JINJO_MMM_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_MMM_CHURCH_RAFTER:
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
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_EMPTY_HONEYCOMB_MMM_FLOORBOARD:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or        #required to break window
                    state.has(ITEM_EGGS, player)                    #Wonderwing also works
                ) and
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and           #required to get to Mumbo's Skull
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                        state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_MMM_FIREPLACE:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and      #you can either climb up the mansion and enter the chimney...
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                ) or
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or       #...or just break down the door and walk in
                    state.has(ITEM_EGGS, player)                #Wonderwing also works
                )
            ),
        LOC_MUMBO_TOKEN_MMM_CELLAR:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_MMM_LOGGO:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or        #required to break window
                    state.has(ITEM_EGGS, player)                    #Wonderwing also works
                ) and
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and           #required to get to Mumbo's Skull
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                        state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_MMM_SINK:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or        #required to break window
                    state.has(ITEM_EGGS, player)                    #Wonderwing also works
                )
            ),
        LOC_MUMBO_TOKEN_MMM_MAZE:
            lambda state: True,
        LOC_MUMBO_TOKEN_MMM_MAZE_HIDDEN_AREA:
            lambda state:
            (
                (                   #you can either turn into a pumpkin and go in through the small gap in the hedge...
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and           #required to get to Mumbo's Skull
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                        state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                        state.has(ITEM_EGGS, player)
                    )
                ) or
                state.has(ITEM_CLIMB, player) #...or just climb onto the roof and fall onto it, your call:)
            ),
        LOC_MUMBO_TOKEN_MMM_SHACK_ROOF:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_MMM_WELL:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and   #required to get to Mumbo's Skull
                    (
                        state.has(ITEM_RAT_A_TAT_RAP, player) or    #required to open church gate
                        state.has(ITEM_BEAK_BARGE, player) or       #Wonderwing also works
                        state.has(ITEM_EGGS, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_MMM_BEHIND_GRAVE:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to open church gate
                state.has(ITEM_BEAK_BARGE, player) or  # Wonderwing also works
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_MMM_CLOCK_TOWER:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to open church gate
                    state.has(ITEM_BEAK_BARGE, player) or  # Wonderwing also works
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_MUMBO_TOKEN_MMM_CHURCH_CHAIR:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or  # required to open church gate
                    state.has(ITEM_BEAK_BARGE, player) or  # Wonderwing also works
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_MMM_CHURCH_RAFTER:
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
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_MUMBO_TOKEN_MMM_NEAR_SHACK:
            lambda state: True,
        LOC_MUMBO_TOKEN_MMM_BEDROOM:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or        #required to break window
                    state.has(ITEM_EGGS, player)                    #Wonderwing also works
                )
            ),
        LOC_MUMBO_TOKEN_MMM_FOUNTAIN:
            lambda state:
            (
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_MMM_NEAR_FOUNTAIN:
            lambda state: True,
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
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player) and       #to hit the switch before entering the engine room
                state.has(ITEM_BEAK_BUSTER, player)     #yes, you really need no other moves to get the Jiggy
            ),
        LOC_JIGGY_RBB_PROPELLER:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player) and           #to hit the switch before entering the engine room
                state.has(ITEM_BEAK_BUSTER, player) and     #yes, you don't need any more moves for this one either
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_RBB_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_RBB_BLUE, player) and
                state.has(ITEM_JINJO_RBB_GREEN, player) and
                state.has(ITEM_JINJO_RBB_ORANGE, player) and
                state.has(ITEM_JINJO_RBB_PURPLE, player) and
                state.has(ITEM_JINJO_RBB_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_RBB_ENGINE_ROOM:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player) and #I THINK you can fall into the cubbyhole where the empty honeycomb is?
                state.has(ITEM_FLAP_FLIP, player) #I couldn't replicate it myself though
            ),
        LOC_EMPTY_HONEYCOMB_RBB_WAREHOUSE:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_MUMBO_TOKEN_RBB_TOLL_BRIDGE:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_RBB_LIFEBOAT:
            lambda state: True,
        LOC_MUMBO_TOKEN_RBB_BEHIND_WITCH_SWITCH_TOWER:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_MUMBO_TOKEN_RBB_BARRACKS:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or   #to break the window
                    state.has(ITEM_EGGS, player)               #Wonderwing works too
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_RBB_ENGINE_ROOM_ENTRY:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_RBB_ENGINE_ROOM_LEFT:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_RBB_ENGINE_ROOM_RIGHT:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_RBB_PERISCOPE_STOREROOM:
            lambda state: True,
        LOC_MUMBO_TOKEN_RBB_NAVIGATION_ROOM:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player) or   #to break the window
                state.has(ITEM_EGGS, player)               #Wonderwing works too
            ),
        LOC_MUMBO_TOKEN_RBB_OVEN:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player) #this is nigh impossible to get without taking damage or Wonderwing
            ),
        LOC_MUMBO_TOKEN_RBB_SMOKESTACK:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_RBB_TOXIC_WASTE_DRUM:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_MUMBO_TOKEN_RBB_SHIP_BOW:
            lambda state: True,
        LOC_MUMBO_TOKEN_RBB_LEFT_SHIPPING_CRATE:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) or    #first, you need to get to the crate, either from
                        state.has(ITEM_CLIMB, player)           #the ship's crane...
                    ) or
                    (
                        state.has(ITEM_EGGS, player) and        #...or by going around the perimeter of the level
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or             #then you need to actually be able to get the token
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_MUMBO_TOKEN_RBB_MIDDLE_SHIPPING_CRATE:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_CLIMB, player)           #first, you need to get to the crate, either from
                    ) or                                        #the ship's crane...
                    (
                        state.has(ITEM_EGGS, player) and        #...or by going around the perimeter of the level
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_FLAP_FLIP, player)           #then you need to actually be able to get the token
                )
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
                state.has(ITEM_TRANSFORMATION_BEE, player) and
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
                state.has(ITEM_WORM, player, 15)
            ),
        LOC_JIGGY_CCW_JINJO:
            lambda state:
            (
                state.has(ITEM_JINJO_CCW_BLUE, player) and
                state.has(ITEM_JINJO_CCW_GREEN, player) and
                state.has(ITEM_JINJO_CCW_ORANGE, player) and
                state.has(ITEM_JINJO_CCW_PURPLE, player) and
                state.has(ITEM_JINJO_CCW_YELLOW, player)
            ),
        LOC_EMPTY_HONEYCOMB_CCW_WINTER_NABNUTS:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BOMB, player)
                )
            ),
        LOC_EMPTY_HONEYCOMB_CCW_WINTER_GNAWTY:
            lambda state:
            (
                state.has(ITEM_SWIM, player) #May require boulder broken in summer?
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_ENTRANCE_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_GARDEN_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_TREETOP_ABOVE_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_BEEHIVE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_CABIN:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_NABNUTS_DRESSER:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_NEAR_EYRIES_NEST:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_THORNS:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_ENTRANCE_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_GNAWTY:
            lambda state:
            (
                state.has(ITEM_BEAK_BARGE, player) or  # required to break the boulder
                state.has(ITEM_BEAK_BUSTER, player) or # Wonderwing MIGHT work but probably not
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_GARDEN:
            lambda state: True,
        LOC_MUMBO_TOKEN_CCW_SUMMER_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_TREETOP_ABOVE_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or   #you can either just climb the ramp...
                (
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        (
                            state.has(ITEM_JUMP, player) and
                            state.has(ITEM_TALON_TROT, player)
                        )
                    ) and
                    (
                        state.has(ITEM_FLAP_FLIP, player) and        #...or climb the leaves and fall onto the platform
                        state.has(ITEM_SHOCK_SPRING_JUMP, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_LEAVES:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and   #either route requires this
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_AFTER_NABNUTS_HOUSE:
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
                    state.has(ITEM_TALON_TROT, player)          #...or climb up the ramp
                )
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_ENTRANCE_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_TREETOP_ABOVE_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or   #you can either just climb the ramp...
                (
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        (
                            state.has(ITEM_JUMP, player) and
                            state.has(ITEM_TALON_TROT, player)
                        )
                    ) and
                    (
                        state.has(ITEM_FLAP_FLIP, player) and        #...or climb the leaves and fall onto the platform
                        state.has(ITEM_SHOCK_SPRING_JUMP, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_LEAVES:
            lambda state:
            (
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
                    (
                        state.has(ITEM_TALON_TROT, player) and  #...or climb up the ramp and fall down the leaves
                        state.has(ITEM_SHOCK_SPRING_JUMP, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_CABIN:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_TREETOP_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_GARDEN:
            lambda state: True,
        LOC_MUMBO_TOKEN_CCW_WINTER_SIR_SLUSH:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_BEEHIVE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_NEAR_NABNUTS_HOUSE:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_TALON_TROT, player) and
                    (
                        state.has(ITEM_JUMP, player) or
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    ) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_BEHIND_LAKE_PLATFORM:
            lambda state: True,
        LOC_DEFEAT_GRUNTILDA:
            lambda state: True,
    }
