import os
import RPi.GPIO as GPIO
from flask import Flask, render_template,Response
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

pin1 = 6
pin2 = 13
pin3 = 19
pin4 = 26
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)
GPIO.setup(pin4,GPIO.OUT)



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome.html')
    # print("Hello Test server")
    # return {
    #     "username":"MIkail",
    #     "password":"1213123"
    # }
    # print("Test route")
    # GPIO.output(18,GPIO.HIGH)
def full():
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.HIGH)


def turnOff():
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.HIGH)

def turnOn():
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.LOW)
                                                
def moveForward():
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.HIGH)

def moveBackward():
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.LOW)

def moveLeft():
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.HIGH)

def moveRight():
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.HIGH)                                             


@app.route('/on')
def on():
    turnOn()
    return {"success":"true"}


@app.route('/off')
def off():
    turnOff()
    # GPIO.output(18,GPIO.LOW)
    return {"success":"true"}

@app.route('/forward')
def forward():
    moveForward()
    # GPIO.output(18,GPIO.HIGH)
    return {"success":"true"}

@app.route('/backward')
def backward():
    moveBackward()
    # GPIO.output(18,GPIO.HIGH)
    return {"success":"true"}

@app.route('/left')
def left():
    moveLeft()
    # GPIO.output(18,GPIO.HIGH)
    return {"success":"true"}

@app.route('/right')
def right():
    moveRight()
    # GPIO.output(18,GPIO.HIGH)
    return {"success":"true"}


if __name__ == '__main__':
    # os.system("sudo rm -r ~/.cache/chromium/Default/Cache/*")
    app.run(debug=True, port=5000,host='0.0.0.0',threaded=True)




GPIO.cleanup()