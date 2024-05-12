import sympy as sp
import math as m
import random as ran
import struct


def get_bit(byte, index):  # pobranie bitu z odpowiedniej pozycji w bajcie
    return (byte >> (8 - (index + 1)) & 1) == 1  # True - bit jest 1, False - bit jest 0


def set_bit(byte, bit, index):  # ustawianie bitu na określonej pozycji w bajcie
    if bit:                     # bit = True jeżeli ustawiamy 1, bit = False jeżeli ustawiamy 0
        result = byte | (128 >> index)
    else:
        result = byte & ~(128 >> index)
    return result


# METODA WERYFIKUJĄCA POPRAWNOŚĆ KLUCZY.
# Ciąg a w kluczu prywatnym (wagi poszczególnych elementów wkładanych do "plecaka") musi być superrosnący, czyli każdy
# kolejny element jest większy od sumy poprzednich elementów
# ponadto szyfrujemy bajty, zatem ciąg a musi mieć 8 elementów
# wartość M musi być liczbą większą od sumy elementów ciągu a
# wartość W musi być liczbą mniejszą od liczby M i ponadto liczby M i W muszą być względnie pierwsze
# ciąg a' będący kluczem prywatnym liczy się na podstawie wzoru (a*W) mod M
# sprawdzane jest zatem czy podany klucz publiczny odpowiada wartościom z klucza prywatnego

def verify_keys(a, a_prim, m_val, w_val, everything=False):
    elements_sum = 0
    if len(a) != 8:
        raise ValueError("Liczba elementów ciągu 'a' w kluczu prywatnym nie wynosi 8.")
    for i in range(8):
        if a[i] < elements_sum:
            raise ValueError("Ciąg 'a' w kluczu prywatnym nie jest superrosnący.")
    if elements_sum > m_val:
        raise ValueError("Wartość 'm' w kluczu prywatnym nie jest większa od sumy elementów w ciągu a.")
    if m.gcd(m_val, w_val) != 1:
        raise ValueError("Wartości 'm' i 'w' w kluczu prywatnym nie są względnie pierwsze.")
    if m_val < w_val:
        raise ValueError("Wartość 'm' nie jest większa od wartości 'w' w kluczu prywatnym.")
    if everything:
        if len(a_prim) != 8:
            raise ValueError("Liczba elementów ciągu 'a_prim' w kluczu publicznym nie wynosi 8.")
        for i in range(8):
            if a_prim[i] != (a[i] * w_val) % m_val:
                raise ValueError("Klucz publiczny nie odpowiada wartościom z klucza prywatnego.")


# GENEROWANIE KLUCZA PUBLICZNEGO
# Dodatkowa funkcjonalność zwracająca string klucza publicznego w postaci szesnastkowej
# na podstawie podanego klucza prywatnego.

def generate_public_key(a_string, m_string, w_string):
    split_a = a_string.split(',')
    a = [int(element, 16) for element in split_a]
    m_val = int(m_string, 16)
    w_val = int(w_string, 16)
    try:
        verify_keys(a, None, m_val, w_val)
        public_key = []
        for i in range(8):
            element = (a[i] * w_val) % m_val
            public_key.append(element)
        public_key_string = ",".join([hex(x)[2:] for x in public_key])
        return public_key_string
    except ValueError as e:
        print("Nie można wygenerować klucza publicznego:", e)


class Knapsack:
    def __init__(self):
        self.a = []  # ciąg a (wagi poszczególnych elementów wkładanych do "plecaka"), klucz prywatny
        self.a_prim = []  # ciąg a' (klucz publiczny, a' = (a*W) mod M)
        self.a_string = ""
        self.a_prim_string = ""
        self.m = 0  # wartość M w kluczu prywatnym
        self.w = 0  # wartość W w kluczu prywatnym
        self.inv_w = 0  # wartość odpowiadająca W^-1 mod M
        self.m_string = ""
        self.w_string = ""

    # METODA GENERUJĄCA KLUCZE.
    # Wybierane są w sposób losowy liczby M i W, 2**63 < M <= 2**64-1 oraz 2**15 < W <= 2**16-1
    # czyli liczba M jest wielkości 8 bajtów, liczba W wielkości 2 bajtów
    # upewniamy się czy są względnie pierwsze, jeżeli nie to wybieramy kolejną wartość W
    # obliczamy W^-1 mod M
    # następnie jednocześnie tworzymy ciągi a i a' (jeden superrosnący, drugi nie superrosnący)
    # otrzymujemy klucz publiczny a' oraz klucz prywatny {M, W, a}

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
        self.a.clear()
        self.a_prim.clear()
        for i in range(8):
            element = ran.randint(2**((i*2)+10), 2**((i*2)+11)-1)
            while element < elements_sum:
                element = ran.randint(2 ** ((i * 2) + 7), 2 ** ((i * 2) + 8)-1)
            elements_sum += element
            self.a.append(element)
            self.a_prim.append((element * self.w) % self.m)
        self.a_string = ",".join([hex(x)[2:] for x in self.a])
        self.a_prim_string = ",".join([hex(x)[2:] for x in self.a_prim])
        self.m_string = hex(self.m)[2:]
        self.w_string = hex(self.w)[2:]

    # METODA USTAWIAJĄCA KLUCZE.
    # Wywoływana przy szyfrowaniu/deszyfrowaniu.

    def set_keys(self, a_string, a_prim_string, m_string, w_string):
        split_a = a_string.split(',')
        a = [int(element, 16) for element in split_a]
        split_a_prim = a_prim_string.split(',')
        a_prim = [int(element, 16) for element in split_a_prim]
        m_val = int(m_string, 16)
        w_val = int(w_string, 16)
        try:
            verify_keys(a, a_prim, m_val, w_val, True)
            self.a = a.copy()
            self.a_string = ",".join([hex(x)[2:] for x in self.a])
            self.a_prim = a_prim.copy()
            self.a_prim_string = ",".join([hex(x)[2:] for x in self.a_prim])
            self.m = m_val
            self.m_string = hex(self.m)[2:]
            self.w = w_val
            self.w_string = hex(self.w)[2:]
            self.inv_w = int(sp.mod_inverse(self.w, self.m))
        except ValueError as e:
            print("Nie można szyfrować przy użyciu wybranych kluczy:", e)

    # SZYFROWANIE.
    # Do szyfrowania wiadomości, którą wysyłamy do odbiorcy, używamy klucza publicznego odbiorcy (a').
    # n-ty bit ustawiony jako 1 w bajcie tekstu jawnego informuje, że do plecaka zostanie włożony element n-ty z a'
    # na podstawie bajtu obliczana jest suma wag tych włożonych elementów, otrzymując kryptogram
    # pakujemy każdą liczbę z tablicy zawierającej kryptogramy odpowiednich bajtów na 8 bajtach (q) jeżeli szyfrowaliśmy
    # plik, natomiast konwertujemy tą tablicę do stringa w postaci szesnastkowej, jeżeli szyfrowaliśmy tekst w oknie

    def encrypt(self, plain_text, is_text):
        if is_text:
            plain_text = plain_text.encode("iso-8859-2")
        cipher = []
        cipher_bytes = bytearray()
        for i in range(len(plain_text)):
            partial_sum = 0
            byte = plain_text[i]
            for j in range(8):
                bit = get_bit(byte, j)
                if bit:
                    partial_sum += self.a_prim[j]
            cipher.append(partial_sum)
        for num in cipher:
            cipher_bytes.extend(struct.pack("q", num))
        if is_text:
            hex_cipher = ['{:016x}'.format(num) for num in cipher]
            hex_cipher = "".join(hex_cipher)
            return hex_cipher
        return cipher_bytes

    # DESZYFROWANIE.
    # Jeżeli nadawca zaszyfrował wiadomość korzystając z klucza publicznego odbiorcy, to odbiorca, chcąc ją odszyfrować
    # korzysta ze swojego klucza prywatnego.
    # jeżeli deszyfrujemy tekst w oknie to konwertujemy string w postaci szesnastkowej do tablicy zawierającej
    # kryptogramy, jeżeli deszyfrujemy plik to rozpakowywujemy 8 bajtów z tablicy bajtów, konwertujemy do inta i
    # tworzymy z tych intów tablicę
    # każdy kryptogram mnożymy przez odwrotność mod M liczby W w modulo M, uzyskując sumę wag przedmiotów włożonych
    # do plecaka przy użyciu wag z ciągu a (klucz prywatny)
    # porównujemy te sumy z elementami ciągu a, iterując od końca
    # jeżeli suma jest większa od wagi sprawdzanego elementu z ciągu a, to oznacza to że ten element został włożony
    # do plecaka i na bicie o pozycji odpowiadającej pozycji elementu z ciągu a ustawiamy 1
    # jeżeli ustawiliśmy 1 to pomniejszamy sumę o wagę sprawdzonego przedmiotu

    def decrypt(self, cipher_text, is_text):
        plain_text = bytearray()
        if is_text:
            cipher_string = [cipher_text[i:i + 16] for i in range(0, len(cipher_text), 16)]
            cipher = [int(hex_str, 16) for hex_str in cipher_string]
        else:
            cipher = []
            for i in range(0, len(cipher_text), 8):
                num = struct.unpack("q", cipher_text[i:i + 8])[0]
                cipher.append(num)
        for i in range(len(cipher)):
            plain_text.append(0)
            cipher[i] *= self.inv_w
            cipher[i] %= self.m
            for j in range(8):
                if cipher[i] >= self.a[7-j]:
                    plain_text[i] = set_bit(plain_text[i], True, 7-j)
                    cipher[i] -= self.a[7-j]
        if is_text:
            plain_text = plain_text.decode("iso-8859-2")
        return plain_text
