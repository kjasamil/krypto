# AUTORZY: Kamil Jaśkiewicz 247682, Nikodem Wojtczak 247823
# ZESTAW IV

import numpy as np
import math as m
import random as r


PC_1 = np.array([57, 49, 41, 33, 25, 17, 9,
                 1, 58, 50, 42, 34, 26, 18,
                 10, 2, 59, 51, 43, 35, 27,
                 19, 11, 3, 60, 52, 44, 36,
                 63, 55, 47, 39, 31, 23, 15,
                 7, 62, 54, 46, 38, 30, 22,
                 14, 6, 61, 53, 45, 37, 29,
                 21, 13, 5, 28, 20, 12, 4], dtype="uint8")

shifts = np.array([1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1], dtype="uint8")

PC_2 = np.array([14, 17, 11, 24, 1, 5,
                 3, 28, 15, 6, 21, 10,
                 23, 19, 12, 4, 26, 8,
                 16, 7, 27, 20, 13, 2,
                 41, 52, 31, 37, 47, 55,
                 30, 40, 51, 45, 33, 48,
                 44, 49, 39, 56, 34, 53,
                 46, 42, 50, 36, 29, 32], dtype="uint8")

IP = np.array([58, 50, 42, 34, 26, 18, 10, 2,
               60, 52, 44, 36, 28, 20, 12, 4,
               62, 54, 46, 38, 30, 22, 14, 6,
               64, 56, 48, 40, 32, 24, 16, 8,
               57, 49, 41, 33, 25, 17, 9, 1,
               59, 51, 43, 35, 27, 19, 11, 3,
               61, 53, 45, 37, 29, 21, 13, 5,
               63, 55, 47, 39, 31, 23, 15, 7], dtype="uint8")

E = np.array([32, 1, 2, 3, 4, 5,
              4, 5, 6, 7, 8, 9,
              8, 9, 10, 11, 12, 13,
              12, 13, 14, 15, 16, 17,
              16, 17, 18, 19, 20, 21,
              20, 21, 22, 23, 24, 25,
              24, 25, 26, 27, 28, 29,
              28, 29, 30, 31, 32, 1], dtype="uint8")

S = np.array([14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
              0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
              4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
              15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13,
              15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
              3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
              0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
              13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9,
              10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
              13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
              13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
              1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12,
              7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
              13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
              10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
              3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14,
              2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
              14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
              4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
              11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3,
              12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
              10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
              9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
              4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13,
              4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
              13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
              1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
              6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12,
              13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
              1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
              7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
              2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11], dtype="uint8")

P = np.array([16, 7, 20, 21,
              29, 12, 28, 17,
              1, 15, 23, 26,
              5, 18, 31, 10,
              2, 8, 24, 14,
              32, 27, 3, 9,
              19, 13, 30, 6,
              22, 11, 4, 25], dtype="uint8")

IP_minus_1 = np.array([40, 8, 48, 16, 56, 24, 64, 32,
                       39, 7, 47, 15, 55, 23, 63, 31,
                       38, 6, 46, 14, 54, 22, 62, 30,
                       37, 5, 45, 13, 53, 21, 61, 29,
                       36, 4, 44, 12, 52, 20, 60, 28,
                       35, 3, 43, 11, 51, 19, 59, 27,
                       34, 2, 42, 10, 50, 18, 58, 26,
                       33, 1, 41, 9, 49, 17, 57, 25], dtype="uint8")


# w programie jako bajt traktowana jest liczba całkowita typu np.uint8

# permutation() -> funkcja permutująca wejściowy blok danych data_bytes_array; typ permutacji określony jest w
# zmiennej permutation_type i jest to jeden z następujących napisów: "pc-1", "pc-2", "ip", "e", "p", "ip-1"
# shape określa rozmiar tablicy bajtów, do której zapisywane będą bity po permutacji, permutation_table określa, jaka
# tablica zostanie użyta w procesie permutacji


def permutation(data_bytes_array, permutation_type):
    if permutation_type == "pc-1":
        shape = np.uint(7)
        permutation_table = PC_1
    elif permutation_type == "pc-2":
        shape = np.uint(6)
        permutation_table = PC_2
    elif permutation_type == "ip":
        shape = np.uint(8)
        permutation_table = IP
    elif permutation_type == "e":
        shape = np.uint(6)
        permutation_table = E
    elif permutation_type == "p":
        shape = np.uint(4)
        permutation_table = P
    elif permutation_type == "ip-1":
        shape = np.uint(8)
        permutation_table = IP_minus_1
    else:
        raise Exception("Niewłaściwy typ permutacji.")
    permuted_data = np.zeros((shape,), dtype="uint8")
    for i in range(shape*np.uint(8)):
        permuted_data = set_bit(permuted_data, i, get_bit(data_bytes_array, permutation_table[i] - 1))
    return permuted_data


# string_to_bytes_array() zwraca tablicę bajtów dla wskazanego napisu; pozwalamy na to, aby w tekstach do szyfrowania
# znajdowały się polskie znaki, stąd enkodowanie odbywa się wg iso-8859-2, gdzie każdy znak zapisywany jest na 1 bajcie


def string_to_bytes_array(string):
    bytes_array = np.array([], dtype="uint8")
    for char in string:
        bytes_array = np.append(bytes_array, np.uint8(char.encode("iso-8859-2")[0]))
    return bytes_array


# bytes_array_to_string() to funkcja odwrotna do powyższej


def bytes_array_to_string(bytes_array):
    bytes_array = bytes(bytes_array)
    return bytes_array.decode("iso-8859-2")


# get_bit() zwraca wartość True jeżeli w tablicy bajtów bytes_array na pozycji index znajduje się 1, w przeciwnym
# przypadku zwraca False; aby odczytać wartość bitu, przesuwamy wszystkie bity w danym bajcie w prawo tak, aby
# na najmniej znaczącej pozycji znalazł się interesujący nas bit, wykonujemy bitowego AND-a na otrzymanej liczbie z
# liczbą 1 i sprawdzamy, czy wynikiem jest 1 (00000001) czy 0 (00000000)


def get_bit(bytes_array, index):
    byte_index = np.uint8(index / 8)
    bit_index = np.uint8(index % 8)
    return (bytes_array[byte_index] >> (8 - (bit_index + 1)) & 1) == 1


# set_bit() ustawia we wskazanej tablicy bajtów na pozycji index - 1, jeżeli bit == True lub 0, jeżeli bit == False;
# aby ustawić 1, znajdujemy maskę, przesuwając bity w liczbie 128 (10000000) o liczbę pozycji odpowiadającą pozycji
# bitu do ustawienia, w przypadku ustawiania 0 maskę dodatkowo negujemy
# aby ustawić 1 wykonujemy bitowego OR-a na bajcie i masce, natomiast, aby ustawić 0, wykonujemy bitowego AND-a
# podmieniamy uzyskany bajt z bajtem w tablicy


def set_bit(bytes_array, index, bit):
    byte_index = np.uint8(index / 8)
    bit_index = np.uint8(index % 8)
    if bit:
        result = np.uint8(bytes_array[byte_index] | (128 >> bit_index))
    else:
        result = np.uint8(bytes_array[byte_index] & ~(128 >> bit_index))
    bytes_array[byte_index] = result
    return bytes_array


# get_64_bit_block() pobiera z tablicy bajtów bytes_array 8-elementową tablicę bajtów (czyli 64-bitowy blok danych)
# zaczynającą się od bitu na pozycji block_index * 8; jeżeli w czasie przepisywania bajtów do bloku wykroczyliśmy
# poza zakres tablicy bajtów, którą podaliśmy na wejściu, dodajemy zera na końcu bloku wyjściowego, aby blok danych
# miał zawsze 64 bity


def get_64_bit_block(bytes_array, block_index):
    start = 8 * block_index
    end = start + 8
    block = np.array([], dtype="uint8")
    for i in range(start, end):
        if i < len(bytes_array):
            block = np.append(block, bytes_array[i])
        else:
            block = np.append(block, np.uint8(0))
    return block


# hex_string_to_bytes_array() służy do konwertowania zaszyfrowanego tekstu bądź kluczy na tablicę bajtów


def hex_string_to_bytes_array(hex_string):
    bytes_array = np.array([], dtype="uint8")
    while hex_string:
        hex_chunk = hex_string[:2]
        bytes_array = np.append(bytes_array, np.uint8(int(hex_chunk, 16)))
        hex_string = hex_string[2:]
    return bytes_array


# divide_key() dzieli 56-bitowy klucz (już poddany permutacji PC-1) na dwie 28-bitowe części (w programie zrealizowano
# to jako 4-bajtowe części z 4 zerami na końcu)
# w pierwszym kroku kopiuje pierwsze 3 bajty z klucza do części C i dodaje na końcu tej części bajt 00000000,
# następnie 4 pierwsze bity czwartego bajtu w części C są bitami od 24 do 27 klucza,
# bity od 0 do 27 w części D są bitami od 28 do 56 klucza,
# po podzieleniu zwracamy tablicę z dwoma częściami C i D


def divide_key(key_bytes_array):
    C = key_bytes_array[:3]
    C = np.append(C, 0)
    D = np.zeros((4,), dtype="uint8")
    for i in range(0, 4):
        bit_to_set = get_bit(key_bytes_array, 24 + i)
        C = set_bit(C, 24 + i, bit_to_set)
    for i in range(0, 28):
        bit_to_set = get_bit(key_bytes_array, 28 + i)
        D = set_bit(D, i, bit_to_set)
    return np.array([C, D], dtype="uint8")


# shift_left() dokonuje rotacji w lewo na bitach w tablicy key_bytes_array o liczbę pozycji określoną w shift,
# czyli bity z początku trafiają na koniec bajtu


def shift_left(key_bytes_array, shift):
    shifted = np.zeros((4,), dtype="uint8")
    for i in range(0, 28):
        bit_to_set = get_bit(key_bytes_array, (i + shift) % 28)
        shifted = set_bit(shifted, i, bit_to_set)
    return shifted


# join_keys() łączy dwie 28-bitowe (w programie 4-bajtowe) połówki klucza: first_half i second_half;
# trzy pierwsze bajty złączonego klucza to trzy pierwsze bajty pierwszej części, bity od 24 do 27 w złączonym kluczu
# do cztery przedostatnie bity pierwszej części, pozostałe bity złączonego klucza od 28 do 55 to bity drugiej części;
# mimo że łączy 4-bajtowe tablice to i tak na końcu dostajemy 56-bitowy blok, czyli tablicę 7-bajtową


def join_keys(first_half, second_half):
    key_to_join = np.zeros((7,), dtype="uint8")
    for i in range(0, 3):
        key_to_join[i] = first_half[i]
    for i in range(24, 28):
        bit_to_set = get_bit(first_half, i)
        key_to_join = set_bit(key_to_join, i, bit_to_set)
    k = np.uint(0)
    for i in range(28, 56):
        bit_to_set = get_bit(second_half, k)
        key_to_join = set_bit(key_to_join, i, bit_to_set)
        k += 1
    return key_to_join


# generate_subkeys() zwraca dla podanej tablicy bajtów 56-bitowego klucza 16 podkluczy w następujący sposób:
# poddaje 64-bitowy klucz permutacji z użyciem tablicy PC-1, przez co otrzymujemy klucz 56-bitowy (permutacja oprócz
# mieszania bitów pomija co ósmy bit klucza)
# dzieli 56-bitowy klucz na dwie połówki 28-bitowe C i D, które są podstawą do dalszych operacji
# poniższe kroki wykonywane są 16 razy:
#   1. bity w części C i D przesuwane są rotacyjnie w lewo o ilość pozycji określoną w tablicy shifts, odczytywana jest
#   z tej tablicy komórka o indeksie takim jak numer iteracji, zapisujemy połówki C i D, ponieważ to na nich będziemy
#   w następnym kroku wykonywać rotację
#   2. po rotacji obie połówki C i D są łączone w 56-bitowy klucz
#   3. złączony klucz poddawany jest permutacji z użyciem tablicy PC-2, przez co otrzymujemy podklucz 48-bitowy
# otrzymujemy w ten sposób 16 podkluczy 48-bitowych


def generate_subkeys(key_bytes_array):
    pc_1_permuted_key = permutation(key_bytes_array, "pc-1")
    divided_key_parts = divide_key(pc_1_permuted_key)
    C = divided_key_parts[0]
    D = divided_key_parts[1]
    subkeys = np.empty((16, 6), dtype="uint8")
    for i in range(0, 16):
        C = shift_left(C, shifts[i])
        D = shift_left(D, shifts[i])
        CD = join_keys(C, D)
        subkeys[i] = permutation(CD, "pc-2")
    return subkeys


# xor() XOR-uje dwie tablice bajtów a i b


def xor(a, b):
    if len(a) != len(b):
        raise Exception("Bloki poddane XOR-owaniu muszą mieć identyczny rozmiar.")
    bytes_num = np.uint8(len(a))
    result = np.array([], dtype="uint8")
    for i in range(0, bytes_num):
        result = np.append(result, np.uint8(a[i] ^ b[i]))
    return result


# funkcja f() jest fragmentem funkcji Feistela; przyjmuje na wejściu 4-bajtową tablicę data_bytes_array i
# 6-bajtowy podklucz round_subkey;
# w pierwszym kroku XOR-ujemy podklucz z rezultatem permutacji rozszerzającej na 4-bajtowym bloku danych (wtedy
# rozmiar bloku danych zgadza się z rozmiarem podklucza, rozszerzamy z 32 do 48 bitów)
# wynik XOR-owania składa się teraz z ośmiu grup sześciu bitów; w każdej grupie pierwszy i ostatni bit tworzy 2-bitową
# liczbę reprezentującą numer wiersza, pozostałe bity (4 bity) reprezentują numer kolumny, numer porządkowy 6-bitowej
# grupy oznacza numer S-boxa, a numery wiersza i kolumny to współrzędne 4-bitowej liczby w odpowiednim S-boxie, które
# podmienią wskazaną 6-bitową grupę na grupę 4-bitową
# otrzymujemy zatem z 48-bitowego bloku danych blok 32-bitowy


def f(data_bytes_array, round_subkey):
    result = xor(round_subkey, permutation(data_bytes_array, "e"))
    output = np.zeros((4,), dtype="uint8")
    for i in range(0, 8):
        start_in_48 = np.uint8(i * 6)
        row = np.array([0], dtype="uint8")
        column = np.array([0], dtype="uint8")
        bit_to_set = get_bit(result, start_in_48)
        row = set_bit(row, 6, bit_to_set)
        bit_to_set = get_bit(result, start_in_48 + 5)
        row = set_bit(row, 7, bit_to_set)
        for j in range(1, 5):
            bit_to_set = get_bit(result, start_in_48 + j)
            column = set_bit(column, j + 3, bit_to_set)
        to_swap = np.array([S[(i * np.uint(64)) + (row * np.uint8(16)) + column]], dtype="uint8")
        start_in_32 = np.uint8(i * 4)
        k = np.uint8(0)
        for j in range(4, 8):
            bit_to_set = get_bit(to_swap, j)
            output = set_bit(output, start_in_32 + k, bit_to_set)
            k += 1
    output = permutation(output, "p")
    return output


# des() to funkcja szyfrująca 64-bitowy blok message_block korzystając z tablicy bajtów 64-bitowego klucza
# key_bytes_array (deszyfruje gdy flaga decryption_flag jest ustawiona na True) algorytmem DES
# na początku generowane są podklucze ze wskazanego klucza
# jeżeli deszyfrujemy, musimy odwrócić kolejność podkluczy
# poddajemy 64-bitowy blok danych permutacji wstępnej korzystając z tablicy IP, następnie dzielimy blok na dwie części
# 32-bitowe - lewą L i prawą R, które są podstawą do dalszych operacji
# poniższe kroki wykonujemy 16 razy:
#   1. nowa część L staje się starą częścią R (z poprzedniej iteracji)
#   2. nowa część R staje się wynikiem XOR-owania starej części L z wynikiem funkcji f wywołanej dla starej części R
#   i podklucza o numerze odpowiadającym numerowi iteracji
# po 16 takich rundach łączymy dwie części L i R, jednak zamieniając ich kolejność, czyli pierwsze 4 bajty to część R,
# natomiast ostatnie 4 to część L
# poddajemy uzyskany 64-bitowy blok danych permutacji końcowej korzystając z tablicy IP-1
# jest to już końcowy efekt szyfrowania korzystając z algorytmu DES


def des(key_bytes_array, message_block, decryption_flag):
    subkeys = generate_subkeys(key_bytes_array)
    if decryption_flag:
        subkeys = subkeys[::-1]
    message_block = permutation(message_block, "ip")
    L = message_block[:4]
    R = message_block[4:]
    for i in range(0, 16):
        old_L = L.copy()
        old_R = R.copy()
        L = old_R
        R = xor(old_L, f(old_R, subkeys[i]))
    output = np.array([0, 0, 0, 0, 0, 0, 0, 0], dtype="uint8")
    for i in range(0, 4):
        output[i] = R[i]
    for i in range(4, 8):
        output[i] = L[i-4]
    output = permutation(output, "ip-1")
    return output


# bytes_array_to_hex_string() konwertuje tablicę bajtów bytes_array na zapis heksadecymalny


def bytes_array_to_hex_string(bytes_array):
    return ''.join(['{:02X}'.format(x) for x in bytes_array])


# check_keys_length() sprawdza czy wszystkie klucze mają prawidłową długość, jeżeli nie, rzuca wyjątek


def check_keys_length(first, second, third):
    if len(first) != 16:
        raise Exception("Pierwszy klucz musi mieć długość 64 bitów.")
    if len(second) != 16:
        raise Exception("Drugi klucz musi mieć długość 64 bitów.")
    if len(third) != 16:
        raise Exception("Trzeci klucz musi mieć długość 64 bitów.")


# encrypt() to właściwa funkcja szyfrująca tekst plain_text z wykorzystaniem kluczy key_1, key_2 oraz key_3
# algorytmem DESX
# sprawdzane jest formatowanie kluczy, w przypadku braku spełnienia warunku poprawności rzucany jest wyjątek
# wszystkie dane na wejściu konwertowane są na tablice bajtów
# znajdujemy liczbę 64-bitowych bloków korzystając z długości tablicy bajtów tekstu, które następnie będą szyfrowane
# dla każdego 64-bitowego bloku:
#   1. XOR-ujemy blok z pierwszym kluczem
#   2. wynik XOR-owania szyfrujemy DES-em korzystając z klucza drugiego
#   3. wynik szyfrowania DES-em XOR-ujemy z kluczem trzecim
# otrzymując zaszyfrowany blok.


def encrypt(plain_text, key_1, key_2, key_3, isText):
    output = np.array([], dtype="uint8")
    if isText:
        text_bytes = string_to_bytes_array(plain_text)
    else:
        text_bytes = plain_text
    print(text_bytes)
    check_keys_length(key_1, key_2, key_3)
    try:
        key_1_bytes = hex_string_to_bytes_array(key_1)
        key_2_bytes = hex_string_to_bytes_array(key_2)
        key_3_bytes = hex_string_to_bytes_array(key_3)
    except ValueError:
        raise Exception("Jeden z kluczy nie jest w systemie szesnastkowym.")
    number_of_blocks = np.uint8(m.ceil(len(text_bytes) / 8))
    for i in range(number_of_blocks):
        block = get_64_bit_block(text_bytes, i)
        block = xor(block, key_1_bytes)
        block = des(key_2_bytes, block, False)
        block = xor(block, key_3_bytes)
        output = np.append(output, block)
    output = bytes_array_to_hex_string(output)
    return output
    # if isText:
    #     output = bytes_array_to_hex_string(output)
    #     return output
    # else:
    #     return output


# decrypt() to funkcja podobna do funkcji encrypt() z tą różnicą że stosujemy klucze w odwrotnej kolejności, łącznie
# ze stosowaniem podkluczy w szyfrowaniu DES w kolejności odwrotnej, dodatkowo sprawdzamy czy długość zaszyfrowanego
# tekstu jest wielokrotnością 64-bitów, jeżeli nie, rzucamy wyjątek
# usuwamy z otrzymanej tablicy bajtów końcowe zera, które zostały dodane przed szyfrowaniem w celu dopełnienia bloku
# otrzymaną tablicę bajtów konwertujemy na napis


def decrypt(cipher_text, key_1, key_2, key_3):
    if len(cipher_text) % 16 != 0:
        raise Exception("Długość zakodowanego bloku danych musi być wielokrotnością 64 bitów.")
    output = np.array([], dtype="uint8")
    try:
        cipher_bytes = hex_string_to_bytes_array(cipher_text)
    except ValueError:
        raise Exception("Szyfr musi być w systemie szesnastkowym.")
    check_keys_length(key_1, key_2, key_3)
    try:
        key_1_bytes = hex_string_to_bytes_array(key_1)
        key_2_bytes = hex_string_to_bytes_array(key_2)
        key_3_bytes = hex_string_to_bytes_array(key_3)
    except ValueError:
        raise Exception("Jeden z kluczy nie jest w systemie szesnastkowym.")
    number_of_blocks = np.uint8(len(cipher_bytes) / 8)
    for i in range(number_of_blocks):
        block = get_64_bit_block(cipher_bytes, i)
        block = xor(block, key_3_bytes)
        block = des(key_2_bytes, block, True)
        block = xor(block, key_1_bytes)
        output = np.append(output, block)
    while output[-1] == np.uint(0):
        output = output[:-1]
    # output = bytes_array_to_string(output)
    return output


# generate_keys() generuje trzy losowe 64-bitowe klucze


def generate_keys():
    keys = []
    for _ in range(3):
        random_number = np.uint64(r.randint(0, 2**64-1))
        keys.append(format(random_number, '016X'))
    return keys


# w programie nie sprawdzamy wyjątków dla funkcji, dla których dane wejściowe są podawane wewnątrz programu
# (zakładamy ich poprawność), jedynie dla funkcji, które będą wywoływane dla danych pobieranych z GUI
