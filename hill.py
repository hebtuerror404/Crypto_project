from sympy import *


def hill_encrypt(plain_text, key, n):
    key_data = []
    row_list = []
    for i in range(len(key)):
        row_list.append(key[i])
        if len(row_list) == n:
            key_data.append(row_list)
            row_list = []
    print(key_data)
    #
    # for i in plain_text:
    #     if i == ' ':
    #         enc_text += ' '
    #         continue
    #     if i.isupper():
    #         enc_text += chr(((ord(i) + ord(key[key_index]) - ord('a') - ord('A')) % 26) + ord('A'))
    #         key_index = (key_index + 1) % len(key)
    #     else:
    #         enc_text += chr(((ord(i) + ord(key[key_index]) - 2 * ord('a')) % 26) + ord('a'))
    #         key_index = (key_index + 1) % len(key)
    # return enc_text


hill_encrypt("hill", [1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
