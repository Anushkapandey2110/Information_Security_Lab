def encrypt(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = message.lower()
    key = key.lower()
    result = ""
    x = 0
    
    for i in message:
        if i in alphabet:
            x = x % len(key)
            index = ((ord(i) - 97) + (ord(key[x]) - 97)) % 26
            result += alphabet[index]
            x += 1
        else:
            result += i  # Preserve non-alphabet characters in the result
    
    return result

def decrypt(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    key = key.lower()
    x = 0
    
    for i in message:
        if i in alphabet:
            x = x % len(key)
            index = ((ord(i) - 97) - (ord(key[x]) - 97)) % 26
            result += alphabet[index]
            x += 1
        else:
            result += i  # Preserve non-alphabet characters in the result
    
    return result

def main():
    message = input('Enter a message\n')
    key = input('Enter the key\n')
    encrypted_message = encrypt(message, key)
    print("Cipher: " + encrypted_message)
    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypt: " + decrypted_message)

if __name__ == "__main__":
    main()

