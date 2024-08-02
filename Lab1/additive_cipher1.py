                                                                         
def encrypt(text, key1):
    result = "" 

    # Traverse text
    for char in text:
        if char == " ":
            result += " "
        elif char.isupper():
            result += chr((ord(char) - 65 + key1) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + key1) % 26 + 97)
        else:
            # Add handling for non-alphabetic characters if needed
            result += char
    return result

def decrypt(ciphertext, key2):
    plaintext = ""
    # Traverse text
    for char in ciphertext:
        if char == " ":
            plaintext += " "
        elif char.isupper():
            plaintext += chr((ord(char) - 65 - key2) % 26 + 65)
        elif char.islower():
            plaintext += chr((ord(char) - 97 - key2) % 26 + 97)
        else:
            # Add handling for non-alphabetic characters if needed
            plaintext += char
    return plaintext


text = input("Enter the text you want to encrypt")
key1 = int(input("Enter the key"))
print ("Text : " + text)
print ("key : " +str(key1))
print ("Cipher : " + encrypt(text, key1))
ciphertext = input("Enter the cipher you want to decrypt")
key2 = int(input("Enter the key"))
print ("Cipher : " + ciphertext)
print ("key : " +str(key2))
print ("Decrypted text: " +  decrypt(ciphertext,key2))



