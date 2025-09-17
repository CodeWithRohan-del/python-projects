
#--------------------Create a project Robo Speaker----------------------------

#Step 1 Import win32com.client for text to speech
import win32com.client

#Step 2 create a speaker object to use for name speaker.speak
speaker = win32com.client.Dispatch("SAPI.SpVoice")

#step 3 input from user to text word and sentence covert text to speech and write while loop
while True:
    text = input("Enter your Text and stop for s:")
    #Run the speaker object
    speaker.speak(text)

    #Check the condition if text == s loop break
    if text =="s":
        print("Speaker stop and Program End..")
        break
    
    #else part print user text
    else:
        print(f"You : {text}")

#---------------------------------Project is ready----------------------------------------------

#--------------------------Thank you--------------------------