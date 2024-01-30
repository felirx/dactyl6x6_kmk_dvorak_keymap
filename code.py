print("Starting")

import board

from kb import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers
from kmk.keys import KC
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()

layers = Layers()

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

SYMBOLS = KC.MO(3)
MEDIAS = KC.TG(4)
NUMPAD = KC.TG(2)
TODVORK = KC.DF(0)
TOQWERT = KC.DF(1)

split = Split(
    split_type=SplitType.UART,
    data_pin=board.GP0,
    data_pin2=board.GP1,
    use_pio=True
)

keyboard.modules = [layers, split]
keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
    [ #base
        KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,      KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,\
        KC.GRAVE, KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,      KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.EQL,\
        KC.TAB,   KC.QUOT,  KC.COMM,  KC.DOT,   KC.P,     KC.Y,       KC.F,     KC.G,     KC.C,     KC.R,     KC.L,     KC.SLSH,\
        KC.CAPS,  KC.A,     KC.O,     KC.E,     KC.U,     KC.I,       KC.D,     KC.H,     KC.T,     KC.N,     KC.S,     KC.MINS,\
        KC.LSFT,  KC.SCLN,  KC.Q,     KC.J,     KC.K,     KC.X,       KC.B,     KC.M,     KC.W,     KC.V,     KC.Z,     KC.RSFT,\
        KC.LCTL,  KC.P1,    KC.P2,    KC.P3,    KC.SPC,   SYMBOLS,    KC.BSPC,  KC.ENT,   KC.P3,    KC.P2,    KC.P1,    KC.RCTL,\
                            KC.P6,    KC.P7,    KC.P8,    NUMPAD,      KC.P6,    KC.P7,    KC.P8,    MEDIAS 
    ],
    [ #QWERTY
        KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,      KC.F7,    KC.F8,      KC.F9,   KC.F10,   KC.F11,   KC.F12,\
        KC.GRAVE, KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,      KC.N6,    KC.N7,      KC.N8,    KC.N9,    KC.N0,   KC.EQL,\
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,       KC.Y,     KC.U,        KC.I,     KC.O,     KC.P,  KC.SLSH,\
        KC.CAPS,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,       KC.H,     KC.J,        KC.K,     KC.L,  KC.SCLN,  KC.MINS,\
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,       KC.N,     KC.M,     KC.COMM,   KC.DOT,  KC.SLSH,  KC.RSFT,\
        KC.LCTL,  KC.P1,    KC.P2,    KC.P3,    KC.SPC,   SYMBOLS,    KC.BSPC,  KC.ENT,     KC.P3,    KC.P2,    KC.P1,  KC.RCTL,\
                            KC.P6,    KC.P7,    KC.P8,    KC.P9,      KC.P6,    KC.P7,      KC.P8,    KC.P9 
    ],
    [ #numpad?
        _______,  _______,  _______,  _______,  _______,  _______,    _______,  _______,  _______,  _______,  _______,  _______,\
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,    XXXXXXX,  XXXXXXX,  KC.PSLS,  KC.PAST,  KC.PMNS,  XXXXXXX,\
        _______,  XXXXXXX,  XXXXXXX,    KC.UP,  XXXXXXX,  XXXXXXX,    XXXXXXX,    KC.P7,    KC.P8,    KC.P9,  KC.PPLS,  XXXXXXX,\
        _______,  XXXXXXX,  KC.LEFT,  KC.DOWN,  KC.RGHT,  XXXXXXX,    XXXXXXX,    KC.P4,    KC.P5,    KC.P6,  KC.PPLS,  XXXXXXX,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,    XXXXXXX,    KC.P1,    KC.P2,    KC.P3,  KC.PENT,  _______,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,  _______,    _______,  _______,    KC.P0,  KC.PDOT,  KC.PENT,  _______,\
                            _______,  _______,  _______,  _______,    _______,  _______,  _______,  _______
     ],
    [ #symbols that are missink from 6x6 
        _______,  _______,  _______,  _______,  _______,  _______,    _______,  _______,  _______,  _______,  _______,  _______,\
        XXXXXXX,  XXXXXXX,  KC.PSCR,  XXXXXXX,  KC.PAUS,  XXXXXXX,    XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,\
        _______,  XXXXXXX,   KC.INS,  KC.HOME,  KC.PGUP,  XXXXXXX,    XXXXXXX,  XXXXXXX,  KC.LCBR , KC.RCBR,  KC.BSLS,  KC.BSLS,\
        _______,  XXXXXXX,   KC.DEL,   KC.END,  KC.PGDN,  XXXXXXX,    XXXXXXX,  XXXXXXX,  KC.LBRC,  KC.RBRC,  KC.PIPE,  KC.PIPE,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,    XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,  _______,    _______,  _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,\
                            _______,  _______,  _______,  _______,    _______,  _______,  _______,  _______
    ],
    [ #mediakeys and memes
        _______,  _______,  _______,  _______,  _______,  _______,    _______,  _______,  _______,  _______,  _______,  _______,\
        XXXXXXX,  XXXXXXX,  XXXXXXX,  TODVORK,  TOQWERT,  XXXXXXX,    XXXXXXX,  KC.MSTP,  KC.MPRV,  KC.MPLY,  KC.MFFD,  XXXXXXX,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,    XXXXXXX,  XXXXXXX,  XXXXXXX , XXXXXXX,  XXXXXXX,  XXXXXXX,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,    XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,    XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,  _______,    _______,  _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,\
                            _______,  _______,  _______,  _______,    _______,  _______,  _______,  _______
    ]
]

if __name__ == '__main__':
    keyboard.go()
