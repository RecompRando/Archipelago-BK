from BaseClasses import MultiWorld, Region, RegionType, Entrance
from Locations import *


def create_regions(world: MultiWorld, player: int):
    menu_region = Region("Menu", RegionType.Generic, "Spiral Mountain", player, world)
    initialize_locations(menu_region, sm_location_table)
    if(world.ShuffleBasicMoves[player].value):
        for location in basic_molehill_location_table.keys():
            menu_region.locations.append(BKLocation(player, location, basic_molehill_location_table[location].address, menu_region))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("SM"):
                menu_region.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, menu_region))
    world.regions.append(menu_region)

    glregion = create_region("Grunty's Lair", player, world)
    initialize_locations(glregion, gl_location_table)
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("GL"):
                menu_region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, menu_region))
    world.regions.append(glregion)

    mmregion = create_region("Mumbo's Mountain", player, world)
    initialize_locations(mmregion, mm_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("MM"):
                menu_region.locations.append(BKLocation(player, location, molehill_location_table[location].address, menu_region))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("MM"):
                menu_region.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, menu_region))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("MM"):
                menu_region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, menu_region))
    world.regions.append(mmregion)

    glfloor2region = create_region("Grunty's Lair 2F", player, world)
    world.regions.append(glfloor2region)

    ttcregion = create_region("Treasure Trove Cove", player, world)
    initialize_locations(ttcregion, ttc_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("TTC"):
                menu_region.locations.append(BKLocation(player, location, molehill_location_table[location].address, menu_region))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("TTC"):
                menu_region.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, menu_region))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("TTC"):
                menu_region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, menu_region))
    world.regions.append(ttcregion)

    ccregion = create_region("Clanker's Cavern", player, world)
    initialize_locations(ccregion, cc_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("CC"):
                menu_region.locations.append(BKLocation(player, location, molehill_location_table[location].address, menu_region))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("CC"):
                menu_region.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, menu_region))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("CC"):
                menu_region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, menu_region))
    world.regions.append(ccregion)

    glfloor3region = create_region("Grunty's Lair 3F", player, world)
    world.regions.append(glfloor3region)

    bsregion = create_region("Bubblegloop Swamp", player, world)
    initialize_locations(bsregion, bs_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("BS"):
                menu_region.locations.append(BKLocation(player, location, molehill_location_table[location].address, menu_region))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("BS"):
                menu_region.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, menu_region))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("BS"):
                menu_region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, menu_region))
    world.regions.append(bsregion)

    glfloor4region = create_region("Grunty's Lair 4F", player, world)
    world.regions.append(glfloor4region)

    glfloor5region = create_region("Grunty's Lair 5F", player, world)
    world.regions.append(glfloor5region)

    fpregion = create_region("Freezeezy Peak", player, world)
    initialize_locations(fpregion, fp_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("FP"):
                menu_region.locations.append(BKLocation(player, location, molehill_location_table[location].address, menu_region))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("FP"):
                menu_region.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, menu_region))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("FP"):
                menu_region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, menu_region))
    world.regions.append(fpregion)

    gvregion = create_region("Gobi's Valley", player, world)
    initialize_locations(gvregion, gv_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("GV"):
                menu_region.locations.append(BKLocation(player, location, molehill_location_table[location].address, menu_region))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("GV"):
                menu_region.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, menu_region))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("GV"):
                menu_region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, menu_region))
    world.regions.append(gvregion)

    glfloor6region = create_region("Grunty's Lair 6F", player, world)
    world.regions.append(glfloor6region)

    mmmregion = create_region("Mad Monster Mansion", player, world)
    initialize_locations(mmmregion, mmm_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("MMM"):
                menu_region.locations.append(BKLocation(player, location, molehill_location_table[location].address, menu_region))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("MMM"):
                menu_region.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, menu_region))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("MMM"):
                menu_region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, menu_region))
    world.regions.append(mmmregion)

    rbbregion = create_region("Rusty Bucket Bay", player, world)
    initialize_locations(rbbregion, rbb_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("RBB"):
                menu_region.locations.append(BKLocation(player, location, molehill_location_table[location].address, menu_region))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("RBB"):
                menu_region.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, menu_region))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("RBB"):
                menu_region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, menu_region))
    world.regions.append(rbbregion)

    glfloor7region = create_region("Grunty's Lair 7F", player, world)
    world.regions.append(glfloor7region)

    ccwregion = create_region("Click Clock Wood", player, world)
    initialize_locations(ccwregion, ccw_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("CCW"):
                menu_region.locations.append(BKLocation(player, location, molehill_location_table[location].address, menu_region))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("CCW"):
                menu_region.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, menu_region))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("CCW"):
                menu_region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, menu_region))
    world.regions.append(ccwregion)

    glfloor8region = create_region("Grunty's Lair 8F", player, world)
    world.regions.append(glfloor8region)


def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule: typing.Optional[typing.Callable] = None):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

    connection = Entrance(player, "", source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)


def create_region(name: str, player: int, world: MultiWorld):
    return Region(name, RegionType.Generic, name, player, world)


def initialize_locations(region: Region, locations, player):
    region.locations += [BKLocation(player, location_name, location_table[location_name].address, region) for location_name in locations]
