def decrypt(hint,key,message):
	alphabet='abcdefghijklmnopqrstuvwxyz'
	hint=hint.lower()
	message=message.lower()
	key=key.lower()
	ind=(ord(hint[0])-97)-(ord(key[0])-97)
	if ind<0:
		ind=ind+26
	print(ind)
	result=""
	for i in message:
		index=(ord(i)-97)+ind
		if index<0:
			index=index+26
		result+=alphabet[int(index%26)]
	
	return result
	

def main():
	hint=input('Enter decrypted text\n')
	key=input('Enter cipher text\n')
	message=input('Enter message to decrypt\n')
	print('decrypted message: '+decrypt(hint,key,message))

if __name__=="__main__":
	main()
