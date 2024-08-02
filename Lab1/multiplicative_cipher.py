def encrypt(text, key):
	result = " "
	for i in range(len(text)):
		if(text[i] == " " ):
			result += " "
		char = text[i]
		if(char.isupper()):
			result += chr((ord(char) * key -65 ) % 26 + 65)
		elif(char.islower()):
			result += chr((ord(char) * key -97 ) % 26 +97)
		else:
			result+=char
	return result
def decrypt(ciphertext, key):
	plaintext = " "
	for i in range(len(ciphertext)):
		if(ciphertext[i] == " "):
			plaintext += " "
		char = ciphertext[i]
		if(char.isupper()):
			plaintext += chr((ord(char) * pow(key, -1, 26) -65 ) % 26 + 65)
		elif(char.islower()):
			plaintext += chr((ord(char) * pow(key, -1, 26) -97 ) % 26 + 97)
		else:
		       plaintext+=char
	return plaintext
text = input("Enter the text")
key = int(input("Enter the key"))
print ( "Text : " + text)
print ( "Key :  " + str(key))
print ( "Cipher : " + encrypt(text,key))
ciphertext = encrypt(text,key)
print ("Decrypted : " + decrypt(ciphertext,key))


