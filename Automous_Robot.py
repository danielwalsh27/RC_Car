#importing libraries, setting up board
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#setup Motors
MotorA = 16
MotorB = 18
MotorE = 22
GPIO.setup(MotorA,GPIO.OUT)
GPIO.setup(MotorB,GPIO.OUT)
GPIO.setup(MotorE,GPIO.OUT)

#setup Steering
SteerA = 15
SteerB = 13
SteerE = 11
GPIO.setup(SteerA,GPIO.OUT)
GPIO.setup(SteerB,GPIO.OUT)
GPIO.setup(SteerE,GPIO.OUT)

#setup Ultrasonic sensor
trig = 40 
echo = 38
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

#setup PWM 
pwm=GPIO.PWM(MotorE,100)
pwm.start(0)

def Left45(speed,delay):
    print("Reverse Left 45")
    pwm.ChangeDutyCycle(speed)
    GPIO.output(MotorA,GPIO.HIGH)
    GPIO.output(MotorB,GPIO.LOW)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.LOW)
    GPIO.output(SteerB,GPIO.HIGH)
    GPIO.output(SteerE,GPIO.HIGH)
    time.sleep(delay)

def Left90(speed,delay):
    print("Reverse Left 90")
    pwm.ChangeDutyCycle(speed)
    GPIO.output(MotorA,GPIO.HIGH)
    GPIO.output(MotorB,GPIO.LOW)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.LOW)
    GPIO.output(SteerB,GPIO.HIGH)
    GPIO.output(SteerE,GPIO.HIGH)
    time.sleep(delay)

def Right45(speed,delay):
    print("Reverse Right 45")
    pwm.ChangeDutyCycle(speed)
    GPIO.output(MotorA,GPIO.HIGH)
    GPIO.output(MotorB,GPIO.LOW)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.HIGH)
    GPIO.output(SteerB,GPIO.LOW)
    GPIO.output(SteerE,GPIO.HIGH)
    time.sleep(delay)

def Right90(speed,delay):
    print("Reverse Right 90")
    pwm.ChangeDutyCycle(speed)
    GPIO.output(MotorA,GPIO.HIGH)
    GPIO.output(MotorB,GPIO.LOW)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.HIGH)
    GPIO.output(SteerB,GPIO.LOW)
    GPIO.output(SteerE,GPIO.HIGH)
    time.sleep(delay)

def forward(speed,delay):
    pwm.ChangeDutyCycle(speed)
    GPIO.output(MotorA,GPIO.LOW)
    GPIO.output(MotorB,GPIO.HIGH)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerE,GPIO.LOW)
    time.sleep(delay)

switch = 0
count = 0
maxIts = 100
while(True):
    count = count + 1
    if(count > maxIts): break
    
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
    distance = duration * 17150  * 0.393701
    distance = round(distance,2)
    print ("Distance:", distance, "in")

    if(distance < 10):
        if(switch == 0):
            Left45(75,1.30)
            switch = 1;
        elif(switch == 1):
            Right90(75,1.60)
            switch = 2;
        elif(switch == 2):
            Left90(75,1.60)
            switch = 3;
        else:
            Right45(75,1.30)
            switch = 0;
        
    elif (distance > 10):
        if(distance > 100):
            forward(100,0)
        elif(distance < 40 and distance > 10):
            forward(40,0)
        else:
            forward(distance,0)
            
print("End Program")
pwm.stop()
GPIO.cleanup()
