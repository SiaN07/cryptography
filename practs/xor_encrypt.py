def xor_encrypt(text, key):
    # Initialize an empty string to store the encrypted result
    encrypted_text = ""

    # Loop through each character in the text
    for char in text:
        # Perform XOR operation between the character's ASCII value and the key
        encrypted_char = chr(ord(char) ^ key)

        # Append the encrypted character to the result string
        encrypted_text += encrypted_char

    return encrypted_text

# Encrypt the string "label" using XOR with key 13
encrypted_string = xor_encrypt("label", 13)
print("Encrypted string:", encrypted_string)
