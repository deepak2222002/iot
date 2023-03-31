import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)


button=9

gpio.setup(red1,gpio.OUT)
gpio.setup(white1,gpio.OUT)
gpio.setup(green1,gpio.OUT)
gpio.setup(red2,gpio.OUT)
gpio.setup(white2,gpio.OUT)
gpio.setup(green2,gpio.OUT)
gpio.setup(button,gpio.IN)

while True:
        gpio.output(red1,gpio.HIGH)
        gpio.output(white1,gpio.HIGH)
        gpio.output(green1,gpio.HIGH)
        time.sleep(1)
        gpio.output(red1,gpio.LOW)
        gpio.output(white1,gpio.LOW)
        gpio.output(green1,gpio.LOW)
        time.sleep(1)
        gpio.output(red2,gpio.HIGH)
        gpio.output(white2,gpio.HIGH)
        gpio.output(green2,gpio.HIGH)
        time.sleep(1)
        gpio.output(red2,gpio.LOW)
        gpio.output(white2,gpio.LOW)
        gpio.output(green2,gpio.LOW)
        time.sleep(1)
        if gpio.input(button)==0:
            while gpio.input(button)==1:
                gpio.output(red1,gpio.HIGH)
                time.sleep(0.5)
                gpio.output(red1,gpio.LOW)
                gpio.output(white1,gpio.HIGH)
                time.sleep(0.5)
                gpio.output(white1,gpio.LOW)
                gpio.output(green1,gpio.HIGH)
                time.sleep(0.5)
                gpio.output(green1,gpio.LOW)
    

    
