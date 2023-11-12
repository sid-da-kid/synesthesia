import pygame
from mido import MidiFile
mid_file = "CMajorMinor.MID"
pygame.init()
pygame.mixer.music.load(mid_file)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.wait(1000)
mid = MidiFile(mid_file, clip=True)
print(mid)
