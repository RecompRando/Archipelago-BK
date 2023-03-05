from ..generic.Rules import set_rule
from BaseClasses import MultiWorld, CollectionState
from .Locations import location_table
from .Regions import connect_regions


def can_access_location(world, state: "CollectionState", player: int, location: str, locations) -> bool:
    for requirements in locations[location].requirements:
        fulfills_requirements = True
        for requirement in requirements:
            if requirement.startswith("Mumbo Token Amount"):
                if not state.has("Mumbo Token", player, int(world.number_of_mumbo_tokens[player].value * .66)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [MM]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value * .01)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [TTC]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value * .08)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [CC]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value * .08)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [BS]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value * .15)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [FP]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value * .32)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [GV]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value * .32)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [MMM]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value * .42)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [RBB]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value * .54)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [CCW]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value * .69)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [FB]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value * .94)):
                    fulfills_requirements = False
            elif requirement == "Jiggy Amount [SP]":
                if not state.has("Jiggy", player, int(world.number_of_jiggies[player].value * .98)):
                    fulfills_requirements = False
            elif requirement == "Note Door Amount [1]":
                if not state.has("Note", player, 50):
                    fulfills_requirements = False
            elif requirement == "Note Door Amount [2]":
                if not state.has("Note", player, 180):
                    fulfills_requirements = False
            elif requirement == "Note Door Amount [3]":
                if not state.has("Note", player, 260):
                    fulfills_requirements = False
            elif requirement == "Note Door Amount [4]":
                if not state.has("Note", player, 350):
                    fulfills_requirements = False
            elif requirement == "Note Door Amount [5]":
                if not state.has("Note", player, 450):
                    fulfills_requirements = False
            elif requirement == "Note Door Amount [6]":
                if not state.has("Note", player, 640):
                    fulfills_requirements = False
            elif requirement == "Note Door Amount [7]":
                if not state.has("Note", player, 765):
                    fulfills_requirements = False
            elif requirement == "Note Door Amount [8]":
                if not state.has("Note", player, 810):
                    fulfills_requirements = False
            elif requirement == "Note Door Amount [9]":
                if not state.has("Note", player, 882):
                    fulfills_requirements = False
            else:
                if not state.has(requirement, player):
                    fulfills_requirements = False
        if fulfills_requirements:
            return True
    return False


def set_location_rule(world: MultiWorld, player: int, location: str, locations):
    set_rule(world.get_location(location, player),
             lambda state: can_access_location(world, state, player, location, locations))


def set_location_rules(world: MultiWorld, player: int):
    for location, data in location_table.items():
        if data.requirements:
            set_location_rule(world, player, location, location_table)


def set_rules(world: MultiWorld, player: int, level_entrances: list[list[str, int]]):
    connect_regions(world, player, "Menu", "Spiral Mountain")
    connect_regions(world, player, "Spiral Mountain", "Grunty's Lair 1F")
    connect_regions(world, player, "Grunty's Lair 1F", level_entrances[0][0]), lambda state: state.has(
        "MM Jiggy Puzzle", player)
    connect_regions(world, player, "Grunty's Lair 1F", "Grunty's Lair 2F"), lambda state: state.has(
        "Talon Trot", player) and state.has("Note Door 1", player)
    connect_regions(world, player, "Grunty's Lair 2F", level_entrances[1][0]), lambda state: state.has(
        "TTC Jiggy Puzzle", player)
    connect_regions(world, player, "Grunty's Lair 2F", "Grunty's Lair 3F"), lambda state: state.has(
        "Flap Flip", player)
    connect_regions(world, player, "Grunty's Lair 3F", level_entrances[2][0]), lambda state: state.has(
        "CC Jiggy Puzzle", player) and state.has("Beak Buster", player) and (state.has("Feathery Flap", player) or
                                                                             state.has("Rat-A-Tat Rap", player) or
                                                                             state.has("Talon Trot", player))
    connect_regions(world, player, "Grunty's Lair 2F", "Grunty's Lair 4F"), lambda state: state.has(
        "Talon Trot", player) and state.has("Note Door 2", player)
    connect_regions(world, player, "Grunty's Lair 4F", level_entrances[3][0]), lambda state: state.has(
        "BS Jiggy Puzzle", player)
    connect_regions(world, player, "Grunty's Lair 4F", "Grunty's Lair 5F"), lambda state: state.has(
        "Shock Spring Jump", player) and state.has("Note Door 3", player)
    connect_regions(world, player, "Grunty's Lair 5F", level_entrances[4][0]), lambda state: state.has(
        "FP Jiggy Puzzle", player)
    connect_regions(world, player, "Grunty's Lair 5F", level_entrances[5][0]), lambda state: state.has(
        "GV Jiggy Puzzle", player) and state.has("Stilt Stride", player) and (state.has("Beak Barge", player) or
                                                                              state.has("Rat-A-Tat Rap", player) or
                                                                              state.has("Eggs", player))
    connect_regions(world, player, "Grunty's Lair 5F", "Grunty's Lair 6F"), lambda state: state.has(
        "Note Door 4", player)
    connect_regions(world, player, "Grunty's Lair 6F", level_entrances[6][0]), lambda state: state.has(
        "MMM Jiggy Puzzle", player)
    connect_regions(world, player, "Grunty's Lair 5F", "Grunty's Lair 7F"), lambda state: state.has(
        "Note Door 5", player)
    connect_regions(world, player, "Grunty's Lair 7F", level_entrances[7][0]), lambda state: state.has(
        "RBB Jiggy Puzzle", player) and state.has("Water Level Switch 1", player)
    connect_regions(world, player, "Grunty's Lair 7F", "Grunty's Lair 8F"), lambda state: state.has(
        "Note Door 6", player) and state.has("Water Level Switch 1", player) and state.has(
        "Water Level Switch 2", player) and (state.has("Flap Flip", player) or (state.has("Rat-A-Tat Rap", player) and
                                                                                state.has("Beak Buster", player)) or
                                             (state.has("Eggs", player) and
                                              state.has("Beak Buster", player)))
    connect_regions(world, player, "Grunty's Lair 8F", level_entrances[8][0]), lambda state: state.has(
        "CCW Jiggy Puzzle", player) and state.has("Talon Trot", player)
    connect_regions(world, player, "Grunty's Lair 8F", "Grunty's Lair - Furnace Fun"), lambda state: state.has(
        "Note Door 7", player) and (state.has("Flap Flip", player) or state.has("Bee Transformation", player) or
                                    (state.has("Talon Trot", player) and state.has("Flight", player)))
    connect_regions(world, player, "Grunty's Lair - Furnace Fun", "Grunty's Lair - Top Floor"), lambda state: state.has(
        "Note Door 8", player)

    set_location_rules(world, player)
