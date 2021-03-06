import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
print ("Moving Forwards")
GPIO.output(Motor1A,False)
GPIO.output(Motor1B,True)
GPIO.output(Motor1E,True)

sleep(2)

print ("Moving Backwards")
GPIO.output(Motor1A,True)
GPIO.output(Motor1B,False)
GPIO.output(Motor1E,True)
 
sleep(2)
 
print ("Stopping motor")
GPIO.output(Motor1E,False)
 
GPIO.cleanup()
                                        
