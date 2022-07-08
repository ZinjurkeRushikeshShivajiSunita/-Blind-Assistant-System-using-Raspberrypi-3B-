import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)
Soil = 21
GPIO.setup(Soil, GPIO.IN)
GPIO.setwarnings(False)   
import cv2
import pyttsx3
import pygame
from gtts import gTTS
import os
buzzer = 13

GPIO.setup(13, GPIO.OUT)
def pmusic(file):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print("Playing...")
        clock.tick(100)

def stopmusic():
    pygame.mixer.music.stop()


def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():
    BUFFER = 4096  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)
thres=0.5 #threshold to detect object

while True:
  got_something = GPIO.input(21)
  print(got_something)
  if got_something:
    print("Moisture Not Detected")
   
    time.sleep(0.2)
   
  else:
    print("Moisture Detected")
    GPIO.output(13, False)
    time.sleep(0.5)
    GPIO.output(13, True)
    pyttsx3.speak("Moisture Detected")
    #myobj = gTTS(text="Moisture Detected", lang='en', slow=False)
    #myobj.save("3.mp3")
    #initMixer()
    #file = '/home/ip/Desktop/blind_Asst/3.mp3'
    #pmusic(file)
    time.sleep(0.1)
