#!/usr/bin/python3


# Import libraries
from gpiozero import *
from flask import Flask, redirect
from time import sleep

# Import functions
from functions.alarm import alarm
from functions.connection import connected, progress
from system.switch import switch_server

# App presets
app = Flask(__name__)

# Main settings
server = True
power = False

# Server switch
btn_switch = Button(2)


@app.route("/")
def ready():

    global power

    if power is False:

        power = True

        return redirect('/system/off')

    else:

        return redirect('/home')


@app.route("/home")
def home():

    while True:

        global server

        if btn_switch.is_pressed:

            if server:
                sleep(.5)
                return redirect('/system/off')
            else:
                sleep(.5)
                return redirect('/system/on')


@app.route("/system/off")
def server_offline():

    global server

    server = False
    switch_server(False)
    print("Server is", str(server))
    return redirect('/home')


@app.route("/system/on")
def server_online():

    global server

    server = True
    switch_server(True)
    print("Server is", str(server))
    return redirect('/home')


@app.route("/alarm")
def alarm_status():

    alarm(True)


if __name__ == '__main__':
    app.run(host='0.0.0.0')