#!/usr/bin/python3


# Import libraries
from gpiozero import *
from flask import Flask

# Import functions
from functions.connection import connected

# App presets
app = Flask(__name__)

# Input presets
button_switch = Button(2)

# Ouput presets
led_Red = LED(3)
led_Green = LED(17)


@app.route("/")
def ready():

    print("Client connected to Server")
    return "Client connected to Server\n"

    connected(True)


if __name__ == '__main__':
    app.run(host='0.0.0.0')