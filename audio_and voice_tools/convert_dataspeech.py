# Here we take a huggingface dataspeech formatted dataset and convert it back to a csv. Extracting and converting the audiobytes column back into wav files. I am only selecting specific columns for the csv. change as needed. Also I am pipe delimiting it

import os
import pandas as pd
from scipy.io.wavfile import write
import numpy as np

# Path to your Parquet file
parquet_file = "path/to/your/mother/fucking/parquet.parquet" #change

# Path to the output CSV file
csv_file = "path/to/output.csv" #change

# Directory to save the audio files
audio_output_dir = "audio_files"
os.makedirs(audio_output_dir, exist_ok=True)


df = pd.read_parquet(parquet_file)

def save_audio_bytes_to_wav(audio_bytes, sample_rate=16000, file_name="audio.wav"): #change samplerate if you need to.
    # Convert bytes to numpy array (assuming 16-bit PCM format)
    audio_data = np.frombuffer(audio_bytes, dtype=np.int16)
    
    # Save the audio data to a .wav file
    write(file_name, sample_rate, audio_data)


audio_paths = []
for idx, row in df.iterrows():
    audio_dict = row['audio']
    
    audio_bytes = audio_dict['bytes']
    
    audio_file_path = os.path.join(audio_output_dir, f"audio_{idx}.wav")
    
    save_audio_bytes_to_wav(audio_bytes, file_name=audio_file_path)
    
    audio_paths.append(audio_file_path)

df['audio'] = audio_paths

# Select only the columns you want
# Adding a new column 'en' with a default value of 'en'
df_filtered = df[['audio', 'speaker_name', 'text']].copy()
df_filtered['en'] = 'en'

# Reorder the columns to match the desired order
df_filtered = df_filtered[['audio', 'speaker_name', 'en', 'text']]

# Save the DataFrame to a pipe-delimited CSV file
df_filtered.to_csv(csv_file, sep='|', index=False)

print(f"CSV file saved to {csv_file}")
print(f"Audio files saved to {audio_output_dir}")
