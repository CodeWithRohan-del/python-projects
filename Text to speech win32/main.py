#        START

#----------------------------------Text to speech in python -------------------------------

# importing win32com.client module
import win32com.client

# set voice type SAPI.SpVoice
speaker = win32com.client.Dispatch("SAPI.SpVoice") 

# play the output
text= "My name is Rohan and languge name is Python "

#Run the voice 
speaker.speak(text)