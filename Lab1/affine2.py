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
    
    try:
        encrypted_message = input('Enter encrypted message\n')
        decrypted_message = decrypt(encrypted_message, 5, 6)
        print('Decrypted: ' + decrypted_message)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
