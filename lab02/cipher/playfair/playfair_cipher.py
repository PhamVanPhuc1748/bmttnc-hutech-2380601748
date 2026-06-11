class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        
        matrix = []
        for char in key:
            if char.isalpha() and char not in matrix: 
                matrix.append(char)
                
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [
            letter for letter in alphabet if letter not in matrix]

        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break

        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        
        clean_text = ""
        for char in plain_text:
            if char.isalpha():
                clean_text += char
                
        prepared_text = ""
        i = 0
        while i < len(clean_text):
            prepared_text += clean_text[i]
            if i + 1 < len(clean_text):
                if clean_text[i] == clean_text[i + 1]: 
                    prepared_text += "X"
                else:
                    prepared_text += clean_text[i + 1]
                    i += 1
            i += 1
            
        encrypted_text = ""

        for i in range(0, len(prepared_text), 2):
            pair = prepared_text[i:i+2]
            if len(pair) == 1:  
                pair += "X"
            
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        banro = ""
        for i in range(len(decrypted_text)):
            if decrypted_text[i] == 'X' and i > 0 and i < len(decrypted_text) - 1:
                if decrypted_text[i-1] == decrypted_text[i+1]:
                    continue
            banro += decrypted_text[i]

        if banro.endswith('X'):
            banro = banro[:-1]

        return banro