#!/usr/bin/env python3
import sys
import time

# Constants for the Linear Congruential Generator (LCG)
A = 1103515245
C = 12345
n = 2**31

# Convert PT to ASCII bytes
txt = "From: ".encode('ASCII')

# CT from the captured txt
# How to read bytes from a file
f = open("captured_ct_easy.txt", "rb")
ct = list(f.read())

# Derive k0 from the first 4 bytes of the ciphertext and plaintext
ki_b=[txt[0]^ct[0], txt[1]^ct[1], txt[2]^ct[2], txt[3]^ct[3]]

ki=ki_b[3]<<24|ki_b[2]<<16|ki_b[1]<<8|ki_b[0]


print("ki:", ki)

# Initialize variables
pt_decrypted = b''  # Initialize decrypted plaintext as bytes

# Perform decryption in 32-bit blocks
for i in range(int(len(ct) / 4)):
    ki_b = [ki % 256, (ki >> 8) % 256, (ki >> 16) %
            256, (ki >> 24) % 256]  # Split ki into bytes
    # XOR ciphertext block with ki
    pt_block = [a ^ b for (a, b) in zip(ki_b, ct[i * 4:i * 4 + 4])]
    # Append decrypted block to the decrypted plaintext
    pt_decrypted += bytes(pt_block)
    ki = (A * ki + C) % n  # Update ki for the next block

# Convert the decrypted bytes to a string using UTF-8 encoding
decrypted_string = pt_decrypted.decode('utf-8', errors='replace')

# Print the decrypted plaintext as bytes
print("Decrypted plaintext:", decrypted_string)
