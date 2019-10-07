import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)

while(True):
    if(count % 100 == 0):
        time.sleep(10)
    gpio.output(trig,False)
    time.sleep(.05)
    gpio.output(trig,True)
    time.sleep(.05)
    gpio.output(trig,False)

    start = time.time()
    end = time.time()
    while (gpio.input(echo) == 0):
        start = time.time()
    while (gpio.input(echo) == 1):
        end = time.time()
    duration = end - start
    distance = duration * 17150
    distance = round(distance,2)
    print ("Distance:", distance, "cm     ")
    distance = distance * 0.393701
    distance = round(distance,2)
    print ("Distance:", distance, "in     ")

  
    
   
