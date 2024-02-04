import wave
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

aud = wave.open("triumph.wav")

sample_freq = aud.getframerate()
frames = aud.getnframes()
audio_wave = aud.readframes(-1)
time = frames / sample_freq

audio_array = np.frombuffer(audio_wave, dtype=np.int16)
aud.close()

image = Image.open('img1.jpg')

width, height = image.size
# print(width, height)

color_enhancer = ImageEnhance.Color(image)
contrast_enhancer = ImageEnhance.Contrast(image)
brightness_enhancer = ImageEnhance.Brightness(image)
sharpness_enhancer = ImageEnhance.Sharpness(image)

cont_value = print(abs(int((audio_array[25000]) / 10000)))
# print(len(audio_array))
image2 = contrast_enhancer.enhance(cont_value)

image2.show












































