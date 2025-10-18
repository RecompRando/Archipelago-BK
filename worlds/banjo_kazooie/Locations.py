from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location, MultiWorld

from .Constants import *


class BKLocation(Location):
    game = "Banjo-Kazooie"


class BKLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable = lambda options: True
    locked_item: Optional[str] = None

location_data_table: Dict[str, BKLocationData] = {
    LOC_TRANSFORMATION_TERMITE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=None,
        locked_item=ITEM_TRANSFORMATION_TERMITE
    ),
    LOC_TRANSFORMATION_CROCODILE: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=None,
        locked_item=ITEM_TRANSFORMATION_CROCODILE
    ),
    LOC_TRANSFORMATION_WALRUS: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=None,
        locked_item=ITEM_TRANSFORMATION_WALRUS
    ),
    LOC_TRANSFORMATION_PUMPKIN: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=None,
        locked_item=ITEM_TRANSFORMATION_PUMPKIN
    ),
    LOC_TRANSFORMATION_BEE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=None,
        locked_item=ITEM_TRANSFORMATION_BEE
    ),
    LOC_JINJO_MM_BLUE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=None
    ),
    LOC_JINJO_MM_GREEN: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=None
    ),
    LOC_JINJO_MM_ORANGE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=None
    ),
    LOC_JINJO_MM_PURPLE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=None
    ),
    LOC_JINJO_MM_YELLOW: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=None
    ),
    LOC_JIGGY_GL_ENTRYWAY: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x00000033
    ),
    LOC_JIGGY_GL_ATOP_MUMBOS_MOUNTAIN: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x00000034
    ),
    LOC_JIGGY_GL_TTC_CANNON: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x00000036
    ),
    LOC_JIGGY_GL_EYE_SWITCHES: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x00000035
    ),
    LOC_JIGGY_GL_WITCHS_HAT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x00000037
    ),
    LOC_JIGGY_GL_ABOVE_FP: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x00000038
    ),
    LOC_JIGGY_GL_SARCOPHAGUS: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0000003A
    ),
    LOC_JIGGY_GL_GRUNTYS_EYE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x00000039
    ),
    LOC_JIGGY_GL_WATER_SWITCH: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0000003B
    ),
    LOC_JIGGY_GL_BEE_TREE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0000003C
    ),
    LOC_JIGGY_MM_CONGA_ORANGE_THROW: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000008
    ),
    LOC_JIGGY_MM_CHIMPY_ORANGE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000009
    ),
    LOC_JIGGY_MM_CONGA_ATTACK: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x0000000A
    ),
    LOC_JIGGY_MM_STONEHENGE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000006
    ),
    LOC_JIGGY_MM_HILLSIDE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000007
    ),
    LOC_JIGGY_MM_MUMBOS_HUT: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000003
    ),
    LOC_JIGGY_MM_TOTEM_POLE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000004
    ),
    LOC_JIGGY_MM_HUT: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000005
    ),
    LOC_JIGGY_MM_MOUNTAINTOP: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000002
    ),
    LOC_JIGGY_MM_JINJO: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x00000001
    ),
    LOC_JIGGY_TTC_NIPPER: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x00000012
    ),
    LOC_JIGGY_TTC_BLUBBER: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x00000014
    ),
    LOC_JIGGY_TTC_SANDCASTLE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x00000010
    ),
    LOC_JIGGY_TTC_SHOCK_SPRING: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0000000D
    ),
    LOC_JIGGY_TTC_X_MARK: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x00000011
    ),
    LOC_JIGGY_TTC_POOL: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0000000F
    ),
    LOC_JIGGY_TTC_CLIFFSIDE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0000000E
    ),
    LOC_JIGGY_TTC_LOCKUP: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x00000013
    ),
    LOC_JIGGY_TTC_LIGHTHOUSE: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0000000C
    ),
    LOC_JIGGY_TTC_JINJO: BKLocationData(
        region=RGN_TREASURE_TROVE_COVE,
        address=0x0000000B
    ),
    LOC_JIGGY_CC_CLANKER_RAISE: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x00000017
    ),
    LOC_JIGGY_CC_CLANKER_TAIL: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x00000018
    ),
    LOC_JIGGY_CC_CLANKER_BOLT: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x00000019
    ),
    LOC_JIGGY_CC_CLANKER_GOLD_TEETH: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0000001B
    ),
    LOC_JIGGY_CC_CLANKER_BLOWHOLE: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0000001D
    ),
    LOC_JIGGY_CC_WONDERWING: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0000001E
    ),
    LOC_JIGGY_CC_STOMACH_RINGS: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0000001C
    ),
    LOC_JIGGY_CC_SNIPPET: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x00000016
    ),
    LOC_JIGGY_CC_UNDERWATER_TUNNEL: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x0000001A
    ),
    LOC_JIGGY_CC_JINJO: BKLocationData(
        region=RGN_CLANKERS_CAVERN,
        address=0x00000015
    ),
    LOC_JIGGY_BGS_EGG: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000021
    ),
    LOC_JIGGY_BGS_CENTER_RACE: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000020
    ),
    LOC_JIGGY_BGS_FLIBBET: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000024
    ),
    LOC_JIGGY_BGS_TANKTUP: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000026
    ),
    LOC_JIGGY_BGS_TIPTUP: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000027
    ),
    LOC_JIGGY_BGS_HUT: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000023
    ),
    LOC_JIGGY_BGS_MUMBOS_HUT_RACE: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000025
    ),
    LOC_JIGGY_BGS_CROCTUS: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000022
    ),
    LOC_JIGGY_BGS_MR_VILE: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x00000028
    ),
    LOC_JIGGY_BGS_JINJO: BKLocationData(
        region=RGN_BUBBLEGLOOP_SWAMP,
        address=0x0000001F
    ),
    LOC_JIGGY_FP_SIR_SLUSH: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x00000031
    ),
    LOC_JIGGY_FP_SNOWMAN_PIPE: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0000002B
    ),
    LOC_JIGGY_FP_TOBOGGAN: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0000002A
    ),
    LOC_JIGGY_FP_SNOWMAN_BUTTONS: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0000002D
    ),
    LOC_JIGGY_FP_CHRISTMAS_TREE: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0000002F
    ),
    LOC_JIGGY_FP_WOZZA: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x00000032
    ),
    LOC_JIGGY_FP_PRESENTS: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0000002E
    ),
    LOC_JIGGY_FP_BOGGY_RACE_1: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x00000030
    ),
    LOC_JIGGY_FP_BOGGY_RACE_2: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x0000002C
    ),
    LOC_JIGGY_FP_JINJO: BKLocationData(
        region=RGN_FREEZEEZY_PEAK,
        address=0x00000029
    ),
    LOC_JIGGY_GV_JINXY: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0000003F
    ),
    LOC_JIGGY_GV_GRABBA: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0000003E
    ),
    LOC_JIGGY_GV_FLIP_PANELS: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000040
    ),
    LOC_JIGGY_GV_WATER_PYRAMID: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000042
    ),
    LOC_JIGGY_GV_ANCIENT_ONES: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000046
    ),
    LOC_JIGGY_GV_RUBEE: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000043
    ),
    LOC_JIGGY_GV_SANDYBUTT: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000041
    ),
    LOC_JIGGY_GV_GOBI: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000044
    ),
    LOC_JIGGY_GV_TRUNKER: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x00000045
    ),
    LOC_JIGGY_GV_JINJO: BKLocationData(
        region=RGN_GOBIS_VALLEY,
        address=0x0000003D
    ),
    LOC_JIGGY_MMM_NAPPER: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0000005D
    ),
    LOC_JIGGY_MMM_CELLAR: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0000005E
    ),
    LOC_JIGGY_MMM_TUMBLAR: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x00000062
    ),
    LOC_JIGGY_MMM_WELL: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0000005C
    ),
    LOC_JIGGY_MMM_FLOWERPOT: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x00000063
    ),
    LOC_JIGGY_MMM_CLOCK_TOWER: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0000005F
    ),
    LOC_JIGGY_MMM_MOTZAND: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x00000060
    ),
    LOC_JIGGY_MMM_LOGGO: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x00000064
    ),
    LOC_JIGGY_MMM_STORM_DRAIN: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x00000061
    ),
    LOC_JIGGY_MMM_JINJO: BKLocationData(
        region=RGN_MAD_MONSTER_MANSION,
        address=0x0000005B
    ),
    LOC_JIGGY_RBB_SMOKESTACK: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000055
    ),
    LOC_JIGGY_RBB_WHISTLE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000054
    ),
    LOC_JIGGY_RBB_WAREHOUSE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000052
    ),
    LOC_JIGGY_RBB_METAL_CAGE: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000059
    ),
    LOC_JIGGY_RBB_CAPTAINS_ROOM: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000058
    ),
    LOC_JIGGY_RBB_BOSS_BOOM_BOX: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000056
    ),
    LOC_JIGGY_RBB_SNORKEL: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000053
    ),
    LOC_JIGGY_RBB_ENGINE_ROOM: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x0000005A
    ),
    LOC_JIGGY_RBB_PROPELLER: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000057
    ),
    LOC_JIGGY_RBB_JINJO: BKLocationData(
        region=RGN_RUSTY_BUCKET_BAY,
        address=0x00000051
    ),
    "GLTF Secret Prize": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x05000000
    ),
    LOC_JIGGY_CCW_TREETOP_ROOM: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x00000050
    ),
    LOC_JIGGY_CCW_TREETOP_SNAREBEAR: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0000004F
    ),
    LOC_JIGGY_CCW_ZUBBA: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0000004C
    ),
    LOC_JIGGY_CCW_LEAVES: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0000004E
    ),
    LOC_JIGGY_CCW_CABIN: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x00000048
    ),
    LOC_JIGGY_CCW_GNAWTY: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0000004B
    ),
    LOC_JIGGY_CCW_PLANT: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0000004D
    ),
    LOC_JIGGY_CCW_NABNUTS: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x0000004A
    ),
    LOC_JIGGY_CCW_EYRIE: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x00000049
    ),
    LOC_JIGGY_CCW_JINJO: BKLocationData(
        region=RGN_CLICK_CLOCK_WOOD,
        address=0x00000047
    ),
    LOC_EMPTY_HONEYCOMB_SM_LOG: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000013
    ),
    LOC_EMPTY_HONEYCOMB_SM_WATERFALL: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000014
    ),
    LOC_EMPTY_HONEYCOMB_SM_TREE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000016
    ),
    LOC_EMPTY_HONEYCOMB_SM_UNDERWATER: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000015
    ),
    LOC_EMPTY_HONEYCOMB_SM_ROCK: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000018
    ),
    LOC_EMPTY_HONEYCOMB_SM_COLLIWOBBLE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000017
    ),
    LOC_EMPTY_HONEYCOMB_MM_HILLSIDE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000001
    ),
    LOC_EMPTY_HONEYCOMB_MM_TOTEM: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000002
    ),
    LOC_EMPTY_HONEYCOMB_TTC_UNDERWATER: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000003
    ),
    LOC_EMPTY_HONEYCOMB_TTC_CRATE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000004
    ),
    LOC_EMPTY_HONEYCOMB_CC_PIPE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000005
    ),
    LOC_EMPTY_HONEYCOMB_CC_GRATE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000006
    ),
    LOC_EMPTY_HONEYCOMB_BGS_TIPTOP_STAND: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000008
    ),
    LOC_EMPTY_HONEYCOMB_BGS_INSIDE_MUMBOS_HUT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000007
    ),
    LOC_EMPTY_HONEYCOMB_FP_SIR_SLUSH: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0200000A
    ),
    LOC_EMPTY_HONEYCOMB_FP_WOZZA: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000009
    ),
    LOC_EMPTY_HONEYCOMB_GV_CACTUS: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0200000B
    ),
    LOC_EMPTY_HONEYCOMB_GV_GOBI: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0200000C
    ),
    LOC_EMPTY_HONEYCOMB_MMM_CHURCH_RAFTER: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000011
    ),
    LOC_EMPTY_HONEYCOMB_MMM_FLOORBOARD: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000012
    ),
    LOC_EMPTY_HONEYCOMB_RBB_ENGINE_ROOM: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x02000010
    ),
    LOC_EMPTY_HONEYCOMB_RBB_WAREHOUSE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0200000F
    ),
    LOC_EMPTY_HONEYCOMB_CCW_WINTER_NABNUTS: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0200000E
    ),
    LOC_EMPTY_HONEYCOMB_CCW_WINTER_GNAWTY: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0200000D
    ),
    LOC_MUMBO_TOKEN_GL_RED_CAULDRON: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000051
    ),
    LOC_MUMBO_TOKEN_GL_DRAIN_PIPE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000053
    ),
    LOC_MUMBO_TOKEN_GL_CCW_PODIUM: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000052
    ),
    LOC_MUMBO_TOKEN_GL_ABOVE_CC_ENTRANCE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000054
    ),
    LOC_MUMBO_TOKEN_GL_BEHIND_SARCOPHAGUS: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000055
    ),
    LOC_MUMBO_TOKEN_GL_ABOVE_FP_ENTRANCE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000056
    ),
    LOC_MUMBO_TOKEN_GL_BEHIND_MUMBO: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000057
    ),
    LOC_MUMBO_TOKEN_GL_BELOW_RBB_ENTRANCE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000059
    ),
    LOC_MUMBO_TOKEN_GL_BY_MMM_PODIUM: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300005A
    ),
    LOC_MUMBO_TOKEN_GL_NEAR_CCW_PODIUM_SWITCH: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000058
    ),
    LOC_MUMBO_TOKEN_MM_BEHIND_PINK_JINJO: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x03000004
    ),
    LOC_MUMBO_TOKEN_MM_CHIMPY: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x03000001
    ),
    LOC_MUMBO_TOKEN_MM_STONEHENGE: BKLocationData(
        region=RGN_MUMBOS_MOUNTAIN,
        address=0x03000002
    ),
    LOC_MUMBO_TOKEN_MM_MUMBOS_HUT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000003
    ),
    LOC_MUMBO_TOKEN_MM_TERMITE_MOUND: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000005
    ),
    LOC_MUMBO_TOKEN_TTC_NIPPER: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300000F
    ),
    LOC_MUMBO_TOKEN_TTC_MAST: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000009
    ),
    LOC_MUMBO_TOKEN_TTC_HOLD: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000006
    ),
    LOC_MUMBO_TOKEN_TTC_SHOCK_SPRING: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300000E
    ),
    LOC_MUMBO_TOKEN_TTC_X_MARK: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300000C
    ),
    LOC_MUMBO_TOKEN_TTC_LOCKUP_LEFT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000007
    ),
    LOC_MUMBO_TOKEN_TTC_LOCKUP_RIGHT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000008
    ),
    LOC_MUMBO_TOKEN_TTC_POOL: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300000D
    ),
    LOC_MUMBO_TOKEN_TTC_CRATE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300000B
    ),
    LOC_MUMBO_TOKEN_TTC_LIGHTHOUSE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300000A
    ),
    LOC_MUMBO_TOKEN_CC_ENTRANCE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000011
    ),
    LOC_MUMBO_TOKEN_CC_CLANKER_TAIL: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000010
    ),
    LOC_MUMBO_TOKEN_CC_CLANKER_GOLD_TEETH: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000014
    ),
    LOC_MUMBO_TOKEN_CC_GRATE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000013
    ),
    LOC_MUMBO_TOKEN_CC_UNDERWATER_TUNNEL: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000012
    ),
    LOC_MUMBO_TOKEN_BGS_BEHIND_YELLOW_JINJO: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000018
    ),
    LOC_MUMBO_TOKEN_BGS_ATOP_CATTAIL: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000017
    ),
    LOC_MUMBO_TOKEN_BGS_CENTRAL_PLATFORM: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300001B
    ),
    LOC_MUMBO_TOKEN_BGS_INSIDE_TANKTUP: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300001C
    ),
    LOC_MUMBO_TOKEN_BGS_INSIDE_HUT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000019
    ),
    LOC_MUMBO_TOKEN_BGS_BEHIND_MUMBOS_HUT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300001A
    ),
    LOC_MUMBO_TOKEN_BGS_BEHIND_MUMBO: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300001E
    ),
    LOC_MUMBO_TOKEN_BGS_UNDER_HUTS_LEFT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000015
    ),
    LOC_MUMBO_TOKEN_BGS_UNDER_HUTS_RIGHT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000016
    ),
    LOC_MUMBO_TOKEN_BGS_INSIDE_MR_VILE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300001D
    ),
    LOC_MUMBO_TOKEN_FP_INSIDE_IGLOO: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000028
    ),
    LOC_MUMBO_TOKEN_FP_BEHIND_PRESENTS: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000021
    ),
    LOC_MUMBO_TOKEN_FP_ABOVE_HOUSE_FLIGHT_PAD: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000022
    ),
    LOC_MUMBO_TOKEN_FP_SIR_SLUSH_WOZZA: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000024
    ),
    LOC_MUMBO_TOKEN_FP_SIR_SLUSH_ISLAND: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000023
    ),
    LOC_MUMBO_TOKEN_FP_TOBOGGAN: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000026
    ),
    LOC_MUMBO_TOKEN_FP_LARGE_SNOWMAN_LEFT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300001F
    ),
    LOC_MUMBO_TOKEN_FP_LARGE_SNOWMAN_RIGHT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000020
    ),
    LOC_MUMBO_TOKEN_FP_UNDER_CHRISTMAS_TREE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000025
    ),
    LOC_MUMBO_TOKEN_FP_UNDERWATER: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000027
    ),
    LOC_MUMBO_TOKEN_GV_BEHIND_JINXY: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300002A
    ),
    LOC_MUMBO_TOKEN_GV_ABOVE_JINXYS_NOSE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000029
    ),
    LOC_MUMBO_TOKEN_GV_INSIDE_JINXY: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000032
    ),
    LOC_MUMBO_TOKEN_GV_OUTSIDE_WATER_PYRAMID_FRONT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300002D
    ),
    LOC_MUMBO_TOKEN_GV_FLIP_PANEL_PYRAMID: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300002E
    ),
    LOC_MUMBO_TOKEN_GV_MOAT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300002B
    ),
    LOC_MUMBO_TOKEN_GV_RUBEE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000031
    ),
    LOC_MUMBO_TOKEN_GV_ATOP_CENTRAL_PYRAMID: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300002C
    ),
    LOC_MUMBO_TOKEN_GV_CENTRAL_PYRAMID_POT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300002F
    ),
    LOC_MUMBO_TOKEN_GV_INSIDE_WATER_PYRAMID: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000030
    ),
    LOC_MUMBO_TOKEN_MMM_FIREPLACE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300003E
    ),
    LOC_MUMBO_TOKEN_MMM_CELLAR: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300003D
    ),
    LOC_MUMBO_TOKEN_MMM_LOGGO: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000074
    ),
    LOC_MUMBO_TOKEN_MMM_SINK: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000041
    ),
    LOC_MUMBO_TOKEN_MMM_MAZE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000037
    ),
    LOC_MUMBO_TOKEN_MMM_MAZE_HIDDEN_AREA: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000036
    ),
    LOC_MUMBO_TOKEN_MMM_SHACK_ROOF: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300003C
    ),
    LOC_MUMBO_TOKEN_MMM_WELL: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300003F
    ),
    LOC_MUMBO_TOKEN_MMM_BEHIND_GRAVE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000038
    ),
    LOC_MUMBO_TOKEN_MMM_CLOCK_TOWER: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000035
    ),
    LOC_MUMBO_TOKEN_MMM_CHURCH_CHAIR: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300003B
    ),
    LOC_MUMBO_TOKEN_MMM_CHURCH_RAFTER: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300003A
    ),
    LOC_MUMBO_TOKEN_MMM_NEAR_SHACK: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000034
    ),
    LOC_MUMBO_TOKEN_MMM_BEDROOM: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000040
    ),
    LOC_MUMBO_TOKEN_MMM_FOUNTAIN: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000039
    ),
    LOC_MUMBO_TOKEN_MMM_NEAR_FOUNTAIN: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000033
    ),
    LOC_MUMBO_TOKEN_RBB_TOLL_BRIDGE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000045
    ),
    LOC_MUMBO_TOKEN_RBB_LIFEBOAT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000044
    ),
    LOC_MUMBO_TOKEN_RBB_BEHIND_WITCH_SWITCH_TOWER: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000047
    ),
    LOC_MUMBO_TOKEN_RBB_BARRACKS: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300004A
    ),
    LOC_MUMBO_TOKEN_RBB_ENGINE_ROOM_ENTRY: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300004F
    ),
    LOC_MUMBO_TOKEN_RBB_ENGINE_ROOM_LEFT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300004D
    ),
    LOC_MUMBO_TOKEN_RBB_ENGINE_ROOM_RIGHT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300004E
    ),
    LOC_MUMBO_TOKEN_RBB_PERISCOPE_STOREROOM: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000050
    ),
    LOC_MUMBO_TOKEN_RBB_NAVIGATION_ROOM: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300004B
    ),
    LOC_MUMBO_TOKEN_RBB_OVEN: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300004C
    ),
    LOC_MUMBO_TOKEN_RBB_SMOKESTACK: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000042
    ),
    LOC_MUMBO_TOKEN_RBB_TOXIC_WASTE_DRUM: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000046
    ),
    LOC_MUMBO_TOKEN_RBB_SHIP_BOW: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000043
    ),
    LOC_MUMBO_TOKEN_RBB_LEFT_SHIPPING_CRATE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000048
    ),
    LOC_MUMBO_TOKEN_RBB_MIDDLE_SHIPPING_CRATE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000049
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_ENTRANCE_SNAREBEAR: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000060
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_GARDEN_SNAREBEAR: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300005F
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_TREETOP_ABOVE_MUMBOS_HUT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300005C
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_BEEHIVE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000061
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_CABIN: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300005B
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_NABNUTS_DRESSER: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000062
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_NEAR_EYRIES_NEST: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300005D
    ),
    LOC_MUMBO_TOKEN_CCW_SPRING_THORNS: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300005E
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_ENTRANCE_SNAREBEAR: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000065
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_GNAWTY: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000067
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_GARDEN: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000064
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_MUMBOS_HUT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000069
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_TREETOP_ABOVE_MUMBOS_HUT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000066
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_LEAVES: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000068
    ),
    LOC_MUMBO_TOKEN_CCW_SUMMER_AFTER_NABNUTS_HOUSE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000063
    ),
    LOC_MUMBO_TOKEN_CCW_FALL_ENTRANCE_SNAREBEAR: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300006B
    ),
    LOC_MUMBO_TOKEN_CCW_FALL_TREETOP_ABOVE_MUMBOS_HUT: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300006E
    ),
    LOC_MUMBO_TOKEN_CCW_FALL_LEAVES: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300006A
    ),
    LOC_MUMBO_TOKEN_CCW_FALL_CABIN: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300006D
    ),
    LOC_MUMBO_TOKEN_CCW_FALL_TREETOP_SNAREBEAR: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300006C
    ),
    LOC_MUMBO_TOKEN_CCW_WINTER_GARDEN: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0300006F
    ),
    LOC_MUMBO_TOKEN_CCW_WINTER_SIR_SLUSH: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000073
    ),
    LOC_MUMBO_TOKEN_CCW_WINTER_BEEHIVE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000071
    ),
    LOC_MUMBO_TOKEN_CCW_WINTER_NEAR_NABNUTS_HOUSE: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000072
    ),
    LOC_MUMBO_TOKEN_CCW_WINTER_BEHIND_LAKE_PLATFORM: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x03000070
    ),
    "MM Eggs Molehill": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x04000006
    ),
    "MM Talon Trot Molehill": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x04000010
    ),
    "MM Beak Buster Molehill": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x04000002
    ),
    "TTC Flight Molehill": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x04000009
    ),
    "TTC Shock Spring Jump Molehill": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0400000D
    ),
    "CC Wonderwing Molehill": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x04000012
    ),
    "BGS Stilt Stride Molehill": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0400000E
    ),
    "FP Beak Bomb Molehill": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x04000001
    ),
    "GV Turbo Talon Trot Molehill": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x04000011
    ),
    "SM Jump Molehill 1": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0001D5B5
    ),
    "SM Jump Molehill 2": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0001D5B6
    ),
    "SM Jump Molehill 3": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0001D5B7
    ),
    "SM Swim Molehill": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0001D5B8
    ),
    "SM Climb Molehill": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0001D5B9
    ),
    "SM Beak Barge Molehill": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0001D5BA
    ),
    "SM Attack Molehill 1": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0001D5BB
    ),
    "SM Attack Molehill 2": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0001D5BC
    ),
    "SM Attack Molehill 3": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0001D5BD
    ),
    # ~ "BLUEEGGS Cheato": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5BE
    # ~ ),
    # ~ "REDFEATHERS Cheato": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5BF
    # ~ ),
    # ~ "GOLDFEATHERS Cheato": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C0
    # ~ ),
    # ~ "Ice Key": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C1
    # ~ ),
    # ~ "Pink Egg": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C2
    # ~ ),
    # ~ "Blue Egg": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C3
    # ~ ),
    # ~ "Cyan Egg": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C4
    # ~ ),
    # ~ "Green Egg": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C5
    # ~ ),
    # ~ "Red Egg": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C6
    # ~ ),
    # ~ "Yellow Egg": BKLocationData(
        # ~ region=RGN_GRUNTILDAS_LAIR,
        # ~ address=0x0001D5C7
    # ~ ),
    "Mumbo's Mountain Note 1": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010218DD
    ),
    "Mumbo's Mountain Note 2": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021791
    ),
    "Mumbo's Mountain Note 3": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102165A
    ),
    "Mumbo's Mountain Note 4": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021537
    ),
    "Mumbo's Mountain Note 5": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102141F
    ),
    "Mumbo's Mountain Note 6": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021317
    ),
    "Mumbo's Mountain Note 7": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021226
    ),
    "Mumbo's Mountain Note 8": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010202F1
    ),
    "Mumbo's Mountain Note 9": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010202BB
    ),
    "Mumbo's Mountain Note 10": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01020281
    ),
    "Mumbo's Mountain Note 11": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01020216
    ),
    "Mumbo's Mountain Note 12": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102018E
    ),
    "Mumbo's Mountain Note 13": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102010A
    ),
    "Mumbo's Mountain Note 14": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01020098
    ),
    "Mumbo's Mountain Note 15": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010200CC
    ),
    "Mumbo's Mountain Note 16": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01020176
    ),
    "Mumbo's Mountain Note 17": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FAF7
    ),
    "Mumbo's Mountain Note 18": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FA8E
    ),
    "Mumbo's Mountain Note 19": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FA16
    ),
    "Mumbo's Mountain Note 20": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F9AB
    ),
    "Mumbo's Mountain Note 21": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F46F
    ),
    "Mumbo's Mountain Note 22": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F2DF
    ),
    "Mumbo's Mountain Note 23": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F145
    ),
    "Mumbo's Mountain Note 24": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F041
    ),
    "Mumbo's Mountain Note 25": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102EF58
    ),
    "Mumbo's Mountain Note 26": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102EF42
    ),
    "Mumbo's Mountain Note 27": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102EF46
    ),
    "Mumbo's Mountain Note 28": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102EFF6
    ),
    "Mumbo's Mountain Note 29": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F0C1
    ),
    "Mumbo's Mountain Note 30": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F236
    ),
    "Mumbo's Mountain Note 31": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F39E
    ),
    "Mumbo's Mountain Note 32": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F515
    ),
    "Mumbo's Mountain Note 33": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F68B
    ),
    "Mumbo's Mountain Note 34": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F777
    ),
    "Mumbo's Mountain Note 35": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FB90
    ),
    "Mumbo's Mountain Note 36": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FADF
    ),
    "Mumbo's Mountain Note 37": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FAF0
    ),
    "Mumbo's Mountain Note 38": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F808
    ),
    "Mumbo's Mountain Note 39": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F75B
    ),
    "Mumbo's Mountain Note 40": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F765
    ),
    "Mumbo's Mountain Note 41": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FDBB
    ),
    "Mumbo's Mountain Note 42": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FD10
    ),
    "Mumbo's Mountain Note 43": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FD11
    ),
    "Mumbo's Mountain Note 44": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F5CD
    ),
    "Mumbo's Mountain Note 45": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F5E1
    ),
    "Mumbo's Mountain Note 46": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F693
    ),
    "Mumbo's Mountain Note 47": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F38B
    ),
    "Mumbo's Mountain Note 48": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F37D
    ),
    "Mumbo's Mountain Note 49": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F435
    ),
    "Mumbo's Mountain Note 50": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FBAA
    ),
    "Mumbo's Mountain Note 51": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FBFA
    ),
    "Mumbo's Mountain Note 52": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FC5A
    ),
    "Mumbo's Mountain Note 53": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F9BF
    ),
    "Mumbo's Mountain Note 54": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102F9CA
    ),
    "Mumbo's Mountain Note 55": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102FA70
    ),
    "Mumbo's Mountain Note 56": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021D2D
    ),
    "Mumbo's Mountain Note 57": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021E20
    ),
    "Mumbo's Mountain Note 58": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021E1A
    ),
    "Mumbo's Mountain Note 59": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021BBB
    ),
    "Mumbo's Mountain Note 60": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021C6D
    ),
    "Mumbo's Mountain Note 61": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021C22
    ),
    "Mumbo's Mountain Note 62": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010214FE
    ),
    "Mumbo's Mountain Note 63": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102150B
    ),
    "Mumbo's Mountain Note 64": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102159C
    ),
    "Mumbo's Mountain Note 65": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102177B
    ),
    "Mumbo's Mountain Note 66": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021835
    ),
    "Mumbo's Mountain Note 67": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010217F4
    ),
    "Mumbo's Mountain Note 68": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021B3C
    ),
    "Mumbo's Mountain Note 69": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021BF5
    ),
    "Mumbo's Mountain Note 70": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021B12
    ),
    "Mumbo's Mountain Note 71": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01022186
    ),
    "Mumbo's Mountain Note 72": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01022094
    ),
    "Mumbo's Mountain Note 73": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102209A
    ),
    "Mumbo's Mountain Note 74": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010E0083
    ),
    "Mumbo's Mountain Note 75": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010EFF4D
    ),
    "Mumbo's Mountain Note 76": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010EFE4D
    ),
    "Mumbo's Mountain Note 77": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010EFE46
    ),
    "Mumbo's Mountain Note 78": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010211FA
    ),
    "Mumbo's Mountain Note 79": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010215C3
    ),
    "Mumbo's Mountain Note 80": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010219FA
    ),
    "Mumbo's Mountain Note 81": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01021799
    ),
    "Mumbo's Mountain Note 82": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01020F57
    ),
    "Mumbo's Mountain Note 83": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01020D88
    ),
    "Mumbo's Mountain Note 84": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01020069
    ),
    "Mumbo's Mountain Note 85": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102006A
    ),
    "Mumbo's Mountain Note 86": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102006B
    ),
    "Mumbo's Mountain Note 87": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102006C
    ),
    "Mumbo's Mountain Note 88": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0102006D
    ),
    "Mumbo's Mountain Note 89": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010208F5
    ),
    "Mumbo's Mountain Note 90": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01020923
    ),
    "Mumbo's Mountain Note 91": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01020952
    ),
    "Mumbo's Mountain Note 92": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01020CB1
    ),
    "Mumbo's Mountain Note 93": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01020D28
    ),
    "Mumbo's Mountain Note 94": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01020D9D
    ),
    "Mumbo's Mountain Note 95": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010C0374
    ),
    "Mumbo's Mountain Note 96": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010C0316
    ),
    "Mumbo's Mountain Note 97": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010C02AA
    ),
    "Mumbo's Mountain Note 98": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010C029A
    ),
    "Mumbo's Mountain Note 99": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010C02FA
    ),
    "Mumbo's Mountain Note 100": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010C0362
    ),
    "Treasure Trove Cove Note 1": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010719EA
    ),
    "Treasure Trove Cove Note 2": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071C0D
    ),
    "Treasure Trove Cove Note 3": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071E29
    ),
    "Treasure Trove Cove Note 4": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071C0A
    ),
    "Treasure Trove Cove Note 5": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070156
    ),
    "Treasure Trove Cove Note 6": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010702D8
    ),
    "Treasure Trove Cove Note 7": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107047C
    ),
    "Treasure Trove Cove Note 8": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071CC5
    ),
    "Treasure Trove Cove Note 9": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071CBE
    ),
    "Treasure Trove Cove Note 10": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071D71
    ),
    "Treasure Trove Cove Note 11": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071E14
    ),
    "Treasure Trove Cove Note 12": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071E2A
    ),
    "Treasure Trove Cove Note 13": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010A010A
    ),
    "Treasure Trove Cove Note 14": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010A0065
    ),
    "Treasure Trove Cove Note 15": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010A053B
    ),
    "Treasure Trove Cove Note 16": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010A0496
    ),
    "Treasure Trove Cove Note 17": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0106FB6F
    ),
    "Treasure Trove Cove Note 18": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0106FF9A
    ),
    "Treasure Trove Cove Note 19": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01060367
    ),
    "Treasure Trove Cove Note 20": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010604A3
    ),
    "Treasure Trove Cove Note 21": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010602BD
    ),
    "Treasure Trove Cove Note 22": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0106FF54
    ),
    "Treasure Trove Cove Note 23": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107EF90
    ),
    "Treasure Trove Cove Note 24": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107EDD8
    ),
    "Treasure Trove Cove Note 25": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107EC2A
    ),
    "Treasure Trove Cove Note 26": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107EA70
    ),
    "Treasure Trove Cove Note 27": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107EBE6
    ),
    "Treasure Trove Cove Note 28": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107EBB0
    ),
    "Treasure Trove Cove Note 29": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107EB78
    ),
    "Treasure Trove Cove Note 30": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107EB42
    ),
    "Treasure Trove Cove Note 31": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107EB41
    ),
    "Treasure Trove Cove Note 32": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107EB28
    ),
    "Treasure Trove Cove Note 33": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107EB10
    ),
    "Treasure Trove Cove Note 34": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107EAF5
    ),
    "Treasure Trove Cove Note 35": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107F2BD
    ),
    "Treasure Trove Cove Note 36": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107F3A0
    ),
    "Treasure Trove Cove Note 37": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107F3ED
    ),
    "Treasure Trove Cove Note 38": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010707ED
    ),
    "Treasure Trove Cove Note 39": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010708EE
    ),
    "Treasure Trove Cove Note 40": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010709F2
    ),
    "Treasure Trove Cove Note 41": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070EFD
    ),
    "Treasure Trove Cove Note 42": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070F48
    ),
    "Treasure Trove Cove Note 43": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070F98
    ),
    "Treasure Trove Cove Note 44": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010713D9
    ),
    "Treasure Trove Cove Note 45": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071495
    ),
    "Treasure Trove Cove Note 46": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071552
    ),
    "Treasure Trove Cove Note 47": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071B66
    ),
    "Treasure Trove Cove Note 48": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071C38
    ),
    "Treasure Trove Cove Note 49": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071D0A
    ),
    "Treasure Trove Cove Note 50": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071695
    ),
    "Treasure Trove Cove Note 51": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071712
    ),
    "Treasure Trove Cove Note 52": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107178F
    ),
    "Treasure Trove Cove Note 53": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071CC6
    ),
    "Treasure Trove Cove Note 54": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071F07
    ),
    "Treasure Trove Cove Note 55": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107213E
    ),
    "Treasure Trove Cove Note 56": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010720A2
    ),
    "Treasure Trove Cove Note 57": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071DB9
    ),
    "Treasure Trove Cove Note 58": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071BCB
    ),
    "Treasure Trove Cove Note 59": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071264
    ),
    "Treasure Trove Cove Note 60": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010712D2
    ),
    "Treasure Trove Cove Note 61": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010711F7
    ),
    "Treasure Trove Cove Note 62": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071176
    ),
    "Treasure Trove Cove Note 63": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070929
    ),
    "Treasure Trove Cove Note 64": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070945
    ),
    "Treasure Trove Cove Note 65": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070859
    ),
    "Treasure Trove Cove Note 66": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070852
    ),
    "Treasure Trove Cove Note 67": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070618
    ),
    "Treasure Trove Cove Note 68": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010707A2
    ),
    "Treasure Trove Cove Note 69": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070935
    ),
    "Treasure Trove Cove Note 70": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070D41
    ),
    "Treasure Trove Cove Note 71": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070D1C
    ),
    "Treasure Trove Cove Note 72": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070D04
    ),
    "Treasure Trove Cove Note 73": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070D02
    ),
    "Treasure Trove Cove Note 74": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070D05
    ),
    "Treasure Trove Cove Note 75": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01050174
    ),
    "Treasure Trove Cove Note 76": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010500B5
    ),
    "Treasure Trove Cove Note 77": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01050038
    ),
    "Treasure Trove Cove Note 78": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0105FFB7
    ),
    "Treasure Trove Cove Note 79": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0105FA71
    ),
    "Treasure Trove Cove Note 80": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0105F9EF
    ),
    "Treasure Trove Cove Note 81": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0105F970
    ),
    "Treasure Trove Cove Note 82": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0105F8E9
    ),
    "Treasure Trove Cove Note 83": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070CC7
    ),
    "Treasure Trove Cove Note 84": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070CF9
    ),
    "Treasure Trove Cove Note 85": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070C74
    ),
    "Treasure Trove Cove Note 86": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070C17
    ),
    "Treasure Trove Cove Note 87": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070BE7
    ),
    "Treasure Trove Cove Note 88": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107FB5D
    ),
    "Treasure Trove Cove Note 89": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107FA87
    ),
    "Treasure Trove Cove Note 90": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107F9AD
    ),
    "Treasure Trove Cove Note 91": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107F894
    ),
    "Treasure Trove Cove Note 92": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070828
    ),
    "Treasure Trove Cove Note 93": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070CA5
    ),
    "Treasure Trove Cove Note 94": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070BD3
    ),
    "Treasure Trove Cove Note 95": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01070BA4
    ),
    "Treasure Trove Cove Note 96": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071625
    ),
    "Treasure Trove Cove Note 97": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0107155A
    ),
    "Treasure Trove Cove Note 98": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01071693
    ),
    "Treasure Trove Cove Note 99": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010717FF
    ),
    "Treasure Trove Cove Note 100": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010717C5
    ),
    "Clanker's Cavern Note 1": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010BF1CA
    ),
    "Clanker's Cavern Note 2": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010BF090
    ),
    "Clanker's Cavern Note 3": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010BF19E
    ),
    "Clanker's Cavern Note 4": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010BF02D
    ),
    "Clanker's Cavern Note 5": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010BFDE3
    ),
    "Clanker's Cavern Note 6": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010BFB60
    ),
    "Clanker's Cavern Note 7": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010BFBD0
    ),
    "Clanker's Cavern Note 8": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010BF89A
    ),
    "Clanker's Cavern Note 9": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B0105
    ),
    "Clanker's Cavern Note 10": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B01B4
    ),
    "Clanker's Cavern Note 11": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B03D5
    ),
    "Clanker's Cavern Note 12": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B05E3
    ),
    "Clanker's Cavern Note 13": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B0740
    ),
    "Clanker's Cavern Note 14": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B0915
    ),
    "Clanker's Cavern Note 15": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B1E02
    ),
    "Clanker's Cavern Note 16": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B203C
    ),
    "Clanker's Cavern Note 17": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B225A
    ),
    "Clanker's Cavern Note 18": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B240B
    ),
    "Clanker's Cavern Note 19": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B25C1
    ),
    "Clanker's Cavern Note 20": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B271B
    ),
    "Clanker's Cavern Note 21": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B286D
    ),
    "Clanker's Cavern Note 22": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B42C5
    ),
    "Clanker's Cavern Note 23": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B45A7
    ),
    "Clanker's Cavern Note 24": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B47DB
    ),
    "Clanker's Cavern Note 25": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B48DE
    ),
    "Clanker's Cavern Note 26": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B4350
    ),
    "Clanker's Cavern Note 27": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B4069
    ),
    "Clanker's Cavern Note 28": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B3E39
    ),
    "Clanker's Cavern Note 29": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B3D0D
    ),
    "Clanker's Cavern Note 30": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B0E1D
    ),
    "Clanker's Cavern Note 31": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B1023
    ),
    "Clanker's Cavern Note 32": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B0E18
    ),
    "Clanker's Cavern Note 33": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B093B
    ),
    "Clanker's Cavern Note 34": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B045C
    ),
    "Clanker's Cavern Note 35": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B0251
    ),
    "Clanker's Cavern Note 36": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B0457
    ),
    "Clanker's Cavern Note 37": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B0940
    ),
    "Clanker's Cavern Note 38": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B1D13
    ),
    "Clanker's Cavern Note 39": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B1E5B
    ),
    "Clanker's Cavern Note 40": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B1F91
    ),
    "Clanker's Cavern Note 41": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B20C9
    ),
    "Clanker's Cavern Note 42": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B2525
    ),
    "Clanker's Cavern Note 43": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B2621
    ),
    "Clanker's Cavern Note 44": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B2715
    ),
    "Clanker's Cavern Note 45": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B2820
    ),
    "Clanker's Cavern Note 46": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B2933
    ),
    "Clanker's Cavern Note 47": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B2A6F
    ),
    "Clanker's Cavern Note 48": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B37B3
    ),
    "Clanker's Cavern Note 49": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B3854
    ),
    "Clanker's Cavern Note 50": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B3905
    ),
    "Clanker's Cavern Note 51": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B389B
    ),
    "Clanker's Cavern Note 52": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B382E
    ),
    "Clanker's Cavern Note 53": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B3562
    ),
    "Clanker's Cavern Note 54": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B337E
    ),
    "Clanker's Cavern Note 55": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B318D
    ),
    "Clanker's Cavern Note 56": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B2F4D
    ),
    "Clanker's Cavern Note 57": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B2D2A
    ),
    "Clanker's Cavern Note 58": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B1E22
    ),
    "Clanker's Cavern Note 59": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B1DB7
    ),
    "Clanker's Cavern Note 60": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B1BC9
    ),
    "Clanker's Cavern Note 61": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B19D7
    ),
    "Clanker's Cavern Note 62": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0122F5C5
    ),
    "Clanker's Cavern Note 63": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0122F600
    ),
    "Clanker's Cavern Note 64": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0122F700
    ),
    "Clanker's Cavern Note 65": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0122F864
    ),
    "Clanker's Cavern Note 66": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0122FA97
    ),
    "Clanker's Cavern Note 67": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01220E76
    ),
    "Clanker's Cavern Note 68": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01220CD5
    ),
    "Clanker's Cavern Note 69": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01220A0D
    ),
    "Clanker's Cavern Note 70": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01221820
    ),
    "Clanker's Cavern Note 71": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01221BA2
    ),
    "Clanker's Cavern Note 72": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01221EAF
    ),
    "Clanker's Cavern Note 73": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0122205D
    ),
    "Clanker's Cavern Note 74": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01221F6C
    ),
    "Clanker's Cavern Note 75": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01221BF9
    ),
    "Clanker's Cavern Note 76": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0122188C
    ),
    "Clanker's Cavern Note 77": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01221640
    ),
    "Clanker's Cavern Note 78": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012104A1
    ),
    "Clanker's Cavern Note 79": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01210249
    ),
    "Clanker's Cavern Note 80": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0121FFF1
    ),
    "Clanker's Cavern Note 81": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0121FD99
    ),
    "Clanker's Cavern Note 82": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0121FB41
    ),
    "Clanker's Cavern Note 83": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0121F8E9
    ),
    "Clanker's Cavern Note 84": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B26C7
    ),
    "Clanker's Cavern Note 85": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B284D
    ),
    "Clanker's Cavern Note 86": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B296F
    ),
    "Clanker's Cavern Note 87": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B2A91
    ),
    "Clanker's Cavern Note 88": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B3842
    ),
    "Clanker's Cavern Note 89": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B3818
    ),
    "Clanker's Cavern Note 90": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B37FF
    ),
    "Clanker's Cavern Note 91": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B37DE
    ),
    "Clanker's Cavern Note 92": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B37B4
    ),
    "Clanker's Cavern Note 93": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B1DAA
    ),
    "Clanker's Cavern Note 94": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010B13A5
    ),
    "Clanker's Cavern Note 95": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012304AB
    ),
    "Clanker's Cavern Note 96": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01230276
    ),
    "Clanker's Cavern Note 97": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01230037
    ),
    "Clanker's Cavern Note 98": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0123FDF8
    ),
    "Clanker's Cavern Note 99": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0123FBB4
    ),
    "Clanker's Cavern Note 100": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0123F8D5
    ),
    "Bubblegloop Swamp Note 1": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0BFD
    ),
    "Bubblegloop Swamp Note 2": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0B3C
    ),
    "Bubblegloop Swamp Note 3": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0A74
    ),
    "Bubblegloop Swamp Note 4": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0972
    ),
    "Bubblegloop Swamp Note 5": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0877
    ),
    "Bubblegloop Swamp Note 6": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0479
    ),
    "Bubblegloop Swamp Note 7": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D03AB
    ),
    "Bubblegloop Swamp Note 8": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D02DB
    ),
    "Bubblegloop Swamp Note 9": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DFA82
    ),
    "Bubblegloop Swamp Note 10": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DF972
    ),
    "Bubblegloop Swamp Note 11": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DF866
    ),
    "Bubblegloop Swamp Note 12": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D09C5
    ),
    "Bubblegloop Swamp Note 13": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0AF9
    ),
    "Bubblegloop Swamp Note 14": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0C31
    ),
    "Bubblegloop Swamp Note 15": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D1581
    ),
    "Bubblegloop Swamp Note 16": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D1B5A
    ),
    "Bubblegloop Swamp Note 17": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D1B4B
    ),
    "Bubblegloop Swamp Note 18": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D1568
    ),
    "Bubblegloop Swamp Note 19": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D03BF
    ),
    "Bubblegloop Swamp Note 20": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D03DC
    ),
    "Bubblegloop Swamp Note 21": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D03F7
    ),
    "Bubblegloop Swamp Note 22": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DF94E
    ),
    "Bubblegloop Swamp Note 23": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DF80B
    ),
    "Bubblegloop Swamp Note 24": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DF6C7
    ),
    "Bubblegloop Swamp Note 25": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DF092
    ),
    "Bubblegloop Swamp Note 26": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DEF66
    ),
    "Bubblegloop Swamp Note 27": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DEE9E
    ),
    "Bubblegloop Swamp Note 28": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DEE01
    ),
    "Bubblegloop Swamp Note 29": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DED8A
    ),
    "Bubblegloop Swamp Note 30": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DF93A
    ),
    "Bubblegloop Swamp Note 31": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DFBB7
    ),
    "Bubblegloop Swamp Note 32": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DFE35
    ),
    "Bubblegloop Swamp Note 33": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DFF73
    ),
    "Bubblegloop Swamp Note 34": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D00A7
    ),
    "Bubblegloop Swamp Note 35": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DFB93
    ),
    "Bubblegloop Swamp Note 36": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DFB59
    ),
    "Bubblegloop Swamp Note 37": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DFCDE
    ),
    "Bubblegloop Swamp Note 38": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DFEA5
    ),
    "Bubblegloop Swamp Note 39": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0049
    ),
    "Bubblegloop Swamp Note 40": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0425
    ),
    "Bubblegloop Swamp Note 41": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0615
    ),
    "Bubblegloop Swamp Note 42": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0765
    ),
    "Bubblegloop Swamp Note 43": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0A47
    ),
    "Bubblegloop Swamp Note 44": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0ED7
    ),
    "Bubblegloop Swamp Note 45": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D103C
    ),
    "Bubblegloop Swamp Note 46": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0FF5
    ),
    "Bubblegloop Swamp Note 47": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0E32
    ),
    "Bubblegloop Swamp Note 48": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0CD1
    ),
    "Bubblegloop Swamp Note 49": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0D4C
    ),
    "Bubblegloop Swamp Note 50": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0F2E
    ),
    "Bubblegloop Swamp Note 51": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0C88
    ),
    "Bubblegloop Swamp Note 52": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0AF5
    ),
    "Bubblegloop Swamp Note 53": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D09DF
    ),
    "Bubblegloop Swamp Note 54": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0727
    ),
    "Bubblegloop Swamp Note 55": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0111FCFE
    ),
    "Bubblegloop Swamp Note 56": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0111FC02
    ),
    "Bubblegloop Swamp Note 57": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0111FB29
    ),
    "Bubblegloop Swamp Note 58": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01110301
    ),
    "Bubblegloop Swamp Note 59": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011103FE
    ),
    "Bubblegloop Swamp Note 60": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011104D9
    ),
    "Bubblegloop Swamp Note 61": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D006C
    ),
    "Bubblegloop Swamp Note 62": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D006D
    ),
    "Bubblegloop Swamp Note 63": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0069
    ),
    "Bubblegloop Swamp Note 64": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D006A
    ),
    "Bubblegloop Swamp Note 65": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D006B
    ),
    "Bubblegloop Swamp Note 66": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DD277
    ),
    "Bubblegloop Swamp Note 67": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DD2DB
    ),
    "Bubblegloop Swamp Note 68": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DD33F
    ),
    "Bubblegloop Swamp Note 69": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DD1DC
    ),
    "Bubblegloop Swamp Note 70": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DCF92
    ),
    "Bubblegloop Swamp Note 71": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DCD27
    ),
    "Bubblegloop Swamp Note 72": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DCA51
    ),
    "Bubblegloop Swamp Note 73": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DC77B
    ),
    "Bubblegloop Swamp Note 74": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DDDC7
    ),
    "Bubblegloop Swamp Note 75": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DE598
    ),
    "Bubblegloop Swamp Note 76": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DE1AA
    ),
    "Bubblegloop Swamp Note 77": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DE1BD
    ),
    "Bubblegloop Swamp Note 78": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DD9DC
    ),
    "Bubblegloop Swamp Note 79": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DD7E8
    ),
    "Bubblegloop Swamp Note 80": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DD9D7
    ),
    "Bubblegloop Swamp Note 81": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DD214
    ),
    "Bubblegloop Swamp Note 82": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DD20F
    ),
    "Bubblegloop Swamp Note 83": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DD020
    ),
    "Bubblegloop Swamp Note 84": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DD018
    ),
    "Bubblegloop Swamp Note 85": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010DDA0B
    ),
    "Bubblegloop Swamp Note 86": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0110F980
    ),
    "Bubblegloop Swamp Note 87": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0110F9C3
    ),
    "Bubblegloop Swamp Note 88": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0110FA33
    ),
    "Bubblegloop Swamp Note 89": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0110F8A4
    ),
    "Bubblegloop Swamp Note 90": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0110F80F
    ),
    "Bubblegloop Swamp Note 91": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0110F74F
    ),
    "Bubblegloop Swamp Note 92": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D01F9
    ),
    "Bubblegloop Swamp Note 93": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D02D7
    ),
    "Bubblegloop Swamp Note 94": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D01F6
    ),
    "Bubblegloop Swamp Note 95": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D011E
    ),
    "Bubblegloop Swamp Note 96": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0AE3
    ),
    "Bubblegloop Swamp Note 97": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0C2E
    ),
    "Bubblegloop Swamp Note 98": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0D77
    ),
    "Bubblegloop Swamp Note 99": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0DAE
    ),
    "Bubblegloop Swamp Note 100": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x010D0DE2
    ),
    "Freezeezy Peak Note 1": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01272B34
    ),
    "Freezeezy Peak Note 2": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127280F
    ),
    "Freezeezy Peak Note 3": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127248D
    ),
    "Freezeezy Peak Note 4": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012720D4
    ),
    "Freezeezy Peak Note 5": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271CF4
    ),
    "Freezeezy Peak Note 6": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271966
    ),
    "Freezeezy Peak Note 7": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271578
    ),
    "Freezeezy Peak Note 8": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271134
    ),
    "Freezeezy Peak Note 9": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01270D17
    ),
    "Freezeezy Peak Note 10": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01270C30
    ),
    "Freezeezy Peak Note 11": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01270D1E
    ),
    "Freezeezy Peak Note 12": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01270A2F
    ),
    "Freezeezy Peak Note 13": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01270544
    ),
    "Freezeezy Peak Note 14": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127010C
    ),
    "Freezeezy Peak Note 15": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127EFAE
    ),
    "Freezeezy Peak Note 16": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127EED2
    ),
    "Freezeezy Peak Note 17": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127EDF8
    ),
    "Freezeezy Peak Note 18": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127ED1B
    ),
    "Freezeezy Peak Note 19": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127EB8A
    ),
    "Freezeezy Peak Note 20": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127EC9C
    ),
    "Freezeezy Peak Note 21": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127EABA
    ),
    "Freezeezy Peak Note 22": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127E9A8
    ),
    "Freezeezy Peak Note 23": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127124C
    ),
    "Freezeezy Peak Note 24": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012711FF
    ),
    "Freezeezy Peak Note 25": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012711C0
    ),
    "Freezeezy Peak Note 26": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271E33
    ),
    "Freezeezy Peak Note 27": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271F07
    ),
    "Freezeezy Peak Note 28": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271FF9
    ),
    "Freezeezy Peak Note 29": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01272329
    ),
    "Freezeezy Peak Note 30": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012724F2
    ),
    "Freezeezy Peak Note 31": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012725F6
    ),
    "Freezeezy Peak Note 32": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01272521
    ),
    "Freezeezy Peak Note 33": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127036F
    ),
    "Freezeezy Peak Note 34": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012705FD
    ),
    "Freezeezy Peak Note 35": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012702A3
    ),
    "Freezeezy Peak Note 36": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127000D
    ),
    "Freezeezy Peak Note 37": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01270077
    ),
    "Freezeezy Peak Note 38": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127FAD2
    ),
    "Freezeezy Peak Note 39": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127FA70
    ),
    "Freezeezy Peak Note 40": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127F770
    ),
    "Freezeezy Peak Note 41": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127F556
    ),
    "Freezeezy Peak Note 42": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127F848
    ),
    "Freezeezy Peak Note 43": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0153FF41
    ),
    "Freezeezy Peak Note 44": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0153FE19
    ),
    "Freezeezy Peak Note 45": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0153FE1C
    ),
    "Freezeezy Peak Note 46": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0153FF3E
    ),
    "Freezeezy Peak Note 47": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01530137
    ),
    "Freezeezy Peak Note 48": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0153037B
    ),
    "Freezeezy Peak Note 49": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01530571
    ),
    "Freezeezy Peak Note 50": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01530691
    ),
    "Freezeezy Peak Note 51": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0153068D
    ),
    "Freezeezy Peak Note 52": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01530575
    ),
    "Freezeezy Peak Note 53": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01530376
    ),
    "Freezeezy Peak Note 54": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01530132
    ),
    "Freezeezy Peak Note 55": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127E546
    ),
    "Freezeezy Peak Note 56": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127E4F4
    ),
    "Freezeezy Peak Note 57": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127E368
    ),
    "Freezeezy Peak Note 58": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127E109
    ),
    "Freezeezy Peak Note 59": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127E920
    ),
    "Freezeezy Peak Note 60": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127ECDC
    ),
    "Freezeezy Peak Note 61": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127F328
    ),
    "Freezeezy Peak Note 62": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127F59A
    ),
    "Freezeezy Peak Note 63": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127F6CF
    ),
    "Freezeezy Peak Note 64": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127FC28
    ),
    "Freezeezy Peak Note 65": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127FE0E
    ),
    "Freezeezy Peak Note 66": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127FAB4
    ),
    "Freezeezy Peak Note 67": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127FAC3
    ),
    "Freezeezy Peak Note 68": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127000F
    ),
    "Freezeezy Peak Note 69": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127042F
    ),
    "Freezeezy Peak Note 70": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012707C0
    ),
    "Freezeezy Peak Note 71": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01270AFE
    ),
    "Freezeezy Peak Note 72": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01270B91
    ),
    "Freezeezy Peak Note 73": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01270E9C
    ),
    "Freezeezy Peak Note 74": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012710E4
    ),
    "Freezeezy Peak Note 75": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01270F98
    ),
    "Freezeezy Peak Note 76": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271584
    ),
    "Freezeezy Peak Note 77": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271700
    ),
    "Freezeezy Peak Note 78": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01272397
    ),
    "Freezeezy Peak Note 79": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012724CC
    ),
    "Freezeezy Peak Note 80": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012721F5
    ),
    "Freezeezy Peak Note 81": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271CBC
    ),
    "Freezeezy Peak Note 82": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271886
    ),
    "Freezeezy Peak Note 83": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271708
    ),
    "Freezeezy Peak Note 84": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012719E1
    ),
    "Freezeezy Peak Note 85": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271F28
    ),
    "Freezeezy Peak Note 86": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0148FF9A
    ),
    "Freezeezy Peak Note 87": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0148FEA7
    ),
    "Freezeezy Peak Note 88": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0148017A
    ),
    "Freezeezy Peak Note 89": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01480377
    ),
    "Freezeezy Peak Note 90": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01480463
    ),
    "Freezeezy Peak Note 91": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01480195
    ),
    "Freezeezy Peak Note 92": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127134D
    ),
    "Freezeezy Peak Note 93": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271157
    ),
    "Freezeezy Peak Note 94": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271119
    ),
    "Freezeezy Peak Note 95": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127117F
    ),
    "Freezeezy Peak Note 96": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0127144B
    ),
    "Freezeezy Peak Note 97": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012716DF
    ),
    "Freezeezy Peak Note 98": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271A5E
    ),
    "Freezeezy Peak Note 99": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271CA8
    ),
    "Freezeezy Peak Note 100": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01271BE6
    ),
    "Gobi's Valley Note 1": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011222F7
    ),
    "Gobi's Valley Note 2": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01122157
    ),
    "Gobi's Valley Note 3": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121F98
    ),
    "Gobi's Valley Note 4": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121DAC
    ),
    "Gobi's Valley Note 5": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121BB1
    ),
    "Gobi's Valley Note 6": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011214C4
    ),
    "Gobi's Valley Note 7": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011214B7
    ),
    "Gobi's Valley Note 8": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121345
    ),
    "Gobi's Valley Note 9": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120FF3
    ),
    "Gobi's Valley Note 10": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120FE7
    ),
    "Gobi's Valley Note 11": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120E5A
    ),
    "Gobi's Valley Note 12": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112F414
    ),
    "Gobi's Valley Note 13": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112F377
    ),
    "Gobi's Valley Note 14": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112F2EC
    ),
    "Gobi's Valley Note 15": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112F261
    ),
    "Gobi's Valley Note 16": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112F1DD
    ),
    "Gobi's Valley Note 17": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120FAB
    ),
    "Gobi's Valley Note 18": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120F4C
    ),
    "Gobi's Valley Note 19": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011213C8
    ),
    "Gobi's Valley Note 20": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121428
    ),
    "Gobi's Valley Note 21": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121577
    ),
    "Gobi's Valley Note 22": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121A86
    ),
    "Gobi's Valley Note 23": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121590
    ),
    "Gobi's Valley Note 24": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121081
    ),
    "Gobi's Valley Note 25": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121740
    ),
    "Gobi's Valley Note 26": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121999
    ),
    "Gobi's Valley Note 27": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121E58
    ),
    "Gobi's Valley Note 28": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121D0A
    ),
    "Gobi's Valley Note 29": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121BBF
    ),
    "Gobi's Valley Note 30": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121A75
    ),
    "Gobi's Valley Note 31": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120D2E
    ),
    "Gobi's Valley Note 32": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120825
    ),
    "Gobi's Valley Note 33": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112030D
    ),
    "Gobi's Valley Note 34": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112FF80
    ),
    "Gobi's Valley Note 35": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112FBF2
    ),
    "Gobi's Valley Note 36": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112FBDF
    ),
    "Gobi's Valley Note 37": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112FBE3
    ),
    "Gobi's Valley Note 38": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112FF62
    ),
    "Gobi's Valley Note 39": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011202DF
    ),
    "Gobi's Valley Note 40": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120395
    ),
    "Gobi's Valley Note 41": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120014
    ),
    "Gobi's Valley Note 42": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112FBC2
    ),
    "Gobi's Valley Note 43": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011205B3
    ),
    "Gobi's Valley Note 44": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112FDB5
    ),
    "Gobi's Valley Note 45": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112FBA1
    ),
    "Gobi's Valley Note 46": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011206B7
    ),
    "Gobi's Valley Note 47": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120B1A
    ),
    "Gobi's Valley Note 48": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120F3E
    ),
    "Gobi's Valley Note 49": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121390
    ),
    "Gobi's Valley Note 50": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011217D0
    ),
    "Gobi's Valley Note 51": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011217DE
    ),
    "Gobi's Valley Note 52": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011217F2
    ),
    "Gobi's Valley Note 53": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01121802
    ),
    "Gobi's Valley Note 54": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011A058C
    ),
    "Gobi's Valley Note 55": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011AEFC0
    ),
    "Gobi's Valley Note 56": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011AF5F7
    ),
    "Gobi's Valley Note 57": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011A0BCA
    ),
    "Gobi's Valley Note 58": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011A05EF
    ),
    "Gobi's Valley Note 59": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011A03BC
    ),
    "Gobi's Valley Note 60": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011A015B
    ),
    "Gobi's Valley Note 61": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112E5B4
    ),
    "Gobi's Valley Note 62": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112E76B
    ),
    "Gobi's Valley Note 63": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112E932
    ),
    "Gobi's Valley Note 64": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112EAE4
    ),
    "Gobi's Valley Note 65": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112EC98
    ),
    "Gobi's Valley Note 66": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112EC45
    ),
    "Gobi's Valley Note 67": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112EBF4
    ),
    "Gobi's Valley Note 68": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112EB91
    ),
    "Gobi's Valley Note 69": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112EA00
    ),
    "Gobi's Valley Note 70": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112E870
    ),
    "Gobi's Valley Note 71": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112E6D0
    ),
    "Gobi's Valley Note 72": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0114165E
    ),
    "Gobi's Valley Note 73": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0114124C
    ),
    "Gobi's Valley Note 74": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0114111F
    ),
    "Gobi's Valley Note 75": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0114F95C
    ),
    "Gobi's Valley Note 76": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0114F61C
    ),
    "Gobi's Valley Note 77": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0114F192
    ),
    "Gobi's Valley Note 78": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0114F089
    ),
    "Gobi's Valley Note 79": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011502DD
    ),
    "Gobi's Valley Note 80": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0115FD02
    ),
    "Gobi's Valley Note 81": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0115FD13
    ),
    "Gobi's Valley Note 82": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011502DB
    ),
    "Gobi's Valley Note 83": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112FCB3
    ),
    "Gobi's Valley Note 84": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112FF42
    ),
    "Gobi's Valley Note 85": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120416
    ),
    "Gobi's Valley Note 86": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120AC2
    ),
    "Gobi's Valley Note 87": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01120884
    ),
    "Gobi's Valley Note 88": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0112046C
    ),
    "Gobi's Valley Note 89": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01130013
    ),
    "Gobi's Valley Note 90": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01130397
    ),
    "Gobi's Valley Note 91": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01130014
    ),
    "Gobi's Valley Note 92": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0113FC8F
    ),
    "Gobi's Valley Note 93": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01160538
    ),
    "Gobi's Valley Note 94": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0116049F
    ),
    "Gobi's Valley Note 95": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0116FFBF
    ),
    "Gobi's Valley Note 96": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0116FE82
    ),
    "Gobi's Valley Note 97": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0116FAA1
    ),
    "Gobi's Valley Note 98": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0116FA6C
    ),
    "Gobi's Valley Note 99": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0116FCEF
    ),
    "Gobi's Valley Note 100": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0116FE1B
    ),
    "Mad Monster Mansion Note 1": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B0AB6
    ),
    "Mad Monster Mansion Note 2": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B0BE5
    ),
    "Mad Monster Mansion Note 3": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B0DF9
    ),
    "Mad Monster Mansion Note 4": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B0E2D
    ),
    "Mad Monster Mansion Note 5": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BFEE0
    ),
    "Mad Monster Mansion Note 6": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B0195
    ),
    "Mad Monster Mansion Note 7": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF975
    ),
    "Mad Monster Mansion Note 8": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF826
    ),
    "Mad Monster Mansion Note 9": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF335
    ),
    "Mad Monster Mansion Note 10": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF299
    ),
    "Mad Monster Mansion Note 11": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B16C0
    ),
    "Mad Monster Mansion Note 12": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B1AE2
    ),
    "Mad Monster Mansion Note 13": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B1EF7
    ),
    "Mad Monster Mansion Note 14": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B1AD4
    ),
    "Mad Monster Mansion Note 15": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF254
    ),
    "Mad Monster Mansion Note 16": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF1A4
    ),
    "Mad Monster Mansion Note 17": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF0F5
    ),
    "Mad Monster Mansion Note 18": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BFC2F
    ),
    "Mad Monster Mansion Note 19": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B07DF
    ),
    "Mad Monster Mansion Note 20": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B1311
    ),
    "Mad Monster Mansion Note 21": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B0764
    ),
    "Mad Monster Mansion Note 22": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012605F1
    ),
    "Mad Monster Mansion Note 23": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012603FF
    ),
    "Mad Monster Mansion Note 24": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0126020A
    ),
    "Mad Monster Mansion Note 25": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0126FCDB
    ),
    "Mad Monster Mansion Note 26": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0126FA3A
    ),
    "Mad Monster Mansion Note 27": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0126FC49
    ),
    "Mad Monster Mansion Note 28": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0126FE3C
    ),
    "Mad Monster Mansion Note 29": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0126002F
    ),
    "Mad Monster Mansion Note 30": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B0AB3
    ),
    "Mad Monster Mansion Note 31": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B12DE
    ),
    "Mad Monster Mansion Note 32": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B0B96
    ),
    "Mad Monster Mansion Note 33": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B0363
    ),
    "Mad Monster Mansion Note 34": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0129FDBD
    ),
    "Mad Monster Mansion Note 35": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0129FDF3
    ),
    "Mad Monster Mansion Note 36": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0129FE3E
    ),
    "Mad Monster Mansion Note 37": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0129FE89
    ),
    "Mad Monster Mansion Note 38": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0129002F
    ),
    "Mad Monster Mansion Note 39": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01290113
    ),
    "Mad Monster Mansion Note 40": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0129015E
    ),
    "Mad Monster Mansion Note 41": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012901A9
    ),
    "Mad Monster Mansion Note 42": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012901A2
    ),
    "Mad Monster Mansion Note 43": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012D038B
    ),
    "Mad Monster Mansion Note 44": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012D0363
    ),
    "Mad Monster Mansion Note 45": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012D02C3
    ),
    "Mad Monster Mansion Note 46": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012D02E4
    ),
    "Mad Monster Mansion Note 47": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011D04AF
    ),
    "Mad Monster Mansion Note 48": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011D05A9
    ),
    "Mad Monster Mansion Note 49": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011D06A4
    ),
    "Mad Monster Mansion Note 50": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011D079E
    ),
    "Mad Monster Mansion Note 51": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF04A
    ),
    "Mad Monster Mansion Note 52": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BEAC4
    ),
    "Mad Monster Mansion Note 53": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BEC52
    ),
    "Mad Monster Mansion Note 54": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BEDE3
    ),
    "Mad Monster Mansion Note 55": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BEC51
    ),
    "Mad Monster Mansion Note 56": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BEABD
    ),
    "Mad Monster Mansion Note 57": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BE92A
    ),
    "Mad Monster Mansion Note 58": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BE797
    ),
    "Mad Monster Mansion Note 59": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BEF73
    ),
    "Mad Monster Mansion Note 60": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF0E0
    ),
    "Mad Monster Mansion Note 61": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF433
    ),
    "Mad Monster Mansion Note 62": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF6EC
    ),
    "Mad Monster Mansion Note 63": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF9A1
    ),
    "Mad Monster Mansion Note 64": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF6EB
    ),
    "Mad Monster Mansion Note 65": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF897
    ),
    "Mad Monster Mansion Note 66": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BF98F
    ),
    "Mad Monster Mansion Note 67": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BFA8B
    ),
    "Mad Monster Mansion Note 68": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011BFB85
    ),
    "Mad Monster Mansion Note 69": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011C124C
    ),
    "Mad Monster Mansion Note 70": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011C0C3B
    ),
    "Mad Monster Mansion Note 71": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011CFF8D
    ),
    "Mad Monster Mansion Note 72": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011C05A0
    ),
    "Mad Monster Mansion Note 73": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011CFA77
    ),
    "Mad Monster Mansion Note 74": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011CF9B3
    ),
    "Mad Monster Mansion Note 75": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011C0131
    ),
    "Mad Monster Mansion Note 76": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011C0045
    ),
    "Mad Monster Mansion Note 77": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011CFC2D
    ),
    "Mad Monster Mansion Note 78": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011CF8ED
    ),
    "Mad Monster Mansion Note 79": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B0DDE
    ),
    "Mad Monster Mansion Note 80": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B0D49
    ),
    "Mad Monster Mansion Note 81": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B01C3
    ),
    "Mad Monster Mansion Note 82": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x011B0258
    ),
    "Mad Monster Mansion Note 83": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0125035F
    ),
    "Mad Monster Mansion Note 84": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0125FF36
    ),
    "Mad Monster Mansion Note 85": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0125FDE1
    ),
    "Mad Monster Mansion Note 86": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0125FFAA
    ),
    "Mad Monster Mansion Note 87": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0125FBBC
    ),
    "Mad Monster Mansion Note 88": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0125FF86
    ),
    "Mad Monster Mansion Note 89": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012501FC
    ),
    "Mad Monster Mansion Note 90": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01300089
    ),
    "Mad Monster Mansion Note 91": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0130FE3E
    ),
    "Mad Monster Mansion Note 92": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0124056C
    ),
    "Mad Monster Mansion Note 93": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0124FFE7
    ),
    "Mad Monster Mansion Note 94": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0124FA6E
    ),
    "Mad Monster Mansion Note 95": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0124FFF4
    ),
    "Mad Monster Mansion Note 96": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012FFF8E
    ),
    "Mad Monster Mansion Note 97": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012FFE5C
    ),
    "Mad Monster Mansion Note 98": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012FFECA
    ),
    "Mad Monster Mansion Note 99": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012F0074
    ),
    "Mad Monster Mansion Note 100": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x012F01A4
    ),
    "Rusty Bucket Bay Note 1": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01310AE7
    ),
    "Rusty Bucket Bay Note 2": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013109FD
    ),
    "Rusty Bucket Bay Note 3": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01310917
    ),
    "Rusty Bucket Bay Note 4": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131082D
    ),
    "Rusty Bucket Bay Note 5": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01310745
    ),
    "Rusty Bucket Bay Note 6": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131FFF9
    ),
    "Rusty Bucket Bay Note 7": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131FF24
    ),
    "Rusty Bucket Bay Note 8": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131FE50
    ),
    "Rusty Bucket Bay Note 9": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131FD7C
    ),
    "Rusty Bucket Bay Note 10": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01312085
    ),
    "Rusty Bucket Bay Note 11": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131203B
    ),
    "Rusty Bucket Bay Note 12": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01311DE2
    ),
    "Rusty Bucket Bay Note 13": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01311B8A
    ),
    "Rusty Bucket Bay Note 14": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01311869
    ),
    "Rusty Bucket Bay Note 15": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131162B
    ),
    "Rusty Bucket Bay Note 16": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134EDAA
    ),
    "Rusty Bucket Bay Note 17": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134EEF4
    ),
    "Rusty Bucket Bay Note 18": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134EDA9
    ),
    "Rusty Bucket Bay Note 19": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134EC59
    ),
    "Rusty Bucket Bay Note 20": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013CFB86
    ),
    "Rusty Bucket Bay Note 21": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013CFFA4
    ),
    "Rusty Bucket Bay Note 22": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013C050C
    ),
    "Rusty Bucket Bay Note 23": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013C01F5
    ),
    "Rusty Bucket Bay Note 24": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013CFFAA
    ),
    "Rusty Bucket Bay Note 25": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013B0384
    ),
    "Rusty Bucket Bay Note 26": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013B0401
    ),
    "Rusty Bucket Bay Note 27": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013B047E
    ),
    "Rusty Bucket Bay Note 28": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013B04FA
    ),
    "Rusty Bucket Bay Note 29": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013B0578
    ),
    "Rusty Bucket Bay Note 30": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131F831
    ),
    "Rusty Bucket Bay Note 31": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131F381
    ),
    "Rusty Bucket Bay Note 32": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013100FA
    ),
    "Rusty Bucket Bay Note 33": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01310226
    ),
    "Rusty Bucket Bay Note 34": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01310352
    ),
    "Rusty Bucket Bay Note 35": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131047E
    ),
    "Rusty Bucket Bay Note 36": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131086D
    ),
    "Rusty Bucket Bay Note 37": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01310741
    ),
    "Rusty Bucket Bay Note 38": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01310615
    ),
    "Rusty Bucket Bay Note 39": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013104E9
    ),
    "Rusty Bucket Bay Note 40": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0139FF1E
    ),
    "Rusty Bucket Bay Note 41": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0139FD01
    ),
    "Rusty Bucket Bay Note 42": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0139013E
    ),
    "Rusty Bucket Bay Note 43": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01390326
    ),
    "Rusty Bucket Bay Note 44": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013DFE48
    ),
    "Rusty Bucket Bay Note 45": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013DFD90
    ),
    "Rusty Bucket Bay Note 46": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013DFCD9
    ),
    "Rusty Bucket Bay Note 47": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013DFC23
    ),
    "Rusty Bucket Bay Note 48": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013FFAC9
    ),
    "Rusty Bucket Bay Note 49": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013FFB9D
    ),
    "Rusty Bucket Bay Note 50": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013FFC70
    ),
    "Rusty Bucket Bay Note 51": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134083E
    ),
    "Rusty Bucket Bay Note 52": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01340906
    ),
    "Rusty Bucket Bay Note 53": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01340775
    ),
    "Rusty Bucket Bay Note 54": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013406AE
    ),
    "Rusty Bucket Bay Note 55": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134FAF5
    ),
    "Rusty Bucket Bay Note 56": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134FA2D
    ),
    "Rusty Bucket Bay Note 57": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134FBBD
    ),
    "Rusty Bucket Bay Note 58": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134FC87
    ),
    "Rusty Bucket Bay Note 59": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134FB59
    ),
    "Rusty Bucket Bay Note 60": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134F9C9
    ),
    "Rusty Bucket Bay Note 61": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134F839
    ),
    "Rusty Bucket Bay Note 62": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0134F9CA
    ),
    "Rusty Bucket Bay Note 63": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01312279
    ),
    "Rusty Bucket Bay Note 64": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01312661
    ),
    "Rusty Bucket Bay Note 65": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01312D69
    ),
    "Rusty Bucket Bay Note 66": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01312981
    ),
    "Rusty Bucket Bay Note 67": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01310578
    ),
    "Rusty Bucket Bay Note 68": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131044C
    ),
    "Rusty Bucket Bay Note 69": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01310320
    ),
    "Rusty Bucket Bay Note 70": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01350AE7
    ),
    "Rusty Bucket Bay Note 71": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01350BC2
    ),
    "Rusty Bucket Bay Note 72": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01350A8C
    ),
    "Rusty Bucket Bay Note 73": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013509B0
    ),
    "Rusty Bucket Bay Note 74": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131ED6A
    ),
    "Rusty Bucket Bay Note 75": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131EAE3
    ),
    "Rusty Bucket Bay Note 76": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131E88F
    ),
    "Rusty Bucket Bay Note 77": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131E71A
    ),
    "Rusty Bucket Bay Note 78": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131E5A5
    ),
    "Rusty Bucket Bay Note 79": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131D47D
    ),
    "Rusty Bucket Bay Note 80": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131D4EC
    ),
    "Rusty Bucket Bay Note 81": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131D0FE
    ),
    "Rusty Bucket Bay Note 82": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131DF95
    ),
    "Rusty Bucket Bay Note 83": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131E0C0
    ),
    "Rusty Bucket Bay Note 84": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0131E1EC
    ),
    "Rusty Bucket Bay Note 85": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01370251
    ),
    "Rusty Bucket Bay Note 86": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0137FCBE
    ),
    "Rusty Bucket Bay Note 87": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0137FC96
    ),
    "Rusty Bucket Bay Note 88": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013700B9
    ),
    "Rusty Bucket Bay Note 89": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01370154
    ),
    "Rusty Bucket Bay Note 90": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0137FEF7
    ),
    "Rusty Bucket Bay Note 91": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0137FD21
    ),
    "Rusty Bucket Bay Note 92": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013701D6
    ),
    "Rusty Bucket Bay Note 93": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013804A6
    ),
    "Rusty Bucket Bay Note 94": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01380537
    ),
    "Rusty Bucket Bay Note 95": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x013805B8
    ),
    "Rusty Bucket Bay Note 96": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01380527
    ),
    "Rusty Bucket Bay Note 97": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x018B115F
    ),
    "Rusty Bucket Bay Note 98": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x018B1548
    ),
    "Rusty Bucket Bay Note 99": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x018B1160
    ),
    "Rusty Bucket Bay Note 100": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x018B0D78
    ),
    "Click Clock Wood Note 1": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014009A1
    ),
    "Click Clock Wood Note 2": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01400C41
    ),
    "Click Clock Wood Note 3": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01400EED
    ),
    "Click Clock Wood Note 4": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01401005
    ),
    "Click Clock Wood Note 5": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0143EED9
    ),
    "Click Clock Wood Note 6": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0143EB4E
    ),
    "Click Clock Wood Note 7": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0143E766
    ),
    "Click Clock Wood Note 8": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0143EAE6
    ),
    "Click Clock Wood Note 9": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014304FB
    ),
    "Click Clock Wood Note 10": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014304FC
    ),
    "Click Clock Wood Note 11": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014304FD
    ),
    "Click Clock Wood Note 12": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014319F4
    ),
    "Click Clock Wood Note 13": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01431B72
    ),
    "Click Clock Wood Note 14": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01431CE2
    ),
    "Click Clock Wood Note 15": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01430384
    ),
    "Click Clock Wood Note 16": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01430385
    ),
    "Click Clock Wood Note 17": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01430399
    ),
    "Click Clock Wood Note 18": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0143E9EE
    ),
    "Click Clock Wood Note 19": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0143E897
    ),
    "Click Clock Wood Note 20": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0143E732
    ),
    "Click Clock Wood Note 21": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01440CAC
    ),
    "Click Clock Wood Note 22": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01440EC3
    ),
    "Click Clock Wood Note 23": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01440641
    ),
    "Click Clock Wood Note 24": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01440457
    ),
    "Click Clock Wood Note 25": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01440226
    ),
    "Click Clock Wood Note 26": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01440168
    ),
    "Click Clock Wood Note 27": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014400C8
    ),
    "Click Clock Wood Note 28": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01442328
    ),
    "Click Clock Wood Note 29": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0144229B
    ),
    "Click Clock Wood Note 30": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01442189
    ),
    "Click Clock Wood Note 31": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01442102
    ),
    "Click Clock Wood Note 32": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01442403
    ),
    "Click Clock Wood Note 33": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014422A5
    ),
    "Click Clock Wood Note 34": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014422A6
    ),
    "Click Clock Wood Note 35": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014425C5
    ),
    "Click Clock Wood Note 36": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0144281D
    ),
    "Click Clock Wood Note 37": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014505A1
    ),
    "Click Clock Wood Note 38": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014505F1
    ),
    "Click Clock Wood Note 39": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01450641
    ),
    "Click Clock Wood Note 40": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014509CE
    ),
    "Click Clock Wood Note 41": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01450E42
    ),
    "Click Clock Wood Note 42": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01451156
    ),
    "Click Clock Wood Note 43": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014512C0
    ),
    "Click Clock Wood Note 44": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01451157
    ),
    "Click Clock Wood Note 45": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01450E43
    ),
    "Click Clock Wood Note 46": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014509C4
    ),
    "Click Clock Wood Note 47": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01450384
    ),
    "Click Clock Wood Note 48": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145FD45
    ),
    "Click Clock Wood Note 49": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145F95C
    ),
    "Click Clock Wood Note 50": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145F5B0
    ),
    "Click Clock Wood Note 51": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145F46D
    ),
    "Click Clock Wood Note 52": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145F669
    ),
    "Click Clock Wood Note 53": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145F8C6
    ),
    "Click Clock Wood Note 54": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145FD3F
    ),
    "Click Clock Wood Note 55": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01450546
    ),
    "Click Clock Wood Note 56": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014CFEAD
    ),
    "Click Clock Wood Note 57": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014C0178
    ),
    "Click Clock Wood Note 58": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014C0465
    ),
    "Click Clock Wood Note 59": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014C019D
    ),
    "Click Clock Wood Note 60": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145E81E
    ),
    "Click Clock Wood Note 61": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145E61A
    ),
    "Click Clock Wood Note 62": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145E468
    ),
    "Click Clock Wood Note 63": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145E2D1
    ),
    "Click Clock Wood Note 64": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145EA3D
    ),
    "Click Clock Wood Note 65": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145FE2A
    ),
    "Click Clock Wood Note 66": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145FDDA
    ),
    "Click Clock Wood Note 67": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145FD8A
    ),
    "Click Clock Wood Note 68": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014508E3
    ),
    "Click Clock Wood Note 69": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145093A
    ),
    "Click Clock Wood Note 70": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x015C0001
    ),
    "Click Clock Wood Note 71": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x015CF9DA
    ),
    "Click Clock Wood Note 72": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x015C00FA
    ),
    "Click Clock Wood Note 73": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x015C063E
    ),
    "Click Clock Wood Note 74": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01600289
    ),
    "Click Clock Wood Note 75": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x016001F3
    ),
    "Click Clock Wood Note 76": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01600158
    ),
    "Click Clock Wood Note 77": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01450292
    ),
    "Click Clock Wood Note 78": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145FF0E
    ),
    "Click Clock Wood Note 79": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145FC86
    ),
    "Click Clock Wood Note 80": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145FC8C
    ),
    "Click Clock Wood Note 81": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145FEFD
    ),
    "Click Clock Wood Note 82": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01450282
    ),
    "Click Clock Wood Note 83": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0145050A
    ),
    "Click Clock Wood Note 84": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01450503
    ),
    "Click Clock Wood Note 85": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0146F7E6
    ),
    "Click Clock Wood Note 86": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0146F3E7
    ),
    "Click Clock Wood Note 87": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0146FDCD
    ),
    "Click Clock Wood Note 88": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0146FB4B
    ),
    "Click Clock Wood Note 89": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01462579
    ),
    "Click Clock Wood Note 90": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0146278E
    ),
    "Click Clock Wood Note 91": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x014629A4
    ),
    "Click Clock Wood Note 92": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01462BBD
    ),
    "Click Clock Wood Note 93": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0146187F
    ),
    "Click Clock Wood Note 94": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x0146187C
    ),
    "Click Clock Wood Note 95": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01461C02
    ),
    "Click Clock Wood Note 96": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01461C01
    ),
    "Click Clock Wood Note 97": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01460425
    ),
    "Click Clock Wood Note 98": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01460409
    ),
    "Click Clock Wood Note 99": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01460528
    ),
    "Click Clock Wood Note 100": BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        address=0x01460890
    ),
    LOC_DEFEAT_GRUNTILDA: BKLocationData(
        region=RGN_GRUNTILDAS_LAIR,
        locked_item=ITEM_VICTORY
    ),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
code_to_location_table = {data.address: name for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}