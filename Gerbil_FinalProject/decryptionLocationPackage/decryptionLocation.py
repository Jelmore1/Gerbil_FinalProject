# Name: Jake Elmore
# email: Elmorejc@mail.uc.edu
# Assignment Number: Assignment 12
# Due Date: April 23 2024
# Course/Section: IS 4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: decrypt location and movie code and print a picture 

# Brief Description of what this module does: decrypt location of the gerbil dictionary
# Citations: 
# Anything else that's relevant:

import json

def decrypt_indices_from_file(json_file, english_words_file):
    '''
    Decrypts the indices from a JSON file using the provided English words file.
    @param: json_file (str): The path to the JSON file containing the encrypted indices.
    english_words_file (str): The path to the file containing English words.
    @Returns: str: The decrypted text.
    '''

    # Read encrypted data from JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extract numbers for the "Gerbil" team
    gerbil_indices = data.get("Gerbil", [])
    
    if not gerbil_indices:
        print("No data found for the Gerbil team.")
        return
    
    # Read English words from file
    with open(english_words_file, 'r', encoding='utf-8') as f:
        english_words = f.readlines()

    # Decrypt Gerbil indices
    decrypted_text = ''
    for index in gerbil_indices:
        decrypted_word = english_words[int(index)].strip()
        decrypted_text += decrypted_word + ' '

    return decrypted_text.strip()

# Example usage:
decrypted_text = decrypt_indices_from_file('EncryptedGroupHints Spring 2024 Section 001-1 (3).json', 'UCEnglish.txt')
if decrypted_text:
    print("Decrypted Gerbil Text:", decrypted_text)