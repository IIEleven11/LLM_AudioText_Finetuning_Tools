import os
import random
import csv

# Define file paths
input_file = r"trainingdata/output.txt"
train_file = r"trainingdata/metadata_train.csv"
eval_file = r"trainingdata/metadata_eval.csv"

# Read the input file
with open(input_file, "r") as f:
    lines = f.readlines()

# Shuffle the lines to ensure random distribution
random.shuffle(lines)

# Calculate the number of evaluation samples (12% of the total)
num_eval_samples = int(len(lines) * 0.12)

# Split the data into training and evaluation sets
eval_lines = lines[:num_eval_samples]
train_lines = lines[num_eval_samples:]


# Function to write metadata to a CSV file
def write_metadata(file_path, lines):
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter="|")
        writer.writerow(["filename", "transcription", "speaker"])
        for line in lines:
            parts = line.strip().split("|")
            parts[0] = f"/wavs/{parts[0]}"  # Prepend /wavs/ to the filename
            writer.writerow(parts)


# Write the training and evaluation metadata files
write_metadata(train_file, train_lines)
write_metadata(eval_file, eval_lines)

print(f"Metadata files created:\n{train_file}\n{eval_file}")
