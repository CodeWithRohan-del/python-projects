
#------------------How to create hindi mp3 file-----------------

# Install gtts module
#cammand --- pip install gtts

#--------------------------------------------------
#importing gtts module class gTTS
from gtts import gTTS

# create a text vriable you want to convert mp3 file
text = "Aaj mai khana khayi hu"

# select the languge handi - hi
languge = "hi"

#pass the value and create
tts = gTTS(text=text,lang=languge,slow=False)

#save the file 
tts.save("Hindi.mp3")

#After save file
print("File was saved..")
