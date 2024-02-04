import wave
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

aud = wave.open("triumph.wav")

sample_freq = aud.getframerate()
frames = aud.readframes(aud.getnframes())
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

# cont_value = print(sum(abs(int.from_bytes((audio_array[25000]) / 10000), byteorder='little', signed=True)))
print(len(audio_array))

cont_value = sum(abs(int.from_bytes(frames[i:i+time], byteorder='little', signed=True))
                         for i in range(0, len(frames), time)) / (len(frames) / 50)

image2 = contrast_enhancer.enhance(cont_value)
image2.show












































