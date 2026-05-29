class RailFenceCipher:
    def __init__(self):
       pass

    def rail_fence_encrypt(self, plaintext, num_rails):
        rails = [[]for _ in range(num_rails)]
        rail_index = 0
        direction = 1
        for char in plaintext:
            if char.isalpha():
                rails[rail_index].append(char)
                rail_index += direction
                if rail_index == 0 or rail_index == num_rails - 1:
                    direction *= -1
                    rair_index += direction
        cipher_text = ''.join([''.join(rail) for rail in rails])
        return cipher_text
    
    def rail_fence_decrypt(self, cipher_text, num_rails):
        rail_lenghths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            if cipher_text[rail_index].isalpha():
                rail_lenghths[rail_index] += 1
                rail_index += direction
                if rail_index == 0 or rail_index == num_rails - 1:
                    direction *= -1
                    rail_index += direction

        rails = []
        start = 0
        for length in rail_lenghths:
            rails.append(list(cipher_text[start:start + length]))
            start += length
        plaintext = ''
        rail_index = 0
        start = 0
        for length in rail_lenghths:
            plaintext += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
               direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plaintext