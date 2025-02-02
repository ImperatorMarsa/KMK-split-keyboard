import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP13,  # col 4
        board.GP12,  # col 3
        board.GP11,  # col 2
        board.GP10,  # col 1
        board.GP9,  # col 0
    )
    row_pins = (
        board.GP7,  # row 0
        board.GP8,  # row 1
        board.GP14,  # row 2
        board.GP15,  # row 3
    )

    diode_orientation = DiodeOrientation.COL2ROW

    # fmt: off
    coord_mapping = [
        05, 01, 02, 03, 04,   35, 36, 37, 38, 34,
        10, 06, 07, 08, 09,   30, 31, 32, 33, 29,
        15, 11, 12, 13, 14,   25, 26, 27, 28, 24,
        00, 16, 17, 18, 19,   20, 21, 22, 23, 39,
    ]
    # fmt:on

    # fmt: off
    led_key_pos =[
            00, 01, 02, 03,   21, 20, 19, 18,
        04, 05, 06, 07, 08,   26, 25, 24, 23, 22,
        09, 10, 11, 12, 13,   31, 30, 29, 28, 27,
        17,     16, 15, 14,   32, 33, 34,     35,
    ]
    # fmt:on
    brightness_limit = 0.2
    rgb_pixel_pin = board.GP28
    num_pixels = 36
    rgb_num_pixels = 36
