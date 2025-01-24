import board
from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

name = str(getmount("/").label)
isRight = True if str(getmount("/").label)[-1] == "R" else False


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP13,
        board.GP12,
        board.GP11,
        board.GP10,
        board.GP9,
    )
    row_pins = (
        board.GP7,
        board.GP8,
        board.GP14,
        board.GP15,
    )

    diode_orientation = DiodeOrientation.COL2ROW
