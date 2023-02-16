from BaseClasses import MultiWorld, Region, RegionType, Entrance
from Locations import *

def create_regions(world: MultiWorld, player: int):
    menu_region = Region("Menu", RegionType.Generic, "Spiral Mountain", player, world)
    initialize_locations(menu_region, sm_location_table)
    world.regions.append(menu_region)

    glregion = Region("Grunty's Lair", player, world)
    initialize_locations(glregion, gl_location_table)
    world.regions.append(glregion)

    mmregion = Region("Mumbo's Mountain", player, world)
    initialize_locations(mmregion, mm_location_table)
    world.regions.append(mmregion)

    glfloor2region = Region("Grunty's Lair 2F", player, world)
    world.regions.append(glfloor2region)

    ttcregion = Region("Treasure Trove Cove", player, world)
    initialize_locations(ttcregion, ttc_location_table)
    world.regions.append(ttcregion)

    ccregion = Region("Clanker's Cavern", player, world)
    initialize_locations(ccregion, cc_location_table)
    world.regions.append(ccregion)

    glfloor3region = Region("Grunty's Lair 3F", player, world)
    world.regions.append(glfloor3region)

    bsregion = Region("Bubblegloop Swamp", player, world)
    initialize_locations(bsregion, bs_location_table)
    world.regions.append(bsregion)

    glfloor4region = Region("Grunty's Lair 4F", player, world)
    world.regions.append(glfloor4region)

    glfloor5region = Region("Grunty's Lair 5F", player, world)
    world.regions.append(glfloor5region)

    fpregion = Region("Freezeezy Peak", player, world)
    initialize_locations(fpregion, fp_location_table)
    world.regions.append(fpregion)

    gvregion = Region("Gobi's Valley", player, world)
    initialize_locations(gvregion, gv_location_table)
    world.regions.append(gvregion)

    glfloor6region = Region("Grunty's Lair 6F", player, world)
    world.regions.append(glfloor6region)

    mmmregion = Region("Mad Monster Mansion", player, world)
    initialize_locations(mmmregion, mmm_location_table)
    world.regions.append(mmmregion)

    rbbregion = Region("Rusty Bucket Bay", player, world)
    initialize_locations(rbbregion, rbb_location_table)
    world.regions.append(rbbregion)

    glfloor7region = Region("Grunty's Lair 7F", player, world)
    world.regions.append(glfloor7region)

    ccwregion = Region("Click Clock Wood", player, world)
    initialize_locations(ccwregion, ccw_location_table)
    world.regions.append(ccwregion)

    glfloor8region = Region("Grunty's Lair 8F", player, world)
    world.regions.append(glfloor8region)


def initialize_locations(region: Region, locations, player):
    region.locations += [BKLocation(player, location_name, region) for location_name in locations]