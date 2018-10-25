from gpiozero import *
from time import sleep

from functions.connection import progress


led_Red = LED(3)
led_Green = LED(17)


def switch_server(status):

    if status:
        sleep(1)
        led_Green.off()
        progress()
        sleep(1)
        led_Red.on()

    else:
        sleep(1)
        led_Red.off()
        progress()
        sleep(1)
        led_Green.on()
