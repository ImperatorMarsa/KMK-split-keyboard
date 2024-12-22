import board
from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

name = str(getmount('/').label)
isRight = True if name.endswith('R') else False

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP15,
        board.GP26,
        board.GP27,
        board.GP28,
        board.GP29,
    )
    row_pins = (
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
    )
    diode_orientation = DiodeOrientation.COL2ROW

    # fmt: off
    coord_mapping = [
        04, 03, 02, 01, 00,   22, 21, 20, 19, 18,
        09, 08, 07, 06, 05,   27, 26, 25, 24, 23,
        14, 13, 12, 11, 10,   32, 31, 30, 29, 28,
                17, 16, 15,   34, 35, 33,
    ]
    # fmt: on
