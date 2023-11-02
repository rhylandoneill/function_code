# Write your code here :-)
import time #imports time library that are needed to run this code
import board #imports board library that are needed to run this code
import digitalio #imports digitalio library that are needed to run this code
import pwmio #imports libraries that are needed to run this code

from adafruit_motor import motor #imports a small section of the adafruit_motor library

left_motor_forward = board.GP12 #Initializes the variable left_motor_forward and attaches it to GP12
left_motor_backward = board.GP13 #Initializes the variable left_motor_backward and attaches it to GP13
right_motor_forward = board.GP16 #Initializes the variable right_motor_forward and attaches it to GP16
right_motor_backward = board.GP17 #Initializes the variable right_motor_backward and attaches it to GP17

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)
pwm_Rc = pwmio.PWMOut(right_motor_forward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)
pwm_Rd = pwmio.PWMOut(right_motor_backward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) #Initializes Left_Motor and cnfiguration line and it is required
Left_Motor_speed = 0 #Initializes the variable Left_Motor_speed to 0
Right_Motor = motor.DCMotor(pwm_Rc, pwm_Rd) #Initializes Right_Motor and configuration line and it is required
Right_Motor_speed = 0 #Initializes the variable Right_Motor_speed to 0

def forward():
    Left_Motor_speed = 1 #Left Motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1 #Right Motor forward
    Right_Motor.throttle = Right_Motor_speed

def backward():
    Left_Motor_speed = -1 #Left Motor backward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right Motor backward
    Right_Motor.throttle = Right_Motor_speed

def left():
    Left_Motor_speed = -1 #Left Motor backward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1 #Right Motor forward
    Right_Motor.throttle = Right_Motor_speed

def right():
    Left_Motor_speed = 1 #Left Motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right Motor backward
    Right_Motor.throttle = Right_Motor_speed

def stop():
    Left_Motor_speed = 0 #Left Motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 0 #Right Motor backward
    Right_Motor.throttle = Right_Motor_speed

while True:
    forward()
    time.sleep(4)
    left()
    time.sleep(3)
    forward()
    time.sleep(4)
    left()
    time.sleep(3)
    forward()
    time.sleep(2)
    left()
    time.sleep(3)
    forward()
    time.sleep(3)
    right()
    time.sleep(4)
    forward()
    time.sleep(3)
    stop()
    time.sleep(3)
