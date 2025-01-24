import board
from kb import KMKKeyboard, isRight

from kmk.keys import KC
from kmk.hid import HIDModes

keyboard = KMKKeyboard()

### Split #########################################################################################
# split_side = SplitSide.LEFT
# data_pin = board.GP1
# data_pin2 = board.GP0
# if isRight:
#     split_side = SplitSide.RIGHT
#     data_pin = board.GP0
#     data_pin2 = board.GP1

# split = Split(
#     uart_interval=20,
#     data_pin=data_pin,
#     data_pin2=data_pin2,
#     split_type=SplitType.UART,
#     split_side=split_side,
# )
# keyboard.modules.append(split)
###################################################################################################

# fmt: off
keyboard.keymap = [
    [
        KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,
        KC.A,  KC.S,  KC.D,  KC.F,  KC.G,
        KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,
        KC.NO, KC.N1, KC.N2, KC.N3, KC.N4,
    ],
]
# fmt: on

if __name__ == "__main__":
    keyboard.go(hid_type=HIDModes.USB)
