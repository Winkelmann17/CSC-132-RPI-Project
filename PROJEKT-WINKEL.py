################################################################################
# Name: Nicholas Winkelmann                                                    
# Date: 10/19/2020                                                             
# Description: LED the Way, programming the Rpi GPIO.
################################################################################

## Importing the breadboard GPIO into Python
##import keyboard
#import RPi.GPIO as GPIO
from time import sleep
from tkinter import *
#GPIO.setmode(GPIO.BCM)
from pynput import keyboard
from pynput.keyboard import Key, Listener

#led = [22, 23, 24, 25, 26, 27]
#GPIO.setup(led, GPIO.OUT)


##Declaring variables equal to the ports they are linked to on the breadboard
class Game(Frame) :
    # the constructor
    def __init__(self, parent):
        #calls the frame class
        Frame.__init__(self, parent)
    def setupGUI(self):
        self.pack(fill=BOTH, expand = 1)
    def play(self):
        self.setupGUI
##    def show(key):
##        if key == Key.up:
##            GPIO.output(24, True)
##            sleep(.1)
##            GPIO.output(24, False)
##        if key == Key.down:
##            GPIO.output(27, True)
##            sleep(.1)
##            GPIO.output(27, False)
##        if key == Key.left:
##            GPIO.output(25, True)
##            sleep(.1)
##            GPIO.output(25, False)
##        if key == Key.right:
##            GPIO.output(26, True)
##            sleep(.1)
##            GPIO.output(26, False)
    def Score(self):
        global score
        if key == Key.up or key == Key.down or key == Key.left or key == Key.right:
            score += 1
            print (score)
            return score
#########################################################3
# Main Program
###########################################################
WIDTH = 800
HEIGHT = 600
# create the window
window = Tk()
window.title("Dance Dance Pi")

# create the GUI
g = Game(window)

# play
g.play()
score = 0
##listener = keyboard.Listener(on_press = Game.show)
##listener.start()
# wait for the window to close
window.mainloop()

