#!/usr/bin/python3

# Import libraries
from flask import Flask
from gpiozero import *

# Import functions
from functions.alarm import alarm

# Import system functions
from system.switch import server_online, server_offline, status_server


# App presets
app = Flask(__name__)

# Main settings
power = False
btn_switch = Button(2)


@app.route("/")
def ready():

    global power

    if power is False:
        power = True
        server_offline()
        return "Server is ready"

    else:
        return "Welcome back"


@app.route('/server/off')
def set_offline():
    server_offline()
    return "Server is Offline\n"


@app.route('/server/on')
def set_online():
    server_online()
    return "Server is Online\n"


@app.route("/alarm/on")
def alarm_on():
    alarm(True)
    return "Server alarm is ON\n"


@app.route("/alarm/off")
def alarm_off():
    alarm(False)
    return "Server alarm is OFF\n"


# btn_switch.is_pressed = status_server()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
