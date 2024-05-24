# This script is used to downsample audio files to 24kHz

import os
from pydub import AudioSegment

# Define the path to your audio files directory
audio_dir = "path/to/audio/files"

# Define the path to the output directory
output_dir = "path/to/output/directory"

os.makedirs(output_dir, exist_ok=True)


audio_types = (".wav",)


audio_files = [
    os.path.join(audio_dir, file)
    for file in os.listdir(audio_dir)
    if file.endswith(audio_types)
]


# downsample
def downsample_audio(file_path, target_sample_rate=24000):
    audio = AudioSegment.from_wav(file_path)
    audio = audio.set_frame_rate(target_sample_rate)
    output_path = os.path.join(
        output_dir, os.path.basename(file_path).replace(".wav", "_24khz.wav")
    )
    audio.export(output_path, format="wav")
    print(f"Downsampled {file_path} to {output_path}")


for audio_file in audio_files:
    downsample_audio(audio_file)
