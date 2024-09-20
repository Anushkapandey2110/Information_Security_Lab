def create_playfair_matrix(keyword):
    matrix = []
    used_chars = set()
    keyword = keyword.replace('j', 'i').lower()
    
    for char in keyword:
        if char not in used_chars and char.isalpha():
            matrix.append(char)
            used_chars.add(char)
    
    for char in 'abcdefghiklmnopqrstuvwxyz':
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]


def preprocess_message(message):
    message = message.lower().replace('j', 'i').replace(" ", "")
    processed_message = ""
    
    i = 0
    while i < len(message):
        if i == len(message) - 1:
            processed_message += message[i] + 'x'
            i += 1
        elif message[i] == message[i + 1]:
            processed_message += message[i] + 'x'
            i += 1
        else:
            processed_message += message[i] + message[i + 1]
            i += 2
    return processed_message


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def playfair_encrypt(matrix, message):
    encrypted_message = ""
    
    for i in range(0, len(message), 2):
        char1 = message[i]
        char2 = message[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        
        if row1 == row2:
            encrypted_message += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_message += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_message += matrix[row1][col2] + matrix[row2][col1]
    
    return encrypted_message


secret_key = "GUIDANCE"
message = "The key is hidden under the door pad"

matrix = create_playfair_matrix(secret_key)
print("Playfair Matrix:")
for row in matrix:
    print(row)

processed_message = preprocess_message(message)
print("\nProcessed Message:", processed_message)

encrypted_message = playfair_encrypt(matrix, processed_message)
print("\nEncrypted Message:", encrypted_message)