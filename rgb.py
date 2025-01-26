import board

from kmk.extensions.RGB import RGB, AnimationModes

rgb = RGB(
    pixel_pin=board.GP28,
    num_pixels=19,
    animation_mode=AnimationModes.SWIRL,
)
