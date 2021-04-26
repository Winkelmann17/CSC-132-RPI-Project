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
from pynput import keyboard
from pynput.keyboard import Key, Listener

led = [22, 23, 24, 25, 26, 27]
GPIO.setup(led, GPIO.OUT)


##Declaring variables equal to the ports they are linked to on the breadboard
class Game:
    global score
    score = 0
    # the constructor
    def __init__(self):
        self.window = Tk()
        self.window.title("Dance Dance Pi-volution!")
        self.window.geometry('800x600')
        self.img1 = PhotoImage(file = "ddr arrows(modified).png")
        self.img2 = PhotoImage(file = "ddr arrows up (gray).png")
        self.img3 = PhotoImage(file = "ddr arrows left (gray).png")
        self.img4 = PhotoImage(file = "ddr arrows right (gray).png")
        self.img1 = self.img1.subsample(5, 5)
        self.img2 = self.img2.subsample(5, 5)
        self.img3 = self.img3.subsample(5, 5)
        self.img4 = self.img4.subsample(5, 5)
    def displayArrows(self):
        arrowUP = Label(self.window, image=self.img2)
        arrowUP.place(x=294, y=20)
        arrowDOWN = Label(self.window, image=self.img1)
        arrowDOWN.place(x=394, y=20)
        arrowLEFT = Label(self.window, image=self.img3)
        arrowLEFT.place(x=194, y=20)
        arrowRIGHT = Label(self.window, image=self.img4)
        arrowRIGHT.place(x=494, y=20)
    def Score(self):
        var = StringVar()
        global label
        label = Label( self.window, textvariable=var)
        var.set(str(score))
        label.pack()
    def addPoint(Score):
        score += 1
        var.set(str(score))
    def show(key):
        if key == Key.up:
            Game.addPoint(label)
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
#########################################################3
# Main Program
###########################################################
print("check")

# create the GUI

g = Game()
g.displayArrows()
g.Score()
# play
listener = keyboard.Listener(on_press = Game.show)
listener.start()
# wait for the window to close

