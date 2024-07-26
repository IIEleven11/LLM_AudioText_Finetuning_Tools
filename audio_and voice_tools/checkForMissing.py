# script that compares filenames in wav folder to filenames in first column of a csv. If anything is missing it will output their names.
# Keep in mind it prepends wavs/ you will need to remove this to use it for things that arent xttsv2

import os
import csv

# Define paths
metadata_train_path = '/home/eleven/alltalk/alltalk_tts/finetune/1/metadata_train.csv'
metadata_eval_path = '/home/eleven/alltalk/alltalk_tts/finetune/1/metadata_eval.csv'
wavs_dir = '/home/eleven/alltalk/alltalk_tts/finetune/1/wavs'
output_csv_path = '/home/eleven/alltalk/alltalk_tts/finetune/1/missing_files.csv'

# Function to read metadata files and extract audio file names
def read_metadata(file_path):
    audio_files = set()
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            # Strip the 'wavs/' prefix
            audio_file = row[0].replace('wavs/', '')
            audio_files.add(audio_file)
    return audio_files

# Read metadata files
train_audio_files = read_metadata(metadata_train_path)
eval_audio_files = read_metadata(metadata_eval_path)

# Get all WAV files in the directory
wav_files = set(f for f in os.listdir(wavs_dir) if f.endswith('.wav'))

# Find missing metadata and missing WAV files
missing_metadata = wav_files - (train_audio_files | eval_audio_files)
missing_wavs = (train_audio_files | eval_audio_files) - wav_files

# Write missing files to a new CSV
with open(output_csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Missing Metadata'])
    for audio_file in missing_metadata:
        writer.writerow([audio_file])
    writer.writerow([])
    writer.writerow(['Missing WAVs'])
    for audio_file in missing_wavs:
        writer.writerow([audio_file])

print(f"Missing files have been written to {output_csv_path}")