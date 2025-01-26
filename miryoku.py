import board
from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.power import Power
from kmk.modules.tapdance import TapDance
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.capsword import CapsWord

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(Power())
keyboard.modules.append(TapDance())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(CapsWord())

# fmt: off
keyboard.keymap = [
# BASE
[
KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P,
KC.HT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.G, KC.H, KC.HT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.QUOT, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200),
KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.HT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.HT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=200),
KC.NO, KC.NO, KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.NO, KC.NO
],
# EXTRA
[
KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P,
KC.HT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.G, KC.H, KC.HT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.QUOT, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200),
KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.HT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.HT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=200),
KC.NO, KC.NO, KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.NO, KC.NO
],
# TAP
[
KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P,
KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.QUOT,
KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH,
KC.NO, KC.NO, KC.ESC, KC.SPC, KC.TAB, KC.ENT, KC.BSPC, KC.DEL, KC.NO, KC.NO
],
# BUTTON
[
KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
KC.NO, KC.NO, KC.MB_MMB, KC.MB_LMB, KC.MB_RMB, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB, KC.NO, KC.NO
],
# NAV
[
KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, KC.TD(KC.CW, KC.CAPS, tap_time=200),
KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.NO, KC.HOME, KC.PGDN, KC.PGUP, KC.END, KC.INS,
KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.ENT, KC.BSPC, KC.DEL, KC.NO, KC.NO
],
# MOUSE
[
KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.MS_LT, KC.MS_DN, KC.MS_UP, KC.MS_RT, KC.NO,
KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.NO, KC.NO, KC.MW_DN, KC.MW_UP, KC.NO, KC.NO,
KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB, KC.NO, KC.NO
],
# MEDIA
[
KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.RGB_HUI, KC.RGB_SAI, KC.RGB_VAI, KC.RGB_TOG,
KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.MPRV, KC.VOLD, KC.VOLU, KC.MNXT, KC.PS_TOG,
KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(9), tap_time=200), KC.TD(KC.NO, KC.DF(6), tap_time=200), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.HID,
KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.MSTP, KC.MPLY, KC.MUTE, KC.NO, KC.NO
],
# NUM
[
KC.LBRC, KC.N7, KC.N8, KC.N9, KC.RBRC, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200),
KC.SCLN, KC.N4, KC.N5, KC.N6, KC.EQL, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
KC.GRV, KC.N1, KC.N2, KC.N3, KC.BSLS, KC.NO, KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.RALT, KC.NO,
KC.NO, KC.NO, KC.DOT, KC.N0, KC.MINS, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
],
# SYM
[
KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200),
KC.COLN, KC.DLR, KC.PERC, KC.CIRC, KC.PLUS, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
KC.TILD, KC.EXLM, KC.AT, KC.HASH, KC.PIPE, KC.NO, KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.RALT, KC.NO,
KC.NO, KC.NO, KC.LPRN, KC.RPRN, KC.UNDS, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
],
# FUN
[
KC.F12, KC.F7, KC.F8, KC.F9, KC.PSCR, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200),
KC.F11, KC.F4, KC.F5, KC.F6, KC.SLCK, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
KC.F10, KC.F1, KC.F2, KC.F3, KC.PAUS, KC.NO, KC.TD(KC.NO, KC.DF(9), tap_time=200), KC.TD(KC.NO, KC.DF(6), tap_time=200), KC.RALT, KC.NO,
KC.NO, KC.NO, KC.APP, KC.SPC, KC.TAB, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
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

if __name__ == "__main__":
    print("starting Miryoku KMK")
    keyboard.go()
