from ..generic.Rules import add_rule, set_rule
from BaseClasses import MultiWorld, CollectionState
from Locations import setup_locations


def set_rules(world: MultiWorld, player: int):
    gruntys_lair_entrances = [
        ["Spiral Mountain", 1],
        ["Grunty's Lair 1F", 2],
        ["Grunty's Lair 2F", 3],
        ["Grunty's Lair 3F", 4],
        ["Grunty's Lair 4F", 5],
        ["Grunty's Lair 5F", 6],
        ["Grunty's Lair 6F", 7],
        ["Grunty's Lair 7F", 8],
        ["Grunty's Lair Top Floor", 9]
    ]

    level_entrances = [
        ["Mumbo's Mountain", 10],
        ["Treasure Trove Cove", 11],
        ["Clanker's Cavern", 12],
        ["Bubblegloop Swamp", 13],
        ["Freezeezy Peak", 14],
        ["Gobi's Valley", 15],
        ["Mad Monster Mansion", 16],
        ["Rusty Bucket Bay", 17],
        ["Click Clock Wood", 18],
    ]

    if world.level_randomizer[player].value:
        world.random.shuffle(level_entrances)
        if world.shuffle_moves[player].value == 0:
            while level_entrances[0][0] != "Mumbo's Mountain" and (
                    level_entrances[3][0] != "Bubblegloop Swamp" or "Freezeezy Peak" or "Mad Monster Mansion" or
                    "Click Clock Wood") and (
                    level_entrances[6][0] != "Bubblegloop Swamp" or "Freezeezy Peak" or "Mad Monster Mansion" or
                    "Click Clock Wood"):
                world.random.shuffle(level_entrances)
        else:
            while (level_entrances[0][0] != "Mumbo's Mountain" or "Bubblegloop Swamp" or "Freezeezy Peak" or
                   "Mad Monster Mansion" or "Click Clock Wood") and (
                    level_entrances[3][0] != "Mumbo's Mountain" or "Bubblegloop Swamp" or "Freezeezy Peak" or
                    "Mad Monster Mansion" or "Click Clock Wood") and (
                    level_entrances[6][0] != "Mumbo's Mountain" or "Bubblegloop Swamp" or "Freezeezy Peak" or
                    "Mad Monster Mansion" or "Click Clock Wood"):
                world.random.shuffle(level_entrances)

    set_location_rules(world, player)
    set_region_rules(world, player)


def set_location_rules(world: MultiWorld, player: int):
    locations = setup_locations(world, player)
    for location, data in locations:
        if data.requirements:
            set_location_rule(world, player, location, locations)


def set_region_rules(world: MultiWorld, player: int):
    for region in world.get_regions(player):
        if region.name == "Mumbo's Mountain":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 1))
        if region.name == "Grunty's Lair 2F":
            set_rule(region.entrances[0], lambda state: state.has("Talon Trot", player, 1) and state.has(
                "Note", player, 50))
        if region.name == "Treasure Trove Cove":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 3))
        if region.name == "Clanker's Cavern":
            set_rule(region.entrances[0],
                     lambda state: state.has("Jiggy", player, 8) and state.has("Flap Flip", player, 1) and state.has(
                         "Swim", player, 1) and state.has("Beak Buster", player, 1) and state.has(
                         "Shock Spring Jump", player, 1))
        if region.name == "Grunty's Lair 3F":
            set_rule(region.entrances[0], lambda state: state.has("Talon Trot", player, 1) and state.has(
                "Note", player, 180))
        if region.name == "Bubblegloop Swamp":
            set_rule(region.entrances[0],
                     lambda state: state.has("Jiggy", player, 15) and state.has("Flap Flip", player, 1) and state.has(
                         "Swim", player, 1) and state.has("Beak Buster", player, 1))
        if region.name == "Grunty's Lair 4F":
            set_rule(region.entrances[0],
                     lambda state: state.has(
                         "Shock Spring Jump", player, 1) and state.has("Note", player, 260))
        if region.name == "Freezeezy Peak":
            set_rule(region.entrances[0],
                     lambda state: state.has("Jiggy", player, 23) and state.has("Stilt Stride", player, 1))
        if region.name == "Gobi's Valley":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 32) and (
                    state.has("Wonderwing", player, 1) or ((state.has("Beak Barge", player, 1) or state.has(
                "Rat-A-Tat Rap", player, 1) or state.has("Eggs", player, 1)) and state.has("Stilt Stride", player,
                                                                                           1))))
        if region.name == "Grunty's Lair 5F":
            set_rule(region.entrances[0], lambda state: state.has("Note", player, 350))
        if region.name == "Grunty's Lair 6F":
            set_rule(region.entrances[0], lambda state: state.has("Swim", player, 1) and state.has(
                "Note", player, 450))
        if region.name == "Mad Monster Mansion":
            set_rule(region.entrances[0], lambda state: state.has("Jiggy", player, 42) and (
                    state.has("Feathery Flap", player, 1) or state.has("Rat-A-Tat Rap", player, 1) or state.has(
                "Talon Trot", player, 1)) and state.has("Swim", player, 1))
        if region.name == "Rusty Bucket Bay":
            set_rule(region.entrances[0],
                     lambda state: state.has("Jiggy", player, 54) and state.has("Swim", player, 1) and (
                             state.has("Beak Barge", player, 1) or state.has("Rat-A-Tat Rap", player,
                                                                             1)) and state.has("Beak Buster",
                                                                                               player, 1))
        if region.name == "Grunty's Lair 7F":
            set_rule(region.entrances[0], lambda state: state.has("Flap Flip", player, 1) or (
                    (state.has("Rat-A-Tat Rap", player, 1) or state.has("Eggs", player, 1)) and state.has(
                "Beak Buster", player, 1)) and state.has("Note", player, 640))
        if region.name == "Click Clock Wood":
            set_rule(region.entrances[0],
                     lambda state: state.has("Jiggy", player, 69) and state.has("Flap Flip", player, 1) and state.has(
                         "Swim", player, 1) and state.has("Talon Trot", player, 1) and state.has("Beak Buster", player,
                                                                                                 1))
        if region.name == "Grunty's Lair 8F":
            set_rule(region.entrances[0], lambda state: state.has("Flap Flip", player, 1) and state.has(
                "Note", player, 765))
        if region.name == "Grunty's Lair Top Floor":
            set_rule(region.entrances[0],
                     lambda state: state.has("Jiggy", player, 94) and state.has("Eggs", player, 1) and state.has(
                         "Flight", player, 1) and ((state.has("Wonderwing") and state.has("Beak Bomb", player,
                                                                                          1)) or state.has(
                         "Beak Buster")) and state.has("Note", player, 810))


def set_location_rule(world: MultiWorld, player: int, location: str, locations):
    set_rule(world.get_location(location, player),
             lambda state: can_access_location(world, state, player, location, locations))


def can_access_location(world, state: "CollectionState", player: int, location: str, locations) -> bool:
    for requirements in locations[location].requirements:
        fulfills_requirements = True
        for requirement in requirements:
            if requirement.startswith("Mumbo Token Amount"):
                if not state.has("Mumbo Token", player, int(world.number_of_mumbo_tokens[player].value*.66)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [MM]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value*.01)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [TTC]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value*.08)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [CC]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value*.08)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [BS]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value*.15)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [FP]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value*.32)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [GV]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value*.32)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [MMM]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value*.42)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [RBB]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value*.54)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [CCW]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value*.69)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [FB]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value*.94)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [SP]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value*.98)):
                    fulfills_requirements = False
            elif requirement == "Node Door Amount [1]":
                if not state.has("Note", player, 50):
                    fulfills_requirements = False
            elif requirement == "Node Door Amount [2]":
                if not state.has("Note", player, 180):
                    fulfills_requirements = False
            elif requirement == "Node Door Amount [3]":
                if not state.has("Note", player, 260):
                    fulfills_requirements = False
            elif requirement == "Node Door Amount [4]":
                if not state.has("Note", player, 350):
                    fulfills_requirements = False
            elif requirement == "Node Door Amount [5]":
                if not state.has("Note", player, 450):
                    fulfills_requirements = False
            elif requirement == "Node Door Amount [6]":
                if not state.has("Note", player, 640):
                    fulfills_requirements = False
            elif requirement == "Node Door Amount [7]":
                if not state.has("Note", player, 765):
                    fulfills_requirements = False
            elif requirement == "Node Door Amount [8]":
                if not state.has("Note", player, 810):
                    fulfills_requirements = False
            elif requirement == "Node Door Amount [9]":
                if not state.has("Note", player, 882):
                    fulfills_requirements = False
            else:
                if not state.has(requirement, player, 1):
                    fulfills_requirements = False
        if fulfills_requirements:
            return True
    return False
