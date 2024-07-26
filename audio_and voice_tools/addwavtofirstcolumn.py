# adds .wav to the first column of a metadata.csv for coqui models

import csv

input_file = '/home/eleven/alltalk/alltalk_tts/finetune/Calypso_7_25/metadata_eval.csv'
output_file = '/home/eleven/alltalk/alltalk_tts/finetune/Calypso_7_25/metadata_eval_modified.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile, delimiter='|')
    writer = csv.writer(outfile, delimiter='|')
    
    for row in reader:
        # Append .wav to the first column
        row[0] = row[0] + '.wav'
        # Write the modified row to the output file
        writer.writerow(row)

print(f"Modified CSV has been saved to {output_file}")