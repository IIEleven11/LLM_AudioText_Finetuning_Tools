# checks a csv for UTF 8 Compliance

import csv
import codecs
import os
import logging
from datetime import datetime

def setup_logging():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = f'logs/utf8_check_{timestamp}.log'
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return log_file

def check_utf8_compliance(file_path):
    logging.info(f"Checking UTF-8 compliance for: {file_path}")
    logging.info("-" * 80)
    
    if not os.path.exists(file_path):
        logging.error(f"Error: File not found at {file_path}")
        return

    file_size = os.path.getsize(file_path)
    logging.info(f"File size: {file_size:,} bytes")
    
    issues_found = []
    total_lines = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read header
            header = file.readline().strip()
            logging.info(f"Header: {header}")
            
            file.seek(0)
            
            csv_reader = csv.reader(file, delimiter='|')
            header = next(csv_reader)
            logging.info(f"CSV Header parsed: {header}")
            
            for line_num, row in enumerate(csv_reader, start=2):
                total_lines += 1
                
                if total_lines % 1000 == 0:  # Progress update every 1000 lines
                    print(f"Processed {total_lines:,} lines...", end='\r')
                
                if not row:  # Skip empty rows
                    continue
                
                for col_num, field in enumerate(row):
                    try:
                        # Test ASCII encoding
                        encoded = field.encode('ascii', errors='strict')
                    except UnicodeEncodeError as e:
                        issue = {
                            'line': line_num,
                            'column': col_num + 1,
                            'content': field,
                            'full_row': row,
                            'type': 'non-ascii'
                        }
                        issues_found.append(issue)

        logging.info(f"\nProcessed total of {total_lines:,} lines.")
        
        if issues_found:
            logging.info(f"\nFound {len(issues_found)} issues:")
            logging.info("=" * 80)
            
            for issue in issues_found:
                if issue['type'] == 'non-ascii':
                    logging.info(f"\nNon-ASCII characters found in line {issue['line']}, column {issue['column']}:")
                else:
                    logging.info(f"\nSpecial characters (þ or ö) found in line {issue['line']}, column {issue['column']}:")
                
                logging.info(f"Field content: {issue['content']}")
                logging.info(f"Full row: {' | '.join(issue['full_row'])}")
                logging.info("-" * 80)
        else:
            logging.info("\nNo UTF-8 compliance issues found.")
            
    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        raise

if __name__ == "__main__":
    file_path = "/home/eleven/multi_speaker_model/outputs/outputs/PARENT_CSV/metadata.csv"
    log_file = setup_logging()
    
    print(f"Starting UTF-8 compliance check. Logging to: {log_file}")
    check_utf8_compliance(file_path)
    print(f"\nUTF-8 compliance check completed. See {log_file} for full details.")
