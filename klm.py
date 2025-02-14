# tag::one[]
from machine import Pin
from picographics import PicoGraphics, DISPLAY_TUFTY_2040
from time import sleep, sleep_ms
from pimoroni import Button
import jpegdec
import time

# https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/modules/picographics/README.md#changing-the-font

# turn LED on and off

led = Pin(25, Pin.OUT)
led.value(1)
sleep(1)
led.value(0)

# end::one[]
# tag::two[]

# Console Input and Output
# name = input("you name: ")
# print ("Hello "+name)

# end::two[]
# tag::three[]

# write Text on Display
display = PicoGraphics(display=DISPLAY_TUFTY_2040)

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
TEAL = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
RED = display.create_pen(255, 0, 0)
GREEN = display.create_pen(0, 255, 0)
BLUE = display.create_pen(0, 0, 255)

button_a = Button(7, invert=False)
button_b = Button(8, invert=False)
button_c = Button(9, invert=False)
button_up = Button(22, invert=False)
button_down = Button(6, invert=False)
button_boot = Button(23, invert=True)

WIDTH, HEIGHT = display.get_bounds()

display.set_font("bitmap8")

# Kölle Alaaf, Kölsch, Konfettiregen, 
# Wie isset?

j = jpegdec.JPEG(display)

button_up = Button(22, invert=False)
button_down = Button(6, invert=False)
button_a = Button(7, invert=False)

artikel = [
    "Et es wie et es.",
    "Et kütt wie et kütt.",
    "Et hätt noch emmer joot jejange.",
    "Wat fott es, es fott.",
    "Et bliev nix wie et wor.",
    "Kenne mer nit, bruche mer nit, fott domet.",
    "Wat wellste maache?",
    "Maach et joot, ävver nit zo off.",
    "Wat soll dä Kwatsch?",
    "Drinks de ejne met?",
    "Do laachs de disch kapott."
]

try:
   # Open the JPEG file
    j.open_file("KLM.jpg")

    # Draws a box around the image

    # Decode the JPEG
    j.decode(0, 0, jpegdec.JPEG_SCALE_FULL, dither=True)

# Handle the error if the image doesn't exist on the flash.
except OSError:
    print("Error: jpg File missing. Copy the PNG file from the example folder to your Pico using Thonny and run the example again.")

def contrastText(d, c, t, x, y, w, h):
    d.set_pen(BLACK)
    d.text(t,  x-2, y-2, w, h)
    d.set_pen(WHITE)
    d.text(t,  x+1, y+2, w, h)
    d.set_pen(c)
    d.text(t, x, y, w, h)


display.set_pen(BLACK)
display.text("Fraag misch ens!", 10, 2, 320, 4)
    
    
text = artikel[4]

display.set_font("bitmap8")

contrastText(display, RED, text, 10, 150, 300, 4)
# contrastText(display, GREEN, "JOT", 240, 55, 80, 4)

# contrastText(display, RED, "NIT SO JOT", 100, 155, 240, 4)

display.update()

led = Pin(25, Pin.OUT)

while True:    
    t = time.ticks_ms() / 1000.0

    while button_up.is_pressed:
        led.value(1)
        time.sleep(1.0)
        led.value(0)
        time.sleep(0.01)


# end::three[]