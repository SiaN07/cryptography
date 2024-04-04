#!/usr/bin/env python3
import binascii
import sys
from sympy import mod_inverse

n = 3885939818809226866639787043363807561348795134092369130950983385470901806736361565466089297128250818994339484840348246849859686706799610146322341287843148253011924185299904669597627551758155800320077912889550691379091497725128289299633986277751193246120847022674590432383681458993045745957361247628898619533833648251443916733282577886721293431036458439415555101097990025528589956459090061384778695974308595402123516471802342910395085919062194938719275688182244497225339097083024039098640715244014285827272513848016293518825950785609827464234980855575137963828480665401893527147121584763680409101485362879563673787527
e = 17
print("This is n: \n")
print(n)
print("\n")

# Choose the message to encrypt.
m = "a"
# Encode each character as an integer
m_int = [ord(letter) for letter in m]
print("Integer: ", m_int)

# Encrypt with RSA 1024 bit, TOP security
c = [(num ** e) % n for num in m_int]
# Save the message
with open("ct_msg.txt", "w") as f:
    f.write('\t'.join(str(p) for p in c))


file1 = open("ct_msg.txt", "r")
print(file1.read())


def calculate_private_exponent(e, n, plaintext, ciphertext):
    phi_n = totient(n)
    d = pow(e, -1, phi_n)
    return d

# Example values


plaintext = 97
ciphertext = 5958260438588051333281183456765537

d = calculate_private_exponent(e, n, plaintext, ciphertext)
print("Private exponent (d):", d)
