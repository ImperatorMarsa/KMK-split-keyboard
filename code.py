import time
import board
import neopixel

# Define the number of pixels and the pin connected to the WS2812 data line
num_pixels = 1
pixel_pin = board.NEOPIXEL

# Initialize the NeoPixel object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels)


# Define the blink animation
def blink(pixel, color, delay):
    pixels[pixel] = color
    time.sleep(delay)
    pixels[pixel] = (0, 0, 0)  # Turn off


# Blink the LED at pixel 0 with purple color and 0.5-second delay
blink(0, (255, 0, 255), 0.5)

# Run the animation loop
while True:
    blink(0, (0, 0, 255), 0.5)  # Blink on
    time.sleep(1)  # Pause for 1 second
    blink(0, (0, 255, 0), 0.5)  # Blink on
    time.sleep(1)  # Pause for 1 second
    blink(0, (255, 0, 0), 0.5)  # Blink on
    time.sleep(1)  # Pause for 1 second
