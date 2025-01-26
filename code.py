import board
from kb import KMKKeyboard
from kmk.hid import HIDModes
from split import split
from keymap import keymap

keyboard = KMKKeyboard()
keyboard.modules.append(split)
keyboard.keymap = keymap

if __name__ == "__main__":
    keyboard.go(hid_type=HIDModes.USB)
