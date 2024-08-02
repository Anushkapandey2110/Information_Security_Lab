def modinv(a, num):
    # Iterate over possible values to find the modular inverse
    for i in range(num):
        if (a * i) % num == 1:
            return i
    return None  # Return None if no modular inverse exists

def encrypt(text, a, b):
	result = " "
	for i in range(len(text)):
		if(text[i] == " "):
			result+= " "
		char=text[i]
		if(char.isupper()):
			result += chr((a * ord(char) +b -65) % 26 +65)
		elif(char.islower()):
			result += chr((a * ord(char) +b -97) % 26 + 97)
		else:
			result+= char
	return result
def decrypt(cipher, a, b):
	plaintext = " "
	for i in range(len(cipher)):
		if(cipher[i] == " "):
			plaintext+= " " 
		char=cipher[i]
		if(char.isupper()):
			plaintext+= chr(( modinv(a,26) * ord(char) -b -65) % 26 +65)
		elif(char.islower()):
			plaintext+= chr(( modinv(a,26) * ord(char) -b -97) % 26 + 97)
		else:
			plaintext+= char
	return plaintext
text = "I am learning Information Security"
a = 15 
b = 20
cipher=encrypt(text, a, b)
print ( "Text :  " + text)
print ( "Key : " + "(" +  str(a) + " "   + str(b) + ")")
print ( "Cipher :" + encrypt(text, a, b)) 
print ( "Decrypted :" + decrypt(cipher, a, b))
