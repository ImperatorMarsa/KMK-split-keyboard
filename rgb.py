import board
from storage import getmount

from kmk.extensions.peg_rgb_matrix import Rgb_matrix, Rgb_matrix_data, Color
from kmk.extensions.RGB import RGB, AnimationModes

# rgb = RGB(
#     pixel_pin=board.GP28,
#     num_pixels=18,
#     animation_mode=AnimationModes.SWIRL,
# )

_W = Color.WHITE
_R = Color.RED
_G = Color.GREEN
_B = Color.BLUE
_Y = Color.YELLOW
_P = Color.PURPLE
_T = Color.TEAL
# fmt: off
_key =[
        _W, _W, _W, _W,   _W, _W, _W, _W,
    _W, _W, _W, _W, _W,   _W, _W, _W, _W, _W,
    _W, _W, _W, _W, _W,   _W, _W, _W, _W, _W,
    _W,     _P, _T, _Y,   _G, _B, _R,     _W,
]
# fmt:on
_rightSide = True if str(getmount("/").label).endswith("R") else False

rgb = Rgb_matrix(
    ledDisplay=_key,
    split=True,
    rightSide=_rightSide,
    disable_auto_write=False,
)
