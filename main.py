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

server = True


@app.route("/")
def ready():

    return redirect('/system/off')


@app.route("/system/off")
def server_offline():

    global server

    server = False
    switch_server(False)
    print("Server is", str(server))
    return "Server is " + str(server)


@app.route("/system/on")
def server_online():

    global server

    server = True
    switch_server(True)
    print("Server is", str(server))
    return "Server is " + str(server)


@app.route("/alarm")
def alarm_status():

    alarm(True)


if __name__ == '__main__':
    app.run(host='0.0.0.0')