from .Constants import *

# ~ def can_play_song(song, state, player):
    # ~ return state.has(song, player) and state.has("Ocarina of Time", player)

def rgn_connection_string(rgn1, rgn2):
    return str(rgn1) + " -> " + str(rgn2)

def get_region_rules(player, options):
    return {
        rgn_connection_string(RGN_SPIRAL_MOUNTAIN, RGN_GRUNTILDAS_LAIR):
            lambda state: True,
    }

def get_location_rules(player, options):
    return {
        # ~ "Keaton Quiz":
            # ~ lambda state: state.has("Keaton Mask", player),
        LOC_DEFEAT_GRUNTILDA:
            lambda state: True,
    }
