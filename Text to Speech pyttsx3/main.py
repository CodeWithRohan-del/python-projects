
#----------------------Text to speech fast iusing pyttsx3----------

# Install pyttsx3
#command -- pip install pyttsx3

#------------------------------------------
# Improting pyttsx3
import pyttsx3

# Create the engine
engine = pyttsx3.init()

#Create a text varible and store the text wont want to speech
text = "This is the first program \n using pyttsx3 in python"

#speak the text
engine.say(text)

#Complete the run
engine.runAndWait()

#-----------------PROGRAM IS READY-----------
