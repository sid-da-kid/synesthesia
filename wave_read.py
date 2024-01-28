import numpy
import wave

aud = wave.open("triumph.wav")

print("Parameters: ", aud.getparams())

aud_time = aud.getnframes() / aud.getframerate()
print(aud_time)

