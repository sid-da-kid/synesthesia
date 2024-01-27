import wave
import numpy as np
import matplotlib.pyplot as plt

aud = wave.open("triumph.wav")

sample_freq = aud.getframerate()
frames = aud.getnframes()
audio_wave = aud.readframes(-1)

aud.close()

time = frames / sample_freq

audio_array = np.frombuffer(audio_wave, dtype=np.int16)
times = np.linspace(0, time, num=frames)

plt.figure(figsize=(15, 5))
plt.plot(times, audio_array)
plt.title("Waveform")
plt.ylabel("Amplitude")
plt.xlabel("Time (s)")
plt.xlim(0, time)
plt.show()
