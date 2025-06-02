from .Constants import *

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
        LOC_JIGGY_MM_CONGA_ORANGE_THROW:
            lambda state: True,
        LOC_JIGGY_MM_CHIMPY_ORANGE:
            lambda state:
            (
                state.has(ITEM_FLAP_FLIP, player) or
                state.has(ITEM_CLIMB, player)
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
                    state.has(ITEM_TALON_TROT, player)
                )
            ),
        LOC_JIGGY_MM_HUT:
            lambda state:
            (
                state.has(ITEM_BEAK_BUSTER, player)
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
        LOC_DEFEAT_GRUNTILDA:
            lambda state: True,
    }
