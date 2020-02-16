#!/usr/bin/env python3

import RPi.GPIO as GPIO #import the raspberry pi GPIO library
from time import sleep #import the sleep function from the time module

#Ignore warnings for now
GPIO.setwarnings(False)

#Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

#Set pi 8 on the board to be the output and set initial value to low
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW)

#run forever
while(True):
    GPIO.output(8, GPIO.HIGH) #Turn LED on
    sleep(1) #sleep for a second before turning off
    GPIO.output(8, GPIO.LOW)
    sleep(1)
