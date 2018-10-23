from gpiozero import *
from time import sleep

led_Yellow = LED(4)


def connected(status):
    while status:
        sleep(1)
        led_Yellow.on()
        sleep(1)
        led_Yellow.off()
