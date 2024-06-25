import csv

# Define the input and output file paths
input_file_path = r"C:\Users\jakem\Downloads\dataset\trainingdata\output.csv"
output_file_path = (
    r"C:\Users\jakem\Downloads\dataset\trainingdata\outmetadata_train_modified.csv"
)

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
