########################################################
# Names : Parker Sikes, Christian Thibodeaux, Marcus Castille
########################################################
from random import randint
@@ -0,0 +1,71 @@
import RPi.GPIO as GPIO


#List of switches from left to right.
switches = [12, 20, 6, 26]
#Use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)
#Sets up multiple gpio pins at once. (list of pins, input/output, the base state without input-off in this case)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#Initializes these values as false, for use later in the program.
input0 = False
input1 = False
input2 = False
input3 = False

def my_callback_one(12):
    if GPIO.input(12):
        input0 = not input0
    if input0:
        Game.binary0 = 1
    else:
        Game.binary0 = 0

def my_callback_two(20):
    if GPIO.input(20):
        input1 = not input1
    if input1:
        Game.binary1 = 1
    else:
        Game.binary1 = 0

def my_callback_three(6):
    if GPIO.input(6):
        input2 = not input2
    if input2:
        Game.binary2 = 1
    else:
        Game.binary2 = 0

def my_callback_four(26):
    if GPIO.input(26):
        input3 = not input3
    if input3:
        Game.binary3 = 1
    else:
        Game.binary3 = 0

GPIO.add_event_detect(12, GPIO.RISING)
GPIO.add_event_detect(20, GPIO.RISING)
GPIO.add_event_detect(6, GPIO.RISING)
GPIO.add_event_detect(26, GPIO.RISING)

GPIO.add_event_callback(12, my_callback_one)
GPIO.add_event_callback(20, my_callback_two)
GPIO.add_event_callback(6, my_callback_three)
GPIO.add_event_callback(26, my_callback_four)


#detect Ctrl + C
except KeyboardInterrupt:
        #reset the GPIO pins
        GPIO.cleanup()
        print("\nReset")


"""
Paper Piano Record function will be nice to move into this project
due to its ability to toggle an input.
Room Project's GUI will also be nice to cannibalize with the right side
showing the current inputs being made.
The left side showing which of the 4 gates have been solved and when complete.
The right side will hold the shifted text for them to solve.
"""
###########################################################################################
# Name:
# Date:
# Description:
###########################################################################################
from Tkinter import *

# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Gates(object):
	# the constructor
	def __init__(self):
        gAnswer = ""
        gCorrect = False

    def compare(self, solution, previous):
        if self.gAnswer == solution:
            if previous == True | self.gName == "G1":
                gCorrect = True

	# returns a string description of the room
	def __str__(self):
		# first, the room name
		s = "You are in {}.\n".format(self.name)

		# next, the items in the room
		s += "You see: "
		for item in self.items.keys():
			s += item + " "
		s += "\n"

		# next, the exits from the room
		s += "Exits: "
		for exit in self.exits.keys():
			s += exit + " "

		return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
	# the constructor
	def __init__(self, parent):
		# call the constructor in the superclass
		Frame.__init__(self, parent)

        binary0 = 0
        binary1 = 0
        binary2 = 0
        binary3 = 0
        solutionInput = "{}{}{}{}".format(binary0,binary1,binary2,binary3)
        GatesList = [G1, G2, G3, G4]

    @property
    def binary0(self):
        return self._binary0

    @binary0.setter
    def binary0(self, value):
        self._binary0 = value

    @property
    def binary1(self):
        return self._binary1

    @binary1.setter
    def binary1(self, value):
        self._binary1 = value

    @property
    def binary2(self):
        return self._binary2

    @binary2.setter
    def binary2(self, value):
        self._binary2 = value

    @property
    def binary0(self):
        return self._binary0

    @binary3.setter
    def binary3(self, value):
        self._binary3 = value

    @property
    def solutionInput(self):
        return self._solutionInput

    @solutionInput.setter
    def solutionInput(self, value):
        self._solutionInput = value


	# creates the Gates
    def createGates(self):
        for i in range (len(GatesList)):
                Game.GatesList[i] = Gates(i)
                i.Answer = "{2:04b}".format(randint(0,16))

	# sets up the GUI
    def setupGUI(self):
        #organize the GUI
        self.pack(fill=BOTH, expand = 1)
        """
        setup the player input at the bottom of the GUI
        sets the background to white and binds the return
        key to the process function in the class
        """
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind(("<Return>"), self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        #setup the image to the left of the GUI
        img = None
        Game.image = Label(self, width=WIDTH / 2, image = img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill = Y)
        Game.image.pack_propagate(False)

        #setup the text on the right of the GUI
        text_frame = Frame(self, width=WIDTH / 2)
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

	# sets the current room image
	def setResultImage(self):

	# sets the status displayed on the right of the GUI
    def setStatus(self, status):
        #Enables the text, clears it, sets it, and finally disables it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        Game.text.insert(END, "Your current input is " + Game.solutionInput)
        Game.text.config(state=DISABLED)

	# plays the game
	def play(self):
		# add the rooms to the game
		self.createGates()
		# configure the GUI
		self.setupGUI()
		# set the current room
		self.setResultImage()
		# set the current status
		self.setStatus("")

	# processes the player's input
	def process(self, event):
        action = Game.player_input.get()
        action = action.lower()

        if action == "run" | "":
            if Game.solutionInput == currentGate.gAnswer:
                if Game.count == 3:
                    
                else:
                    Game.count += 1


##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Puzzle in the Stars")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
GPIO.cleanup
