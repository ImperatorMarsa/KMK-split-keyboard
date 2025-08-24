from kmk.hid import HIDModes
from split import split
from miryoku import keyboard

keyboard.modules.append(split)

if __name__ == "__main__":
    keyboard.go(hid_type=HIDModes.USB)
