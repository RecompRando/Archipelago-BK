from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld

from .Constants import *


class BKItem(Item):
    game = "Banjo-Kazooie"


class BKItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable = lambda options: True


item_data_table: Dict[str, BKItemData] = {
    ITEM_JUMP: BKItemData(
        code=0x0400000A,
        type=ItemClassification.progression
    ),
    ITEM_FEATHERY_FLAP: BKItemData(
        code=0x04000007,
        type=ItemClassification.progression
    ),
    ITEM_FLAP_FLIP: BKItemData(
        code=0x04000008,
        type=ItemClassification.progression
    ),
    ITEM_SWIM: BKItemData(
        code=0x0400000F,
        type=ItemClassification.progression
    ),
    ITEM_CLIMB: BKItemData(
        code=0x04000005,
        type=ItemClassification.progression
    ),
    ITEM_BEAK_BARGE: BKItemData(
        code=0x04000000,
        type=ItemClassification.progression
    ),
    ITEM_CLAW_SWIPE: BKItemData(
        code=0x04000004,
        type=ItemClassification.progression
    ),
    ITEM_ROLL: BKItemData(
        code=0x0400000C,
        type=ItemClassification.progression
    ),
    ITEM_RAT_A_TAT_RAP: BKItemData(
        code=0x0400000B,
        type=ItemClassification.progression
    ),
    ITEM_EGGS: BKItemData(
        code=0x04000006,
        type=ItemClassification.progression
    ),
    ITEM_TALON_TROT: BKItemData(
        code=0x04000010,
        type=ItemClassification.progression
    ),
    ITEM_TALON_TROT_SPEED_ONLY: BKItemData(
        code=0x04000013,
        type=ItemClassification.useful,
        can_create=lambda options: False
    ),
    ITEM_BEAK_BUSTER: BKItemData(
        code=0x04000002,
        type=ItemClassification.progression
    ),
    ITEM_FLIGHT: BKItemData(
        code=0x04000009,
        type=ItemClassification.progression
    ),
    ITEM_SHOCK_SPRING_JUMP: BKItemData(
        code=0x0400000D,
        type=ItemClassification.progression
    ),
    ITEM_WONDERWING: BKItemData(
        code=0x04000012,
        type=ItemClassification.progression
    ),
    ITEM_STILT_STRIDE: BKItemData(
        code=0x0400000E,
        type=ItemClassification.progression
    ),
    ITEM_BEAK_BOMB: BKItemData(
        code=0x04000001,
        type=ItemClassification.progression
    ),
    ITEM_TURBO_TALON_TROT: BKItemData(
        code=0x04000011,
        type=ItemClassification.progression
    ),
    ITEM_SHNIGEDY_DING_DONG: BKItemData(
        code=0x69000000,
        type=ItemClassification.useful,
        can_create=lambda options: False
    ),
    ITEM_BLUBBER_GOLD: BKItemData(
        code=0x06000001,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_RED_PRESENT: BKItemData(
        code=0x06000002,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_GREEN_PRESENT: BKItemData(
        code=0x06000003,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_BLUE_PRESENT: BKItemData(
        code=0x06000004,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_WORM: BKItemData(
        code=0x06000005,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_ACORN: BKItemData(
        code=0x06000006,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_MM_BLUE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_MM_GREEN: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_MM_ORANGE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_MM_PURPLE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_MM_YELLOW: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_TTC_BLUE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_TTC_GREEN: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_TTC_ORANGE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_TTC_PURPLE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_TTC_YELLOW: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_CC_BLUE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_CC_GREEN: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_CC_ORANGE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_CC_PURPLE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_CC_YELLOW: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_BGS_BLUE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_BGS_GREEN: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_BGS_ORANGE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_BGS_PURPLE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_BGS_YELLOW: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_FP_BLUE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_FP_GREEN: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_FP_ORANGE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_FP_PURPLE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_FP_YELLOW: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_GV_BLUE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_GV_GREEN: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_GV_ORANGE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_GV_PURPLE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_GV_YELLOW: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_MMM_BLUE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_MMM_GREEN: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_MMM_ORANGE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_MMM_PURPLE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_MMM_YELLOW: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_RBB_BLUE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_RBB_GREEN: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_RBB_ORANGE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_RBB_PURPLE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_RBB_YELLOW: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_CCW_BLUE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_CCW_GREEN: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_CCW_ORANGE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_CCW_PURPLE: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_JINJO_CCW_YELLOW: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_WITCH_SWITCH_MM: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_WITCH_SWITCH_TTC: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_WITCH_SWITCH_CC: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_WITCH_SWITCH_BGS: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_WITCH_SWITCH_FP: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_WITCH_SWITCH_GV: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_WITCH_SWITCH_MMM: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_WITCH_SWITCH_RBB: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_WITCH_SWITCH_CCW: BKItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
    ITEM_SEASON_SPRING: BKItemData(
        code=0x0001FFC0,
        type=ItemClassification.progression,
    ),
    ITEM_SEASON_SUMMER: BKItemData(
        code=0x0001FFC1,
        type=ItemClassification.progression,
    ),
    ITEM_SEASON_AUTUMN: BKItemData(
        code=0x0001FFC2,
        type=ItemClassification.progression,
    ),
    ITEM_SEASON_WINTER: BKItemData(
        code=0x0001FFC3,
        type=ItemClassification.progression,
    ),
    ITEM_JIGGY: BKItemData(
        code=0x0001FBE2,
        type=ItemClassification.progression,
        num_exist=98
    ),
    ITEM_JIGGY_FILLER: BKItemData(
        code=0xFF01FBE2,
        type=ItemClassification.filler,
        num_exist=2
    ),
    ITEM_MUMBO_TOKEN: BKItemData(
        code=0x0001FBE3,
        type=ItemClassification.progression,
        num_exist=75
    ),
    ITEM_MUMBO_TOKEN_FILLER: BKItemData(
        code=0xFF01FBE3,
        type=ItemClassification.filler,
        num_exist=41
    ),
    ITEM_NOTE: BKItemData(
        code=0x0001FBE4,
        type=ItemClassification.progression_skip_balancing,
        num_exist=750,
        can_create=lambda options: options.notesanity.value
    ),
    ITEM_NOTE_FILLER: BKItemData(
        code=0xFF01FBE4,
        type=ItemClassification.filler,
        num_exist=150,
        can_create=lambda options: options.notesanity.value
    ),
    ITEM_EMPTY_HONEYCOMB: BKItemData(
        code=0x0001FBE5,
        type=ItemClassification.useful,
        num_exist=24
    ),
    # ~ "Acorn": BKItemData(
        # ~ code=0x0001FBE5,
        # ~ type=ItemClassification.useful,
        # ~ num_exist=24
    # ~ ),
    "BLUEEGGS Cheato": BKItemData(
        code=0x0001FBE6,
        type=ItemClassification.useful,
        can_create=lambda options: False
    ),
    "REDFEATHERS Cheato": BKItemData(
        code=0x0001FBE7,
        type=ItemClassification.useful,
        can_create=lambda options: False
    ),
    "GOLDFEATHERS Cheato": BKItemData(
        code=0x0001FBE8,
        type=ItemClassification.useful,
        can_create=lambda options: False
    ),
    ITEM_DOUBLE_HEALTH: BKItemData(
        code=0x0001FBE9,
        type=ItemClassification.useful
    ),
    ITEM_TRANSFORMATION_TERMITE: BKItemData(
        code=0x0001FFB0,
        type=ItemClassification.progression,
    ),
    ITEM_TRANSFORMATION_CROCODILE: BKItemData(
        code=0x0001FFB1,
        type=ItemClassification.progression,
    ),
    ITEM_TRANSFORMATION_WALRUS: BKItemData(
        code=0x0001FFB2,
        type=ItemClassification.progression,
    ),
    ITEM_TRANSFORMATION_PUMPKIN: BKItemData(
        code=0x0001FFB3,
        type=ItemClassification.progression,
    ),
    ITEM_TRANSFORMATION_BEE: BKItemData(
        code=0x0001FFB4,
        type=ItemClassification.progression,
    ),
    ITEM_SNS_KEY_ICE: BKItemData(
        code=0x05000007,
        type=ItemClassification.progression
    ),
    ITEM_SNS_EGG_PINK: BKItemData(
        code=0x05000005,
        type=ItemClassification.progression
    ),
    ITEM_SNS_EGG_BLUE: BKItemData(
        code=0x05000004,
        type=ItemClassification.progression
    ),
    ITEM_SNS_EGG_CYAN: BKItemData(
        code=0x05000006,
        type=ItemClassification.progression
    ),
    ITEM_SNS_EGG_GREEN: BKItemData(
        code=0x05000003,
        type=ItemClassification.progression
    ),
    ITEM_SNS_EGG_RED: BKItemData(
        code=0x05000002,
        type=ItemClassification.progression
    ),
    ITEM_SNS_EGG_YELLOW: BKItemData(
        code=0x05000001,
        type=ItemClassification.progression
    ),
    ITEM_HONEYCOMB: BKItemData(
        code=0x0001FBF1,
        type=ItemClassification.filler,
        can_create=lambda options: False
    ),
    ITEM_EGG_REFILL: BKItemData(
        code=0x0001FBF2,
        type=ItemClassification.filler,
        can_create=lambda options: False
    ),
    ITEM_REDFEATHER_REFILL: BKItemData(
        code=0x0001FBF3,
        type=ItemClassification.filler,
        can_create=lambda options: False
    ),
    ITEM_GOLDFEATHER_REFILL: BKItemData(
        code=0x0001FBF4,
        type=ItemClassification.filler,
        can_create=lambda options: False
    ),
    ITEM_EXTRA_LIFE: BKItemData(
        code=0x0001FBF5,
        type=ItemClassification.filler,
        can_create=lambda options: False
    ),
    # Level Unlock Items (9 total - MM is always open)
    ITEM_OPEN_TTC: BKItemData(
        code=0x0001FFE3,
        type=ItemClassification.progression,
    ),
    ITEM_OPEN_CC: BKItemData(
        code=0x0001FFE4,
        type=ItemClassification.progression,
    ),
    ITEM_OPEN_BGS: BKItemData(
        code=0x0001FFE5,
        type=ItemClassification.progression,
    ),
    ITEM_OPEN_FP: BKItemData(
        code=0x0001FFE6,
        type=ItemClassification.progression,
    ),
    ITEM_OPEN_GV: BKItemData(
        code=0x0001FFE7,
        type=ItemClassification.progression,
    ),
    ITEM_OPEN_MMM: BKItemData(
        code=0x0001FFE8,
        type=ItemClassification.progression,
    ),
    ITEM_OPEN_RBB: BKItemData(
        code=0x0001FFE9,
        type=ItemClassification.progression,
    ),
    ITEM_OPEN_CCW: BKItemData(
        code=0x0001FFEA,
        type=ItemClassification.progression,
    ),
    ITEM_OPEN_FIGHT: BKItemData(
        code=0x0001FFEB,
        type=ItemClassification.progression,
    ),

    # Warp Cauldron Items (4 paired)
    ITEM_CAULDRON_PURPLE: BKItemData(
        code=0x0001FFD0,
        type=ItemClassification.progression,
    ),
    ITEM_CAULDRON_GREEN: BKItemData(
        code=0x0001FFD1,
        type=ItemClassification.progression,
    ),
    ITEM_CAULDRON_ORANGE: BKItemData(
        code=0x0001FFD2,
        type=ItemClassification.progression,
    ),
    ITEM_CAULDRON_YELLOW: BKItemData(
        code=0x0001FFD3,
        type=ItemClassification.progression,
    ),
    ITEM_VICTORY: BKItemData(
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
code_to_item_table = {data.code: name for name, data in item_data_table.items() if data.code is not None}