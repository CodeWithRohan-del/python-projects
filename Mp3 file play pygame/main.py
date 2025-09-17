
#importing pygame Module
import pygame

#Initialize all imported module 
pygame.init()

#Initialize the mixer foe Audio
pygame.mixer.init()

# Load the mp3 file 
pygame.mixer.music.load("output.mp3")#Enter your mp3 file name 

# play the mp3 file 
pygame.mixer.music.play()

#keep the program running while playing music
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)