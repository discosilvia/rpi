# 3/6
# This is Python 3 code
#import libraries
import RPi.GPIO as GPIO
import time
import pygame.mixer

#Fire up the sound mixer
pygame.mixer.init(22100, -16, 2, 512)
#gets rid of delay

#set GPIO numbering mode and define input and output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT) #relay - don't use pin 18, apperently cannot be combined with audio
GPIO.setup(7,GPIO.IN) #wire and loop
GPIO.setup(16,GPIO.IN) # button

try:
        #Specify MP3
        pygame.mixer.music.load("/home/pi/Desktop/example.mp3")
        print("loaded mp3")

        while (1 == 1):
                print ("tap start to begin!")
        
                #play function
                def play():
                        if pygame.mixer.music.get_busy() == True:
                                #print("unpausing mp3")
                                pygame.mixer.music.unpause()
                        else: 
                                #print("first time playing mp3")
                                #music repeats indefinitely
                                pygame.mixer.music.play(-1)

                def pause():
                        pygame.mixer.music.pause()

                #empty while loop that exits when button pressed
                while GPIO.input(16) == 0:
                        pass #Pass is a null operation

                print ("live")
                #flicker to start      
                GPIO.output(22,True) #relay is on when low
                time.sleep(0.2)
                GPIO.output(22,False) #relay is on when low
                time.sleep(0.2)
                GPIO.output(22,True) #relay is on when low
                time.sleep(0.2)
                GPIO.output(22,False) #relay is on when low

                #while loop until button pressed
                while GPIO.input(16) == 0:
                        if GPIO.input(7) == 1:
                                # turn on sound
                                play()
                                #turn on relay      
                                GPIO.output(22,True)                         
                        elif GPIO.input(7) == 0:
                                # turn off sound
                                pause()
                                # turn off relay
                                GPIO.output(22,False)
                           

                print ("off")

#cleanup the GPIO pins before ending
except KeyboardInterrupt:
        print ("ctrl c")
except:
        print ("other error")
finally:
        GPIO.cleanup()
