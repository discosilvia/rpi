# 27/5 10:40
# This is Python 3 code
#import libraries
import RPi.GPIO as GPIO
import time
import pygame.mixer
import glob
import random

#Fire up the sound mixer
pygame.mixer.init()

#set GPIO numbering mode and define input and output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT) #relay - don't use pin 18, apperently cannot be combined with audio
GPIO.setup(7,GPIO.IN) #wire and loop
GPIO.setup(16,GPIO.IN) # button

print ("tap start to begin!")

#Specify folder of MP3s
soundfiles = glob.glob("/home/pi/Desktop/*.mp3")
pygame.mixer.music.load(random.choice(soundfiles)) #moved this out of play funtion

#play function
def play():
        if pygame.mixer.music.get_busy() == true:
                print("unpausing mp3")
                #this might not work :/
                pygame.mixer.music.unpause()
        else: 
                print("first time playing mp3")
                #music repeats indefinitely
                pygame.mixer.music.play(-1)

def pause():
        print("mp3 paused")
        pygame.mixer.music.pause()

#empty while loop that exits when button pressed
while GPIO.input(16)==0:
        pass #Pass is a null operation

print ("live")

#wait for debounce before beginning
time.sleep(0.5)

#while loop until button pressed
while GPIO.input(16) == 0:
        if GPIO.input(7) == 1:
                #turn on relay      
                GPIO.output(22,False) #relay is on when low
                # turn on sound
                play()
        elif GPIO.input(7) == 0:
                # turn off relay
                GPIO.output(22,True) #relay is on when high
                # turn off sound
                pause()   

print ("off")

#cleanup the GPIO pins before ending
GPIO.cleanup()
