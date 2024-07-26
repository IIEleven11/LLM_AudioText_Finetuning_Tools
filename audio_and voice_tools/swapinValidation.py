# # takes the validated text from the validation.py script and swaps it within the metadata.csv's, careful with these because the validated text is sometimes incorrect. 

import csv

# File paths
mismatches_file = '/home/eleven/alltalk/mismatches_output.csv'
metadata_eval_file = '/home/eleven/alltalk/alltalk_tts/finetune/1/metadata_eval.csv'
metadata_train_file = '/home/eleven/alltalk/alltalk_tts/finetune/1/metadata_train.csv'

# Read mismatches file into a dictionary
mismatches = {}
with open(mismatches_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='|')
    for row in reader:
        mismatches[row['audio_file']] = row['validated_text']

# Function to update metadata files
def update_metadata_file(file_path, mismatches):
    updated_rows = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='|')
        for row in reader:
            audio_file = row['audio_file'].replace('wavs/', '')
            if audio_file in mismatches:
                row['text'] = mismatches[audio_file]
            updated_rows.append(row)

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames, delimiter='|')
        writer.writeheader()
        writer.writerows(updated_rows)

# Update metadata_eval.csv
update_metadata_file(metadata_eval_file, mismatches)

# Update metadata_train.csv
update_metadata_file(metadata_train_file, mismatches)

print("Metadata files updated successfully.")