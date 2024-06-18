import csv
import random

# Define the input and output file paths
input_file = '/home/eleven/dataset/metadata_train.csv'
output_file = '/home/eleven/dataset/metadata_eval.csv'

# Read the input file and store its contents
with open(input_file, 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile, delimiter='|')
    rows = list(reader)

# Calculate 10% of the total number of entries
num_entries = len(rows)
num_sample = int(num_entries * 0.1)

# Randomly select 10% of the entries
sampled_rows = random.sample(rows, num_sample)

# Remove the selected entries from the original list
remaining_rows = [row for row in rows if row not in sampled_rows]

# Write the remaining entries back to the original file
with open(input_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile, delimiter='|')
    writer.writerows(remaining_rows)

# Write the selected 10% entries to a new file
with open(output_file, 'w', newline='', encoding='utf-8') as samplefile:
    writer = csv.writer(samplefile, delimiter='|')
    writer.writerows(sampled_rows)