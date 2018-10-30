from gpiozero import *
from time import sleep

from functions.connection import progress

led_Red = LED(3)
led_Green = LED(17)

server = True


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


def server_offline():

    global server

    server = False
    switch_server(False)
    return "Server is Offline\n"


def server_online():

    global server

    server = True
    switch_server(True)
    return "Server is Online\n"


def status_server():

    global server

    if server:
        sleep(.5)
        server_offline()
    else:
        sleep(.5)
        server_online()
