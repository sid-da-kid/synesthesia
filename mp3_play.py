import pygame
from pygame import mixer
mp3_file = "HappySample.mp3"
pygame.init()
mixer.music.load(mp3_file)
mixer.music.play()
while mixer.music.get_busy():
    pygame.time.wait(1000)
exit()