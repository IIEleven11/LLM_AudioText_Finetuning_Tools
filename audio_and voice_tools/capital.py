# capitalize metadata properly (hopefully)
import csv
import nltk

input_csv = '/home/eleven/alltalk/mismatches_output.csv'
output_csv = '/home/eleven/alltalk/mismatches_output_grammar_capitalized.csv'

def capitalize_text(text):
    sentences = nltk.sent_tokenize(text)
    capitalized_sentences = []
    
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        
        capitalized_words = []
        for i, (word, tag) in enumerate(tagged_words):
            if i == 0 or tag in ('NNP', 'NNPS'):  # Capitalize first word and proper nouns
                capitalized_words.append(word.capitalize())
            else:
                capitalized_words.append(word)
        
        capitalized_sentences.append(' '.join(capitalized_words))
    
    return ' '.join(capitalized_sentences)

with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile, delimiter='|')
    writer = csv.writer(outfile, delimiter='|')
    
    # Write the header
    header = next(reader)
    writer.writerow(header)
    
    for row in reader:
        # Capitalize the second and third columns
        row[1] = capitalize_text(row[1])
        row[2] = capitalize_text(row[2])
        writer.writerow(row)

print(f"Capitalized text has been written to {output_csv}")