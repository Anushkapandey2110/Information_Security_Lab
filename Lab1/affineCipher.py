def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def encrypt(message, a, b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    message = message.lower()
    for i in message:
        if i in alphabet:
            index = ((a * (ord(i) - 97) + b) % 26)
            result += alphabet[index]
        else:
            result += i
    return result

def decrypt(message, a, b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    message = message.lower()
    a_inv = mod_inverse(a, 26)
    for i in message:
        if i in alphabet:
            index = (a_inv * ((ord(i) - 97) - b) % 26)
            result += alphabet[index]
        else:
            result += i
    return result

def main():
    message = input('Enter a message\n')
    a = int(input('Enter a (must be prime)\n'))
    b = int(input('Enter b\n'))
    
    if a < 1 or b < 0 or b >= 26:
        print('Invalid input for a or b.')
        return
    
    try:
        encrypted_message = encrypt(message, a, b)
        print('Cipher: ' + encrypted_message)
        decrypted_message = decrypt(encrypted_message, a, b)
        print('Decrypted: ' + decrypted_message)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

