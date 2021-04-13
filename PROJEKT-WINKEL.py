################################################################################
# Name: Nicholas Winkelmann                                                    
# Date: 10/19/2020                                                             
# Description: LED the Way, programming the Rpi GPIO.
################################################################################

## Importing the breadboard GPIO into Python
##import keyboard
import RPi.GPIO as GPIO
from time import sleep
from tkinter import *
GPIO.setmode(GPIO.BCM)
from pynput.keyboard import Key, Listener

led = [22, 23, 24, 25, 26, 27]
GPIO.setup(led, GPIO.OUT)


##Declaring variables equal to the ports they are linked to on the breadboard
class Game(Frame) :
    global Key.up
    global Key.down
    global Key.left
    global Key.right
    Key.up = up
    Key.down = down
    Key.left = left
    Key.right = right
    # the constructor
    def __init__(self, parent):
        #calls the frame class
        Frame.__init__(self, parent)
    def KeySetup(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def setupGUI(self):
        pass

        

    def play(self):
        self.setupGUI
    def show(key):
    
        if key == up:
            GPIO.output(24, True)
            sleep(.1)
            GPIO.output(24, False)
        if key == down:
            GPIO.output(27, True)
            sleep(.1)
            GPIO.output(27, False)
        if key == left:
            GPIO.output(25, True)
            sleep(.1)
            GPIO.output(25, False)
        if key == right:
            GPIO.output(26, True)
            sleep(.1)
            GPIO.output(26, False)


def show(key):
    
    if key == Key.up:
        GPIO.output(24, True)
        sleep(.1)
        GPIO.output(24, False)
    if key == Key.down:
        GPIO.output(27, True)
        sleep(.1)
        GPIO.output(27, False)
    if key == Key.left:
        GPIO.output(25, True)
        sleep(.1)
        GPIO.output(25, False)
    if key == Key.right:
        GPIO.output(26, True)
        sleep(.1)
        GPIO.output(26, False)
    if key == Key.delete:
        return False
with Listener(on_press = show) as listener:
    listener.join()

#########################################################3
# Main Program
###########################################################
WIDTH = 800
HEIGHT = 600
print("fatass")
# create the window
window = Tk()
window.title("Dance Dance Pi")

# create the GUI
g = Game(window)

# play
g.play()

# wait for the window to close
window.mainloop()

