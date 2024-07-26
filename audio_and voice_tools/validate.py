
# Scritp that takes your transcribed metadata and validates it against another transcription of the same audio.
#  outputing a csv with anything that should be changed. Still need to implement capital letters
import os
import pandas as pd
import torch
import torchaudio
from tqdm import tqdm
import whisper
import re
import string
from word2number import w2n

def normalize_text(text):
    return text.lower().strip()

def post_process_text(text):
    # This is a simple post-processing step to ensure the first letter of each sentence is capitalized.
    sentences = text.split('. ')
    sentences = [s.capitalize() for s in sentences]
    return '. '.join(sentences)

def validate_audio_transcriptions(csv_paths, audio_folder, whisper_model, target_language):
    metadata_dfs = []
    for csv_path in csv_paths:
        metadata_df = pd.read_csv(csv_path, sep='|')
        metadata_dfs.append(metadata_df)
    metadata_df = pd.concat(metadata_dfs, ignore_index=True)
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model(whisper_model, device=device)
    
    mismatches = []
    missing_files = []
    total_files = metadata_df.shape[0]
    
    for index, row in tqdm(metadata_df.iterrows(), total=total_files, unit="file"):
        audio_file = row['audio_file']
        expected_text = row['text']
        audio_file_name = audio_file.replace("wavs/", "")
        audio_path = os.path.normpath(os.path.join(audio_folder, audio_file_name))
        
        if not os.path.exists(audio_path):
            missing_files.append(audio_file_name)
            continue
        
        result = model.transcribe(audio_path)
        transcribed_text = result["text"]
        transcribed_text = post_process_text(transcribed_text)  # Apply post-processing
        
        normalized_expected_text = normalize_text(expected_text)
        normalized_transcribed_text = normalize_text(transcribed_text)
        
        if normalized_transcribed_text != normalized_expected_text:
            mismatches.append([audio_file_name, normalized_transcribed_text, normalized_expected_text])
    
    if missing_files:
        print("The following files are missing and should be removed from the CSV files:")
        for file_name in missing_files:
            print(f"- {file_name}")
    
    return pd.DataFrame(mismatches, columns=["audio_file", "Text", "Expected_Text"])

def process_transcriptions(csv_paths, audio_folder, whisper_model, target_language):
    mismatches_df = validate_audio_transcriptions(csv_paths, audio_folder, whisper_model, target_language)
    # Save the DataFrame to a CSV file with pipe as the delimiter
    mismatches_df.to_csv('mismatches_output.csv', index=False, sep='|')
    return mismatches_df

# Example usage:
csv_paths = ['/home/eleven/alltalk/alltalk_tts/finetune/1/metadata_train.csv', '/home/eleven/alltalk/alltalk_tts/finetune/1/metadata_eval.csv']
audio_folder = '/home/eleven/alltalk/alltalk_tts/finetune/1/wavs'
whisper_model = 'large-v3'
target_language = 'en'
mismatches_df = process_transcriptions(csv_paths, audio_folder, whisper_model, target_language)
print(mismatches_df)