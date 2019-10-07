import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
MotorA = 16
MotorB = 18
MotorE = 22
SteerA = 15
SteerB = 13
SteerE = 11
trig = 40 
echo = 38
GPIO.setup(MotorA,GPIO.OUT)
GPIO.setup(MotorB,GPIO.OUT)
GPIO.setup(MotorE,GPIO.OUT)
GPIO.setup(SteerA,GPIO.OUT)
GPIO.setup(SteerB,GPIO.OUT)
GPIO.setup(SteerE,GPIO.OUT)
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)


while(True):
    GPIO.output(trig,False)
    time.sleep(.05)
    GPIO.output(trig,True)
    time.sleep(.05)
    GPIO.output(trig,False)

    #start = time.time()
    #end = time.time()
    while (GPIO.input(echo) == 0):
        start = time.time()
    while (GPIO.input(echo) == 1):
        end = time.time()
    duration = end - start
    distance = duration * 17150
    distance = round(distance,2)
    print ("Distance:", distance, "cm     ")

    if(distance < 20):
        print ("Moving Backwards & Turn Right")
        GPIO.output(MotorA,True)
        GPIO.output(MotorB,False)
        GPIO.output(MotorE,True)
        GPIO.output(SteerA,True)
        GPIO.output(SteerB,False)
        GPIO.output(SteerE,True)
        time.sleep(0.1)
    if (distance > 20):
        print ("Moving Forwards")
        GPIO.output(MotorA,False)
        GPIO.output(MotorB,True)
        GPIO.output(MotorE,True)
        GPIO.output(SteerE,False)
        time.sleep(0)











print ("Moving Forwards & Turn Left")
GPIO.output(MotorA,False)
GPIO.output(MotorB,True)
GPIO.output(MotorE,True)
GPIO.output(SteerA,False)
GPIO.output(SteerB,True)
GPIO.output(SteerE,True)
sleep(2)

print ("Moving Backwards & Turn Right")
GPIO.output(MotorA,True)
GPIO.output(MotorB,False)
GPIO.output(MotorE,True)
GPIO.output(SteerA,True)
GPIO.output(SteerB,False)
GPIO.output(SteerE,True)
sleep(2)
 
print ("Stopping motor")
GPIO.output(MotorE,False)
GPIO.output(SteerE,False)

print ("PWM test")
GPIO.output(MotorE,GPIO.HIGH)
pwm1 = GPIO.PWM(MotorA,100)
pwm2 = GPIO.PWM(MotorB,100)
pwm3 = GPIO.PWM(MotorE,100)
dc = 0
pwm1.start(dc)
pwm2.start(dc)
pwm3.start(dc)

dc = 70
print ("PWM speed of: ", dc)
pwm1.ChangeDutyCycle(dc)
pwm2.ChangeDutyCycle(dc)
#pwm3.ChangeDutyCycle(dc)
GPIO.output(MotorA,GPIO.LOW)
GPIO.output(MotorB,GPIO.HIGH)
GPIO.output(MotorE,GPIO.HIGH)

sleep (3)

dc = 99
print ("PWM speed of: ", dc)
pwm1.ChangeDutyCycle(dc)
pwm2.ChangeDutyCycle(dc)
pwm3.ChangeDutyCycle(dc)
GPIO.output(MotorA,GPIO.LOW)
GPIO.output(MotorB,GPIO.HIGH)
GPIO.output(MotorE,GPIO.HIGH)
sleep (6)










while False:
      for dc in range(28, 33, 1):    # Loop 0 to 100 stepping dc by 5 each loop
            print ("PWM speed of: ", dc)
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)
            pwm3.ChangeDutyCycle(dc)
            GPIO.output(MotorA,GPIO.LOW)
            GPIO.output(MotorB,GPIO.HIGH)
            GPIO.output(MotorE,GPIO.HIGH)
            sleep (6)

      for dc in range(55, 65, 1):    # Loop 0 to 100 stepping dc by 5 each loop
            print ("PWM speed of: ", dc)
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)
            pwm3.ChangeDutyCycle(dc)
            GPIO.output(MotorA,GPIO.LOW)
            GPIO.output(MotorB,GPIO.HIGH)
            GPIO.output(MotorE,GPIO.HIGH)
            sleep (3)

GPIO.cleanup()
