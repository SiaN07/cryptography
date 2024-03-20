#!/usr/bin/env python3
import sys
import random
import time
# I seed my random generator
random.seed(time.time())
# I choose at random my parameters for LCG
# GOOD LUCK BRUTEFORCING THEM! AHAHAHAHAHAHAHAHAHAHAHAHAHAH
A = random.randrange(2**128)
C = random.randrange(2**128)
n = 256
# Convert PT to ASCII bytes
txt = "From: ".encode('ASCII')

# Read the ciphertext from the file
f = open("captured_ct.txt", "rb")
ct = list(f.read())

# Derive k0 by XORing b'F' with ct[0]
k0 = ord('F') ^ ct[0]

# Initialize variables
pt_decrypted = b''  # Initialize decrypted plaintext as bytes
decrypted_string = ""

# Brute-force search for A and C
for A_candidate in range(256):
    for C_candidate in range(256):
        A = A_candidate
        C = C_candidate
        n = 256

        # Initialize k0 for each combination of A and C
        ki = k0

        # Perform decryption in 32-bit blocks
        pt_decrypted = b''
        for i in range(len(ct)):
            # XOR ciphertext byte with ki
            pt_byte = ki ^ ct[i]
            # Append decrypted byte to the decrypted plaintext
            pt_decrypted += bytes([pt_byte])
            # Calculate ki for the next byte using LCG formula
            ki = (A * ki + C) % n

        # Convert the decrypted bytes to a string using UTF-8 encoding
        decrypted_string = pt_decrypted.decode('utf-8', errors='replace')

        # Check if the decrypted string starts with "From: "
        if decrypted_string.startswith("From: "):
            print("Decrypted plaintext:", decrypted_string)
            print("A:", A)
            print("C:", C)
            sys.exit()  # Exit after finding the correct A and C
