# main.py
# Name: Connor Walsh
# email: walsh2ct@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23, 2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This is our final project based in encryption/decryption
# Brief Description of what this module does. This module is the main that runs our three functions.
# Citations:
# Anything else that's relevant:

from decryptionLocationPackage.decryptionLocation import *
from decryptMoviePackage.decryptMovie import *
from displayPhotoPackage.displayPhoto import *

if __name__ == "__main__":
    # prints our location on campus
    decrypted_text = decryptIndices('EncryptedGroupHints Spring 2024 Section 001-1 (3).json', 'UCEnglish.txt')
    print("Our location:", decrypted_text)
    # prints the name of our movie
    findMovieName()
    # loads and displays our photo
    displayPhoto()
    