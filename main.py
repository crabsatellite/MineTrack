from pydub import AudioSegment
import os

# Get the current directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# Define input and output folders
input_folder = os.path.join(current_directory, 'input')
output_folder = os.path.join(current_directory, 'output')

sample_rate = 44100

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through all the files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(('.mp3', '.wav', '.flac', '.ogg')):
        file_path = os.path.join(input_folder, file_name)
        output_file_name = os.path.splitext(file_name)[0] + '.ogg'
        output_file_path = os.path.join(output_folder, output_file_name)

        audio = AudioSegment.from_file(file_path)
        mono_audio = audio.set_channels(1)  # Mono channel
        mono_audio = mono_audio.set_frame_rate(sample_rate)  # Sample rate

        # Check if the audio is longer than 10 minutes
        if len(mono_audio) > 10 * 60 * 1000:
            # Cut the audio to 10 minutes
            mono_audio = mono_audio[:10 * 60 * 1000]

            # Create a fade out effect for the last 30 seconds
            fade_duration = 5 * 1000  # 30 seconds
            mono_audio = mono_audio.fade_out(fade_duration)

        # Export the file
        mono_audio.export(output_file_path, format='ogg')

print("Conversion completed!")
