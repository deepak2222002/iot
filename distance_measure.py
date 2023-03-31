import RPi.GPIO as gpio
import time

echo=2
trig=3
led=27

gpio.setmode(gpio.BCM) 
gpio.setup(echo,gpio.IN)
gpio.setup(trig,gpio.OUT)
gpio.setup(led,gpio.OUT)

while True:
    gpio.output(trig,False)
    time.sleep(0.5)
    gpio.output(trig,True)
    time.sleep(0.00001)
    gpio.output(trig,False)
    
    while gpio.input(echo)==0:
        start=time.time()
        print(start,"start")
    while gpio.input(echo)==1:
        stop=time.time()
        print(stop,"stop")
    time_interval= stop-start
    distance = time_interval*17000
    
    print(distance)
    distance = round(distance,2)
    
    if distance<=10:
        gpio.output(led,gpio.HIGH)
        time.sleep(1)
    else:
        gpio.output(led,gpio.LOW)
        
    
    print(f"distance : {distance} cm")
    time.sleep(0.5)