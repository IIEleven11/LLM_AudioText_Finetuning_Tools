import csv
import os

# Define file paths
train_file_path = "/home/eleven/dataset/StyleTTS2FineTune/makeDataset/tools/datasetss/working/metadata.csv"
eval_file_path = "/home/eleven/dataset/StyleTTS2FineTune/makeDataset/tools/datasetss/working/metadata_eval.csv"
over_file_path = "/home/eleven/dataset/StyleTTS2FineTune/makeDataset/tools/datasetss/working/metadata_over.csv"

# Function to process a CSV file
def process_csv(file_path, over_entries):
    with open(file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='|')
        header = next(reader)
        rows = list(reader)

    # Filter rows and collect over-length entries
    filtered_rows = []
    for row in rows:
        if len(row[1]) > 250:
            over_entries.append(row)
        else:
            filtered_rows.append(row)

    # Write the filtered rows back to the original file
    with open(file_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter='|')
        writer.writerow(header)
        writer.writerows(filtered_rows)

# Collect over-length entries
over_entries = []

# Process both CSV files
process_csv(train_file_path, over_entries)
process_csv(eval_file_path, over_entries)

# Write over-length entries to the new file
with open(over_file_path, 'w', newline='', encoding='utf-8') as overfile:
    writer = csv.writer(overfile, delimiter='|')
    writer.writerow(['audio_file', 'text', 'speaker_name'])  # Assuming the same header
    writer.writerows(over_entries)

print(f"Processed files and moved over-length entries to {over_file_path}")