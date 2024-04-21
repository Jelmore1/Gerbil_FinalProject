'''
Created on Apr 18, 2024

@author: walsh
'''
import json
from cryptography.fernet import Fernet

def read_encrypted_message(file_path, team_name):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data.get(team_name)

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
    return decrypted_message

def findMovieName():
    file_path = 'TeamsAndEncryptedMessagesForDistribution - 001.json'
    team_name = "Gerbil"
    key = b'8viv7QrLsAKgvcV3JsZkKjZwQiinhtPQhUvbS2B14LM='

    encrypted_message = read_encrypted_message(file_path, team_name)
    decrypted_message = decrypt_message(encrypted_message[0], key)
    print("Our Movie:", decrypted_message)