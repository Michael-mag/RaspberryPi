#!/usr/bin/env python3
"""
    Project : Motion Sensor Using PIR Sensor
    Developed by: MICHAEL MAGAISA
    Email : m.magaisa@jacobs-university.de
    Email : michaelpmagaisa@gmail.com

"""

import RPi.GPIO as GPIO
import time
#import error as err


pir_sensor = 11 #set pin 8(GPIO 14) to sensor
buzzer = 7 #set pin 7(GPIO 4) to buzzer
sensor_state = 0
GPIO.setwarnings(False) #Ignore warnings
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor, GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)


try:
    while True:
        time.sleep(0.1)
        sensor_state = GPIO.input(pir_sensor)
        if sensor_state == 1:
            print("\nMotion detected!!!...\n")
            GPIO.output(buzzer,True)
            time.sleep(1)
            GPIO.output(buzzer,False)
            time.sleep(3)
        else:
            print("No motion")
except KeyboardInterrupt as k:
    pass
finally:
    GPIO.cleanup()

if __name__ == '__main__':
    prepare()
    run()
