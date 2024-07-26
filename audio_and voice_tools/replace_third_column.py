#replaces the third column of a pipe delimted csv audio_file|text|speaker_name to whatever you want. in this case i used "coqui"

import csv

# Define the input and output file paths. 
input_file_path = r"C:\dataset\trainingdata\output.csv"
output_file_path = (r"C:\trainingdata\outmetadata_train_modified.csv")

# Open the input file for reading and the output file for writing
with open(input_file_path, "r", newline="") as infile, open(
    output_file_path, "w", newline=""
) as outfile:
    reader = csv.reader(infile, delimiter="|")
    writer = csv.writer(outfile, delimiter="|")

    # Iterate over each row in the input file
    for row in reader:
        # Change the third column from "1" to "coqui"
        if row[2] == "1":
            row[2] = "coqui"
        # Write the modified row to the output file
        writer.writerow(row)

print("CSV file has been modified and saved as", output_file_path)
