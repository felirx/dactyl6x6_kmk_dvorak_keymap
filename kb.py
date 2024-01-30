import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
            board.GP6,
            board.GP7,
            board.GP8,
            board.GP9,
            board.GP10,
            board.GP11
    )
    row_pins = (
            board.GP16,
            board.GP17,
            board.GP18,
            board.GP19,
            board.GP20,
            board.GP21,
            board.GP22
    )
    diode_orientation = DiodeOrientation.COL2ROW
    # flake8: noqa
    # fmt: off
    coord_mapping = [             
         0,  1,  2,  3,  4,  5,     47, 46, 45, 44, 43, 42,
         6,  7,  8,  9, 10, 11,     53, 52, 51, 50, 49, 48, 
        12, 13, 14, 15, 16, 17,     59, 58, 57, 56, 55, 54,
        18, 19, 20, 21, 22, 23,     65, 64, 63, 62, 61, 60,
        24, 25, 26, 27, 28, 29,     71, 70, 69, 68, 67, 66,
        30, 31, 32, 33, 34, 35,     77, 76, 75, 74, 73, 72,
                38, 39, 40, 41,     83, 82, 81, 80
    ]  
