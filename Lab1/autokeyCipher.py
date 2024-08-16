def encrypt(message,key):
	keyword=key+message[:len(message)-1]
	print(keyword)
	result=""
	for i,x in keyword,message:
		print(i,x)
		
	return keyword

def main():
	encrypt("hello","n")
if __name__ == "__main__":
	main() 
