from pydub import AudioSegment
import os
import logging
from datetime import datetime

# Get the current directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# Define input and output folders
input_folder = os.path.join(current_directory, 'input')
output_folder = os.path.join(current_directory, 'output')

sample_rate = 44100
limit_length = False  # Default: don't limit length

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Setup logging: append to the log file instead of overwriting
log_file = os.path.join(current_directory, 'conversion_log.txt')
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

# Log the start of a new session
logging.info('Starting new audio conversion session')

# Iterate through all the files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(('.mp3', '.wav', '.flac', '.ogg', '.m4a', ".mp4", ".wmv", ".xwm")):
        file_path = os.path.join(input_folder, file_name)
        output_file_name = os.path.splitext(file_name)[0] + '.ogg'
        output_file_path = os.path.join(output_folder, output_file_name)

        audio = AudioSegment.from_file(file_path)
        mono_audio = audio.set_channels(1)  # Mono channel
        mono_audio = mono_audio.set_frame_rate(sample_rate)  # Sample rate

        # Decrease/Increase the volume, in dB. Negative values decrease the volume, positive values increase it.
        decreased_volume_audio = mono_audio.apply_gain(0.0)

        # Check if the length needs to be limited
        if limit_length:
            # Check if the audio is longer than 20 minutes
            if len(decreased_volume_audio) > 20 * 60 * 1000:
                # Cut the audio to 20 minutes
                decreased_volume_audio = decreased_volume_audio[:20 * 60 * 1000]

                # Create a fade out effect for the last 5 seconds (adjustable)
                fade_duration = 5 * 1000  # 5 seconds fade out
                decreased_volume_audio = decreased_volume_audio.fade_out(fade_duration)

        # Calculate length in seconds and ticks
        audio_length_seconds = len(decreased_volume_audio) / 1000  # Convert milliseconds to seconds
        length_in_ticks = int(audio_length_seconds * 20)  # Convert to game ticks

        # Print and log the result
        print(f'File: {file_name}, Length in ticks: {length_in_ticks}, Length in seconds: {audio_length_seconds}')
        logging.info(f'File: {file_name}, Length in ticks: {length_in_ticks}, Length in seconds: {audio_length_seconds}')

        # Export the file
        decreased_volume_audio.export(output_file_path, format='ogg')

print("Conversion completed!")
logging.info('Audio conversion session completed\n')
