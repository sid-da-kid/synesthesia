import numpy
import wave

aud = wave.open("arcade.wav")

print("Number of channels: ", aud.getnchannels())
print("Sample width: ", aud.getsampwidth())
print("Frame rate: ", aud.getframerate())
print("Number of frames: ", aud.getnframes())
print("Parameters: ", aud.getparams())

aud_time = aud.getnframes() / aud.getframerate()
print(aud_time)

