# -*- coding: UTF-8 -*-
def vigenere_encrypt(plain_text, key):
    key = key.lower()
    enc_text = ""
    key_index = 0
    for i in plain_text:
        if i == ' ':
            enc_text += ' '
            continue
        if i.isupper():
            enc_text += chr(((ord(i) + ord(key[key_index]) - ord('a') - ord('A')) % 26) + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            enc_text += chr(((ord(i) + ord(key[key_index]) - 2 * ord('a')) % 26) + ord('a'))
            key_index = (key_index + 1) % len(key)
    return enc_text


def vigenere_decrypt(enc_text, key):
    key = key.lower()
    plain_text = ""
    key_index = 0
    for i in enc_text:
        if i == ' ':
            plain_text += ' '
            continue
        if i.isupper():
            plain_text += chr(((ord(i) - ord(key[key_index]) + ord('a') - ord('A')) % 26) + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            plain_text += chr(((ord(i) - ord(key[key_index])) % 26) + ord('a'))
            key_index = (key_index + 1) % len(key)

    return plain_text


def vigenere_info():
    print("---------------------------------------------Vigenere密码简介---------------------------------------")
    print("维吉尼亚密码（又译维热纳尔密码）是使用一系列凯撒密码组成密码字母表的加密算法，属于多表密码的一种简单形式。")
    print("在一个凯撒密码中，字母表中的每一字母都会作一定的偏移，例如偏移量为3时，A就转换为了D、B转换为了E……")
    print("而维吉尼亚密码则是由一些偏移量不同的恺撒密码组成。")
    print("为了生成密码，需要使用表格法。这一表格包括了26行字母表，每一行都由前一行向左偏移一位得到。")
    print("具体使用哪一行字母表进行编译是基于密钥进行的，在过程中会不断地变换。")
    print("解密的过程则与加密相反。例如：根据密钥第一个字母L所对应的L行字母表，发现密文第一个字母L位于A列，因而明文")
    print("第一个字母为A。密钥第二个字母E对应E行字母表，而密文第二个字母X位于此行T列，因而明文第二个字母")
    print("为T。以此类推便可得到明文。")
