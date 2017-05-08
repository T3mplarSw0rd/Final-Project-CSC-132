import RPi.GPIO as GPIO
from random import randint                
from Tkinter import *

def binaryConverter(decimal):
        num1 = 0
        num2 = 0
        num3 = 0
        num4 = 0
        if(decimal / 8 == 1):
                num1 = 1
                decimal = decimal - 8
        if(decimal / 4 == 1):
                num2 = 1
                decimal = decimal - 4
        if(decimal / 2 == 1):
                num3 = 1
                decimal = decimal - 2
        if(decimal / 1 == 1):
                num4 = 1
                decimal = decimal - 1
 
        return str(num1) + str(num2) + str(num3) + str(num4)
def process(event):
        action = player_input.get()
        action = action.lower()
        if(action == "help"):
                text.insert(END, "The final goal is to complete 4 conversions, then a means of decoding the scrambled phrase at the top will be given. Enter this phrase into the text box to complete the challenge. \n")
        elif(action == "stardust"):
                text.insert(END, "Congratulations, you finished the challenge!")
        else:
               text.insert(END, "Invalid command. Try help")
        player_input.delete(0, END)
def onclick():
        pass
goal = randint(1, 15)
print(goal)
binaryGoal = binaryConverter(goal)
print(binaryGoal)
root = Tk()
text = Text(root)
text.insert(INSERT, " Decipher this word: opvnzqop \n Current goal is to convert " + str(goal) + " to binary using the buttons on the breadboard. \n")

text.pack(side=TOP, fill=X)

player_input = Entry(root)
player_input.bind("<Return>", process)
player_input.pack(side=BOTTOM, fill=X)
player_input.focus()


#List of switches from left to right.
switches = [12, 20, 6, 26]
#Use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)
#Sets up multiple gpio pins at once. (list of pins, input/output, the base state without input-off in this case)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Initializes these values as false, for use later in the program.
input1 = False
input2 = False
input3 = False
input4 = False
gate = 0
try:
        while(True):
                #Initially note that no switch is pressed
                #This helps with switch debouncing
                root.update_idletasks()
                
                pressed = False
                
                #so long as no switch is currently pressed
                while (not pressed and gate < 4):
                        
                        #... we can check the status of each switch
                        for i in range(len(switches)):
                                #if one switch is pressed
                                while (GPIO.input(switches[i]) == True):
                                        
                                        #note the index
                                        val = i
                                        #note that a switch has now been pressed
                                                
                                                
                                        pressed = True
                #Changes the input value of the button being pressed to the opposite
                if(val == 0):
                        input1 =  not input1
                elif(val == 1):
                        input2 =  not input2
                elif(val == 2):
                        input3 =  not input3
                elif(val == 3):
                        input4 =  not input4

                #Each pair of if/else sets the associated bit to a 1 or a 0 depending on whether that input is true of false
                if(input1):
                        binary1 = "1"
                else:
                        binary1 = "0"
                if(input2):
                        binary2 = "1"
                else:
                        binary2 = "0"
                if(input3):
                        binary3 = "1"
                else:
                        binary3 = "0"
                if(input4):
                        binary4 = "1"
                else:
                        binary4 = "0"
                #prints the four inputs one after the other.
                currentInput =  binary1 + binary2 + binary3 + binary4 
                if(gate < 4):
                        print(binary1 + binary2 + binary3 + binary4)
                
                if(gate < 4):
                        text.insert(END, "Your current input is " + currentInput + ". \n")
                

                if(currentInput == binaryGoal):
                        
                        gate = gate + 1
                        text.delete(1.0, END)
                        text.insert(END, "Decipher this word: opvnzqop \n")
                        text.insert(END, "Correct \n")
                        goal = randint(1, 15)
                        binaryGoal = binaryConverter(goal)
                        if(gate < 4):
                                text.insert(INSERT, "New goal is " + str(goal) + ". \n")
                        input1 = False
                        input2 = False
                        input3 = False
                        input4 = False
                        if(gate == 4):
                                text.insert(INSERT, "Use a ceasarian cypher. 4 letters back. \n *A caesarian cypher is a means of decoding/encoding in which letters in a word or phrase is shifted a certain number in a direction. E -> 4 letters back -> A for example. \n")
                                text.insert(END, "Enter the decoded word and press enter. \n")
                                binaryGoal = "break"
                                player_input.focus()
                if(gate >= 4):
                        
                        player_input.bind("<Return>", process)
                root.update()
                
#detect Ctrl + C
except KeyboardInterrupt:
        #reset the GPIO pins
        GPIO.cleanup()
        print("\nReset")


