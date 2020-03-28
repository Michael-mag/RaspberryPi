
#!/usr/bin/env python3

"""
Author : MICHAEL MAGAISA
Email : m.magaisa@jacobs-university
Date : 1.03.2020


A web API used to blink an LED

"""

import os
import time
import RPi.GPIO as GPIO
from flask import Flask , render_template, request,url_for , jsonify

#define the custom paths in which the html and the static styling files are
template_path = os.path.abspath('../templates/html_pages') #for html files
static_path =  os.path.abspath('../static') #make everyone inside static static
#if the css, js and images are put in this folder path then they are made static


app = Flask(__name__,
               template_folder = template_path,
               static_folder = static_path
           )

class BLINK:
   def __init__ (self):
       self.app = app
       app.config["DEBUG"] = True

       #some setup
       GPIO.setmode(GPIO.BCM) #Set to physical pin numbering in board
       GPIO.setwarnings(False) #disable warnings
       #Set pi 8 on the board to be the output and set initial value to low
       #make a dictionary of the pins to be used
       pins = {
          21 : {'name' : 'GPIO 21', 'state' : GPIO.LOW},
          18 : {'name' : 'GPIO 24', 'state' : GPIO.LOW}}
                #make each pin stored in the dictionary initially LOW
       for pin in pins:
           GPIO.setup(pin, GPIO.OUT, initial = GPIO.LOW)




       #landing page
       @app.route('/')
       def landing_page():
           #first for each pin inside the pins dictionary report the state
           for pin in pins:
               #store the state in the state variable of the pins dictionary
               pins[pin]['state'] = GPIO.input(pin)


           homedata = {
                'pins' : pins
           }
           #render the html template and pass the variables inside homedata
           return render_template('index.html',**homedata)


       #perfom some action
       @app.route("/<changePin>/<action>")
       def action(changePin, action) :
           #convert the pin from the url into an integer
           changePin = int(changePin)
           #get the device name whose pin is changed
           device = pins[changePin]['name']

           try:
               #depending on the state that is reported, either turn the led on or off
               if action == "on":
                   GPIO.output(changePin, GPIO.HIGH)
                   display = device + "Turned ON." #message to be displayed on web
               if action == "off":
                   GPIO.output(changePin,GPIO.LOW)
                   display = device + "Turned OFF" #display this on the web
           except Exception as e:
               print("An error occured, read below : \n")
               print(e)

           #read and store the current state of each pin inside the pins dictionary
           for pin in pins:
               pins[pin]['state'] = GPIO.input(pin)

           actionData = {
               "pins" : pins
           }
           #render the actions html template and pass in the variables in the actions
               #dictionary
           return render_template('action.html', **actionData)

if __name__ == "__main__":
   """
       Using my router, I have my Mac and my Pi connected on the same network
           so that I will be able to ssh it from my mac and connect to the
           pi webserver from any device that is also on my network
       The IP address of the Pi is 192.168.0.102
       To be able to access it from my Mac, I have to pass in the IP adress as the
           host argument in the api.app.run() below.
       Also the port number has to be specified as I blocked the default port
           for other reasons
   """
   api = BLINK()
   api.app.run(host='192.168.0.102', port=8080, debug=True)
