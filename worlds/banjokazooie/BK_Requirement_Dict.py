from .BK_Enums import BK_Str_Enums

JIGGY_REQUIREMENT_DICT:dict = {
    BK_Str_Enums.JIGGY_AMOUNT_MM: lambda world, player: int(world.number_of_jiggies[player].value * 0.01),
    BK_Str_Enums.JIGGY_AMOUNT_TTC: lambda world, player: int(world.number_of_jiggies[player].value * 0.08),
    BK_Str_Enums.JIGGY_AMOUNT_CC: lambda world, player: int(world.number_of_jiggies[player].value * 0.08),
    BK_Str_Enums.JIGGY_AMOUNT_BS: lambda world, player: int(world.number_of_jiggies[player].value * 0.15),
    BK_Str_Enums.JIGGY_AMOUNT_FP: lambda world, player: int(world.number_of_jiggies[player].value * 0.32),
    BK_Str_Enums.JIGGY_AMOUNT_GV: lambda world, player: int(world.number_of_jiggies[player].value * 0.32),
    BK_Str_Enums.JIGGY_AMOUNT_MMM: lambda world, player: int(world.number_of_jiggies[player].value * 0.42),
    BK_Str_Enums.JIGGY_AMOUNT_RBB: lambda world, player: int(world.number_of_jiggies[player].value * 0.54),
    BK_Str_Enums.JIGGY_AMOUNT_CCW: lambda world, player: int(world.number_of_jiggies[player].value * 0.69),
    BK_Str_Enums.JIGGY_AMOUNT_FB: lambda world, player: int(world.number_of_jiggies[player].value * 0.94),
    BK_Str_Enums.JIGGY_AMOUNT_SP: lambda world, player: int(world.number_of_jiggies[player].value * 0.98),
}

NOTE_REQUIREMENT_DICT:dict = {
    BK_Str_Enums.NOTE_DOOR_AMOUNT_1: 50,
    BK_Str_Enums.NOTE_DOOR_AMOUNT_2: 180,
    BK_Str_Enums.NOTE_DOOR_AMOUNT_3: 260,
    BK_Str_Enums.NOTE_DOOR_AMOUNT_4: 350,
    BK_Str_Enums.NOTE_DOOR_AMOUNT_5: 450,
    BK_Str_Enums.NOTE_DOOR_AMOUNT_6: 640,
    BK_Str_Enums.NOTE_DOOR_AMOUNT_7: 765,
    BK_Str_Enums.NOTE_DOOR_AMOUNT_8: 810,
    BK_Str_Enums.NOTE_DOOR_AMOUNT_9: 882,
}