# This is just started. The design needs to improve, as well as functionality
import time

# examples of ord and chr functions
# print(ord("A"))
# print(chr(65))

def message_encrypted():
    '''THis function just accepts the message and encrypts it'''
    message_unencrypted = input("Please enter a message that you would like to send:  ")
    encrypted_message = ""
    for letter in message_unencrypted:
        encrypted_letter = chr(ord(letter) + 1)
        encrypted_message = encrypted_message + encrypted_letter
    return encrypted_message


def message_decrypted():
    message = message_encrypted()
    print("Your encrypted message is: ", message)
    time.sleep(3)
    print("Give me some time to decrypted, my CPU is ancient...")
    time.sleep(5)
    decrypted_message = ""
    for letter in message:
        decrypted_letter = chr(ord(letter) - 1)
        decrypted_message = decrypted_message + decrypted_letter
    return decrypted_message


print(message_decrypted())





















