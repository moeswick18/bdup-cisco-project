__store_space = []

def encrypt_message(text):
    cipher = ''
    for char in text:
        if char == " ":
        	__store_space.append(text.find(char))
        	continue
        elif not char.isalpha():
        	continue
        code = ord(char) + 3
        if code > ord('Z') and char < "[":
            code = (ord('A') + 3) - (ord('Z') - ord(char)) - 1
        elif code > ord('z') and char < "{":
            code = (ord('a') + 3) - (ord('z') - ord(char)) - 1
        cipher += chr(code)
    return cipher

def decrypt_message(cipher):
    decipher = ''
    text = ''
    for char in cipher:
        code = ord(char) - 3
        if code < ord('A') :
            code = (ord('A') - 3) + (ord('Z') - ord(char)) - 1
        elif code > ord('z') and char < "{":
            code = (ord('a') - 3) + (ord('z') - ord(char)) - 1
        decipher += chr(code)
    if text == '':
    	for i in __store_space:
    		text = decipher[:i] + " "
    if text:
    	text += decipher[len(text)-1:]
    return text
