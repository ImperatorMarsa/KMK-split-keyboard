import board
from kb import KMKKeyboard, isRight

from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.holdtap import HoldTap
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

### Split #########################################################################################
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
###################################################################################################

### HoldTap #######################################################################################
holdtap = HoldTap()
keyboard.modules.append(holdtap)

LCTL = KC.HT(KC.ESC, KC.LCTL)
LGUI = KC.HT(KC.SPC, KC.LGUI)
LSFT = KC.HT(KC.ENTER, KC.LSFT)
LALT = KC.HT(KC.BSPACE, KC.LALT)
###################################################################################################

### Layers ########################################################################################
keyboard.modules.append(Layers())

NUM_LAYER = KC.MO(1)
###################################################################################################

XXXX = KC.NO
____ = KC.TRANSPARENT
# fmt: off
keyboard.keymap = [
    [
#QWE_LAYER
KC.Q, KC.W, KC.E, KC.R,   KC.T,     KC.Y, KC.U, KC.I,      KC.O,   KC.P,
KC.A, KC.S, KC.D, KC.F,   KC.G,     KC.H, KC.J, KC.K,      KC.L,   KC.SCLN,
KC.Z, KC.X, KC.C, KC.V,   KC.B,     KC.N, KC.M, KC.COMM,   KC.DOT, KC.SLSH,

XXXX, XXXX, XXXX, LCTL,   LGUI,     LSFT, LALT, NUM_LAYER, XXXX,   XXXX,
    ],
    [
#NUM_LAYER
 KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,     KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,
 KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,     KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
KC.F11, KC.LABK, KC.LCBR, KC.LBRC, KC.LPRN,     KC.RPRN, KC.RBRC, KC.RCBR, KC.RABK, KC.F12,

  XXXX,    XXXX,    ____,    ____,    ____,     ____,    ____,    XXXX,    XXXX,    XXXX,
    ],
]
# fmt: on

if __name__ == "__main__":
    keyboard.go(hid_type=HIDModes.USB)
