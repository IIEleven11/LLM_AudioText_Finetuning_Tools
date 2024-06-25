#make dataset Gaussian

import os
import random
from pydub import AudioSegment

# Path to the directory containing the WAV files
input_dir = r"C:\Users\jakem\Downloads\dataset\resolveout1"
output_dir = r"C:\Users\jakem\Downloads\dataset\resolveout1\concatout"

os.makedirs(output_dir, exist_ok=True)


wav_files = [f for f in os.listdir(input_dir) if f.endswith(".wav")]


combined_audio = AudioSegment.empty()


for wav_file in wav_files:
    file_path = os.path.join(input_dir, wav_file)
    audio = AudioSegment.from_wav(file_path)
    combined_audio += audio

mean_length = 7.5  # Mean of the Gaussian distribution (midpoint of 1 to 14 seconds)
std_dev = 2  # Standard deviation to control the spread


current_position = 0
segment_number = 1
while current_position < len(combined_audio):
    # Generate a random segment length from a Gaussian distribution
    segment_length = int(
        random.gauss(mean_length, std_dev) * 1000
    )
    segment_length = max(
        1000, min(segment_length, 14000)
    )  # Ensure length is within 1 to 14 seconds


    segment = combined_audio[current_position : current_position + segment_length]
    current_position += segment_length

    segment_path = os.path.join(output_dir, f"segment_{segment_number}.wav")
    segment.export(segment_path, format="wav")
    segment_number += 1

print("All segments have been created and exported.")
