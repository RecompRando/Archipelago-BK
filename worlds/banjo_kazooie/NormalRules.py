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
    )

def can_reach_cc_entrance(state, player):
    return (
        state.has(ITEM_FLAP_FLIP, player) and
        state.has(ITEM_BEAK_BUSTER, player) and
        (
            state.has(ITEM_RAT_A_TAT_RAP, player) or
            state.has(ITEM_FEATHERY_FLAP, player) or
            state.has(ITEM_TALON_TROT, player)
        )
    )

def can_reach_bgs_puzzle_from_world_room(state, player):
    return (
        can_reach_cc_entrance(state, player) and
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

def can_reach_gv_rest_of_level(state, player):
    return (
        state.has(ITEM_TALON_TROT, player) or
        state.has(ITEM_TURBO_TALON_TROT, player)
    )

#def gobi_moved_to_ccw(state, player):
    #TODO

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

def can_reach_mmm_second_floor(state, player):
    return (
        state.has(ITEM_CLIMB, player) and
        (
            state.has(ITEM_RAT_A_TAT_RAP, player) or  #required to break window
            state.has(ITEM_EGGS, player)              #Wonderwing also works
        )
    )

def can_reach_mmm_third_floor(state, player):
    return (
        can_reach_mmm_second_floor(state, player) and
        state.has(ITEM_SHOCK_SPRING_JUMP, player)
    )

def can_hit_one_water_switch(state, player):
    return (
        # break gate outside MMM
            can_break_breakable_gates(state, player) and
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

def can_reach_ccw_nabnuts_house(state, player):
    return (
        state.has(ITEM_FLIGHT, player) or
        (
            state.has(ITEM_TALON_TROT, player) and
            state.has(ITEM_SHOCK_SPRING_JUMP, player) and
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            )
        )
    )

def can_traverse_bgs(state, player):
    return (
        state.has(ITEM_JUMP, player) or
        state.has(ITEM_FEATHERY_FLAP, player) or # required to access most of the level
        state.has(ITEM_RAT_A_TAT_RAP, player)
        # or state.has(ITEM_FLAP_FLIP, player)   #this is awful, so I'm commenting it out for now
    )

def can_break_breakable_gates(state, player):
    return (
        state.has(ITEM_RAT_A_TAT_RAP, player) or
        state.has(ITEM_BEAK_BARGE, player) or
        state.has(ITEM_EGGS, player)
    )

def can_break_rbb_windows(state, player):
    return (
        state.has(ITEM_RAT_A_TAT_RAP, player) or
        state.has(ITEM_EGGS, player)
    )

def can_reach_ccw_spring_switch(state, player):
    return (
        state.has(ITEM_BEAK_BUSTER, player)
    )

def can_reach_ccw_summer_switch(state, player):
    return (
        can_reach_ccw_spring_switch(state, player) and
        state.has(ITEM_TALON_TROT, player) and
        (
            state.has(ITEM_JUMP, player) or
            state.has(ITEM_FEATHERY_FLAP, player) or
            state.has(ITEM_RAT_A_TAT_RAP, player)
        ) and
        state.has(ITEM_SHOCK_SPRING_JUMP, player)
    )

def can_reach_ccw_fall_switch(state, player):
    return (
        can_reach_ccw_summer_switch(state, player)
    )

def can_reach_ccw_winter_switch(state, player):
    return (
        can_reach_ccw_fall_switch(state, player)
    )

def can_reach_ccw_beehive(state, player, season = None):
    if season == ITEM_SEASON_SPRING:
        return (
            (
                state.has(ITEM_SEASON_SPRING, player) and
                state.has(ITEM_TALON_TROT, player)
            )
        )
    elif season == ITEM_SEASON_SUMMER:
        return (
            state.has(ITEM_SEASON_SUMMER, player) and
            (
                state.has(ITEM_TALON_TROT, player) or
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER)
            )
        )
    elif season == ITEM_SEASON_FALL:
        return (
            state.has(ITEM_SEASON_FALL, player) and
            (
                state.has(ITEM_TALON_TROT, player) or
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL)
            )
        )
    elif season == ITEM_SEASON_WINTER:
        return (
            state.has(ITEM_SEASON_WINTER, player) and
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            )
        )
    else:
        return (
            can_reach_ccw_beehive(state, player, ITEM_SEASON_SPRING) or
            can_reach_ccw_beehive(state, player, ITEM_SEASON_SUMMER) or
            can_reach_ccw_beehive(state, player, ITEM_SEASON_FALL) or
            can_reach_ccw_beehive(state, player, ITEM_SEASON_WINTER)
        )

def can_reach_ccw_cabin(state, player, season = None):
    if season == ITEM_SEASON_SPRING:
        return (
            state.has(ITEM_SEASON_SPRING, player) and
            state.has(ITEM_TALON_TROT, player) and
            state.has(ITEM_SHOCK_SPRING_JUMP, player) and
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_JUMP, player)
            )
        )
    elif season == ITEM_SEASON_SUMMER:
        return (
            state.has(ITEM_SEASON_SUMMER, player) and
            state.has(ITEM_SHOCK_SPRING_JUMP, player) and
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ) and
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_TALON_TROT, player)
            )
        )
    elif season == ITEM_SEASON_FALL:
        return (
            state.has(ITEM_SEASON_FALL, player) and
            state.has(ITEM_SHOCK_SPRING_JUMP, player) and
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ) and
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_TALON_TROT, player)
            )
        )
    elif season == ITEM_SEASON_WINTER:
        return (
            state.has(ITEM_SEASON_WINTER, player) and
            (
                (
                    state.has(ITEM_TALON_TROT, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        (
                            state.has(ITEM_JUMP, player) and
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) or
                state.has(ITEM_FLIGHT, player)
            )
        )
    else:
        return (
            can_reach_ccw_cabin(state, player, ITEM_SEASON_SPRING) or
            can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER) or
            can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL) or
            can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER)
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
                state.has(ITEM_JIGGY, player, 3) and  # 1+2+5+7
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_50_NOTE_DOOR, RGN_CLANKERS_CAVERN):
            lambda state:
            (
                state.has(ITEM_JIGGY, player, 8) and  # 1+2+5+7
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                can_reach_cc_entrance(state, player)
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
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_
                )
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
        rgn_connection_string(RGN_GRUNTILDAS_LAIR_810_NOTE_DOOR, RGN_GRUNTILDAS_LAIR_FIGHT):
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
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_GREEN_PRESENT_FP_NEAR_RAMP:
            lambda state: True,
        LOC_BLUE_PRESENT_FP_GIANT_SNOWMAN_NOSE:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) or
                (
                    state.has(ITEM_FLIGHT, player)
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
        LOC_SEASON_SPRING:
            lambda state:
            (
                can_reach_ccw_spring_switch(state, player)
            ),
        LOC_SEASON_SUMMER:
            lambda state:
            (
                can_reach_ccw_summer_switch(state, player)
            ),
        LOC_SEASON_FALL:
            lambda state:
            (
                can_reach_ccw_fall_switch(state, player)
            ),
        LOC_SEASON_WINTER:
            lambda state:
            (
                can_reach_ccw_winter_switch(state, player)
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
                    can_break_breakable_gates(state, player)
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
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BUSTER, player)
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
                can_reach_cc_entrance(state, player) and
                state.has(ITEM_FLAP_FLIP, player)
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
        LOC_SNS_KEY_ICE:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_WALRUS, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_SNS_EGG_PINK:
            lambda state:
            (
                state.has(ITEM_SNS_EGG_PINK, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_SNS_EGG_BLUE:
            lambda state:
            (
                state.has(ITEM_SNS_EGG_BLUE, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_SNS_EGG_CYAN:
            lambda state:
            (
                state.has(ITEM_SNS_EGG_CYAN, player) and
                (
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_SNS_EGG_GREEN:
            lambda state:
            (
                state.has(ITEM_SNS_EGG_GREEN, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                can_reach_mmm_second_floor(state, player)
            ),
        LOC_SNS_EGG_RED:
            lambda state:
            (
                state.has(ITEM_SNS_EGG_RED, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or   #to break the window and the wooden door
                    state.has(ITEM_EGGS, player)                #Wonderwing probably works?
                )
            ),
        LOC_SNS_EGG_YELLOW:
            lambda state:
            (
                state.has(ITEM_SNS_EGG_YELLOW, player) and
                can_reach_ccw_nabnuts_house(state, player) and
                state.has(ITEM_RAT_A_TAT_RAP, player)
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
            lambda state:
            (
                state.has(ITEM_BLUBBER_GOLD, player, 2)
            ),
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
                state.has(ITEM_FLIGHT, player)
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
        LOC_JINJO_CC_BLUE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JINJO_CC_GREEN:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JINJO_CC_ORANGE:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player)
                ) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JINJO_CC_PURPLE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JINJO_CC_YELLOW:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_JUMP, player)
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
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
                state.has(ITEM_CLIMB, player) and
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
                state.has(ITEM_CLIMB, player) and
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
        LOC_NOTE_CC_LEFT_ENTRY_PIPE_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
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
        LOC_NOTE_CC_LEFT_ENTRY_PIPE_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
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
        LOC_NOTE_CC_LEFT_ENTRY_PIPE_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
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
        LOC_NOTE_CC_LEFT_ENTRY_PIPE_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
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
        LOC_NOTE_CC_RIGHT_ENTRY_PIPE_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_JUMP, player)
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_CC_RIGHT_ENTRY_PIPE_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_JUMP, player)
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_CC_RIGHT_ENTRY_PIPE_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_JUMP, player)
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_CC_RIGHT_ENTRY_PIPE_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_JUMP, player)
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_CC_CLANKER_PIPE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKER_PIPE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKER_PIPE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKER_PIPE_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKER_PIPE_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKER_PIPE_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKER_FLOOR_PIPE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKER_FLOOR_PIPE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKER_FLOOR_PIPE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKER_FLOOR_PIPE_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKER_FLOOR_PIPE_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKER_FLOOR_PIPE_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKER_FLOOR_PIPE_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_GLOWING_ROOM_8:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_ANCHOR_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_ANCHOR_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_ANCHOR_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_ANCHOR_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_ANCHOR_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_ANCHOR_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_ANCHOR_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_ANCHOR_8:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_SPINE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_SPINE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_SPINE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_SPINE_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_SPINE_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_SPINE_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_SPINE_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_SPINE_8:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_SPINE_9:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_SPINE_10:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RAISED_CLANKER_PIPE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RAISED_CLANKER_PIPE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RAISED_CLANKER_PIPE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RAISED_CLANKER_PIPE_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RAISED_CLANKER_PIPE_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RAISED_CLANKER_PIPE_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RAISED_CLANKER_PIPE_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RAISED_CLANKER_PIPE_8:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RAISED_CLANKER_PIPE_9:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RAISED_CLANKER_PIPE_10:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_PLATFORM_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_PLATFORM_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_PLATFORM_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_PLATFORM_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_STARBOARD_GILLS_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_STARBOARD_GILLS_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_STARBOARD_GILLS_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_STARBOARD_GILLS_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_STARBOARD_GILLS_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_PORTSIDE_GILLS_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_PORTSIDE_GILLS_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_PORTSIDE_GILLS_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_MOUTH_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_MOUTH_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_MOUTH_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_MOUTH_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_MOUTH_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_MOUTH_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_MOUTH_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_CLANKERS_MOUTH_8:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_SAWS_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_SAWS_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_SAWS_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_SAWS_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_SAWS_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_BLOWHOLE_SAWS_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_CC_RIGHT_CUBBY_PIPE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_CC_RIGHT_CUBBY_PIPE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_CC_RIGHT_CUBBY_PIPE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_CC_RIGHT_CUBBY_PIPE_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_CC_RIGHT_DUCT_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_CC_RIGHT_DUCT_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_CC_RIGHT_DUCT_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_CC_RIGHT_DUCT_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_CC_RIGHT_DUCT_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_CC_LEFT_CUBBIES_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_CC_LEFT_CUBBIES_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_CC_AFT_SAWS_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_CC_AFT_SAWS_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_CC_AFT_SAWS_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CC_AFT_SAWS_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CC_AFT_SAWS_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CC_AFT_SAWS_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_WONDERWING, player)
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
                can_traverse_bgs(state, player) and
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
                can_traverse_bgs(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_TIPTUP:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_HUT:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_MUMBOS_HUT_RACE:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_JIGGY_BGS_CROCTUS:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_EGGS, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or    #required to reach all Croctus locations
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_JIGGY_BGS_MR_VILE:
            lambda state:
            (
                can_traverse_bgs(state, player) and
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
        LOC_JINJO_BGS_BLUE:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_TALON_TROT, player) or
                            state.has(ITEM_STILT_STRIDE, player)
                        )
                    )
                )
            ),
        LOC_JINJO_BGS_GREEN:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                )
            ),
        LOC_JINJO_BGS_ORANGE:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_JINJO_BGS_PURPLE:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_JINJO_BGS_YELLOW:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_EMPTY_HONEYCOMB_BGS_TIPTUP_STAND:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_EMPTY_HONEYCOMB_BGS_INSIDE_MUMBOS_HUT:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
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
        LOC_MUMBO_TOKEN_BGS_BEHIND_YELLOW_JINJO:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_ATOP_CATTAIL:
            lambda state:
            (
                can_traverse_bgs(state, player) and
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
                can_traverse_bgs(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_MUMBO_TOKEN_BGS_INSIDE_HUT:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_MUMBO_TOKEN_BGS_BEHIND_MUMBOS_HUT:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_BEHIND_MUMBO:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_UNDER_HUTS_LEFT:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_UNDER_HUTS_RIGHT:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_MUMBO_TOKEN_BGS_INSIDE_MR_VILE:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_ENTRY_BRIDGE_1:
            lambda state: True,
        LOC_NOTE_BGS_ENTRY_BRIDGE_2:
            lambda state: True,
        LOC_NOTE_BGS_ENTRY_BRIDGE_3:
            lambda state: True,
        LOC_NOTE_BGS_ENTRY_BRIDGE_4:
            lambda state: True,
        LOC_NOTE_BGS_ENTRY_BRIDGE_5:
            lambda state: True,
        LOC_NOTE_BGS_SWITCH_LOG_1:
            lambda state: True,
        LOC_NOTE_BGS_SWITCH_LOG_2:
            lambda state: True,
        LOC_NOTE_BGS_SWITCH_LOG_3:
            lambda state: True,
        LOC_NOTE_BGS_STUMP_LOG_1:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_STUMP_LOG_2:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_STUMP_LOG_3:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_TURTLE_LOG_1:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_TURTLE_LOG_2:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_TURTLE_LOG_3:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_TANKTUPS_FLIPPERS_1:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_TANKTUPS_FLIPPERS_2:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_TANKTUPS_FLIPPERS_3:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_TANKTUPS_FLIPPERS_4:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_PILLAR_LOG_1:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_PILLAR_LOG_2:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_PILLAR_LOG_3:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_CROCODILE_LOG_1:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_CROCODILE_LOG_2:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_CROCODILE_LOG_3:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_CROCODILES_SNOUT_1:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_CROCODILES_SNOUT_2:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_CROCODILES_SNOUT_3:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_CROCODILES_SNOUT_4:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_CROCODILES_SNOUT_5:
            lambda state:
            (
                can_traverse_bgs(state, player)
            ),
        LOC_NOTE_BGS_BEHIND_EGG_1:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_EGG_2:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_EGG_3:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_EGG_4:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_EGG_5:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_FIRST_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_FIRST_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_FIRST_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_FIRST_BRIDGE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_FIRST_BRIDGE_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_SECOND_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_SECOND_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_SECOND_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_SECOND_BRIDGE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_THIRD_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_THIRD_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_THIRD_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_THIRD_BRIDGE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_THIRD_BRIDGE_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_THIRD_BRIDGE_6:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_THIRD_BRIDGE_7:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_FOURTH_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_FOURTH_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_FOURTH_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_FOURTH_BRIDGE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_INSIDE_TANKTUP_1:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_INSIDE_TANKTUP_2:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_INSIDE_TANKTUP_3:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_INSIDE_TANKTUP_4:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_INSIDE_TANKTUP_5:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_INSIDE_TANKTUP_6:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_DESTROY_HUT_1:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_DESTROY_HUT_2:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_DESTROY_HUT_3:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_DESTROY_HUT_4:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_DESTROY_HUT_5:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_BGS_CATTAIL_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_TALON_TROT, player) or
                            state.has(ITEM_STILT_STRIDE, player)
                        )
                    )
                )
            ),
        LOC_NOTE_BGS_CATTAIL_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_TALON_TROT, player) or
                            state.has(ITEM_STILT_STRIDE, player)
                        )
                    )
                ) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    (
                        state.has(ITEM_JUMP, player) or
                        state.has(ITEM_BEAK_BUSTER, player)
                    )
                )
            ),
        LOC_NOTE_BGS_CATTAIL_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_TALON_TROT, player) or
                            state.has(ITEM_STILT_STRIDE, player)
                        )
                    )
                )
            ),
        LOC_NOTE_BGS_BEHIND_JINJO_1:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_JINJO_2:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_JINJO_3:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_JINJO_4:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_JINJO_5:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_MAZE_1:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_MAZE_2:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_MAZE_3:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_MAZE_4:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_MAZE_5:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_MAZE_6:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_MAZE_7:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_MAZE_8:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_MAZE_9:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_MAZE_10:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_MAZE_11:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_MAZE_12:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_RIGHT_NOSTRIL_1:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_RIGHT_NOSTRIL_2:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_RIGHT_NOSTRIL_3:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_LEFT_NOSTRIL_1:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_LEFT_NOSTRIL_2:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_LEFT_NOSTRIL_3:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_UNDER_PILLAR_1:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_UNDER_PILLAR_2:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_UNDER_PILLAR_3:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_UNDER_PILLAR_4:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player) and
                state.has(ITEM_TRANSFORMATION_CROCODILE, player)
            ),
        LOC_NOTE_BGS_BEHIND_PILLARS_1:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_PILLARS_2:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_PILLARS_3:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_PILLARS_4:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_BGS_BEHIND_PILLARS_5:
            lambda state:
            (
                can_traverse_bgs(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
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
        LOC_JINJO_FP_BLUE:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) or
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_JINJO_FP_GREEN:
            lambda state: True,
        LOC_JINJO_FP_ORANGE:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                state.has(ITEM_TRANSFORMATION_WALRUS, player) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_JINJO_FP_PURPLE:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JINJO_FP_YELLOW:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
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
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_FLIGHT, player)
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
        LOC_NOTE_FP_UPPER_BOGGY_RAMP_1:
            lambda state: True,
        LOC_NOTE_FP_UPPER_BOGGY_RAMP_2:
            lambda state: True,
        LOC_NOTE_FP_UPPER_BOGGY_RAMP_3:
            lambda state: True,
        LOC_NOTE_FP_UPPER_BOGGY_RAMP_4:
            lambda state: True,
        LOC_NOTE_FP_UPPER_BOGGY_RAMP_5:
            lambda state: True,
        LOC_NOTE_FP_LOWER_BOGGY_RAMP_1:
            lambda state: True,
        LOC_NOTE_FP_LOWER_BOGGY_RAMP_2:
            lambda state: True,
        LOC_NOTE_FP_LOWER_BOGGY_RAMP_3:
            lambda state: True,
        LOC_NOTE_FP_LOWER_BOGGY_RAMP_4:
            lambda state: True,
        LOC_NOTE_FP_BEHIND_TREE_1:
            lambda state: True,
        LOC_NOTE_FP_BEHIND_TREE_2:
            lambda state: True,
        LOC_NOTE_FP_BEHIND_TREE_3:
            lambda state: True,
        LOC_NOTE_FP_BEHIND_TREE_4:
            lambda state: True,
        LOC_NOTE_FP_BEHIND_TREE_5:
            lambda state: True,
        LOC_NOTE_FP_JINJO_PRESENTS_1:
            lambda state: True,
        LOC_NOTE_FP_JINJO_PRESENTS_2:
            lambda state: True,
        LOC_NOTE_FP_JINJO_PRESENTS_3:
            lambda state: True,
        LOC_NOTE_FP_JINJO_PRESENTS_4:
            lambda state: True,
        LOC_NOTE_FP_SLUSH_PRESENT_1:
            lambda state: True,
        LOC_NOTE_FP_SLUSH_PRESENT_2:
            lambda state: True,
        LOC_NOTE_FP_SLUSH_PRESENT_3:
            lambda state: True,
        LOC_NOTE_FP_SLUSH_PRESENT_4:
            lambda state: True,
        LOC_NOTE_FP_SKULL_HOUSE_1:
            lambda state: True,
        LOC_NOTE_FP_SKULL_HOUSE_2:
            lambda state: True,
        LOC_NOTE_FP_SKULL_HOUSE_3:
            lambda state: True,
        LOC_NOTE_FP_SLUSH_HOUSE_1:
            lambda state: True,
        LOC_NOTE_FP_SLUSH_HOUSE_2:
            lambda state: True,
        LOC_NOTE_FP_SLUSH_HOUSE_3:
            lambda state: True,
        LOC_NOTE_FP_BEEHIVE_PLATFORM_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_BEEHIVE_PLATFORM_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_BEEHIVE_PLATFORM_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_BEEHIVE_PLATFORM_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_LEFT_FOOT_1:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_LEFT_FOOT_2:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_LEFT_FOOT_3:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_LEFT_FOOT_4:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_LEFT_FOOT_5:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_RIGHT_FOOT_1:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_RIGHT_FOOT_2:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_RIGHT_FOOT_3:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_RIGHT_FOOT_4:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_RIGHT_FOOT_5:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_INSIDE_TREE_1:
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
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_FP_INSIDE_TREE_2:
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
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_FP_INSIDE_TREE_3:
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
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_FP_INSIDE_TREE_4:
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
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_FP_INSIDE_TREE_5:
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
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_FP_INSIDE_TREE_6:
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
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_FP_INSIDE_TREE_7:
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
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_FP_INSIDE_TREE_8:
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
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_FP_INSIDE_TREE_9:
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
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_FP_INSIDE_TREE_10:
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
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_FP_INSIDE_TREE_11:
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
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_FP_INSIDE_TREE_12:
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
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_FP_WOZZA_PLATFORM_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_WOZZA_PLATFORM_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_WOZZA_PLATFORM_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_WOZZA_PLATFORM_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_6:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_7:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_8:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_9:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_10:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_11:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_12:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_13:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_14:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_SCARF_15:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_NECK_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_NECK_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_NECK_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_NECK_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_HAT_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_HAT_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_HAT_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_HAT_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_HAT_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_HAT_6:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_HAT_7:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_SNOWMANS_HAT_8:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_NOTE_FP_MUMBOS_SKULL_1:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_FP_MUMBOS_SKULL_2:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_FP_MUMBOS_SKULL_3:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_FP_MUMBOS_SKULL_4:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_FP_MUMBOS_SKULL_5:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_FP_MUMBOS_SKULL_6:
            lambda state:
            (
                (
                    state.has(ITEM_FLIGHT, player) or    #required to reach Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_FP_MUMBO_ISLAND_1:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_FP_MUMBO_ISLAND_2:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_FP_MUMBO_ISLAND_3:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_FP_MUMBO_ISLAND_4:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_FP_MUMBO_ISLAND_5:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_FP_MUMBO_ISLAND_6:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_FP_MUMBO_ISLAND_7:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_FP_MUMBO_ISLAND_8:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_FP_MUMBO_ISLAND_9:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_MOLEHILL_GV_NEAR_KAZOOIE_PYRAMID:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_JIGGY_GV_JINXY:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_JIGGY_GV_GRABBA:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_JIGGY_GV_FLIP_PANELS:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    state.has(ITEM_BEAK_BUSTER, player)
                )
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
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_JIGGY_GV_RUBEE:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_BEAK_BOMB, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_JIGGY_GV_SANDYBUTT:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_JIGGY_GV_GOBI:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_JIGGY_GV_TRUNKER:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    state.has(ITEM_BEAK_BUSTER, player) and
                    (
                        (
                            state.has(ITEM_CLIMB, player) and
                            (
                                state.has(ITEM_FEATHERY_FLAP, player) or #to get on top of Trunker, you can either
                                state.has(ITEM_RAT_A_TAT_RAP, player) or #climb up a nearby tree and jump across, or...
                                (
                                    state.has(ITEM_JUMP, player) and
                                    state.has(ITEM_TALON_TROT, player)
                                )
                            )
                        ) or
                        (
                            state.has(ITEM_FLAP_FLIP, player) or #...or get to the flight pad and fly over
                            (
                                state.has(ITEM_JUMP, player) and
                                (
                                    state.has(ITEM_FEATHERY_FLAP, player) or
                                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                                    state.has(ITEM_TALON_TROT, player)
                                )
                            )
                        )
                    ) and
                    state.has(ITEM_FLIGHT, player)
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
        LOC_JINJO_GV_BLUE:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_JINJO_GV_GREEN:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_JINJO_GV_ORANGE:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_JINJO_GV_PURPLE:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_JINJO_GV_YELLOW:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_EMPTY_HONEYCOMB_GV_CACTUS:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_BEAK_BUSTER, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_EMPTY_HONEYCOMB_GV_GOBI:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_MUMBO_TOKEN_GV_BEHIND_JINXY:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    state.has(ITEM_STILT_STRIDE, player)
                )
            ),
        LOC_MUMBO_TOKEN_GV_ABOVE_JINXYS_NOSE:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_MUMBO_TOKEN_GV_INSIDE_JINXY:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_GV_OUTSIDE_WATER_PYRAMID_FRONT:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_MUMBO_TOKEN_GV_FLIP_PANEL_PYRAMID:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_MUMBO_TOKEN_GV_MOAT:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_MUMBO_TOKEN_GV_RUBEE:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_MUMBO_TOKEN_GV_ATOP_CENTRAL_PYRAMID:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    state.has(ITEM_EGGS, player) or #if you raise the tomb, you can just walk up it
                    (
                        (
                            (
                                state.has(ITEM_FLAP_FLIP, player) and
                                (
                                    state.has(ITEM_FEATHERY_FLAP, player) or
                                    state.has(ITEM_RAT_A_TAT_RAP, player)
                                )
                            ) or
                            (
                                state.has(ITEM_JUMP, player) and
                                (
                                    state.has(ITEM_FEATHERY_FLAP, player) or
                                    state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                                    state.has(ITEM_TALON_TROT, player)
                                )
                            )
                        ) and
                        state.has(ITEM_FLIGHT, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_GV_CENTRAL_PYRAMID_POT:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_MUMBO_TOKEN_GV_INSIDE_WATER_PYRAMID:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_GV_ENTRYWAY_SLOPE_1:
            lambda state: True,
        LOC_NOTE_GV_ENTRYWAY_SLOPE_2:
            lambda state: True,
        LOC_NOTE_GV_ENTRYWAY_SLOPE_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_ENTRYWAY_SLOPE_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_ENTRYWAY_SLOPE_5:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_RIGHT_PAW_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_RIGHT_PAW_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_RIGHT_PAW_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_LEFT_PAW_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_LEFT_PAW_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_LEFT_PAW_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_MAGIC_CARPET_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_MAGIC_CARPET_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_MAGIC_CARPET_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_MAGIC_CARPET_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_MAGIC_CARPET_5:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_TOMB_STAIRS_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_TOMB_STAIRS_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_TOMB_STAIRS_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_TOMB_STAIRS_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_PYRAMID_STAIRS_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_PYRAMID_STAIRS_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_PYRAMID_STAIRS_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_PYRAMID_STAIRS_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_FLIP_PYRAMID_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_FLIP_PYRAMID_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_FLIP_PYRAMID_FRONT_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_FLIP_PYRAMID_FRONT_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_FLIP_PYRAMID_FRONT_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_FLIP_PYRAMID_FRONT_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_AROUND_TOMB_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_AROUND_TOMB_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_AROUND_TOMB_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_AROUND_TOMB_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_AROUND_TOMB_5:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_AROUND_TOMB_6:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_AROUND_TOMB_7:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_AROUND_TOMB_8:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_AROUND_TOMB_9:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_TT_PLATFORM_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_TT_PLATFORM_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_RACE_PATH_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_RACE_PATH_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_RACE_PATH_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_RACE_PATH_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_5:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_6:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_7:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_BEHIND_JINXY_8:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_JINXY_FLOOR_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_GV_JINXY_FLOOR_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_GV_JINXY_FLOOR_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_GV_JINXY_FLOOR_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player)
            ),
        LOC_NOTE_GV_JINXY_CARPETS_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_GV_JINXY_CARPETS_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_GV_JINXY_CARPETS_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_FLAP_FLIP, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_GV_GRABBAS_PLATFORM_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_GRABBAS_PLATFORM_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_GRABBAS_PLATFORM_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_GRABBAS_PLATFORM_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_GRABBAS_PLATFORM_5:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_GRABBAS_PLATFORM_6:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_GRABBAS_PLATFORM_7:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_GRABBAS_PLATFORM_8:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_GRABBAS_PLATFORM_9:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_GRABBAS_PLATFORM_10:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_GRABBAS_PLATFORM_11:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_NOTE_GV_TOMB_ENTRYWAY_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_TOMB_ENTRYWAY_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_TOMB_ENTRYWAY_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_TOMB_EXIT_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_TOMB_EXIT_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_TOMB_EXIT_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_TOMB_EXIT_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player)
            ),
        LOC_NOTE_GV_INSIDE_WATER_PYRAMID_1:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_GV_INSIDE_WATER_PYRAMID_2:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_GV_INSIDE_WATER_PYRAMID_3:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_GV_INSIDE_WATER_PYRAMID_4:
            lambda state:
            (
                state.has(ITEM_TURBO_TALON_TROT, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_GV_TOMB_MOAT_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_GV_TOMB_MOAT_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_GV_TOMB_MOAT_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_GV_TOMB_MOAT_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_GV_TOMB_MOAT_5:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_GV_TOMB_MOAT_6:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_GV_INSIDE_FLIP_PYRAMID_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_GV_INSIDE_FLIP_PYRAMID_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_GV_INSIDE_FLIP_PYRAMID_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_GV_INSIDE_FLIP_PYRAMID_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_1:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_2:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_3:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_4:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_5:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_6:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_7:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_NOTE_GV_INSIDE_RUBEES_PYRAMID_8:
            lambda state:
            (
                can_reach_gv_rest_of_level(state, player) and
                (
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                        )
                    ) or
                    (
                        state.has(ITEM_JUMP, player) and
                        (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or   #required to get on top of Jinxy
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
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
                    can_break_breakable_gates(state, player) or
                    state.has(ITEM_BEAK_BUSTER, player)
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
                        state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                        can_break_breakable_gates(state, player)
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
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_TALON_TROT, player) and
                    state.has(ITEM_CLIMB, player)
            ),
        LOC_JIGGY_MMM_MOTZAND:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_JIGGY_MMM_LOGGO:
            lambda state:
            (
                    can_reach_mmm_second_floor(state, player) and
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
            ),
        LOC_JIGGY_MMM_STORM_DRAIN:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player)
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
        LOC_JINJO_MMM_BLUE:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_JINJO_MMM_GREEN:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_JINJO_MMM_ORANGE:
            lambda state: True,
        LOC_JINJO_MMM_PURPLE:
            lambda state:
            (
                can_break_breakable_gates(state, player)
            ),
        LOC_JINJO_MMM_YELLOW:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player)
            ),
        LOC_EMPTY_HONEYCOMB_MMM_CHURCH_RAFTER:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    state.has(ITEM_FLIGHT, player)
            ),
        LOC_EMPTY_HONEYCOMB_MMM_FLOORBOARD:
            lambda state:
            (
                    can_reach_mmm_second_floor(state, player) and
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_MMM_FIREPLACE:
            lambda state:
            (
                    (
                    state.has(ITEM_CLIMB, player) and      #you can either climb up the mansion and enter the chimney...
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
                ) or
                    can_break_breakable_gates(state, player)          #or just break down the front door and walk in
            ),
        LOC_MUMBO_TOKEN_MMM_CELLAR:
            lambda state:
            (
                can_break_breakable_gates(state, player)
            ),
        LOC_MUMBO_TOKEN_MMM_LOGGO:
            lambda state:
            (
                can_reach_mmm_second_floor(state, player) and
                (
                        can_break_breakable_gates(state, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_MUMBO_TOKEN_MMM_SINK:
            lambda state:
            (
                can_reach_mmm_second_floor(state, player)
            ),
        LOC_MUMBO_TOKEN_MMM_MAZE:
            lambda state: True,
        LOC_MUMBO_TOKEN_MMM_MAZE_HIDDEN_AREA:
            lambda state:
            (
                (                   #you can either turn into a pumpkin and go in through the small gap in the hedge...
                        can_break_breakable_gates(state, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player)
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
                        can_break_breakable_gates(state, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_MUMBO_TOKEN_MMM_BEHIND_GRAVE:
            lambda state:
            (
                can_break_breakable_gates(state, player)
            ),
        LOC_MUMBO_TOKEN_MMM_CLOCK_TOWER:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_MMM_CHURCH_CHAIR:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player) and
                    state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_MUMBO_TOKEN_MMM_CHURCH_RAFTER:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
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
                can_reach_mmm_second_floor(state, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_MUMBO_TOKEN_MMM_FOUNTAIN:
            lambda state:
            (
                state.has(ITEM_EGGS, player)
            ),
        LOC_MUMBO_TOKEN_MMM_NEAR_FOUNTAIN:
            lambda state: True,
        LOC_NOTE_MMM_ENTRANCE_WALL_1:
            lambda state: True,
        LOC_NOTE_MMM_ENTRANCE_WALL_2:
            lambda state: True,
        LOC_NOTE_MMM_ENTRANCE_WALL_3:
            lambda state: True,
        LOC_NOTE_MMM_ENTRANCE_WALL_4:
            lambda state: True,
        LOC_NOTE_MMM_HEDGE_MAZE_1:
            lambda state: True,
        LOC_NOTE_MMM_HEDGE_MAZE_2:
            lambda state: True,
        LOC_NOTE_MMM_HEDGE_MAZE_3:
            lambda state: True,
        LOC_NOTE_MMM_HEDGE_MAZE_4:
            lambda state: True,
        LOC_NOTE_MMM_HEDGE_MAZE_5:
            lambda state: True,
        LOC_NOTE_MMM_HEDGE_MAZE_6:
            lambda state: True,
        LOC_NOTE_MMM_FOUNTAIN_1:
            lambda state: True,
        LOC_NOTE_MMM_FOUNTAIN_2:
            lambda state: True,
        LOC_NOTE_MMM_FOUNTAIN_3:
            lambda state: True,
        LOC_NOTE_MMM_FOUNTAIN_4:
            lambda state: True,
        LOC_NOTE_MMM_GRAVEYARD_ALCOVE_1:
            lambda state: True,
        LOC_NOTE_MMM_GRAVEYARD_ALCOVE_2:
            lambda state: True,
        LOC_NOTE_MMM_GRAVEYARD_ALCOVE_3:
            lambda state: True,
        LOC_NOTE_MMM_GUTTER_DRAIN_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                        can_break_breakable_gates(state, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_MMM_GUTTER_DRAIN_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                        can_break_breakable_gates(state, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_MMM_GUTTER_DRAIN_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                        can_break_breakable_gates(state, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_MMM_GUTTER_DRAIN_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                        can_break_breakable_gates(state, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_1:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_2:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_3:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_4:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_5:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_6:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_7:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_MMM_DINING_ROOM_CHAIR_8:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_MMM_UPPER_GUTTERS_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_UPPER_GUTTERS_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_UPPER_GUTTERS_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_UPPER_GUTTERS_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_1:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player)
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_2:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player)
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_3:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player)
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_4:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player)
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_5:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player)
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_6:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player)
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_7:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player)
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_8:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player)
            ),
        LOC_NOTE_MMM_PAINTING_ROOM_9:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player)
            ),
        LOC_NOTE_MMM_BEDROOM_DRESSER_1:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_MMM_BEDROOM_DRESSER_2:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_MMM_BEDROOM_DRESSER_3:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_MMM_BEDROOM_DRESSER_4:
            lambda state:
            (
                can_reach_mmm_third_floor(state, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player)
                )
            ),
        LOC_NOTE_MMM_BASEMENT_WINE_RACK_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                (
                        can_break_breakable_gates(state, player) or
                        state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_NOTE_MMM_BASEMENT_WINE_RACK_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                (
                        can_break_breakable_gates(state, player) or
                        state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_NOTE_MMM_BASEMENT_WINE_RACK_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                (
                        can_break_breakable_gates(state, player) or
                        state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_NOTE_MMM_BASEMENT_WINE_RACK_4:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                (
                        can_break_breakable_gates(state, player) or
                        state.has(ITEM_BEAK_BUSTER, player)
                )
            ),
        LOC_NOTE_MMM_CHURCH_ROOF_1:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CHURCH_ROOF_2:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CHURCH_ROOF_3:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CHURCH_ROOF_4:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CHURCH_ROOF_5:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CHURCH_ROOF_6:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CHURCH_ROOF_7:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CHURCH_ROOF_8:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CHURCH_ROOF_9:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CHURCH_ROOF_10:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CLOCK_TOWER_1:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CLOCK_TOWER_2:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CLOCK_TOWER_3:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_CLOCK_TOWER_4:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_JUMP, player) and
                    (
                    state.has(ITEM_TALON_TROT, player) or
                    (
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player)
                    )
                )
            ),
        LOC_NOTE_MMM_ON_TUMBLARS_SHACK_1:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_ON_TUMBLARS_SHACK_2:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_ON_TUMBLARS_SHACK_3:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_ON_TUMBLARS_SHACK_4:
            lambda state:
            (
                state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_CHURCH_PEW_1:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_WONDERWING, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player) and
                    state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MMM_CHURCH_PEW_2:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_WONDERWING, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player) and
                    state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MMM_CHURCH_PEW_3:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_WONDERWING, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player) and
                    state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MMM_CHURCH_PEW_4:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_WONDERWING, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player) and
                    state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MMM_ORGAN_PEDALS_1:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_MMM_ORGAN_PEDALS_2:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player)
            ),
        LOC_NOTE_MMM_ORGAN_PIPES_1:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_ORGAN_PIPES_2:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_ORGAN_PIPES_3:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_ORGAN_PIPES_4:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_BEAK_BUSTER, player) and
                    state.has(ITEM_TURBO_TALON_TROT, player) and
                    state.has(ITEM_FLAP_FLIP, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player)
            ),
        LOC_NOTE_MMM_WELL_LEDGES_1:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_MMM_WELL_LEDGES_2:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_MMM_WELL_LEDGES_3:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_MMM_WELL_LEDGES_4:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player) or
                (
                    state.has(ITEM_JUMP, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                        can_break_breakable_gates(state, player)
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                        can_break_breakable_gates(state, player)
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                        can_break_breakable_gates(state, player)
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                        can_break_breakable_gates(state, player)
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                        can_break_breakable_gates(state, player)
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                        can_break_breakable_gates(state, player)
                )
            ),
        LOC_NOTE_MMM_INSIDE_WELL_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                (
                        state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                        state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                        can_break_breakable_gates(state, player)
                )
            ),
        LOC_NOTE_MMM_MUMBOS_SKULL_1:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MMM_MUMBOS_SKULL_2:
            lambda state:
            (
                    can_break_breakable_gates(state, player) and
                    state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_MMM_INSIDE_TUMBLARS_SHACK_1:
            lambda state:
            (
                can_break_breakable_gates(state, player)
            ),
        LOC_NOTE_MMM_INSIDE_TUMBLARS_SHACK_2:
            lambda state:
            (
                can_break_breakable_gates(state, player)
            ),
        LOC_NOTE_MMM_INSIDE_TUMBLARS_SHACK_3:
            lambda state:
            (
                can_break_breakable_gates(state, player)
            ),
        LOC_NOTE_MMM_INSIDE_TUMBLARS_SHACK_4:
            lambda state:
            (
                can_break_breakable_gates(state, player)
            ),
        LOC_NOTE_MMM_RAIN_BARREL_1:
            lambda state:
            (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                    can_break_breakable_gates(state, player)
            ),
        LOC_NOTE_MMM_RAIN_BARREL_2:
            lambda state:
            (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                    can_break_breakable_gates(state, player)
            ),
        LOC_NOTE_MMM_RAIN_BARREL_3:
            lambda state:
            (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                    can_break_breakable_gates(state, player)
            ),
        LOC_NOTE_MMM_RAIN_BARREL_4:
            lambda state:
            (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                    can_break_breakable_gates(state, player)
            ),
        LOC_NOTE_MMM_RAIN_BARREL_5:
            lambda state:
            (
                    state.has(ITEM_TRANSFORMATION_PUMPKIN, player) and
                    state.has(ITEM_FLAP_FLIP, player) and  #required to get to Mumbo's Skull
                    can_break_breakable_gates(state, player)
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
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_FLAP_FLIP, player) or        #you can either climb on top of the box...
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        (
                            state.has(ITEM_JUMP, player) and
                            state.has(ITEM_TALON_TROT, player)
                        )
                    ) or
                    (
                        state.has(ITEM_TALON_TROT, player) and  #...or take the ladder (or the toll roads around)
                        state.has(ITEM_SHOCK_SPRING_JUMP, player)
                    )
                )
            ),
        LOC_JIGGY_RBB_CAPTAINS_ROOM:
            lambda state:
            (
                can_break_rbb_windows(state, player) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player) or        #to get the Jiggy
                    state.has(ITEM_BEAK_BUSTER, player)          #not tested but probably works?
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
        LOC_JINJO_RBB_BLUE:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or  # you can climb the ladder (or the box on the ship)...
                (
                    state.has(ITEM_EGGS, player) and  # or take the toll bridges around
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_JINJO_RBB_GREEN:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or   #you can climb the ladder (or the box on the ship)...
                    (
                        state.has(ITEM_EGGS, player) and    #or take the toll bridges around
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or    #you need these to get the Jinjo safely regardless
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_JINJO_RBB_ORANGE:
            lambda state:
            (
                state.has(ITEM_EGGS, player) and    #you pay the troll toll, like it or not:P
                state.has(ITEM_CLIMB, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or  #to climb the box on the ship
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_JINJO_RBB_PURPLE:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JINJO_RBB_YELLOW:
            lambda state:
            (
                state.has(ITEM_FEATHERY_FLAP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
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
                state.has(ITEM_SWIM, player) and   #evading Snacker is fairly reasonable for this
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
                can_break_rbb_windows(state, player) and
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
                can_break_rbb_windows(state, player)
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
                (
                    state.has(ITEM_CLIMB, player) or   #you can climb the ladder (or the box on the ship)...
                    (
                        state.has(ITEM_EGGS, player) and    #or take the toll bridges around
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or    #you need these to get the token safely regardless
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_RBB_SHIP_BOW:
            lambda state: True,
        LOC_MUMBO_TOKEN_RBB_LEFT_SHIPPING_CRATE:
            lambda state:
            (
                (                                   #first, you need to get to the crate, either from
                state.has(ITEM_CLIMB, player) or    #the ladder (or ship's crane)...
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
                (                                   #first, you need to get to the crate, either from
                state.has(ITEM_CLIMB, player) or    #the ladder (or ship's crane)...
                    (
                        state.has(ITEM_EGGS, player) and        #...or by going around the perimeter of the level
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_FLAP_FLIP, player)            #then you need to actually be able to get the token
                )
            ),
        LOC_NOTE_RBB_GANGPLANK_1:
            lambda state: True,
        LOC_NOTE_RBB_GANGPLANK_2:
            lambda state: True,
        LOC_NOTE_RBB_GANGPLANK_3:
            lambda state: True,
        LOC_NOTE_RBB_GANGPLANK_4:
            lambda state: True,
        LOC_NOTE_RBB_GANGPLANK_5:
            lambda state: True,
        LOC_NOTE_RBB_AFT_RAMP_1:
            lambda state: True,
        LOC_NOTE_RBB_AFT_RAMP_2:
            lambda state: True,
        LOC_NOTE_RBB_AFT_RAMP_3:
            lambda state: True,
        LOC_NOTE_RBB_AFT_RAMP_4:
            lambda state: True,
        LOC_NOTE_RBB_AFT_DECK_1:
            lambda state: True,
        LOC_NOTE_RBB_AFT_DECK_2:
            lambda state: True,
        LOC_NOTE_RBB_AFT_DECK_3:
            lambda state: True,
        LOC_NOTE_RBB_AFT_DECK_4:
            lambda state: True,
        LOC_NOTE_RBB_AFT_DECK_5:
            lambda state: True,
        LOC_NOTE_RBB_AFT_DECK_6:
            lambda state: True,
        LOC_NOTE_RBB_FAN_ROOM_1:
            lambda state: True,
        LOC_NOTE_RBB_FAN_ROOM_2:
            lambda state: True,
        LOC_NOTE_RBB_FAN_ROOM_3:
            lambda state: True,
        LOC_NOTE_RBB_FAN_ROOM_4:
            lambda state: True,
        LOC_NOTE_RBB_KITCHEN_1:
            lambda state: True,
        LOC_NOTE_RBB_KITCHEN_2:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FEATHERY_FLAP, player) or    #this counter is a little higher up than the others
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_NOTE_RBB_KITCHEN_3:
            lambda state: True,
        LOC_NOTE_RBB_KITCHEN_4:
            lambda state: True,
        LOC_NOTE_RBB_KITCHEN_5:
            lambda state: True,
        LOC_NOTE_RBB_STOREROOM_SHELF_1:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_STOREROOM_SHELF_2:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_STOREROOM_SHELF_3:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_STOREROOM_SHELF_4:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_STOREROOM_SHELF_5:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_WHISTLES_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_WHISTLES_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_RBB_LOWER_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_LOWER_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_LOWER_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_LOWER_BRIDGE_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_UPPER_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_UPPER_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_UPPER_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_UPPER_BRIDGE_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_BUNK_ROOM_1:
            lambda state:
            (
                can_break_rbb_windows(state, player)
            ),
        LOC_NOTE_RBB_BUNK_ROOM_2:
            lambda state:
            (
                can_break_rbb_windows(state, player)
            ),
        LOC_NOTE_RBB_BUNK_ROOM_3:
            lambda state:
            (
                can_break_rbb_windows(state, player)
            ),
        LOC_NOTE_RBB_BUNK_ROOM_4:
            lambda state:
            (
                can_break_rbb_windows(state, player)
            ),
        LOC_NOTE_RBB_NAVIGATION_ROOM_1:
            lambda state:
            (
                can_break_rbb_windows(state, player)
            ),
        LOC_NOTE_RBB_NAVIGATION_ROOM_2:
            lambda state:
            (
                can_break_rbb_windows(state, player)
            ),
        LOC_NOTE_RBB_NAVIGATION_ROOM_3:
            lambda state:
            (
                can_break_rbb_windows(state, player)
            ),
        LOC_NOTE_RBB_NAVIGATION_ROOM_4:
            lambda state:
            (
                can_break_rbb_windows(state, player)
            ),
        LOC_NOTE_RBB_CAPTAINS_BEDROOM_1:
            lambda state:
            (
                can_break_rbb_windows(state, player)
            ),
        LOC_NOTE_RBB_CAPTAINS_BEDROOM_2:
            lambda state:
            (
                can_break_rbb_windows(state, player)
            ),
        LOC_NOTE_RBB_CAPTAINS_BEDROOM_3:
            lambda state:
            (
                can_break_rbb_windows(state, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_RIGHT_1:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_RIGHT_2:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_RIGHT_3:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_RIGHT_4:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_LEFT_1:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_LEFT_2:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_LEFT_3:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_LEFT_4:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_CENTER_1:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_BEAK_BUSTER, player)         #to hit the switch before entering
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_CENTER_2:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_BEAK_BUSTER, player)         #to hit the switch before entering
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_CENTER_3:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_BEAK_BUSTER, player)         #to hit the switch before entering
            ),
        LOC_NOTE_RBB_ENGINE_ROOM_CENTER_4:
            lambda state:
            (
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BARGE, player) or   #to open the engine room door
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_CLIMB, player) and
                state.has(ITEM_BEAK_BUSTER, player)         #to hit the switch before entering
            ),
        LOC_NOTE_RBB_JINJO_GRATE_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_RBB_JINJO_GRATE_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_RBB_JINJO_GRATE_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_RBB_JINJO_GRATE_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_RBB_CRANE_CATWALK_1:
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
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_CRANE_CATWALK_2:
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
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_CRANE_CATWALK_3:
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
                state.has(ITEM_CLIMB, player)
            ),
        LOC_NOTE_RBB_FLOODED_WAREHOUSE_1:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_EGGS, player) and    #to get to the notes, you can either take the toll road...
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
        LOC_NOTE_RBB_FLOODED_WAREHOUSE_2:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_EGGS, player) and    #to get to the notes, you can either take the toll road...
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
        LOC_NOTE_RBB_FLOODED_WAREHOUSE_3:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_EGGS, player) and    #to get to the notes, you can either take the toll road...
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
        LOC_NOTE_RBB_FLOODED_WAREHOUSE_4:
            lambda state:
            (
                (
                    (
                        state.has(ITEM_EGGS, player) and    #to get to the notes, you can either take the toll road...
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
        LOC_NOTE_RBB_SNACKERS_POOL_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_EGGS, player)
                )

            ),
        LOC_NOTE_RBB_SNACKERS_POOL_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_EGGS, player)
                )

            ),
        LOC_NOTE_RBB_SNACKERS_POOL_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_EGGS, player)
                )

            ),
        LOC_NOTE_RBB_SNACKERS_POOL_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_EGGS, player)
                )

            ),
        LOC_NOTE_RBB_SNACKERS_POOL_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_EGGS, player)
                )

            ),
        LOC_NOTE_RBB_TOXIC_BARREL_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or   #you can climb the ladder (or the box on the ship)...
                (
                    state.has(ITEM_EGGS, player) and    #or take the toll bridges around
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_RBB_TOXIC_BARREL_2:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or   #you can climb the ladder (or the box on the ship)...
                    (
                        state.has(ITEM_EGGS, player) and    #or take the toll bridges around
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or    #you need these to get the note safely regardless
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_RBB_TOXIC_BARREL_3:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or   #you can climb the ladder (or the box on the ship)...
                    (
                        state.has(ITEM_EGGS, player) and    #or take the toll bridges around
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or    #you need these to get the note safely regardless
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_NOTE_RBB_TOXIC_CRANE_1:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_FLAP_FLIP, player) or        #you can either climb on top of the box...
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        (
                            state.has(ITEM_JUMP, player) and
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) or
                (
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                        state.has(ITEM_CLIMB, player) or  #...or take the ladder (or the toll roads around)
                        (
                            state.has(ITEM_EGGS, player) and
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ),
        LOC_NOTE_RBB_TOXIC_CRANE_2:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_FLAP_FLIP, player) or        #you can either climb on top of the box...
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        (
                            state.has(ITEM_JUMP, player) and
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) or
                (
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                        state.has(ITEM_CLIMB, player) or  #...or take the ladder (or the toll roads around)
                        (
                            state.has(ITEM_EGGS, player) and
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ),
        LOC_NOTE_RBB_TOXIC_CRANE_3:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_FLAP_FLIP, player) or        #you can either climb on top of the box...
                        state.has(ITEM_RAT_A_TAT_RAP, player) or
                        (
                            state.has(ITEM_JUMP, player) and
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                ) or
                (
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                        state.has(ITEM_CLIMB, player) or  #...or take the ladder (or the toll roads around)
                        (
                            state.has(ITEM_EGGS, player) and
                            state.has(ITEM_TALON_TROT, player)
                        )
                    )
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_1_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                    state.has(ITEM_EGGS, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_1_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                    state.has(ITEM_EGGS, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_1_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                    state.has(ITEM_EGGS, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_1_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                    state.has(ITEM_EGGS, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_1_5:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_1_6:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_1_7:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_1_8:
            lambda state:
            (
                (
                    state.has(ITEM_CLIMB, player) or
                    (
                        state.has(ITEM_EGGS, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_3_1:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                    state.has(ITEM_EGGS, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_3_2:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                    state.has(ITEM_EGGS, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_3_3:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                    state.has(ITEM_EGGS, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_RBB_WAREHOUSE_3_4:
            lambda state:
            (
                state.has(ITEM_CLIMB, player) or
                (
                    state.has(ITEM_EGGS, player) and
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_NOTE_RBB_ANCHOR_ROOM_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_RBB_ANCHOR_ROOM_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_RBB_ANCHOR_ROOM_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_NOTE_RBB_ANCHOR_ROOM_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_CCW_TREETOP_ROOM:
            lambda state:
            (
                can_break_breakable_gates(state, player) and
                (
                    (
                        can_reach_ccw_cabin(state, player, ITEM_SEASON_SPRING) and
                        state.has(ITEM_FLAP_FLIP, player)
                    ) or
                    (
                        can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER) and
                        state.has(ITEM_FLAP_FLIP, player)
                    ) or
                    (
                        can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER) and
                        (
                            state.has(ITEM_FLAP_FLIP, player) or
                            state.has(ITEM_FLIGHT, player)
                        )
                    )
                )
            ),
        LOC_JIGGY_CCW_TREETOP_SNAREBEAR:
            lambda state:
            (
                (
                    state.has(ITEM_SEASON_SPRING, player) and
                    state.has(ITEM_TRANSFORMATION_BEE, player) and
                    (
                        state.has(ITEM_TALON_TROT, player) or       #required to access Mumbo's Skull
                        state.has(ITEM_STILT_STRIDE, player)
                    )
                ) or
                (
                    state.has(ITEM_SEASON_WINTER, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_JIGGY_CCW_ZUBBA:
            lambda state:
            (
                can_reach_ccw_beehive(state, player, ITEM_SEASON_SPRING) and
                state.has(ITEM_BEAK_BUSTER, player)         #yes, you can beat the Zubbas with just Beak Buster
            ),
        LOC_JIGGY_CCW_LEAVES:
            lambda state:
            (
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER)
            ),
        LOC_JIGGY_CCW_CABIN:
            lambda state:
            (
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER)
            ),
        LOC_JIGGY_CCW_GNAWTY:
            lambda state:
            (
                (
                    state.has(ITEM_SEASON_SUMMER, player) and
                    (
                        state.has(ITEM_BEAK_BARGE, player) or           #required to break the boulder
                        state.has(ITEM_BEAK_BUSTER, player) or
                        state.has(ITEM_EGGS, player)
                    )
                ) and
                state.has(ITEM_SEASON_FALL, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_JIGGY_CCW_PLANT:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player) and
                state.has(ITEM_SEASON_SUMMER, player) and
                state.has(ITEM_SEASON_FALL, player) and
                state.has(ITEM_EGGS, player) and
                state.has(ITEM_BEAK_BUSTER, player) and         #needs all Gobi events prior done
                (
                    can_reach_ccw_beehive(state, player, ITEM_SEASON_SPRING) or
                    can_reach_ccw_beehive(state, player, ITEM_SEASON_SUMMER)
                )
            ),
        LOC_JIGGY_CCW_NABNUTS:
            lambda state:
            (
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL) and
                state.has(ITEM_ACORN, player, 6)
            ),
        LOC_JIGGY_CCW_EYRIE:
            lambda state:
            (
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SPRING) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER) and
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
        LOC_JINJO_CCW_BLUE:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_JINJO_CCW_GREEN:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player) and
                (
                    (
                        state.has(ITEM_TRANSFORMATION_BEE, player) and
                        (
                            state.has(ITEM_TALON_TROT, player) or       #required to access Mumbo's Skull
                            state.has(ITEM_STILT_STRIDE, player)
                        )
                    ) or
                    (
                        can_reach_ccw_cabin(state, player, ITEM_SEASON_SPRING) and
                        state.has(ITEM_FLAP_FLIP, player) and
                        state.has(ITEM_WONDERWING, player)
                    )
                )
            ),
        LOC_JINJO_CCW_ORANGE:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_JINJO_CCW_PURPLE:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player) and
                state.has(ITEM_TRANSFORMATION_BEE, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or       #required to access Mumbo's Skull
                    state.has(ITEM_STILT_STRIDE, player)
                )
            ),
        LOC_JINJO_CCW_YELLOW:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player)
            ),
        LOC_EMPTY_HONEYCOMB_CCW_WINTER_NABNUTS:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    state.has(ITEM_BEAK_BOMB, player)
                )
            ),
        LOC_EMPTY_HONEYCOMB_CCW_WINTER_GNAWTY:
            lambda state:
            (
                (
                    state.has(ITEM_SEASON_SUMMER, player) and
                    (
                        state.has(ITEM_BEAK_BARGE, player) or           #required to break the boulder
                        state.has(ITEM_BEAK_BUSTER, player) or
                        state.has(ITEM_EGGS, player)
                    )
                ) and
                state.has(ITEM_SEASON_WINTER, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_ENTRANCE_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player) and
                (
                    (
                        state.has(ITEM_TRANSFORMATION_BEE, player) and
                        (
                            state.has(ITEM_TALON_TROT, player) or       #required to access Mumbo's Skull
                            state.has(ITEM_STILT_STRIDE, player)
                        )
                    ) or
                    (
                        state.has(ITEM_WONDERWING, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_GARDEN_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player) and
                (
                    (
                        state.has(ITEM_TRANSFORMATION_BEE, player) and
                        (
                            state.has(ITEM_TALON_TROT, player) or       #required to access Mumbo's Skull
                            state.has(ITEM_STILT_STRIDE, player)
                        )
                    ) or
                    (
                        state.has(ITEM_WONDERWING, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_TREETOP_ABOVE_MUMBOS_HUT:
            lambda state:
            (
                can_reach_ccw_beehive(state, player, ITEM_SEASON_SPRING)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_BEEHIVE:
            lambda state:
            (
                can_reach_ccw_beehive(state, player, ITEM_SEASON_SPRING)
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_CABIN:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player) and
                (
                    (
                        state.has(ITEM_TRANSFORMATION_BEE, player) and
                        (
                            state.has(ITEM_TALON_TROT, player) or       #required to access Mumbo's Skull
                            state.has(ITEM_STILT_STRIDE, player)
                        )
                    ) or
                    (
                        can_reach_ccw_cabin(state, player, ITEM_SEASON_SPRING)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_NABNUTS_DRESSER:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player) and
                (
                    (
                        state.has(ITEM_TRANSFORMATION_BEE, player) and
                        (
                            state.has(ITEM_TALON_TROT, player) or       #required to access Mumbo's Skull
                            state.has(ITEM_STILT_STRIDE, player)
                        )
                    ) or
                    (
                        can_reach_ccw_cabin(state, player, ITEM_SEASON_SPRING)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_NEAR_EYRIES_NEST:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player) and
                (
                    (
                        state.has(ITEM_TRANSFORMATION_BEE, player) and
                        (
                            state.has(ITEM_TALON_TROT, player) or       #required to access Mumbo's Skull
                            state.has(ITEM_STILT_STRIDE, player)
                        )
                    ) or
                    (
                        can_reach_ccw_cabin(state, player, ITEM_SEASON_SPRING)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SPRING_THORNS:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player) and
                (
                    state.has(ITEM_STILT_STRIDE, player) or
                    (
                        state.has(ITEM_TRANSFORMATION_BEE, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_ENTRANCE_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_GNAWTY:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                (
                    state.has(ITEM_BEAK_BARGE, player) or           #required to break the boulder
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_GARDEN:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player)
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_MUMBOS_HUT:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
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
                can_reach_ccw_beehive(state, player, ITEM_SEASON_SUMMER)
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_LEAVES:
            lambda state:
            (
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER)
            ),
        LOC_MUMBO_TOKEN_CCW_SUMMER_AFTER_NABNUTS_HOUSE:
            lambda state:
            (
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER)
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_ENTRANCE_SNAREBEAR:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_TREETOP_ABOVE_MUMBOS_HUT:
            lambda state:
            (
                can_reach_ccw_beehive(state, player, ITEM_SEASON_FALL)
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_LEAVES:
            lambda state:
            (
                can_reach_ccw_beehive(state, player, ITEM_SEASON_FALL)
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_CABIN:
            lambda state:
            (
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL)
            ),
        LOC_MUMBO_TOKEN_CCW_FALL_TREETOP_SNAREBEAR:
            lambda state:
            (
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL) and
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_GARDEN:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player)
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_SIR_SLUSH:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                state.has(ITEM_FLIGHT, player) and
                state.has(ITEM_BEAK_BOMB, player)
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_BEEHIVE:
            lambda state:
            (
                can_reach_ccw_beehive(state, player, ITEM_SEASON_WINTER)
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_NEAR_NABNUTS_HOUSE:
            lambda state:
            (
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER)
            ),
        LOC_MUMBO_TOKEN_CCW_WINTER_BEHIND_LAKE_PLATFORM:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player)
            ),
        LOC_NOTE_CCW_SPRING_ENTRANCE_1:
            lambda state: True,
        LOC_NOTE_CCW_SPRING_ENTRANCE_2:
            lambda state: True,
        LOC_NOTE_CCW_SPRING_ENTRANCE_3:
            lambda state: True,
        LOC_NOTE_CCW_SPRING_ENTRANCE_4:
            lambda state: True,
        LOC_NOTE_CCW_SPRING_GARDEN_1:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_GARDEN_2:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_GARDEN_3:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_GARDEN_4:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_GOBI_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_GOBI_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_GOBI_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_FLOODED_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_FLOODED_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_FLOODED_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_HIGH_MUMBO_WALL_1:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_HIGH_MUMBO_WALL_2:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_HIGH_MUMBO_WALL_3:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_LOW_MUMBO_WALL_1:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_LOW_MUMBO_WALL_2:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SPRING_LOW_MUMBO_WALL_3:
            lambda state:
            (
                state.has(ITEM_SEASON_SPRING, player)
            ),
        LOC_NOTE_CCW_SUMMER_ENTRY_LEAVES_1:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player)
            ),
        LOC_NOTE_CCW_SUMMER_ENTRY_LEAVES_2:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player)
            ),
        LOC_NOTE_CCW_SUMMER_GNAWTY_ENTRYWAY_1:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                (
                    state.has(ITEM_BEAK_BARGE, player) or           #required to break the boulder
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_CCW_SUMMER_GNAWTY_ENTRYWAY_2:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                (
                    state.has(ITEM_BEAK_BARGE, player) or           #required to break the boulder
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_EGGS, player)
                )
            ),
        LOC_NOTE_CCW_SUMMER_ZUBBA_BRIDGE_1:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                can_reach_ccw_beehive(state, player, ITEM_SEASON_SUMMER)
            ),
        LOC_NOTE_CCW_SUMMER_ZUBBA_BRIDGE_2:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                can_reach_ccw_beehive(state, player, ITEM_SEASON_SUMMER)
            ),
        LOC_NOTE_CCW_SUMMER_ZUBBA_BRIDGE_3:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                can_reach_ccw_beehive(state, player, ITEM_SEASON_SUMMER)
            ),
        LOC_NOTE_CCW_SUMMER_TREEHOUSE_1:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER)
            ),
        LOC_NOTE_CCW_SUMMER_TREEHOUSE_2:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER)
            ),
        LOC_NOTE_CCW_SUMMER_TREEHOUSE_3:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER)
            ),
        LOC_NOTE_CCW_SUMMER_TREEHOUSE_4:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER)
            ),
        LOC_NOTE_CCW_SUMMER_NABNUTS_PLATFORM_1:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SUMMER_NABNUTS_PLATFORM_2:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SUMMER_NABNUTS_PLATFORM_3:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SUMMER_NABNUTS_PLATFORM_4:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_SUMMER_NABNUTS_PLATFORM_5:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_SUMMER) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_AUTUMN_MUMBO_SNAREBEAR_1:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CCW_AUTUMN_MUMBO_SNAREBEAR_2:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CCW_AUTUMN_MUMBO_SNAREBEAR_3:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_1:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_2:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_3:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_4:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_5:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_6:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_7:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_8:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_9:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_10:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_11:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_12:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_13:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_14:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_15:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_LOWER_TREE_PATH_16:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_MUMBOS_SKULL_1:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CCW_AUTUMN_MUMBOS_SKULL_2:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CCW_AUTUMN_MUMBOS_SKULL_3:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CCW_AUTUMN_MUMBOS_SKULL_4:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                (
                    state.has(ITEM_TALON_TROT, player) or
                    state.has(ITEM_STILT_STRIDE, player)
                ) and
                (
                    state.has(ITEM_JUMP, player) or
                    state.has(ITEM_FLAP_FLIP, player)
                )
            ),
        LOC_NOTE_CCW_AUTUMN_GOBIS_GARDEN_1:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_GOBIS_GARDEN_2:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_GOBIS_GARDEN_3:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_GOBIS_GARDEN_4:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_GOBIS_GARDEN_5:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player)
            ),
        LOC_NOTE_CCW_AUTUMN_GOBI_SNAREBEAR_1:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CCW_AUTUMN_GOBI_SNAREBEAR_2:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CCW_AUTUMN_GOBI_SNAREBEAR_3:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                state.has(ITEM_WONDERWING, player)
            ),
        LOC_NOTE_CCW_AUTUMN_GNAWTYS_SHELF_1:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                (
                    state.has(ITEM_BEAK_BARGE, player) or           #required to break the boulder
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_SEASON_FALL, player) and
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
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
        LOC_NOTE_CCW_AUTUMN_GNAWTYS_SHELF_2:
            lambda state:
            (
                state.has(ITEM_SEASON_SUMMER, player) and
                (
                    state.has(ITEM_BEAK_BARGE, player) or           #required to break the boulder
                    state.has(ITEM_BEAK_BUSTER, player) or
                    state.has(ITEM_EGGS, player)
                ) and
                state.has(ITEM_SEASON_FALL, player) and
                state.has(ITEM_SWIM, player) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
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
        LOC_NOTE_CCW_AUTUMN_ZUBBAS_HIVE_1:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_beehive(state, player, ITEM_SEASON_FALL) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_CCW_AUTUMN_ZUBBAS_HIVE_2:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_beehive(state, player, ITEM_SEASON_FALL) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_CCW_AUTUMN_ZUBBAS_HIVE_3:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_beehive(state, player, ITEM_SEASON_FALL) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_CCW_AUTUMN_ZUBBAS_HIVE_4:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_beehive(state, player, ITEM_SEASON_FALL) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_NOTE_CCW_AUTUMN_NABNUTSS_SHELF_1:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_CCW_AUTUMN_NABNUTSS_SHELF_2:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_CCW_AUTUMN_NABNUTSS_SHELF_3:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL) and
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_1:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_2:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_3:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_4:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_5:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_6:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_7:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL)
            ),
        LOC_NOTE_CCW_AUTUMN_EYRIES_NEST_8:
            lambda state:
            (
                state.has(ITEM_SEASON_FALL, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_FALL)
            ),
        LOC_NOTE_CCW_WINTER_SLUSH_BRANCHES_1:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_beehive(state, player, ITEM_SEASON_WINTER)
            ),
        LOC_NOTE_CCW_WINTER_SLUSH_BRANCHES_2:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_beehive(state, player, ITEM_SEASON_WINTER)
            ),
        LOC_NOTE_CCW_WINTER_SLUSH_BRANCHES_3:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_beehive(state, player, ITEM_SEASON_WINTER)
            ),
        LOC_NOTE_CCW_WINTER_SLUSH_BRANCHES_4:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_beehive(state, player, ITEM_SEASON_WINTER)
            ),
        LOC_NOTE_CCW_WINTER_TREEHOUSE_ROOF_1:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER) and #you can TECHNICALLY do this with just flight but...
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_WINTER_TREEHOUSE_ROOF_2:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER) and #you can TECHNICALLY do this with just flight but...
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_WINTER_TREEHOUSE_ROOF_3:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER) and #you can TECHNICALLY do this with just flight but...
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_WINTER_TREEHOUSE_ROOF_4:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER) and #you can TECHNICALLY do this with just flight but...
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_TALON_TROT, player)
            ),
        LOC_NOTE_CCW_WINTER_SLUSH_PLATFORM_1:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER)
            ),
        LOC_NOTE_CCW_WINTER_SLUSH_PLATFORM_2:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER)
            ),
        LOC_NOTE_CCW_WINTER_SLUSH_PLATFORM_3:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER)
            ),
        LOC_NOTE_CCW_WINTER_SLUSH_PLATFORM_4:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER)
            ),
        LOC_NOTE_CCW_WINTER_HIGHEST_PLATFORMS_1:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_CCW_WINTER_HIGHEST_PLATFORMS_2:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_CCW_WINTER_HIGHEST_PLATFORMS_3:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_NOTE_CCW_WINTER_HIGHEST_PLATFORMS_4:
            lambda state:
            (
                state.has(ITEM_SEASON_WINTER, player) and
                can_reach_ccw_cabin(state, player, ITEM_SEASON_WINTER) and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        # Egg and Feather Rules

        LOC_BEGG_MM_BEHIND_STONEHENGE_PILLAR_1:
            lambda state: True,
        LOC_BEGG_MM_BEHIND_STONEHENGE_PILLAR_2:
            lambda state: True,
        LOC_BEGG_MM_BEHIND_STONEHENGE_PILLAR_3:
            lambda state: True,
        LOC_BEGG_MM_BEHIND_STONEHENGE_PILLAR_4:
            lambda state: True,
        LOC_BEGG_MM_BEHIND_STONEHENGE_PILLAR_5:
            lambda state: True,
        LOC_BEGG_MM_INSIDE_DESTROYED_HUT_1:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
                and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_JUMP, player)
                )
            ),
        LOC_BEGG_MM_INSIDE_DESTROYED_HUT_2:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
                and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_JUMP, player)
                )
            ),
        LOC_BEGG_MM_INSIDE_DESTROYED_HUT_3:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
                and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_JUMP, player)
                )
            ),
        LOC_BEGG_MM_INSIDE_DESTROYED_HUT_4:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
                and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_JUMP, player)
                )
            ),
        LOC_BEGG_MM_INSIDE_DESTROYED_HUT_5:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
                and
                (
                    state.has(ITEM_FLAP_FLIP, player) or
                    state.has(ITEM_JUMP, player)
                )
            ),
        LOC_BEGG_MM_CHIMPY_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_CHIMPY_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_CHIMPY_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_CHIMPY_4:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_CHIMPY_5:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_CHIMPY_6:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_CHIMPY_7:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_CHIMPY_8:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_INSIDE_MUMBOS_1:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_INSIDE_MUMBOS_2:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_INSIDE_MUMBOS_3:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_INSIDE_MUMBOS_4:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_INSIDE_MUMBOS_5:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_INSIDE_MUMBOS_6:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_INSIDE_MUMBOS_7:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_INSIDE_MUMBOS_8:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_INSIDE_MUMBOS_9:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_INSIDE_MUMBOS_10:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_INSIDE_MUMBOS_11:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_INSIDE_MUMBOS_12:
            lambda state:
            (
                state.has(ITEM_JUMP, player) or
                state.has(ITEM_FLAP_FLIP, player)
            ),
        LOC_BEGG_MM_TERMITE_MOUND_1:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_BEGG_MM_TERMITE_MOUND_2:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_BEGG_MM_TERMITE_MOUND_3:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_BEGG_MM_TERMITE_MOUND_4:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_BEGG_MM_TERMITE_MOUND_5:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_BEGG_MM_TERMITE_MOUND_6:
            lambda state:
            (
                state.has(ITEM_TRANSFORMATION_TERMITE, player)
            ),
        LOC_BEGG_GL_AROUND_RED_CAULDRON_1:
            lambda state: True,
        LOC_BEGG_GL_AROUND_RED_CAULDRON_2:
            lambda state: True,
        LOC_BEGG_GL_AROUND_RED_CAULDRON_3:
            lambda state: True,
        LOC_BEGG_GL_AROUND_RED_CAULDRON_4:
            lambda state: True,
        LOC_BEGG_GL_AROUND_RED_CAULDRON_5:
            lambda state: True,
        LOC_BEGG_GL_AROUND_RED_CAULDRON_6:
            lambda state: True,
        LOC_BEGG_GL_AROUND_RED_CAULDRON_7:
            lambda state: True,
        LOC_BEGG_GL_AROUND_RED_CAULDRON_8:
            lambda state: True,
        LOC_BEGG_GL_NEAR_CCW_SWITCH_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_GL_NEAR_CCW_SWITCH_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_GL_NEAR_CCW_SWITCH_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_GL_NEAR_CCW_SWITCH_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_GL_NEAR_CCW_SWITCH_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_GL_NEAR_CCW_SWITCH_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_GL_NEAR_CCW_SWITCH_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_GL_AROUND_BGS_PAINTING_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_GL_AROUND_BGS_PAINTING_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_GL_AROUND_BGS_PAINTING_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_GL_AROUND_BGS_PAINTING_4:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_GL_AROUND_BGS_PAINTING_5:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_GL_AROUND_BGS_PAINTING_6:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_GL_AROUND_BGS_PAINTING_7:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_GL_AROUND_BGS_PAINTING_8:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_SWIM, player) and
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_GL_AROUND_FP_PAINTING_1:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_BEGG_GL_AROUND_FP_PAINTING_2:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_BEGG_GL_AROUND_FP_PAINTING_3:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_BEGG_GL_AROUND_FP_PAINTING_4:
            lambda state:
            (
                state.has(ITEM_STILT_STRIDE, player)
            ),
        LOC_BEGG_TTC_INSIDE_NIPPER_1:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_BEGG_TTC_INSIDE_NIPPER_2:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_BEGG_TTC_INSIDE_NIPPER_3:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_BEGG_TTC_INSIDE_NIPPER_4:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_BEGG_TTC_INSIDE_NIPPER_5:
            lambda state:
            (
                state.has(ITEM_RAT_A_TAT_RAP, player)
            ),
        LOC_BEGG_TTC_PATH_TO_LIGHT_1:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_BEGG_TTC_PATH_TO_LIGHT_2:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_BEGG_TTC_PATH_TO_LIGHT_3:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_BEGG_TTC_PATH_TO_LIGHT_4:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_BEGG_TTC_PATH_TO_LIGHT_5:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_BEGG_TTC_PATH_TO_LIGHT_6:
            lambda state:
            (
                can_reach_ttc_flight_pad(state, player) and
                state.has(ITEM_FLIGHT, player)
            ),
        LOC_BEGG_TTC_TREE_STAIRS_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_BEGG_TTC_TREE_STAIRS_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_BEGG_TTC_TREE_STAIRS_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_BEGG_TTC_TREE_STAIRS_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_BEGG_TTC_TREE_OVERLOOKING_BLUBBER_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_BEGG_TTC_TREE_OVERLOOKING_BLUBBER_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_BEGG_TTC_TREE_OVERLOOKING_BLUBBER_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_BEGG_TTC_TREE_OVERLOOKING_BLUBBER_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_BEGG_TTC_TREE_OVERLOOKING_POOLS_1:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_BEGG_TTC_TREE_OVERLOOKING_POOLS_2:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_BEGG_TTC_TREE_OVERLOOKING_POOLS_3:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_BEGG_TTC_TREE_OVERLOOKING_POOLS_4:
            lambda state:
            (
                state.has(ITEM_FLIGHT, player) and
                (
                    state.has(ITEM_CLIMB, player) or
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_BEGG_CC_RIGHT_CUBBY_PIPE_1:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            (
                                    state.has(ITEM_JUMP, player) and
                                    state.has(ITEM_TALON_TROT, player)
                            )
                    )
            ),
        LOC_BEGG_CC_RIGHT_CUBBY_PIPE_2:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            (
                                    state.has(ITEM_JUMP, player) and
                                    state.has(ITEM_TALON_TROT, player)
                            )
                    )
            ),
        LOC_BEGG_CC_RIGHT_BELOW_CUBBY_PIPE_1:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    (
                            state.has(ITEM_JUMP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
            ),
        LOC_BEGG_CC_RIGHT_BELOW_CUBBY_PIPE_2:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    (
                            state.has(ITEM_JUMP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
            ),
        LOC_BEGG_CC_RIGHT_BELOW_CUBBY_PIPE_3:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    (
                            state.has(ITEM_JUMP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
            ),
        LOC_BEGG_CC_RIGHT_BELOW_CUBBY_PIPE_4:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    (
                            state.has(ITEM_JUMP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
            ),
        LOC_BEGG_CC_RIGHT_BELOW_CUBBY_PIPE_5:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    (
                            state.has(ITEM_JUMP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
            ),
        LOC_BEGG_CC_RIGHT_BELOW_CUBBY_PIPE_6:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    (
                            state.has(ITEM_JUMP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
            ),
        LOC_BEGG_CC_RIGHT_BELOW_CUBBY_PIPE_7:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    (
                            state.has(ITEM_JUMP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
            ),
        LOC_BEGG_CC_RIGHT_BELOW_CUBBY_PIPE_8:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    (
                            state.has(ITEM_JUMP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
            ),
        LOC_BEGG_CC_RIGHT_BELOW_CUBBY_PIPE_9:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    (
                            state.has(ITEM_JUMP, player) or
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
            ),
        LOC_BEGG_CC_INSIDE_BREAKABLE_GRATE_1:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            (
                                    state.has(ITEM_JUMP, player) and
                                    state.has(ITEM_TALON_TROT, player)
                            )
                    ) and
                    state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_CC_INSIDE_BREAKABLE_GRATE_2:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            (
                                    state.has(ITEM_JUMP, player) and
                                    state.has(ITEM_TALON_TROT, player)
                            )
                    ) and
                    state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_CC_INSIDE_BREAKABLE_GRATE_3:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            (
                                    state.has(ITEM_JUMP, player) and
                                    state.has(ITEM_TALON_TROT, player)
                            )
                    ) and
                    state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_CC_INSIDE_BREAKABLE_GRATE_4:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            (
                                    state.has(ITEM_JUMP, player) and
                                    state.has(ITEM_TALON_TROT, player)
                            )
                    ) and
                    state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_CC_INSIDE_BREAKABLE_GRATE_5:
            lambda state:
            (
                    state.has(ITEM_SWIM, player) and
                    state.has(ITEM_CLIMB, player) and
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                            state.has(ITEM_FEATHERY_FLAP, player) or
                            state.has(ITEM_RAT_A_TAT_RAP, player) or
                            (
                                    state.has(ITEM_JUMP, player) and
                                    state.has(ITEM_TALON_TROT, player)
                            )
                    ) and
                    state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_BEGG_CC_INSIDE_CLANKERS_STOMACH_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_CC_INSIDE_CLANKERS_STOMACH_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_CC_INSIDE_CLANKERS_STOMACH_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_CC_INSIDE_CLANKERS_STOMACH_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_CC_INSIDE_CLANKERS_STOMACH_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_CC_INSIDE_CLANKERS_STOMACH_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_CC_INSIDE_CLANKERS_STOMACH_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_BEGG_CC_INSIDE_CLANKERS_STOMACH_8:
            lambda state:
            (
                state.has(ITEM_SWIM, player)
            ),
        LOC_REDF_GL_OUTSIDE_CC_1:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_REDF_GL_OUTSIDE_CC_2:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_REDF_GL_OUTSIDE_CC_3:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_REDF_GL_OUTSIDE_CC_4:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) and
                state.has(ITEM_BEAK_BUSTER, player) and
                (
                    state.has(ITEM_FEATHERY_FLAP, player) or
                    state.has(ITEM_RAT_A_TAT_RAP, player) or
                    (
                        state.has(ITEM_JUMP, player) and
                        state.has(ITEM_TALON_TROT, player)
                    )
                )
            ),
        LOC_REDF_GL_AROUND_GRUNTY_STATUE_1:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_REDF_GL_AROUND_GRUNTY_STATUE_2:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_REDF_GL_AROUND_GRUNTY_STATUE_3:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_REDF_GL_AROUND_GRUNTY_STATUE_4:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_REDF_GL_AROUND_GRUNTY_STATUE_5:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_REDF_GL_AROUND_GRUNTY_STATUE_6:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_REDF_GL_AROUND_GRUNTY_STATUE_7:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_REDF_GL_AROUND_GRUNTY_STATUE_8:
            lambda state:
            (
                state.has(ITEM_SWIM, player) or
                state.has(ITEM_BEAK_BUSTER, player)
            ),
        LOC_REDF_TTC_SHIP_MAST_1:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_REDF_TTC_SHIP_MAST_2:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_REDF_TTC_SHIP_MAST_3:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_REDF_TTC_SHIP_MAST_4:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_REDF_TTC_SHIP_MAST_5:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_REDF_TTC_SHIP_MAST_7:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_REDF_TTC_SHIP_MAST_8:
            lambda state:
            (
                state.has(ITEM_TALON_TROT, player) or
                (
                    can_reach_ttc_flight_pad(state, player) and
                    state.has(ITEM_FLIGHT, player)
                )
            ),
        LOC_REDF_TTC_ROCK_POOL_1:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_REDF_TTC_ROCK_POOL_2:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_REDF_TTC_ROCK_POOL_3:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_REDF_TTC_ROCK_POOL_4:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_REDF_TTC_ROCK_POOL_5:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_REDF_TTC_ROCK_POOL_6:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_REDF_TTC_ROCK_POOL_7:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player) and
                state.has(ITEM_SWIM, player)
            ),
        LOC_REDF_TTC_ROCK_POOL_8:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player) and
                state.has(ITEM_SWIM, player)
            ),
    LOC_REDF_TTC_ROCK_POOL_9:
            lambda state:
            (
                can_reach_ttc_upper_ledge(state, player) and
                state.has(ITEM_SWIM, player)
            ),
    LOC_REDF_TTC_ROCK_POOL_ISLAND_FLIGHT_1:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player)
    ),
    LOC_REDF_TTC_ROCK_POOL_ISLAND_FLIGHT_2:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player)
    ),
    LOC_REDF_TTC_ROCK_POOL_ISLAND_FLIGHT_3:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player) and
        (
            state.has(ITEM_FLAP_FLIP, player) or
            state.has(ITEM_FLIGHT, player)
        )
    ),
    LOC_REDF_TTC_ROCK_POOL_ISLAND_FLIGHT_4:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player) and
        (
            state.has(ITEM_FLAP_FLIP, player) or
            state.has(ITEM_FLIGHT, player)
        )
    ),
    LOC_REDF_TTC_WORLD_ENTRY_FLIGHT_1:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player)
    ),
    LOC_REDF_TTC_WORLD_ENTRY_FLIGHT_2:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player)
    ),
    LOC_REDF_TTC_WORLD_ENTRY_FLIGHT_3:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player) and
        (
            state.has(ITEM_FLAP_FLIP, player) or
            state.has(ITEM_FLIGHT, player)
        )
    ),
    LOC_REDF_TTC_WORLD_ENTRY_FLIGHT_4:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player) and
        (
            state.has(ITEM_FLAP_FLIP, player) or
            state.has(ITEM_FLIGHT, player)
        )
    ),
    LOC_REDF_TTC_SANDCASTLE_FLIGHT_1:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_FLIGHT_2:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_FLIGHT_3:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player) and
        (
            state.has(ITEM_FLAP_FLIP, player) or
            state.has(ITEM_FLIGHT, player)
        )
    ),
    LOC_REDF_TTC_SANDCASTLE_FLIGHT_4:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player) and
        (
            state.has(ITEM_FLAP_FLIP, player) or
            state.has(ITEM_FLIGHT, player)
        )
    ),
    LOC_REDF_TTC_NIPPER_TREE_1:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_NIPPER_TREE_2:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_NIPPER_TREE_3:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_NIPPER_TREE_4:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_NIPPER_TREE_5:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_NIPPER_TREE_6:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_NIPPER_TREE_7:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_NIPPER_TREE_8:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_ENTRY_TREE_1:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_ENTRY_TREE_2:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_ENTRY_TREE_3:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_ENTRY_TREE_4:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_ENTRY_TREE_5:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_ENTRY_TREE_6:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_ENTRY_TREE_7:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_ENTRY_TREE_8:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_TREE_1:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_TREE_2:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_TREE_3:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_TREE_4:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_TREE_5:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_TREE_6:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_TREE_7:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_TREE_8:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_TREE_9:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_TREE_10:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_TREE_11:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SANDCASTLE_TREE_12:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRING_BEACH_TREE_1:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRING_BEACH_TREE_2:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRING_BEACH_TREE_3:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRING_BEACH_TREE_4:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRING_BEACH_TREE_5:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRING_BEACH_TREE_6:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRING_BEACH_TREE_7:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRING_BEACH_TREE_8:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRING_BEACH_TREE_9:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRING_BEACH_TREE_10:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRING_BEACH_TREE_11:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRING_BEACH_TREE_12:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_PATH_TO_X_BEACH_TREE_1:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_PATH_TO_X_BEACH_TREE_2:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_PATH_TO_X_BEACH_TREE_3:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_PATH_TO_X_BEACH_TREE_4:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_PATH_TO_X_BEACH_TREE_5:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_PATH_TO_X_BEACH_TREE_6:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_PATH_TO_X_BEACH_TREE_7:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_PATH_TO_X_BEACH_TREE_8:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_PATH_TO_X_BEACH_TREE_9:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_PATH_TO_X_BEACH_TREE_10:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_PATH_TO_X_BEACH_TREE_11:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_PATH_TO_X_BEACH_TREE_12:
    lambda state:
    (
        state.has(ITEM_CLIMB, player)
    ),
    LOC_REDF_TTC_SHOCK_SPRINGS_1:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player) and
        (
            state.has(ITEM_FLIGHT, player) or
            state.has(ITEM_SHOCK_SPRING_JUMP, player)
        )
    ),
    LOC_REDF_TTC_SHOCK_SPRINGS_2:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player) and
        (
            state.has(ITEM_FLIGHT, player) or
            state.has(ITEM_SHOCK_SPRING_JUMP, player)
        )
    ),
    LOC_REDF_TTC_SHOCK_SPRINGS_3:
    lambda state:
    (
        can_reach_ttc_middle_ledge(state, player) and
        (
            state.has(ITEM_FLIGHT, player) or
            state.has(ITEM_SHOCK_SPRING_JUMP, player)
        )
    ),
    LOC_REDF_TTC_BEACH_CHEST_1:
    lambda state:
    (
        state.has(ITEM_FLAP_FLIP, player)
    ),
    LOC_REDF_TTC_BEACH_CHEST_2:
    lambda state:
    (
        state.has(ITEM_FLAP_FLIP, player)
    ),
    LOC_REDF_TTC_BEACH_CHEST_3:
    lambda state:
    (
        state.has(ITEM_FLAP_FLIP, player)
    ),
    LOC_REDF_TTC_BEACH_CHEST_4:
    lambda state:
    (
        state.has(ITEM_FLAP_FLIP, player)
    ),
    LOC_REDF_TTC_BEACH_CHEST_5:
    lambda state:
    (
        state.has(ITEM_FLAP_FLIP, player)
    ),
    LOC_REDF_TTC_BEACH_CHEST_6:
    lambda state:
    (
        state.has(ITEM_FLAP_FLIP, player)
    ),
    LOC_REDF_TTC_BEACH_CHEST_7:
    lambda state:
    (
        state.has(ITEM_FLAP_FLIP, player)
    ),
    LOC_REDF_TTC_BEACH_CHEST_8:
    lambda state:
    (
        state.has(ITEM_FLAP_FLIP, player)
    ),
    LOC_REDF_TTC_MAP_PATH_1:
    lambda state:
    (
        state.has(ITEM_FEATHERY_FLAP, player) or
        state.has(ITEM_RAT_A_TAT_RAP, player) or
        (
            state.has(ITEM_JUMP, player) and
            state.has(ITEM_TALON_TROT, player)
        )
    ),
    LOC_REDF_TTC_MAP_PATH_2:
    lambda state:
    (
        state.has(ITEM_FEATHERY_FLAP, player) or
        state.has(ITEM_RAT_A_TAT_RAP, player) or
        (
            state.has(ITEM_JUMP, player) and
            state.has(ITEM_TALON_TROT, player)
        )
    ),
    LOC_REDF_TTC_MAP_PATH_3:
    lambda state:
    (
        state.has(ITEM_FEATHERY_FLAP, player) or
        state.has(ITEM_RAT_A_TAT_RAP, player) or
        (
            state.has(ITEM_JUMP, player) and
            state.has(ITEM_TALON_TROT, player)
        ) and
        (
            state.has(ITEM_FLAP_FLIP, player) or
            state.has(ITEM_FLIGHT, player)
        )
    ),
    LOC_REDF_TTC_MAP_PATH_4:
    lambda state:
    (
        state.has(ITEM_FEATHERY_FLAP, player) or
        state.has(ITEM_RAT_A_TAT_RAP, player) or
        (
            state.has(ITEM_JUMP, player) and
            state.has(ITEM_TALON_TROT, player)
        ) and
        (
            state.has(ITEM_FLAP_FLIP, player) or
            state.has(ITEM_FLIGHT, player)
        )
    ),
    LOC_REDF_CC_CLANKER_TAIL_1:
    lambda state:
    (
        state.has(ITEM_SWIM, player)
    ),
    LOC_REDF_CC_CLANKER_TAIL_2:
    lambda state:
    (
        state.has(ITEM_SWIM, player)
    ),
    LOC_REDF_CC_CLANKER_TAIL_3:
    lambda state:
    (
        state.has(ITEM_SWIM, player)
    ),
    LOC_REDF_CC_CLANKER_TAIL_4:
    lambda state:
    (
        state.has(ITEM_SWIM, player)
    ),
    LOC_REDF_CC_CLANKER_TAIL_5:
    lambda state:
    (
        state.has(ITEM_SWIM, player)
    ),
    LOC_REDF_CC_CLANKER_TAIL_6:
    lambda state:
    (
        state.has(ITEM_SWIM, player)
    ),
    LOC_REDF_CC_INSIDE_CLANKERS_STOMACH_1:
    lambda state:
    (
        state.has(ITEM_SWIM, player)
    ),
    LOC_REDF_CC_INSIDE_CLANKERS_STOMACH_2:
    lambda state:
    (
        state.has(ITEM_SWIM, player)
    ),
    LOC_REDF_CC_INSIDE_CLANKERS_STOMACH_3:
    lambda state:
    (
        state.has(ITEM_SWIM, player)
    ),
    LOC_REDF_CC_INSIDE_CLANKERS_STOMACH_4:
    lambda state:
    (
        state.has(ITEM_SWIM, player)
    ),
    LOC_REDF_MMM_ROOFTOP_FEATHER_1:
    lambda state:
    (
        state.has(ITEM_CLIMB, player) and
        state.has(ITEM_SHOCK_SPRING_JUMP, player)
    ),
    LOC_REDF_MMM_ROOFTOP_FEATHER_2:
    lambda state:
    (
        state.has(ITEM_CLIMB, player) and
        state.has(ITEM_SHOCK_SPRING_JUMP, player)
    ),
    LOC_REDF_MMM_ROOFTOP_FEATHER_3:
    lambda state:
    (
        state.has(ITEM_CLIMB, player) and
        state.has(ITEM_SHOCK_SPRING_JUMP, player)
    ),
    LOC_REDF_MMM_ROOFTOP_FEATHER_4:
    lambda state:
    (
        state.has(ITEM_CLIMB, player) and
        state.has(ITEM_SHOCK_SPRING_JUMP, player)
    ),
    LOC_GOLDF_GL_UNDER_BGS_BRIDGES:
    lambda state:
    (
        can_traverse_bgs(state, player) and
        state.has(ITEM_STILT_STRIDE, player) and
        state.has(ITEM_TRANSFORMATION_CROCODILE, player)
    ),
    LOC_GOLDF_GL_SWAMP_CHEATO:
    lambda state:
    (
        can_traverse_bgs(state, player) and
        state.has(ITEM_STILT_STRIDE, player) and
        state.has(ITEM_TRANSFORMATION_CROCODILE, player) and
        (
            state.has(ITEM_BEAK_BARGE, player) or
            state.has(ITEM_RAT_A_TAT_RAP, player) or
            state.has(ITEM_BEAK_BUSTER, player) or
            state.has(ITEM_EGGS, player)
        )
    ),
    LOC_GOLDF_CC_PLATFORM_NEAR_CLANKER_1:
    lambda state:
    (
            state.has(ITEM_SWIM, player) and
            (
                state.has(ITEM_JUMP, player) or
                (
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
                )
            )
    ),
    LOC_GOLDF_CC_PLATFORM_NEAR_CLANKER_2:
    lambda state:
    (
            state.has(ITEM_SWIM, player) and
            (
                state.has(ITEM_JUMP, player) or
                (
                    state.has(ITEM_SHOCK_SPRING_JUMP, player) and
                    (
                        state.has(ITEM_FEATHERY_FLAP, player) or
                        state.has(ITEM_RAT_A_TAT_RAP, player)
                    )
                )
            )
    ),
    LOC_GOLDF_CC_CRATES_INSIDE_CLANKER_1:
    lambda state:
    (
        state.has(ITEM_SWIM, player) and  # required to access most of the level
        state.has(ITEM_FLAP_FLIP, player) and  # required to jump through all the rings
        (
            state.has(ITEM_FEATHERY_FLAP, player) or
            state.has(ITEM_RAT_A_TAT_RAP, player) or
            (
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_TALON_TROT, player)
            )
        )
    ),
    LOC_GOLDF_CC_CRATES_INSIDE_CLANKER_2:
    lambda state:
    (
        state.has(ITEM_SWIM, player) and  # required to access most of the level
        state.has(ITEM_FLAP_FLIP, player) and  # required to jump through all the rings
        (
            state.has(ITEM_FEATHERY_FLAP, player) or
            state.has(ITEM_RAT_A_TAT_RAP, player) or
            (
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_TALON_TROT, player)
            )
        )
    ),
    LOC_GOLDF_CC_CRATES_INSIDE_CLANKER_3:
    lambda state:
    (
        state.has(ITEM_SWIM, player) and  # required to access most of the level
        state.has(ITEM_FLAP_FLIP, player) and  # required to jump through all the rings
        (
            state.has(ITEM_FEATHERY_FLAP, player) or
            state.has(ITEM_RAT_A_TAT_RAP, player) or
            (
                state.has(ITEM_JUMP, player) and
                state.has(ITEM_TALON_TROT, player)
            )
        )
    ),
    LOC_GOLDF_CC_FLIGHT_PAD_LEDGE:
    lambda state:
    (
            state.has(ITEM_SWIM, player) and
            state.has(ITEM_FLIGHT, player)
    ),
    LOC_GOLDF_CC_SAWBLADES_1:
    lambda state:
    (
            state.has(ITEM_SWIM, player) and
            state.has(ITEM_FLIGHT, player) and
            state.has(ITEM_WONDERWING, player)
    ),
    LOC_GOLDF_CC_SAWBLADES_2:
    lambda state:
    (
            state.has(ITEM_SWIM, player) and
            state.has(ITEM_FLIGHT, player) and
            state.has(ITEM_WONDERWING, player)
    ),
    LOC_GOLDF_CC_SAWBLADES_3:
    lambda state:
    (
            state.has(ITEM_SWIM, player) and
            state.has(ITEM_FLIGHT, player) and
            state.has(ITEM_WONDERWING, player)
    ),
    LOC_GOLDF_CC_SAWBLADES_4:
    lambda state:
    (
            state.has(ITEM_SWIM, player) and
            state.has(ITEM_FLIGHT, player) and
            state.has(ITEM_WONDERWING, player)
    ),
    LOC_GOLDF_CC_SAWBLADES_5:
    lambda state:
    (
            state.has(ITEM_SWIM, player) and
            state.has(ITEM_FLIGHT, player) and
            state.has(ITEM_WONDERWING, player)
    ),
    LOC_GOLDF_MMM_MAZE_2:
    lambda state: True,

    LOC_GOLDF_MMM_MAZE_BEHIND_HUT_1:
    lambda state:
    (
            can_break_breakable_gates(state, player) and
            state.has(ITEM_FLAP_FLIP, player)
    ),
    LOC_GOLDF_MMM_MAZE_BEHIND_HUT_2:
    lambda state:
    (
            can_break_breakable_gates(state, player) and
            state.has(ITEM_FLAP_FLIP, player)
    ),
    LOC_DEFEAT_GRUNTILDA:
            lambda state: True,
    }
