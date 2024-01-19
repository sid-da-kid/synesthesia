import wave
import numpy as np
import matplotlib.pyplot as plt

aud = wave.open("arcade.wav")

sample_freq = aud.getframerate()
n_samples = aud.getnframes()
signal_wave = aud.readframes(-1)

aud.close()

t_audio = n_samples / sample_freq
print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)
times = np.linspace(0, t_audio, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")



