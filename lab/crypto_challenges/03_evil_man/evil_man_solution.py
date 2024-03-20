import random
import time

# Load the ciphertext from the file
with open("deepest_secrets.txt", "rb") as f:
    enc = list(f.read())

# Extract the seed from the last bytes of the file
sample = str(time.time()).encode('ASCII')
enc_time = enc[len(enc) - len(sample) + 1 : len(enc)]
dec_time = [i ^ 0x88 for i in enc_time]

# Rebuild the seed as a string
enc_seed = ''.join([chr(i) for i in dec_time if chr(i).isdigit()])

# Convert the seed to a float
seed = float(enc_seed)

print('The random seed used for key generation is:', enc_seed)

# Seed the random number generator
random.seed(seed)

# Generate the key
key = [random.randrange(256) for _ in range(len(enc) - len(sample) + 1)]
print('The key used for encryption is:', key)

# Decrypt and print the message
dec_msg = [c ^ k for (c, k) in zip(enc[:len(enc) - len(sample) + 1], key)]
print(''.join([chr(i) for i in dec_msg]))
