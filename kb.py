from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        pins[29],
        pins[28],
        pins[27],
        pins[26],
        pins[15],
    )
    row_pins = (
        pins[11],
        pins[12],
        pins[13],
        pins[14],
        pins[14],
    )
    diode_orientation = DiodeOrientation.COL2ROW
    data_pin = pins[1]
    data_pin2 = pins[0]

    # fmt: off
    coord_mapping = [
        00, 01, 02, 03, 04, 05,   29, 28, 27, 26, 25, 24,
        06, 07, 08, 09, 10, 11,   35, 34, 33, 32, 31, 30,
        12, 13, 14, 15, 16, 17,   41, 40, 39, 38, 37, 36,
        18, 19, 20, 21, 22, 23,   47, 46, 45, 44, 43, 42,
    ]
    # fmt:on
