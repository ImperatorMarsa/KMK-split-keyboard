import board
from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
from kmk.scanners import DiodeOrientation

name = str(getmount('/').label)
isRight = True if name.endswith('R') else False

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP29,
        board.GP28,
        board.GP27,
        board.GP26,
        board.GP15,
    )
    row_pins = (
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP14,
    )
    diode_orientation = DiodeOrientation.COL2ROW

    # fmt: off
    coord_mapping = [
        00, 01, 02, 03, 04,   18, 19, 20, 21, 22,
        05, 06, 07, 08, 09,   23, 24, 25, 26, 27,
        10, 11, 12, 13, 14,   28, 29, 30, 31, 32,
                15, 16, 17,   33, 34, 35
    ]
    # fmt: on
