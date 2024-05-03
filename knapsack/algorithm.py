import numpy as np
import sympy as sp
import math as m
import random as ran


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


knap = Knapsack()
print(knap.a_string)
print(knap.a_prim_string)
print(knap.m_string)
print(knap.w_string)
