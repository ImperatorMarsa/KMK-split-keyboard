import board
from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.split import SplitSide

splitSide = SplitSide.RIGHT if str(getmount("/").label).endswith("R") else SplitSide.LEFT


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP13,  # col 4
        board.GP12,  # col 3
        board.GP11,  # col 2
        board.GP10,  # col 1
        board.GP9,  # col 0
    )
    row_pins = (
        board.GP7,  # row 0
        board.GP8,  # row 1
        board.GP14,  # row 2
        board.GP15,  # row 3
    )

    diode_orientation = DiodeOrientation.COL2ROW

    # fmt: off
    coord_mapping = [
        05, 01, 02, 03, 04,   35, 36, 37, 38, 34,
        10, 06, 07, 08, 09,   30, 31, 32, 33, 29,
        15, 11, 12, 13, 14,   25, 26, 27, 28, 24,
            16, 17, 18, 19,   20, 21, 22, 23,
    ]
    # fmt:on
