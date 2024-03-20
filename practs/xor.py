# XOR return 0 if the bits are the same and 1 if they are the same
# For Integers: convert first from decimal to binary

def compute_xor(num, txt):
    # Convert both to binary
    binary_num = bin(num)[2:]
    binary_txt = ''.join(format(ord(char), '08b') for char in txt)

    # Make sure the two are the same length
    max_len = max(len(binary_num), len(binary_txt))

    binary_num = binary_num.zfill(max_len)
    binary_txt = binary_txt.zfill(max_len)

    binary_result = ''.join(str(int(bit1) ^ int(bit2))
                            for bit1, bit2 in zip(binary_num, binary_txt))

    # Perform XOR operation
    print("Binary Result:", binary_result)

    # Convert back the binary to string
    # Change the binary result to multiples of 8 bits

    binary_result_padded = binary_result.zfill(((len(binary_result)+7)//8)*8)

    # Split the binary string into 8-bit chunks
    chunks = [binary_result_padded[i:i+8]
              for i in range(0, len(binary_result_padded), 8)]

    # Convert each chunk to its corresponding ASCII characters
    result = ''.join(chr(int(chunk, 2)) for chunk in chunks)

    # Join all the characters together to form a string
    print("Resulting String: ", result)


compute_xor(13, "label")
