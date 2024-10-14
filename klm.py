# tag::one[]
from machine import Pin
from picographics import PicoGraphics, DISPLAY_TUFTY_2040
from time import sleep, sleep_ms
from pimoroni import Button

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

display.set_pen(WHITE)
display.text("Kölsch", 0, 0, 320, 4)
display.text("Intellijenz", 10, 30, 320, 4)

display.set_pen(RED)
display.text("Annemie, ich kann nit mieh!", 0, 100, 320, 4)
display.update()

button_a = Button(7, invert=False)
button_b = Button(8, invert=False)
button_c = Button(9, invert=False)
button_up = Button(22, invert=False)
button_down = Button(6, invert=False)
button_boot = Button(23, invert=True)

WIDTH, HEIGHT = display.get_bounds()

# Kölle Alaaf, Kölsch, Konfettiregen, 
# Wie isset?

while True:
    if button_a.is_pressed:                               # if a button press is detected then...
        display.set_pen(BLACK)                            # set pen to black
        display.clear()                                   # clear display to the pen colour
        display.set_pen(WHITE)                            # change the pen colour
        display.text("Annemie, ich kann nit mieh!", 10, 10, WIDTH - 10, 3)  # display some text on the screen
        display.update()                                  # update the display
        sleep(1)                                    # pause for a sec

    elif button_b.is_pressed:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(TEAL)
        display.text("Mer muss och jünne künne.", 10, 10, WIDTH - 10, 3)
        display.update()
        sleep(1)

    elif button_c.is_pressed:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(MAGENTA)
        display.text("Fließ kanns de vürdäusche, fuul muss de schon sin.", 10, 10, WIDTH - 10, 3)
        display.update()
        sleep(1)

    elif button_up.is_pressed:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(YELLOW)
        display.text("Jede Jeck es anders", 10, 10, WIDTH - 10, 3)
        display.update()
        sleep(1)

    elif button_down.is_pressed:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(GREEN)
        display.text("Button DOWN pressed", 10, 10, WIDTH - 10, 3)
        display.update()
        sleep(1)

    elif button_boot.is_pressed:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(BLUE)
        display.text("Button BOOT/USR pressed", 10, 10, WIDTH - 10, 3)
        display.update()
        sleep(1)

    else:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(RED)
        display.text("Kölsch Intellijenz", 10, 10, WIDTH, 3)
        display.update()

    sleep(0.1)  # this number is how frequently Tufty checks for button presseswhile True:
    if button_a.is_pressed:                               # if a button press is detected then...
        display.set_pen(BLACK)                            # set pen to black
        display.clear()                                   # clear display to the pen colour
        display.set_pen(WHITE)                            # change the pen colour
        display.text("Annemie, ich kann nit mieh!", 10, 10, WIDTH - 10, 3)  # display some text on the screen
        display.update()                                  # update the display
        sleep(1)                                    # pause for a sec

    elif button_b.is_pressed:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(TEAL)
        display.text("Mer muss och jünne künne.", 10, 10, WIDTH - 10, 3)
        display.update()
        sleep(1)

    elif button_c.is_pressed:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(MAGENTA)
        display.text("Fließ kanns de vürdäusche, fuul muss de schon sin.", 10, 10, WIDTH - 10, 3)
        display.update()
        sleep(1)

    elif button_up.is_pressed:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(YELLOW)
        display.text("Jede Jeck es anders", 10, 10, WIDTH - 10, 3)
        display.update()
        sleep(1)

    elif button_down.is_pressed:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(GREEN)
        display.text("Button DOWN pressed", 10, 10, WIDTH - 10, 3)
        display.update()
        sleep(1)

    elif button_boot.is_pressed:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(BLUE)
        display.text("Button BOOT/USR pressed", 10, 10, WIDTH - 10, 3)
        display.update()
        sleep(1)

    else:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(WHITE)
        display.text("Kölsch Intellijenz", 10, 10, WIDTH, 3)
        display.update()

    sleep(0.1)  # this number is how frequently Tufty checks for button presses

# end::three[]