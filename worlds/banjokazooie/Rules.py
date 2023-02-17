from ..generic.Rules import add_rule, set_rule
from BaseClasses import MultiWorld, CollectionState
from Locations import setup_locations


def set_rules(world: MultiWorld, player: int):
    set_location_rules(world, player)
    set_region_rules(world, player)


def set_location_rules(world: MultiWorld, player: int):
    locations = setup_locations(world, player)
    for location in locations:
        if locations[location].requirements:
            set_location_rule(world, player, location, locations)


def set_region_rules(world: MultiWorld, player: int):
    for region in world.get_regions(player):
        if region.name == "Mumbo's Mountain":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 1))
        if region.name == "Grunty's Lair 2F":
            set_rule(region.entrances[0], lambda state: state.has("Talon Trot", player, 1))
        if region.name == "Treasure Trove Cove":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 3))
        if region.name == "Clanker's Cavern":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 8) and state.has("Jump", player, 1) and state.has("Flap Flip", player, 1) and state.has("Swim", player, 1) and state.has("Beak Buster", player, 1) and state.has("Shock Spring Jump", player, 1))
        if region.name == "Grunty's Lair 3F":
            set_rule(region.entrances[0], lambda state: state.has("Talon Trot", player, 1))
        if region.name == "Bubblegloop Swamp":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 15) and state.has("Flap Flip", player, 1) and state.has("Swim", player, 1) and state.has("Beak Buster", player, 1))
        if region.name == "Grunty's Lair 4F":
            set_rule(region.entrances[0], lambda state: state.has("Jump", player, 1) and state.has("Shock Spring Jump", player, 1))
        if region.name == "Freezeezy Peak":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 23) and state.has("Stilt Stride", player, 1))
        if region.name == "Gobi's Valley":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 32) and (state.has("Wonderwing", player, 1) or ((state.has("Beak Barge", player, 1) or state.has("Rat-A-Tat Rap", player, 1) or state.has("Eggs", player, 1)) and state.has("Stilt Stride", player, 1))))
        if region.name == "Grunty's Lair 5F":
            set_rule(region.entrances[0], lambda state: state.has("Swim", player, 1))
        if region.name == "Mad Monster Mansion":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 42) and (state.has("Feathery Flap", player, 1) or state.has("Rat-A-Tat Rap", player, 1) or state.has("Talon Trot", player, 1)) and state.has("Swim", player, 1))
        if region.name == "Rusty Bucket Bay":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 54) and state.has("Swim", player, 1) and (state.has("Beak Barge", player, 1) or state.has("Rat-A-Tat Rap", player, 1)) and state.has("Beak Buster", player, 1))
        if region.name == "Grunty's Lair 6F":
            set_rule(region.entrances[0], lambda state: state.has("Flap Flip", player, 1) or ((state.has("Rat-A-Tat Rap", player, 1) or state.has("Eggs", player, 1)) and state.has("Beak Buster", player, 1)))
        if region.name == "Click Clock Wood":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 69) and state.has("Flap Flip", player, 1) and state.has("Swim", player, 1) and state.has("Talon Trot", player, 1) and state.has("Beak Buster", player, 1))
        if region.name == "Grunty's Lair 7F":
            set_rule(region.entrances[0], lambda state: state.has("Flap Flip", player, 1))
        if region.name == "Grunty's Lair Top Floor":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 94) and state.has("Eggs", player, 1) and state.has("Flight", player, 1) and ((state.has("Wonderwing") and state.has("Beak Bomb", player, 1)) or state.has("Beak Buster")))


def set_location_rule(world: MultiWorld, player: int, location: str, locations):
    set_rule(world.get_location(location, player), lambda state: can_access_location(state, player, location, locations))


def can_access_location(state: "CollectionState", player: int, location: str, locations) -> bool:
    for requirements in locations[location].requirements:
        fulfills_requirements = True
        for requirement in requirements:
            if not state.has(requirement, player, 1):
                fulfills_requirements = False
        if fulfills_requirements:
            return True
    return False
