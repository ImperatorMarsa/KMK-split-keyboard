import board
from kb import KMKKeyboard, isRight

from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide

keyboard = KMKKeyboard()

split_side = SplitSide.LEFT
data_pin = board.GP1
data_pin2 = board.GP0
if isRight:
    split_side = SplitSide.RIGHT
    data_pin = board.GP0
    data_pin2 = board.GP1

split = Split(
    uart_interval=20,
    data_pin=data_pin,
    data_pin2=data_pin2,
    split_type=SplitType.UART,
    split_side=split_side,
)

keyboard.modules.append(split)

XXXX = KC.NO
# fmt: off
keyboard.keymap = [
    [
        #QWERTY
        KC.Q, KC.W,    KC.E,    KC.R,    KC.T,   KC.Y,   KC.U,   KC.I,    KC.O,   KC.P,
        KC.A, KC.S,    KC.D,    KC.F,    KC.G,   KC.H,   KC.J,   KC.K,    KC.L,   KC.SCLN,
        KC.Z, KC.X,    KC.C,    KC.V,    KC.B,   KC.N,   KC.M,   KC.COMM, KC.DOT, KC.SLSH,

        XXXX, XXXX, KC.LCTL, KC.LGUI, KC.LALT,   KC.SPC, KC.ENT, KC.BSPC, XXXX,   XXXX,
    ],
]
# fmt: on

if __name__ == "__main__":
    keyboard.go(hid_type=HIDModes.USB)
