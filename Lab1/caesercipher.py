def caesercipher(message,shift):

	
	alphabet='abcdefghijklmnopqrstuvwxyz'
	message=message.lower()
	
	result=""
	
	for letter in message :
		if letter in alphabet :
			index=alphabet.find(letter)
			index=(index+int(shift))%26
			
			if index<0 :
				index=index+26;
			
			result=result+alphabet[index]
		
		else:
			result=result+letter #if symbol is . / space etc
	
	return result
	
def decrypt(message,shift):

	alphabet='abcdefghijklmnopqrstuvwxyz'
	message=message.lower()
	result=""
	
	for letter in message:
		if letter in alphabet:
			index=alphabet.find(letter)
			index=(index-int(shift))%26
			if index<0:
				index=inex+26
		
			result=result+alphabet[index]
		else:
			result=result+letter
	return result
	

def main():
   message=input('Enter a message to encrypt\n')
   shift=input('\nEnter shift\n')
   print(message)
   print(caesercipher(message,shift))
   
   message=input('\nEnter message to decrypt\n')
   shift=input('\nEnter shift\n')
   print(message)
   print(decrypt(message,shift))

if __name__ == "__main__":
    main()
    
#abcdefghijklmnopqrstuvwxyz

