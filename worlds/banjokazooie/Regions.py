from BaseClasses import MultiWorld, Region, Entrance
from Locations import *


def create_regions(world: MultiWorld, player: int):
    menu_region = Region("Menu", player, world, "Spiral Mountain")
    if(world.ShuffleBasicMoves[player].value):
        for location in basic_molehill_location_table.keys():
            menu_region.locations.append(BKLocation(player, location, basic_molehill_location_table[location].address, menu_region))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("SM"):
                menu_region.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, menu_region))
    world.regions.append(menu_region)

    glfloor1region = create_region("Grunty's Lair 1F", player, world)
    initialize_locations(glfloor1region, glf1_location_table)
    world.regions.append(glfloor1region)

    mmregion = create_region("Mumbo's Mountain", player, world)
    initialize_locations(mmregion, mm_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("MM"):
                mmregion.locations.append(BKLocation(player, location, molehill_location_table[location].address, mmregion))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("MM"):
                mmregion.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, mmregion))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("MM"):
                mmregion.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, mmregion))
    world.regions.append(mmregion)

    glfloor2region = create_region("Grunty's Lair 2F", player, world)
    initialize_locations(glfloor2region, glf2_location_table)
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("GLF2"):
                glfloor2region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, glfloor2region))
    world.regions.append(glfloor2region)

    ttcregion = create_region("Treasure Trove Cove", player, world)
    initialize_locations(ttcregion, ttc_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("TTC"):
                ttcregion.locations.append(BKLocation(player, location, molehill_location_table[location].address, ttcregion))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("TTC"):
                ttcregion.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, ttcregion))
    if(world.ShuffleSecrets[player].value):
        ttcregion.locations.append(BKLocation(player, "Sharkfood Island Egg", secrets_location_table["Pink Egg"].address, ttcregion))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("TTC"):
                ttcregion.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, ttcregion))
    world.regions.append(ttcregion)

    ccregion = create_region("Clanker's Cavern", player, world)
    initialize_locations(ccregion, cc_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("CC"):
                ccregion.locations.append(BKLocation(player, location, molehill_location_table[location].address, ccregion))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("CC"):
                ccregion.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, ccregion))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("CC"):
                ccregion.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, ccregion))
    world.regions.append(ccregion)

    glfloor3region = create_region("Grunty's Lair 3F", player, world)
    initialize_locations(glfloor3region, glf3_location_table)
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("GLF3"):
                glfloor3region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, glfloor3region))
    world.regions.append(glfloor3region)

    bsregion = create_region("Bubblegloop Swamp", player, world)
    initialize_locations(bsregion, bs_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("BS"):
                bsregion.locations.append(BKLocation(player, location, molehill_location_table[location].address, bsregion))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("BS"):
                bsregion.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, bsregion))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("BS"):
                bsregion.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, bsregion))
    world.regions.append(bsregion)

    glfloor4region = create_region("Grunty's Lair 4F", player, world)
    initialize_locations(glfloor4region, glf4_location_table)
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("GLF4"):
                glfloor4region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, glfloor4region))
    world.regions.append(glfloor4region)

    fpregion = create_region("Freezeezy Peak", player, world)
    initialize_locations(fpregion, fp_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("FP"):
                fpregion.locations.append(BKLocation(player, location, molehill_location_table[location].address, fpregion))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("FP"):
                fpregion.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, fpregion))
    if(world.ShuffleSecrets[player].value):
        fpregion.locations.append(BKLocation(player, "Ice Key", secrets_location_table["Ice Key"].address, fpregion))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("FP"):
                fpregion.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, fpregion))
    world.regions.append(fpregion)

    gvregion = create_region("Gobi's Valley", player, world)
    initialize_locations(gvregion, gv_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("GV"):
                gvregion.locations.append(BKLocation(player, location, molehill_location_table[location].address, gvregion))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("GV"):
                gvregion.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, gvregion))
    if(world.ShuffleSecrets[player].value):
        gvregion.locations.append(BKLocation(player, "Gobi's Valley Egg", secrets_location_table["Blue Egg"].address, gvregion))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("GV"):
                gvregion.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, gvregion))
    world.regions.append(gvregion)

    glfloor5region = create_region("Grunty's Lair 5F", player, world)
    initialize_locations(glfloor5region, glf5_location_table)
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("GLF5"):
                glfloor5region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, glfloor5region))
    world.regions.append(glfloor5region)

    mmmregion = create_region("Mad Monster Mansion", player, world)
    initialize_locations(mmmregion, mmm_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("MMM"):
                mmmregion.locations.append(BKLocation(player, location, molehill_location_table[location].address, mmmregion))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("MMM"):
                mmmregion.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, mmmregion))
    if(world.ShuffleSecrets[player].value):
        mmmregion.locations.append(BKLocation(player, "Cellar Egg", secrets_location_table["Cyan Egg"].address, mmmregion))
        mmmregion.locations.append(BKLocation(player, "Bathroom Egg", secrets_location_table["Green Egg"].address, mmmregion))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("MMM"):
                mmmregion.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, mmmregion))
    world.regions.append(mmmregion)

    rbbregion = create_region("Rusty Bucket Bay", player, world)
    initialize_locations(rbbregion, rbb_location_table)
    if(world.ShuffleMoves[player].value):
        for location in molehill_location_table.keys():
            if location.contains("RBB"):
                rbbregion.locations.append(BKLocation(player, location, molehill_location_table[location].address, rbbregion))
    if(world.ShuffleEmptyHoneycombs[player].value):
        for location in empty_honeycomb_location_table.keys():
            if location.contains("RBB"):
                rbbregion.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, rbbregion))
    if(world.ShuffleSecrets[player].value):
        rbbregion.locations.append(BKLocation(player, "Captain's Room Egg", secrets_location_table["Red Egg"].address, rbbregion))
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("RBB"):
                rbbregion.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, rbbregion))
    world.regions.append(rbbregion)

    glfloor6region = create_region("Grunty's Lair 6F", player, world)
    initialize_locations(glfloor6region, glf6_location_table)
    if(world.ShuffleMumboTokens[player].value):
        for location in mumbo_token_location_table.keys():
            if location.contains("GLF6"):
                glfloor6region.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, glfloor6region))
    world.regions.append(glfloor6region)

    ccwregion = create_region("Click Clock Wood", player, world)
    initialize_locations(ccwregion, ccw_location_table)
    if world.ShuffleMoves[player].value:
        for location in molehill_location_table.keys():
            if location.contains("CCW"):
                ccwregion.locations.append(BKLocation(player, location, molehill_location_table[location].address, ccwregion))
    if world.ShuffleEmptyHoneycombs[player].value:
        for location in empty_honeycomb_location_table.keys():
            if location.contains("CCW"):
                ccwregion.locations.append(BKLocation(player, location, empty_honeycomb_location_table[location].address, ccwregion))
    if world.ShuffleSecrets[player].value:
        ccwregion.locations.append(BKLocation(player, "Nabnut's Egg", secrets_location_table["Yellow Egg"].address, ccwregion))
    if world.ShuffleMumboTokens[player].value:
        for location in mumbo_token_location_table.keys():
            if location.contains("CCW"):
                ccwregion.locations.append(BKLocation(player, location, mumbo_token_location_table[location].address, ccwregion))
    world.regions.append(ccwregion)

    glfloor7region = create_region("Grunty's Lair 7F", player, world)
    world.regions.append(glfloor7region)

    gltopfloorregion = create_region("Grunty's Lair Top Floor", player, world)
    world.regions.append(gltopfloorregion)


def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule: typing.Optional[typing.Callable] = None):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

    connection = Entrance(player, "", source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)


def create_region(name: str, player: int, world: MultiWorld):
    return Region(name, player, world, name)


def initialize_locations(region: Region, locations, player: int):
    region.locations += [BKLocation(player, location_name, location_table[location_name].address, region) for location_name in locations]
