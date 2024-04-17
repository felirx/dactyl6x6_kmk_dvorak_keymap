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
            board.GP11,
            board.GP12,
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
         0,  1,  2,  3,  4,  5,             54, 53, 52, 51, 50, 49,
         7,  8,  9, 10, 11, 12, 13,     62, 61, 60, 59, 58, 57, 56,
        14, 15, 16, 17, 18, 19, 20,     69, 68, 67, 66, 65, 64, 63,
        21, 22, 23, 24, 25, 26, 27,     76, 75, 74, 73, 72, 71, 70,
        28, 29, 30, 31, 32, 33,             82, 81, 80, 79, 78, 77,
        35, 36, 37, 38, 39, 40,             89, 88, 87, 86, 85, 84,
                44, 45, 46, 47,             96, 95, 94, 93
    ]  
