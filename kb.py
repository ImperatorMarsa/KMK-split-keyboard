import board
from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

name = str(getmount("/").label)
isRight = True if str(getmount("/").label)[-1] == "R" else False


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP13,  # col 4
        board.GP12,  # col 3
        board.GP11,  # col 2
        board.GP10,  # col 1
        board.GP9,  # col 0
    )
    # row_pins = (
    #     board.GP15,  # row 3
    #     board.GP14,  # row 2
    #     board.GP8,  # row 1
    #     board.GP7,  # row 0
    # )
    row_pins = (
        board.GP7,  # row 0
        board.GP8,  # row 1
        board.GP14,  # row 2
        board.GP15,  # row 3
    )

    diode_orientation = DiodeOrientation.COL2ROW

    # fmt: off
    coord_mapping = [
        05, 01, 02, 03, 04,   24, 23, 22, 21, 25,
        10, 06, 07, 08, 09,   29, 28, 27, 26, 30,
        15, 11, 12, 13, 14,   34, 33, 32, 31, 35,
        00, 16, 17, 18, 19,   39, 38, 37, 36, 20,
    ]
    # coord_mapping = [ # Right
    #     00, 01, 02, 03, 09,
    #     05, 06, 07, 08, 14,
    #     10, 11, 12, 13, 19,
    #     04, 15, 16, 17, 18,
    # ]
    # coord_mapping = [ # Left
    #     05, 01, 02, 03, 04,
    #     10, 06, 07, 08, 09,
    #     15, 11, 12, 13, 14,
    #     00, 16, 17, 18, 19,
    # ]
    # fmt:on
