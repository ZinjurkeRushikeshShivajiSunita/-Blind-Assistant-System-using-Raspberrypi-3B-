import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # This command is to Disable Warning....!!!!

buzzer = 13

GPIO.setup(13, GPIO.OUT)
while True:
        GPIO.output(13, True)
        time.sleep(5)
        GPIO.output(13, False)
        time.sleep(1)
