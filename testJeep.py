#Importing Libraries
#https://business.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051
import RPi.GPIO as gpio
import time
import sys

# Initializing all variables
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
dc_L = 0
dc_R = 0

# Setup for Lights
headlights = 38
taillights = 40
gpio.setup(headlights,gpio.OUT)
gpio.setup(taillights,gpio.OUT)

# Setup for Left
LeftA = 13
LeftB = 15
LeftE = 11
gpio.setup(LeftA,gpio.OUT)
gpio.setup(LeftB,gpio.OUT)
gpio.setup(LeftE,gpio.OUT)
CL_A = gpio.PWM(LeftA,100)
CL_B = gpio.PWM(LeftB,100)
CL_E = gpio.PWM(LeftE,100)
CL_A.start(dc_L)
CL_B.start(dc_L)
CL_E.start(dc_L)

# Setup forRight
RightA = 16
RightB = 18
RightE = 22
gpio.setup(RightA,gpio.OUT)
gpio.setup(RightB,gpio.OUT)
gpio.setup(RightE,gpio.OUT)
CR_A = gpio.PWM(RightA,100)
CR_B = gpio.PWM(RightB,100)
CR_E = gpio.PWM(RightE,100)
CR_A.start(dc_R)
CR_B.start(dc_R)
CR_E.start(dc_R)

# Function Defintions 
def forward (speed):
    gpio.output(taillights,False)
    print ("Forward : ", speed)
    CL_A.ChangeDutyCycle(0)
    CL_B.ChangeDutyCycle(speed)
    CL_E.ChangeDutyCycle(speed)
    CR_A.ChangeDutyCycle(0)
    CR_B.ChangeDutyCycle(speed)
    CR_E.ChangeDutyCycle(speed)
    gpio.output(LeftA,False)
    gpio.output(LeftB,True)
    gpio.output(LeftE,True)
    gpio.output(RightA,False)
    gpio.output(RightB,True)
    gpio.output(RightE,True)
    gpio.output(taillights,True)

def left (t):
    gpio.output(taillights,False)
    print ("Left  ", t)
    CL_A.ChangeDutyCycle(100)
    CL_B.ChangeDutyCycle(0)
    CL_E.ChangeDutyCycle(100)
    CR_A.ChangeDutyCycle(0)
    CR_B.ChangeDutyCycle(100)
    CR_E.ChangeDutyCycle(100)
    gpio.output(LeftA,True)
    gpio.output(LeftB,False)
    gpio.output(LeftE,True)
    gpio.output(RightA,False)
    gpio.output(RightB,True) 
    gpio.output(RightE,True)
    time.sleep(t)
    gpio.output(taillights,True)

def right (t):
    gpio.output(taillights,False)
    print ("Right  ", t)
    CL_A.ChangeDutyCycle(0)
    CL_B.ChangeDutyCycle(100)
    CL_E.ChangeDutyCycle(100)
    CR_A.ChangeDutyCycle(100)
    CR_B.ChangeDutyCycle(0)
    CR_E.ChangeDutyCycle(100)
    gpio.output(LeftA,False)
    gpio.output(LeftB,True)
    gpio.output(LeftE,True)
    gpio.output(RightA,True)
    gpio.output(RightB,False)
    gpio.output(RightE,True)
    time.sleep(t)
    gpio.output(taillights,True)

def back (speed):
    gpio.output(taillights,False)
    print ("Back: ", speed)
    CL_A.ChangeDutyCycle(speed)
    CL_B.ChangeDutyCycle(0)
    CL_E.ChangeDutyCycle(speed)
    CR_A.ChangeDutyCycle(speed)
    CR_B.ChangeDutyCycle(0)
    CR_E.ChangeDutyCycle(speed)
    gpio.output(LeftA,True)
    gpio.output(LeftB,False)
    gpio.output(LeftE,True)
    gpio.output(RightA,True)
    gpio.output(RightB,False)
    gpio.output(RightE,True)
    gpio.output(taillights,True)

def controlCar ():
    print ("User Control")
    med = 50
    fas = 99
    while True:
        t = 0
        c = sys.stdin.read(1)
        if c == '1':
            gpio.output(headlights,True)
        if c == '2':
            gpio.output(headlights,False)
        if c == 'w':
            forward(100);   time.sleep(t)
        if c == 'a':
            left (1);       time.sleep(t)
        if c == 's':
            back(100);      time.sleep(t)
        if c == 'd':
            right (1);      time.sleep(t)
        if c == ' ':
            forward(0)
        if c == 'q':
            break
        if c == 'h':
            print ("w = Forward() ");  print ("a = Left() ")
            print ("d = Right () ");   print ("s = Back() ")
            print ("q = quit ");       print ("1/2 = lights");
            print ("9/0 = Taillights")

# ******************************( *MAIN* )*****************************

gpio.output(headlights,True)
gpio.output(taillights,True)
#forward(40)
#time.sleep(1)
#right (2)
#time.sleep(2)
#forward(0)
left (1.2)
forward(0)


gpio.cleanup()
