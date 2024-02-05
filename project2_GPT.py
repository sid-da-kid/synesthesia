import wave
import numpy as np
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load your audio file using wave module
audio_path = "triumph.wav"
aud = wave.open(audio_path, 'rb')

# Set up the figure and axis for the animation
fig, ax = plt.subplots()
image_path = "img1.jpg"
image = Image.open(image_path)
imgplot = ax.imshow(image, animated=True)

# Set the number of frames based on the audio length
num_frames = aud.getnframes()
frame_rate = aud.getframerate()
duration = num_frames / frame_rate
sample_width = aud.getsampwidth()
frames = aud.readframes(aud.getnframes())

# Function to update the image for each frame
def update(frame):
    # Calculate the current time in the audio
    current_time = frame / frame_rate

    # Read a frame of audio data
    aud_data = np.frombuffer(aud.readframes(1), dtype=np.int16)

    color_enhancer = ImageEnhance.Color(image)
    contrast_enhancer = ImageEnhance.Contrast(image)
    brightness_enhancer = ImageEnhance.Brightness(image)
    sharpness_enhancer = ImageEnhance.Sharpness(image)


    print(f"Total frames in audio: {sample_width}")

    # Using a specific frame
    value = abs(frames[10000])

    # Using the mean amplitude
    # cont_value = sum(abs(int.from_bytes(frames[i:i+sample_width], byteorder='little', signed=True)) 
    #                          for i in range(0, len(frames), sample_width)) / len(frames)

    image2 = color_enhancer.enhance(value)
    image2.show()

    # Process the audio data to determine the contrast adjustment
    # Your audio processing logic goes here

    # Update the image based on the audio processing result
    # Modify the image using Pillow or any other image processing library
    # Update img here with the processed image

    imgplot.set_array(image)

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=1000/frame_rate, repeat=False)

plt.show()