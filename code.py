import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split

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
split = Split(
    data_pin=board.GP0,
    data_pin2=board.GP1,
)
keyboard.modules = [split]

# fmt: off
keyboard.keymap = [
    [
        #QWERTY
        KC.Q, KC.W, KC.E, KC.R, KC.T,   KC.Y, KC.U, KC.I,    KC.O,   KC.P,
        KC.A, KC.S, KC.D, KC.F, KC.G,   KC.H, KC.J, KC.K,    KC.L,   KC.SCLN,
        KC.Z, KC.X, KC.C, KC.V, KC.B,   KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH,

           KC.LCTL, KC.LGUI, KC.LALT,   KC.SPC, KC.ENT, KC.BSPC,
    ],
]
# fmt: on

if __name__ == "__main__":
    keyboard.go()
