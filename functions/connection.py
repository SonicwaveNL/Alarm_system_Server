from gpiozero import *
from time import sleep

led_Yellow = LED(4)

# Shows with a blinking light that the server is in progress


def progress():

    blink = 0

    while blink < 3:
        sleep(0.5)
        led_Yellow.on()
        sleep(0.5)
        led_Yellow.off()
        blink += 1