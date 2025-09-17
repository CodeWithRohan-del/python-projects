#----------------Welcome---------------------

#------------------How to craete mp3 file in python-----------
#START
# open Terminal and install gtts module 
# run command - pip install gtts

#--------------------------------------------
#Importing gtts module class gTTS
from gtts import gTTS

# text you want to convert mp3 file
text = "mera nama rohan hai"

# set your languge
# hindi = "hi" 
#English = "en"
languge = "hi"

# passing the text languge and engin
tts = gTTS(text=text,lang=languge,slow=False)

# you want to save the file name 
tts.save("my first.mp3")

# After save the file print
print("File saved on dir")

# This code present on the github link