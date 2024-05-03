import numpy as np
import sympy as sp
import math as m
import random as ran


def get_bit(byte, index):
    return (byte >> (8 - (index + 1)) & 1) == 1


def set_bit(byte, bit, index):
    if bit:
        result = byte | (128 >> index)
    else:
        result = byte & ~(128 >> index)
    return result


class Knapsack:
    def __init__(self):
        self.a = []
        self.a_prim = []
        self.a_string = ""
        self.a_prim_string = ""
        self.m = 0
        self.w = 0
        self.inv_w = 0
        self.m_string = ""
        self.w_string = ""
        self.generate_keys()

    def generate_keys(self):
        self.m = ran.randint(2**63, 2**64-1)
        prime_m = int(sp.nextprime(self.m))
        if prime_m > 2**64-1:
            prime_m = int(sp.prevprime(self.m))
        self.m = prime_m
        self.w = ran.randint(2 ** 15, 2 ** 16-1)
        prime_w = int(sp.nextprime(self.w))
        if prime_w > 2**16-1:
            prime_w = int(sp.prevprime(self.w))
        self.w = prime_w
        while m.gcd(self.m, self.w) != 1:
            self.w = int(sp.nextprime(self.w))
            if self.w > self.m:
                raise Exception("Error")
        self.inv_w = int(sp.mod_inverse(self.w, self.m))
        elements_sum = 0
        for i in range(8):
            element = ran.randint(2**((i*2)+7), 2**((i*2)+8)-1)
            while element < elements_sum:
                element = ran.randint(2 ** ((i * 2) + 7), 2 ** ((i * 2) + 8)-1)
            elements_sum += element
            self.a.append(element)
            self.a_prim.append((element * self.w) % self.m)
        self.a_string = ",".join([hex(x)[2:] for x in self.a])
        self.a_prim_string = ",".join([hex(x)[2:] for x in self.a_prim])
        self.m_string = hex(self.m)[2:]
        self.w_string = hex(self.w)[2:]

    def encrypt(self, plain_text, is_text):
        if is_text:
            plain_text = plain_text.encode("iso-8859-2")
        cipher = []
        for i in range(len(plain_text)):
            partial_sum = 0
            byte = plain_text[i]
            for j in range(8):
                bit = get_bit(byte, j)
                if bit:
                    partial_sum += self.a_prim[j]
            cipher.append(partial_sum)
        cipher = ",".join([hex(x)[2:] for x in cipher])
        cipher = cipher.encode("iso-8859-2")
        return cipher

    def decrypt(self, cipher_text, is_text):
        plain_text = bytearray()
        cipher_text = cipher_text.decode("iso-8859-2")
        cipher_text = cipher_text.split(",")
        cipher_text = [int(hex_str, 16) for hex_str in cipher_text]
        for i in range(len(cipher_text)):
            plain_text.append(0)
            cipher_text[i] *= self.inv_w
            cipher_text[i] %= self.m
            for j in range(8):
                if cipher_text[i] >= self.a[7-j]:
                    plain_text[i] = set_bit(plain_text[i], True, 7-j)
                    cipher_text[i] -= self.a[7-j]
        if is_text:
            plain_text = plain_text.decode("iso-8859-2")
        return plain_text

# TESTING PURPOSES


knap = Knapsack()
print("klucz prywatny", knap.a_string)
print("Klucz jawny", knap.a_prim_string)
print("Wartość m", knap.m_string)
print("Wartość w", knap.w_string)
encrypted = knap.encrypt("Gżegżółka", True)
print("Kryptogram", encrypted)
print("Odszyfrowane:", knap.decrypt(encrypted, True))
