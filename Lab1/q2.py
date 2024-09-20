def vigenere_cipher(plaintext, key):
    encrypted = ""
    decrypted = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0
    
    # Encrypting
    for char in plaintext:
        if char.isalpha():
            offset = ord('a')
            p = ord(char) - offset
            k = ord(key[key_index % key_length]) - offset
            encrypted += chr((p + k) % 26 + offset)
            key_index += 1
        else:
            encrypted += char
    
    key_index = 0
    # Decrypting
    for char in encrypted:
        if char.isalpha():
            offset = ord('a')
            c = ord(char) - offset
            k = ord(key[key_index % key_length]) - offset
            decrypted += chr((c - k + 26) % 26 + offset)
            key_index += 1
        else:
            decrypted += char
    
    return encrypted, decrypted


def autokey_cipher(plaintext, initial_key):
    encrypted = ""
    decrypted = ""
    key = [initial_key] + [ord(char) - ord('a') for char in plaintext]
    key_index = 0
    
    # Encrypting
    for i, char in enumerate(plaintext):
        if char.isalpha():
            offset = ord('a')
            p = ord(char) - offset
            k = key[key_index]
            encrypted += chr((p + k) % 26 + offset)
            key_index += 1
        else:
            encrypted += char
    
    key_index = 0
    # Decrypting
    for i, char in enumerate(encrypted):
        if char.isalpha():
            offset = ord('a')
            c = ord(char) - offset
            k = key[key_index]
            decrypted_char = chr((c - k + 26) % 26 + offset)
            decrypted += decrypted_char
            key[key_index + 1] = ord(decrypted_char) - offset
            key_index += 1
        else:
            decrypted += char
    
    return encrypted, decrypted

message = "the house is being sold tonight"

# Vigenere cipher with key = "dollars"
vigenere_encrypted, vigenere_decrypted = vigenere_cipher(message, "dollars")
print(f"Vigenere Cipher:\nEncrypted: {vigenere_encrypted}\nDecrypted: {vigenere_decrypted}\n")

message = "thehouseisbeingsoldtonight" 

# Autokey cipher with key = 7
autokey_encrypted, autokey_decrypted = autokey_cipher(message, 7)
print(f"Autokey Cipher:\nEncrypted: {autokey_encrypted}\nDecrypted: {autokey_decrypted}")