import RPi.GPIO as GPIO
import gpiozero
import cv2
import time


servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization
def open():
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
def close():    
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    p.stop()
    GPIO.cleanup()
