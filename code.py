import board
from storage import getmount

from kb import KMKKeyboard

from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide

keyboard = KMKKeyboard()

# Split keyboard support
split_side = SplitSide.LEFT
split_side = SplitSide.RIGHT
split = Split(
    use_pio=True,
    data_pin=keyboard.data_pin,
    data_pin2=keyboard.data_pin2,
)
keyboard.modules.append(split)

keyboard.row_pins = (
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
)
keyboard.col_pins = (
    board.GP29,
    board.GP28,
    board.GP27,
    board.GP26,
    board.GP15,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

XXXX = KC.NO
# fmt: off
keyboard.keymap = [
    [   # QWERTY
        KC.Q, KC.W, KC.E,    KC.R,    KC.T,          KC.Y,   KC.U,   KC.I,    KC.O,   KC.P,
        KC.A, KC.S, KC.D,    KC.F,    KC.G,          KC.H,   KC.J,   KC.K,    KC.L,   KC.SCLN,
        KC.Z, KC.X, KC.C,    KC.V,    KC.B,          KC.N,   KC.M,   KC.COMM, KC.DOT, KC.SLSH,

        XXXX, XXXX, KC.LCTL, KC.LGUI, KC.LALT,       KC.SPC, KC.ENT, KC.BSPC, XXXX,   XXXX,
    ],
]
# fmt: on

if __name__ == "__main__":
    keyboard.go(hid_type=HIDModes.USB)
