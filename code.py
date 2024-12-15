import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.row_pins = (
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
)
keyboard.col_pins = (
    board.GP15,
    board.GP26,
    board.GP27,
    board.GP28,
    board.GP29,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        #
        KC.Q,KC.W,KC.E,KC.R,KC.T,
        #
        KC.A,KC.S,KC.D,KC.F,KC.G,
        #
        KC.Z,KC.X,KC.C,KC.V,KC.B,
        #
        KC.Y,KC.U,KC.I,
    ]
]

if __name__ == "__main__":
    keyboard.go()
