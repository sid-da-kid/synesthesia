import wave
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load your audio file using wave module
audio_path = "triumph.wav"
audio_file = wave.open(audio_path, 'rb')

# Set up the figure and axis for the animation
fig, ax = plt.subplots()
image_path = "img1.jpg"
img = Image.open(image_path)
imgplot = ax.imshow(img, animated=True)

# Set the number of frames based on the audio length
num_frames = audio_file.getnframes()
frame_rate = audio_file.getframerate()
duration = num_frames / frame_rate

# Function to update the image for each frame
def update(frame):
    # Calculate the current time in the audio
    current_time = frame / frame_rate

    # Read a frame of audio data
    audio_data = np.frombuffer(audio_file.readframes(audio_file.getnframes()), dtype=np.int16)

    # Normalize the audio data to the range [-1, 1]
    normalized_audio = audio_data / np.iinfo(np.int16).max

    # Calculate the amplitude of the audio signal
    amplitude = np.max(np.abs(normalized_audio))

    # Scale the contrast based on the amplitude (you can adjust the scaling factor)
    contrast_scaling_factor = 1 + 4 * amplitude

    # Update the image based on the audio processing result
    processed_img = Image.eval(img, lambda x: x * contrast_scaling_factor)

    imgplot.set_array(processed_img)

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=20, repeat=False)

plt.show()