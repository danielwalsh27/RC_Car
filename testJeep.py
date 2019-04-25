#Importing Libraries
#https://business.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051
import RPi.GPIO as GPIO
import time
import sys

# Initializing all variables
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
dc_L = 0
dc_R = 0

# Setup for Lights
headlights = 38
taillights = 40
GPIO.setup(headlights,GPIO.OUT)
GPIO.setup(taillights,GPIO.OUT)

# Setup for Left
LeftA = 13
LeftB = 15
LeftE = 11
GPIO.setup(LeftA,GPIO.OUT)
GPIO.setup(LeftB,GPIO.OUT)
GPIO.setup(LeftE,GPIO.OUT)
CL_A = GPIO.PWM(LeftA,100)
CL_B = GPIO.PWM(LeftB,100)
CL_E = GPIO.PWM(LeftE,100)
CL_A.start(dc_L)
CL_B.start(dc_L)
CL_E.start(dc_L)

# Setup forRight
RightA = 16
RightB = 18
RightE = 22
GPIO.setup(RightA,GPIO.OUT)
GPIO.setup(RightB,GPIO.OUT)
GPIO.setup(RightE,GPIO.OUT)
CR_A = GPIO.PWM(RightA,100)
CR_B = GPIO.PWM(RightB,100)
CR_E = GPIO.PWM(RightE,100)
CR_A.start(dc_R)
CR_B.start(dc_R)
CR_E.start(dc_R)

# Function Defintions 
def forward (speed):
    GPIO.output(taillights,False)
    print ("Forward : ", speed)
    CL_A.ChangeDutyCycle(0)
    CL_B.ChangeDutyCycle(speed)
    CL_E.ChangeDutyCycle(speed)
    CR_A.ChangeDutyCycle(0)
    CR_B.ChangeDutyCycle(speed)
    CR_E.ChangeDutyCycle(speed)
    GPIO.output(LeftA,GPIO.LOW)
    GPIO.output(LeftB,GPIO.HIGH)
    GPIO.output(LeftE,GPIO.HIGH)
    GPIO.output(RightA,GPIO.LOW)
    GPIO.output(RightB,GPIO.HIGH)
    GPIO.output(RightE,GPIO.HIGH)
    GPIO.output(taillights,True)

def left (t):
    GPIO.output(taillights,False)
    print ("Left  ", t)
    #CL_A.ChangeDutyCycle(99)
    #CL_B.ChangeDutyCycle(0)
    #CL_E.ChangeDutyCycle(99)
    #CR_A.ChangeDutyCycle(0)
    #CR_B.ChangeDutyCycle(99)
    #CR_E.ChangeDutyCycle(99)
    GPIO.output(LeftA,True)
    GPIO.output(LeftB,False)
    GPIO.output(LeftE,True)
    GPIO.output(RightA,False)
    GPIO.output(RightB,True) 
    GPIO.output(RightE,True)
    time.sleep(t)
    GPIO.output(taillights,True)

def right (t):
    GPIO.output(taillights,False)
    print ("Right  ", t)
    CL_A.ChangeDutyCycle(0)
    CL_B.ChangeDutyCycle(99)
    CL_E.ChangeDutyCycle(99)
    CR_A.ChangeDutyCycle(99)
    CR_B.ChangeDutyCycle(0)
    CR_E.ChangeDutyCycle(99)
    GPIO.output(LeftA,False)
    GPIO.output(LeftB,True)
    GPIO.output(LeftE,True)
    GPIO.output(RightA,True)
    GPIO.output(RightB,False)
    GPIO.output(RightE,True)
    time.sleep(t)
    GPIO.output(taillights,True)

def back (speed):
    GPIO.output(taillights,False)
    print ("Back: ", speed)
    CL_A.ChangeDutyCycle(speed)
    CL_B.ChangeDutyCycle(0)
    CL_E.ChangeDutyCycle(speed)
    CR_A.ChangeDutyCycle(speed)
    CR_B.ChangeDutyCycle(0)
    CR_E.ChangeDutyCycle(speed)
    GPIO.output(LeftA,GPIO.HIGH)
    GPIO.output(LeftB,GPIO.LOW)
    GPIO.output(LeftE,GPIO.HIGH)
    GPIO.output(RightA,GPIO.HIGH)
    GPIO.output(RightB,GPIO.LOW)
    GPIO.output(RightE,GPIO.HIGH)
    GPIO.output(taillights,True)

def controlCar ():
    print ("User Control")
    med = 50
    fas = 99
    while True:
        t = 0
        c = sys.stdin.read(1)
        if c == '1':
            GPIO.output(headlights,True)
        if c == '2':
            GPIO.output(headlights,False)
        if c == 'w':
            forward(med);   time.sleep(t)
        if c == 'a':
            left (1);       time.sleep(t)
        if c == 's':
            back(med);      time.sleep(t)
        if c == 'd':
            right (1);      time.sleep(t)
        if c == 'i':
            forward (fas);  time.sleep(t)
        if c == 'j':
            left (2);       time.sleep(t)
        if c == 'k':
            back (fas);     time.sleep(t)
        if c == 'l':
            right (2);      time.sleep(t)
        if c == ' ':
            forward(0)
        if c == 'q':
            break
        if c == 'h':
            print ("w = Forward (",med,")"); print ("a = Left (",med,")")
            print ("d = Right (",med,")");   print ("s = Back (",med,")")
            print ("i = Forward (",fas,")"); print ("j = Left(",fas,")")
            print ("k = Back (",fas,")");    print ("l = Right (",fas,")");
            print ("q = quit ") ; print ("1/2 = lights");

# ******************************( *MAIN* )*****************************

GPIO.output(headlights,True)
GPIO.output(taillights,True)
#forward(40)
#time.sleep(1)
#right (2)
#time.sleep(2)
#forward(0)
left (1.2)
forward(0)




GPIO.cleanup()
