import wave
from PIL import Image, ImageEnhance

def change_contrast_based_on_audio(image_path, audio_path, contrast_factor=1.0):
    # Load the image
    image = Image.open(image_path)

    # Load the audio file using the wave library
    audio_file = wave.open(audio_path, 'rb')
    sample_width = audio_file.getsampwidth()
    frame_rate = audio_file.getframerate()
    frames = audio_file.readframes(audio_file.getnframes())

    # Calculate the mean amplitude as a representation of audio intensity
    mean_amplitude = sum(abs(int.from_bytes(frames[i:i+sample_width], byteorder='little', signed=True))
                         for i in range(0, len(frames), sample_width)) / len(frames)

    # Modify the contrast based on the audio intensity
    modified_contrast = contrast_factor * mean_amplitude / 32767  # Assuming 16-bit audio

    # Apply the contrast change to the image
    enhancer = ImageEnhance.Contrast(image)
    contrasted_image = enhancer.enhance(modified_contrast)

    # Save the result
    contrasted_image.save("output_image.jpg")

# Example usage
image_path = "img1.jpg"
audio_path = "triumph.wav"
change_contrast_based_on_audio(image_path, audio_path, contrast_factor=1.5)
