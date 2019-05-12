# -*- coding: UTF-8 -*-
from sympy import *

def hill_encrypt(plain_text, key, n):
    plain_text = ''.join(plain_text.split())
    key_data = []
    row_list = []
    for i in range(len(key)):
        row_list.append(key[i])
        if len(row_list) == n:
            key_data.append(row_list)
            row_list = []
    key_matrix = Matrix(key_data)
    plaintext_list = []
    for i in plain_text:
        if i.isupper():
            plaintext_list.append(ord(i) - ord('A'))
        else:
            plaintext_list.append(ord(i) - ord('a'))
    plaintext_matrix = Matrix([plaintext_list])
    enctext_matrix = plaintext_matrix * key_matrix
    enctext_list = list(enctext_matrix)
    enc_text = ""
    for i in enctext_list:
        enc_text += chr(i % 26 + ord('a'))
    return enc_text


def hill_decrypt(enc_text, key, n):
    enc_text = ''.join(enc_text.split())
    key_data = []
    row_list = []
    for i in range(len(key)):
        row_list.append(key[i])
        if len(row_list) == n:
            key_data.append(row_list)
            row_list = []
    key_matrix = Matrix(key_data).inv_mod(26)
    enctext_list = []
    for i in enc_text:
        if i.isupper():
            enctext_list.append(ord(i) - ord('A'))
        else:
            enctext_list.append(ord(i) - ord('a'))
    enctext_matrix = Matrix([enctext_list])
    plaintext_matrix = enctext_matrix * key_matrix
    plaintext_list = list(plaintext_matrix)
    plain_text = ""
    for i in plaintext_list:
        plain_text += chr(i % 26 + ord('a'))
    return plain_text


def hill_info():
    print("---------------------------------------------Hill密码简介---------------------------------------")
    print("希尔密码是运用基本矩阵论原理的替换密码，由Lester S. Hill在1929年发明。")
    print("每个字母当作26进制数字：A=0, B=1, C=2... 一串字母当成n维向量，跟一个n×n的矩阵相乘，再将得出的结果模26。")
    print("注意用作加密的矩阵（即密匙）在Z26必须是可逆的，否则就不可能解码。只有矩阵的行列式和26互质，才是可逆的。")
