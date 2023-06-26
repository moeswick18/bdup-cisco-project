from caesar_cipher import *

user_text_input = input()

print(encrypt_message(user_text_input))
print(decrypt_message(encrypt_message(user_text_input)))
