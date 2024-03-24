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

RAISE = KC.MO(3)
MEMES = KC.TG(4)
LOWER = KC.TG(2)
LOWEH = KC.MO(2)
TODVORK = KC.DF(1)
TOQWERT = KC.DF(0)

split = Split(
    split_type=SplitType.UART,
    data_pin=board.GP0,
    data_pin2=board.GP1,
    use_pio=True,
    uart_flip=True
)

keyboard.modules = [layers, split]
keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
    [ #QWERTY
        KC.F12,   KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,      KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,\
        KC.GRAVE, KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,      KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.RBRC,\
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,       KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.LBRC,\
        KC.ESC,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,       KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,\
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,       KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,\
        XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.LALT,  XXXXXXX,  XXXXXXX,    LOWER,    KC.DEL,   KC.RALT,  KC.MINUS, KC.EQUAL, KC.RCTL,\
                            KC.LCTL,  KC.SPC,   KC.LSFT,  KC.LGUI,    RAISE,    KC.RSFT,  KC.BSPC,  LOWEH
     ],
    [ #backup dvorak if no sys support
        KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,      KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,\
        KC.GRAVE, KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,      KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.EQUAL,\
        KC.TAB,   KC.QUOT,  KC.COMM,  KC.DOT,   KC.P,     KC.Y,       KC.F,     KC.G,     KC.C,     KC.R,     KC.L,     KC.SLASH,\
        KC.ESC,   KC.A,     KC.O,     KC.E,     KC.U,     KC.I,       KC.D,     KC.H,     KC.T,     KC.N,     KC.S,     KC.MINS,\
        KC.LSFT,  KC.SCLN,  KC.Q,     KC.J,     KC.K,     KC.X,       KC.B,     KC.M,     KC.W,     KC.V,     KC.Z,     KC.RSFT,\
        XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.LALT,  XXXXXXX,  XXXXXXX,    LOWER,    KC.DEL,   KC.RALT,  KC.LBRC,  KC.RBRC,  KC.RCTL,\
                            KC.LCTL,  KC.SPC,   KC.LSFT,  KC.LGUI,    RAISE,    KC.RSFT,  KC.BSPC,  LOWEH
     ],
    [ #numpad, mediakeys, arrows, stuff
        _______,  _______,  _______,  _______,  _______,  _______,    _______,  _______,  _______,  _______,  _______,  _______,\
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,    XXXXXXX,  XXXXXXX,  KC.PSLS,  KC.PAST,  KC.PMNS,  XXXXXXX,\
        _______,  KC.LPRN,  KC.RPRN,  KC.UP,    KC.MINUS, KC.EQUAL,   XXXXXXX,  KC.P7,    KC.P8,    KC.P9,    KC.PPLS,  XXXXXXX,\
        _______,  KC.LCBR,  KC.LEFT,  KC.DOWN,  KC.RGHT,  KC.PIPE,    KC.CAPS,  KC.P4,    KC.P5,    KC.P6,    KC.ENT,   XXXXXXX,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.V,     KC.BSLS,    XXXXXXX,  KC.P1,    KC.P2,    KC.P3,    KC.PENT,  _______,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,  _______,    _______,  _______,  KC.P0,    KC.PDOT,  KC.PENT,  _______,\
                            _______,  _______,  _______,  _______,    _______,  _______,  _______,  _______
     ],
    [ #symbols that are missink from 6x6 
        _______,  _______,  _______,  _______,  _______,  _______,    _______,  _______,  _______,  _______,  _______,  _______,\
        XXXXXXX,  KC.INS,   KC.PSCR,  XXXXXXX,  KC.PAUS,  KC.HOME,    TODVORK,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.PGUP,    TOQWERT,  XXXXXXX,  XXXXXXX , XXXXXXX,  XXXXXXX,  XXXXXXX,\
        _______,  KC.MSTP,  KC.MPRV,  KC.MPLY,  KC.MNXT,  KC.PGDN,    MEMES,    XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.END,     XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,  _______,    _______,  _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,\
                            _______,  _______,  _______,  _______,    _______,  _______,  _______,  _______
    ],
    [ #memes
        _______,  _______,  _______,  _______,  _______,  _______,    _______,  _______,  _______,  _______,  _______,  _______,\
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  MEMES,      KC.N6,    XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,    KC.Y,     XXXXXXX,  XXXXXXX , XXXXXXX,  XXXXXXX,  XXXXXXX,\
        _______,  KC.A,     KC.S,     KC.D,     KC.F,     XXXXXXX,    XXXXXXX,  KC.J,     KC.K,     KC.L,     KC.SCLN,  XXXXXXX,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,    XXXXXXX,  KC.M,     KC.COMM,  KC.DOT,   XXXXXXX,  _______,\
        _______,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,  _______,    KC.Z,     XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  _______,\
                            XXXXXXX,  _______,  XXXXXXX,  _______,    _______,  _______,  _______,  _______
    ]
]

if __name__ == '__main__':
    keyboard.go()
