from gpiozero import *
from time import sleep

buzzer_Alarm = Buzzer(27)


def alarm(status):
    while status:
        sleep(1)
        buzzer_Alarm.on()
        sleep(1)
        buzzer_Alarm.off()
