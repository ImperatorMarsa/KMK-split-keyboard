from kb import KMKKeyboard
from encoder import encoder_handler, setUpEncoder

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.power import Power
from kmk.modules.tapdance import TapDance
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.capsword import CapsWord
from kmk.extensions.international import International

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(Power())
keyboard.modules.append(TapDance())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(CapsWord())
keyboard.extensions.append(International())
keyboard.modules.append(encoder_handler)

setUpEncoder(encoder_handler)
# tap_time
tt = 200

# --- Помощники для читаемости ---
_______ = KC.TRNS
XXXXXXX = KC.NO

### HomeRow functions
A_ALT = KC.HT(KC.A, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=tt)
S_GUI = KC.HT(KC.S, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=tt)
D_CTL = KC.HT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=tt)
F_SFT = KC.HT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=tt)

J_SFT = KC.HT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=tt)
K_CTL = KC.HT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=tt)
L_GUI = KC.HT(KC.L, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=tt)
QUOT_ALT = KC.HT(KC.QUOT, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=tt)
###

# fmt: off
keyboard.keymap = [
# BASE
[
KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P,
A_ALT, S_GUI, D_CTL, F_SFT, KC.G, KC.H, J_SFT, K_CTL, L_GUI, QUOT_ALT,
KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=tt), KC.HT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=tt), KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.HT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=tt), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=tt),
XXXXXXX, XXXXXXX, KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=tt), KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=tt), KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=tt), KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=tt), KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=tt), KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=tt), XXXXXXX, XXXXXXX
],
# EXTRA
[
KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P,
A_ALT, S_GUI, D_CTL, F_SFT, KC.G, KC.H, J_SFT, K_CTL, L_GUI, QUOT_ALT,
KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=tt), KC.HT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=tt), KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.HT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=tt), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=tt),
XXXXXXX, XXXXXXX, KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=tt), KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=tt), KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=tt), KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=tt), KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=tt), KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=tt), XXXXXXX, XXXXXXX
],
# TAP
[
KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P,
KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.QUOT,
KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH,
XXXXXXX, XXXXXXX, KC.ESC, KC.SPC, KC.TAB, KC.ENT, KC.BSPC, KC.DEL, XXXXXXX, XXXXXXX
],
# BUTTON
[
XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
KC.LALT, KC.LGUI, KC.LCTL, KC.LSFT, XXXXXXX, XXXXXXX, KC.LSFT, KC.LCTL, KC.LGUI, KC.LALT,
XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
XXXXXXX, XXXXXXX, KC.MB_MMB, KC.MB_LMB, KC.MB_RMB, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB, XXXXXXX, XXXXXXX
],
# NAV
[
KC.TD(XXXXXXX, KC.RELOAD, tap_time=tt), KC.TD(XXXXXXX, KC.DF(2), tap_time=tt), KC.TD(XXXXXXX, KC.DF(1), tap_time=tt), KC.TD(XXXXXXX, KC.DF(0), tap_time=tt), XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
KC.LALT, KC.LGUI, KC.LCTL, KC.LSFT, XXXXXXX, KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, KC.TD(KC.CW, KC.CAPS, tap_time=tt),
XXXXXXX, KC.RALT, KC.TD(XXXXXXX, KC.DF(7), tap_time=tt), KC.TD(XXXXXXX, KC.DF(4), tap_time=tt), XXXXXXX, KC.HOME, KC.PGDN, KC.PGUP, KC.END, KC.INS,
XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.ENT, KC.BSPC, KC.DEL, XXXXXXX, XXXXXXX
],
# MOUSE
[
KC.TD(XXXXXXX, KC.RELOAD, tap_time=tt), KC.TD(XXXXXXX, KC.DF(2), tap_time=tt), KC.TD(XXXXXXX, KC.DF(1), tap_time=tt), KC.TD(XXXXXXX, KC.DF(0), tap_time=tt), XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
KC.LALT, KC.LGUI, KC.LCTL, KC.LSFT, XXXXXXX, KC.MS_LT, KC.MS_DN, KC.MS_UP, KC.MS_RT, XXXXXXX,
XXXXXXX, KC.RALT, KC.TD(XXXXXXX, KC.DF(8), tap_time=tt), KC.TD(XXXXXXX, KC.DF(5), tap_time=tt), XXXXXXX, XXXXXXX, KC.MW_DN, KC.MW_UP, XXXXXXX, XXXXXXX,
XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB, XXXXXXX, XXXXXXX
],
# MEDIA
[
KC.TD(XXXXXXX, KC.RELOAD, tap_time=tt), KC.TD(XXXXXXX, KC.DF(2), tap_time=tt), KC.TD(XXXXXXX, KC.DF(1), tap_time=tt), KC.TD(XXXXXXX, KC.DF(0), tap_time=tt), XXXXXXX, XXXXXXX, KC.RGB_HUI, KC.RGB_SAI, KC.RGB_VAI, KC.RGB_TOG,
KC.LALT, KC.LGUI, KC.LCTL, KC.LSFT, XXXXXXX, KC.MPRV, KC.VOLD, KC.VOLU, KC.MNXT, KC.PS_TOG,
XXXXXXX, KC.RALT, KC.TD(XXXXXXX, KC.DF(9), tap_time=tt), KC.TD(XXXXXXX, KC.DF(6), tap_time=tt), XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.HID,
XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.MSTP, KC.MPLY, KC.MUTE, XXXXXXX, XXXXXXX
],
# NUM
[
KC.LBRC, KC.N7, KC.N8, KC.N9, KC.RBRC, XXXXXXX, KC.TD(XXXXXXX, KC.DF(0), tap_time=tt), KC.TD(XXXXXXX, KC.DF(1), tap_time=tt), KC.TD(XXXXXXX, KC.DF(2), tap_time=tt), KC.TD(XXXXXXX, KC.RELOAD, tap_time=tt),
KC.SCLN, KC.N4, KC.N5, KC.N6, KC.EQL, XXXXXXX, KC.LSFT, KC.LCTL, KC.LGUI, KC.LALT,
KC.GRV, KC.N1, KC.N2, KC.N3, KC.BSLS, XXXXXXX, KC.TD(XXXXXXX, KC.DF(7), tap_time=tt), KC.TD(XXXXXXX, KC.DF(4), tap_time=tt), KC.RALT, XXXXXXX,
XXXXXXX, XXXXXXX, KC.DOT, KC.N0, KC.MINS, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX
],
# SYM
[
KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR, XXXXXXX, KC.TD(XXXXXXX, KC.DF(0), tap_time=tt), KC.TD(XXXXXXX, KC.DF(1), tap_time=tt), KC.TD(XXXXXXX, KC.DF(2), tap_time=tt), KC.TD(XXXXXXX, KC.RELOAD, tap_time=tt),
KC.COLN, KC.DLR, KC.PERC, KC.CIRC, KC.PLUS, XXXXXXX, KC.LSFT, KC.LCTL, KC.LGUI, KC.LALT,
KC.TILD, KC.EXLM, KC.AT, KC.HASH, KC.PIPE, XXXXXXX, KC.TD(XXXXXXX, KC.DF(8), tap_time=tt), KC.TD(XXXXXXX, KC.DF(5), tap_time=tt), KC.RALT, XXXXXXX,
XXXXXXX, XXXXXXX, KC.LPRN, KC.RPRN, KC.UNDS, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX
],
# FUN
[
KC.F12, KC.F7, KC.F8, KC.F9, KC.PSCR, XXXXXXX, KC.TD(XXXXXXX, KC.DF(0), tap_time=tt), KC.TD(XXXXXXX, KC.DF(1), tap_time=tt), KC.TD(XXXXXXX, KC.DF(2), tap_time=tt), KC.TD(XXXXXXX, KC.RELOAD, tap_time=tt),
KC.F11, KC.F4, KC.F5, KC.F6, KC.SLCK, XXXXXXX, KC.LSFT, KC.LCTL, KC.LGUI, KC.LALT,
KC.F10, KC.F1, KC.F2, KC.F3, KC.PAUS, XXXXXXX, KC.TD(XXXXXXX, KC.DF(9), tap_time=tt), KC.TD(XXXXXXX, KC.DF(6), tap_time=tt), KC.RALT, XXXXXXX,
XXXXXXX, XXXXXXX, KC.APP, KC.SPC, KC.TAB, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX
],
]
# fmt: on

layer_names_list = [
    "Base",
    "Extra",
    "Tap",
    "Button",
    "Nav",
    "Mouse",
    "Media",
    "Num",
    "Sym",
    "Fun",
]
