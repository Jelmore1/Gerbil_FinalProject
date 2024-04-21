# Name: Connor Walsh
# email: walsh2ct@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23, 2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This is our final project based in encryption/decryption

# Brief Description of what this module does. This module creates three functions that reads an encrypted message, decrypts that message, then prints the results.
# Citations:
# Anything else that's relevant:
import json
from cryptography.fernet import Fernet

def readEncryptedMessage(file_path, teamName):
    '''
    Reads the encrypted message for the specified team from the JSON file.
    @param
        file_path: The path to the JSON file containing encrypted messages.
        team_name: The name of the team whose encrypted message is to be retrieved.
    @returns The encrypted message for our team Gerbil
    '''
    with open(file_path, "r") as file:
        data = json.load(file)
        return data.get(teamName)

def decryptMessage(encryptedMessage, key):
    '''
    Decrypts the encrypted message using the provided key.
    @param
        encryptedMessage: The encrypted message to be decrypted.
        key: The decryption key.
    @return str: The decrypted message
    '''
    fernet = Fernet(key)
    decryptedMessage = fernet.decrypt(encryptedMessage.encode()).decode()
    return decryptedMessage

def findMovieName():
    '''
    Main function that prints the decrypted message
    '''
    file_path = 'TeamsAndEncryptedMessagesForDistribution - 001.json'
    teamName = "Gerbil"
    key = b'8viv7QrLsAKgvcV3JsZkKjZwQiinhtPQhUvbS2B14LM='

    encryptedMessage = readEncryptedMessage(file_path, teamName)
    decryptedMessage = decryptMessage(encryptedMessage[0], key)
    print("Our Movie:", decryptedMessage)