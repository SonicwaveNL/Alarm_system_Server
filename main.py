#!/usr/bin/python3

# Import libraries
from flask import Flask
from gpiozero import *
from time import sleep
import threading

# Import system functions
from system.switch import server_online, server_offline, server, status_server, led_Red


# App presets
app = Flask(__name__)

# Main settings
power = False
status_alarm = False
buzzer_Alarm = Buzzer(27)
btn_switch = Button(2)


# Switches the server when the black button is pressed & Turns the alarm on/off when client hits the red button
@app.before_first_request
def light_thread():
    def run():

        while True:

            if btn_switch.is_pressed:

                print("Switching server!")

                status_server()

            if status_alarm:

                sleep(0.5)
                buzzer_Alarm.on()
                led_Red.off()
                sleep(0.5)
                buzzer_Alarm.off()
                led_Red.on()

    thread = threading.Thread(target=run)
    thread.start()


# Turns the server on when the first client connects
@app.route("/")
def ready():

    global power

    if power is False:
        power = True
        server_offline()
        return "Server is ready"

    else:
        return "Welcome back"


# Switches the server to OFF
@app.route('/server/off')
def set_offline():
    server_offline()
    return "Server is Offline\n"


# Switches the server to ON
@app.route('/server/on')
def set_online():
    server_online()
    return "Server is Online\n"


# Switches the alarm to ON
@app.route("/alarm/on")
def alarm_on():

    global status_alarm

    # Checks if the server is online
    if server:
        status_alarm = False
        return "Server alarm is ON\n"
    else:
        status_alarm = True
        return "Server is offline\n"


# Switches the alarm to OFF
@app.route("/alarm/off")
def alarm_off():
    global status_alarm
    status_alarm = True
    return "Server alarm is OFF\n"


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
