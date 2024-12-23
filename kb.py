import board
from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

name = str(getmount("/").label)
isRight = True if str(getmount("/").label)[-1] == "R" else False

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
    )

    diode_orientation = DiodeOrientation.COL2ROW
