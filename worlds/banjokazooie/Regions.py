from BaseClasses import MultiWorld, Region, Entrance
from .Locations import *


def connect_regions(world: MultiWorld, player, source: str, target: str, rule: typing.Optional[typing.Callable] = None):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

    connection = Entrance(player, source_region.name + " -> " + target_region.name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)


def create_region(name: str, player: int, world: MultiWorld):
    return Region(name, player, world, name)


def create_regions(world: MultiWorld, player: int):
    menu_region = Region("Menu", player, world)
    world.regions.append(menu_region)

    sm_region = Region("Spiral Mountain", player, world)
    for location, data in empty_honeycomb_location_table:
        if location.contains("SM"):
            sm_region.locations.append(BKLocation(player, location, data.code, sm_region))
    if world.shuffle_basic_moves[player].value:
        for location, data in basic_molehill_location_table:
            sm_region.locations.append(BKLocation(player, location, data.code, sm_region))
    world.regions.append(sm_region)

    gl_floor_1_region = create_region("Grunty's Lair 1F", player, world)
    initialize_locations(gl_floor_1_region, glf1_location_table, player)
    world.regions.append(gl_floor_1_region)

    mm_region = create_region("Mumbo's Mountain", player, world)
    initialize_locations(mm_region, mm_location_table, player)
    if world.shuffle_moves[player].value != 0:
        for location, data in molehill_location_table:
            if location.contains("MM"):
                mm_region.locations.append(BKLocation(player, location, data.code, mm_region))
    for location, data in empty_honeycomb_location_table:
        if location.contains("MM"):
            mm_region.locations.append(BKLocation(player, location, data.code, mm_region))
    for location, data in mumbo_token_location_table:
        if location.contains("MM"):
            mm_region.locations.append(BKLocation(player, location, data.code, mm_region))
    for location, data in mm_notes_location_table:
        mm_region.locations.append(BKLocation(player, location, data.code, mm_region))
    world.regions.append(mm_region)

    gl_floor_2_region = create_region("Grunty's Lair 2F", player, world)
    initialize_locations(gl_floor_2_region, glf2_location_table, player)
    for location, data in mumbo_token_location_table:
        if location.contains("GLF2"):
            gl_floor_2_region.locations.append(BKLocation(player, location, data.code, gl_floor_2_region))
    world.regions.append(gl_floor_2_region)

    ttc_region = create_region("Treasure Trove Cove", player, world)
    initialize_locations(ttc_region, ttc_location_table, player)
    for location, data in empty_honeycomb_location_table:
        if location.contains("TTC"):
            ttc_region.locations.append(BKLocation(player, location, data.code, ttc_region))
    for location, data in mumbo_token_location_table:
        if location.contains("TTC"):
            ttc_region.locations.append(BKLocation(player, location, data.code, ttc_region))
    for location, data in ttc_notes_location_table:
        ttc_region.locations.append(BKLocation(player, location, data.code, ttc_region))
    if world.shuffle_moves[player].value:
        for location, data in molehill_location_table:
            if location.contains("TTC"):
                ttc_region.locations.append(BKLocation(player, location, data.code, ttc_region))
    if world.shuffle_secrets[player].value:
        ttc_region.locations.append(BKLocation(
            player, "Sharkfood Island Egg", secrets_location_table["Pink Egg"].code, ttc_region))
    world.regions.append(ttc_region)

    gl_floor_3_region = create_region("Grunty's Lair 3F", player, world)
    initialize_locations(gl_floor_3_region, glf3_location_table, player)
    for location, data in mumbo_token_location_table:
        if location.contains("GLF3"):
            gl_floor_3_region.locations.append(BKLocation(player, location, data.code, gl_floor_3_region))
    world.regions.append(gl_floor_3_region)

    cc_region = create_region("Clanker's Cavern", player, world)
    initialize_locations(cc_region, cc_location_table, player)
    for location, data in empty_honeycomb_location_table:
        if location.contains("CC"):
            cc_region.locations.append(BKLocation(player, location, data.code, cc_region))
    for location, data in mumbo_token_location_table:
        if location.contains("CC"):
            cc_region.locations.append(BKLocation(player, location, data.code, cc_region))
    for location, data in cc_notes_location_table:
        cc_region.locations.append(BKLocation(player, location, data.code, cc_region))
    if world.shuffle_moves[player].value:
        for location, data in molehill_location_table:
            if location.contains("CC"):
                cc_region.locations.append(BKLocation(player, location, data.code, cc_region))
    world.regions.append(cc_region)

    gl_floor_4_region = create_region("Grunty's Lair 4F", player, world)
    initialize_locations(gl_floor_4_region, glf4_location_table, player)
    if world.shuffle_cheato[player].value:
        gl_floor_4_region.locations.append(
            BKLocation(player, "BLUEEGGS Cheato", cheato_location_table["BLUEEGGS Cheato"].code, gl_floor_4_region))
    world.regions.append(gl_floor_4_region)

    bs_region = create_region("Bubblegloop Swamp", player, world)
    initialize_locations(bs_region, bs_location_table, player)
    for location, data in empty_honeycomb_location_table:
        if location.contains("BS"):
            bs_region.locations.append(BKLocation(player, location, data.code, bs_region))
    for location, data in mumbo_token_location_table:
        if location.contains("BS"):
            bs_region.locations.append(BKLocation(player, location, data.code, bs_region))
    for location, data in bs_notes_location_table:
        bs_region.locations.append(BKLocation(player, location, data.code, bs_region))
    if world.shuffle_moves[player].value:
        for location, data in molehill_location_table:
            if location.contains("BS"):
                bs_region.locations.append(BKLocation(player, location, data.code, bs_region))
    world.regions.append(bs_region)

    gl_floor_5_region = create_region("Grunty's Lair 5F", player, world)
    initialize_locations(gl_floor_5_region, glf5_location_table, player)
    for location, data in mumbo_token_location_table:
        if location.contains("GLF5"):
            gl_floor_5_region.locations.append(BKLocation(player, location, data.code, gl_floor_5_region))
    world.regions.append(gl_floor_5_region)

    fp_region = create_region("Freezeezy Peak", player, world)
    initialize_locations(fp_region, fp_location_table, player)
    for location, data in empty_honeycomb_location_table:
        if location.contains("FP"):
            fp_region.locations.append(BKLocation(player, location, data.code, fp_region))
    for location, data in mumbo_token_location_table:
        if location.contains("FP"):
            fp_region.locations.append(BKLocation(player, location, data.code, fp_region))
    for location, data in fp_notes_location_table:
        fp_region.locations.append(BKLocation(player, location, data.code, fp_region))
    if world.shuffle_moves[player].value:
        for location, data in molehill_location_table:
            if location.contains("FP"):
                fp_region.locations.append(BKLocation(player, location, data.code, fp_region))
    if world.shuffle_secrets[player].value:
        fp_region.locations.append(BKLocation(player, "Ice Key", secrets_location_table["Ice Key"].code, fp_region))
    world.regions.append(fp_region)

    gv_region = create_region("Gobi's Valley", player, world)
    initialize_locations(gv_region, gv_location_table, player)
    for location, data in empty_honeycomb_location_table:
        if location.contains("GV"):
            gv_region.locations.append(BKLocation(player, location, data.code, gv_region))
    for location, data in mumbo_token_location_table:
        if location.contains("GV"):
            gv_region.locations.append(BKLocation(player, location, data.code, gv_region))
    for location, data in gv_notes_location_table:
        gv_region.locations.append(BKLocation(player, location, data.code, gv_region))
    if world.shuffle_moves[player].value:
        for location, data in molehill_location_table:
            if location.contains("GV"):
                gv_region.locations.append(BKLocation(player, location, data.code, gv_region))
    if world.shuffle_secrets[player].value:
        gv_region.locations.append(BKLocation(
            player, "Gobi's Valley Egg", secrets_location_table["Blue Egg"].code, gv_region))
    world.regions.append(gv_region)

    gl_floor_6_region = create_region("Grunty's Lair 6F", player, world)
    initialize_locations(gl_floor_6_region, glf6_location_table, player)
    for location, data in mumbo_token_location_table:
        if location.contains("GLF6"):
            gl_floor_6_region.locations.append(BKLocation(player, location, data.code, gl_floor_6_region))
    if world.shuffle_cheato[player].value:
        gl_floor_6_region.locations.append(
            BKLocation(player, "REDFEATHERS Cheato", cheato_location_table["REDFEATHERS Cheato"].code, gl_floor_6_region))
    world.regions.append(gl_floor_6_region)

    gl_floor_7_region = create_region("Grunty's Lair 7F", player, world)
    initialize_locations(gl_floor_7_region, glf7_location_table, player)
    for location, data in mumbo_token_location_table:
        if location.contains("GLF7"):
            gl_floor_7_region.locations.append(BKLocation(player, location, data.code, gl_floor_7_region))
    if world.shuffle_cheato[player].value:
        gl_floor_7_region.locations.append(
            BKLocation(player, "GOLDFEATHERS Cheato", cheato_location_table["GOLDFEATHERS Cheato"].code, gl_floor_7_region))
    world.regions.append(gl_floor_7_region)

    mmm_region = create_region("Mad Monster Mansion", player, world)
    initialize_locations(mmm_region, mmm_location_table, player)
    for location, data in empty_honeycomb_location_table:
        if location.contains("MMM"):
            mmm_region.locations.append(BKLocation(player, location, data.code, mmm_region))
    for location, data in mumbo_token_location_table:
        if location.contains("MMM"):
            mmm_region.locations.append(BKLocation(player, location, data.code, mmm_region))
    for location, data in mmm_notes_location_table:
        mmm_region.locations.append(BKLocation(player, location, data.code, mmm_region))
    if world.shuffle_secrets[player].value:
        mmm_region.locations.append(BKLocation(
            player, "Cellar Egg", secrets_location_table["Cyan Egg"].code, mmm_region))
        mmm_region.locations.append(BKLocation(
            player, "Bathroom Egg", secrets_location_table["Green Egg"].code, mmm_region))
    world.regions.append(mmm_region)

    rbb_region = create_region("Rusty Bucket Bay", player, world)
    initialize_locations(rbb_region, rbb_location_table, player)
    for location, data in empty_honeycomb_location_table:
        if location.contains("RBB"):
            rbb_region.locations.append(BKLocation(player, location, data.code, rbb_region))
    for location, data in mumbo_token_location_table:
        if location.contains("RBB"):
            rbb_region.locations.append(BKLocation(player, location, data.code, rbb_region))
    for location, data in rbb_notes_location_table:
        rbb_region.locations.append(BKLocation(player, location, data.code, rbb_region))
    if world.shuffle_secrets[player].value:
        rbb_region.locations.append(BKLocation(
            player, "Captain's Room Egg", secrets_location_table["Red Egg"].code, rbb_region))
    world.regions.append(rbb_region)

    gl_floor_8_region = create_region("Grunty's Lair 8F", player, world)
    initialize_locations(gl_floor_8_region, glf8_location_table, player)
    for location, data in mumbo_token_location_table:
        if location.contains("GLF8"):
            gl_floor_8_region.locations.append(BKLocation(player, location, data.code, gl_floor_8_region))
    world.regions.append(gl_floor_8_region)

    ccw_region = create_region("Click Clock Wood", player, world)
    initialize_locations(ccw_region, ccw_location_table, player)
    for location, data in empty_honeycomb_location_table:
        if location.contains("CCW"):
            ccw_region.locations.append(BKLocation(player, location, data.code, ccw_region))
    for location, data in mumbo_token_location_table:
        if location.contains("CCW"):
            ccw_region.locations.append(BKLocation(player, location, data.code, ccw_region))
    for location, data in ccw_notes_location_table:
        ccw_region.locations.append(BKLocation(player, location, data.code, ccw_region))
    if world.shuffle_secrets[player].value:
        ccw_region.locations.append(BKLocation(
            player, "Nabnut's Egg", secrets_location_table["Yellow Egg"].code, ccw_region))
    world.regions.append(ccw_region)

    gl_floor_furnace_fun_region = create_region("Grunty's Lair - Furnace Fun", player, world)
    world.regions.append(gl_floor_furnace_fun_region)

    gl_top_floor_region = create_region("Grunty's Lair - Top Floor", player, world)
    world.regions.append(gl_top_floor_region)


def initialize_locations(region: Region, locations, player: int):
    region.locations += [BKLocation(player, location_name, location_table[location_name].address, region)
                         for location_name in locations]
