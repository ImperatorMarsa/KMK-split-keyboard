import board
from kb import KMKKeyboard, isRight

from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.holdtap import HoldTap
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros, UnicodeModeIBus

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
LSFT = KC.HT(KC.ENTER, KC.LSFT)
LALT = KC.HT(KC.BSPACE, KC.LALT)
###################################################################################################

### Layers ########################################################################################
keyboard.modules.append(Layers())

M_LSFT = KC.LM(1, KC.LSFT)
###################################################################################################

### Layers ########################################################################################
macros = Macros(unicode_mode=UnicodeModeIBus)
keyboard.modules.append(macros)

COMMA = KC.MACRO(",")

Rs_B = KC.MACRO("б")
Rl_B = KC.MACRO("Б")

Rs_J = KC.MACRO("ж")
Rl_J = KC.MACRO("Ж")

Rs_YU = KC.MACRO("ю")
Rl_YU = KC.MACRO("Ю")
###################################################################################################

XXXX = KC.NO
____ = KC.TRANSPARENT
# fmt: off
keyboard.keymap = [
    [
        #QWERTY
        KC.Q, KC.W, KC.E, KC.R,   KC.T,     KC.Y,   KC.U, KC.I, KC.O,  KC.P,
        KC.A, KC.S, KC.D, KC.F,   KC.G,     KC.H,   KC.J, KC.K, KC.L,  Rs_J,
        KC.Z, KC.X, KC.C, KC.V,   KC.B,     KC.N,   KC.M, Rs_B, Rs_YU, KC.DOT,

        XXXX, XXXX, XXXX, LCTL, KC.SPC,     M_LSFT, LALT, XXXX, XXXX,  XXXX,
    ],
    [
        #QWERTY
        ____, ____, ____, ____, ____,     ____, ____, ____, ____,  ____,
        ____, ____, ____, ____, ____,     ____, ____, ____, ____,  Rl_J,
        ____, ____, ____, ____, ____,     ____, ____, Rl_B, Rl_YU, COMMA,

        XXXX, XXXX, ____, ____, ____,     ____, ____, ____, XXXX,  XXXX,
    ],
]
# fmt: on

if __name__ == "__main__":
    keyboard.go(hid_type=HIDModes.USB)
