import csv
import codecs

def check_utf8_compliance(file_path):
    print(f"Checking UTF-8 compliance for: {file_path}")
    print("-" * 80)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter='|')
            next(csv_reader)  # Skip header row
            
            for line_num, row in enumerate(csv_reader, start=2):  # Start from 2 to account for header
                try:
                    # Try to encode and decode each field to check UTF-8 compliance
                    for field in row:
                        field.encode('utf-8').decode('utf-8')
                except UnicodeEncodeError as e:
                    print(f"UTF-8 encoding error in line {line_num}:")
                    print(f"Content: {' | '.join(row)}")
                    print(f"Error: {str(e)}")
                    print("-" * 80)
                except UnicodeDecodeError as e:
                    print(f"UTF-8 decoding error in line {line_num}:")
                    print(f"Content: {' | '.join(row)}")
                    print(f"Error: {str(e)}")
                    print("-" * 80)
                except Exception as e:
                    print(f"Other error in line {line_num}:")
                    print(f"Content: {' | '.join(row)}")
                    print(f"Error: {str(e)}")
                    print("-" * 80)

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error reading file: {str(e)}")

if __name__ == "__main__":
    file_path = "/home/eleven/multi_speaker_model/outputs/outputs/PARENT_CSV/metadata.csv"
    check_utf8_compliance(file_path)
    print("UTF-8 compliance check completed.")