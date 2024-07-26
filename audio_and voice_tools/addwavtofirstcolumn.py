# adds .wav to the first column of a metadata.csv for coqui models

import csv

input_file = 'path/to/metadata_eval.csv then also do the path/to/metadata_train.csv'
output_file = 'path/to/metadata_eval/train_modified.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile, delimiter='|')
    writer = csv.writer(outfile, delimiter='|')
    
    for row in reader:
        row[0] = row[0] + '.wav'
        writer.writerow(row)

print(f"Modified CSV has been saved to {output_file}")
