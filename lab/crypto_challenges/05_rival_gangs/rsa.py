def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


def decrypt(ciphertext, private_key, modulus):
    return pow(ciphertext, private_key, modulus)


def solution():
    # Public key
    e = 17
    N = 5555555555931888888891173

    # Intercepted message
    ciphertext = 2439412161939172626535641

    # Correct prime factors of N
    # https://www.dcode.fr/rsa-cipher
    p = 1000000000061
    q = 5555555555593

    # Correct calculation of φ(N)
    phi = (p - 1) * (q - 1)

    # Calculate private key
    d = modinv(e, phi)

    # Decrypt the intercepted message
    plaintext = decrypt(ciphertext, d, N)
    print("Decrypted combination:", plaintext)

    pt = str(plaintext)

    return pt

