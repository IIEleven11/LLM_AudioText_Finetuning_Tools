import os
import subprocess

# Directory containing the wav files
input_dir = "/home/eleven/dataset/StyleTTS2FineTune/makeDataset/tools/segmentedAudio"

# Iterate over all files in the directory
for filename in os.listdir(input_dir):
    if filename.endswith(".wav"):
        # Construct full file path
        file_path = os.path.join(input_dir, filename)

        # Construct output file path
        output_file_path = file_path.replace(".wav", "_16bit_22050_mono.wav")

        # Use SoX to convert the file to 16-bit PCM, 22050 Hz, mono
        subprocess.run(
            ["sox", file_path, "-r", "40000", "-c", "1", "-b", "16", output_file_path]
        )

print("All wav files have been converted to 16-bit PCM, 22050 Hz, mono.")
