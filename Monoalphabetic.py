# -*- coding: UTF-8 -*-
KEYWORD = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


def make_keylist(key):
    key = ''.join(key.split()).lower()
    key_list = []
    for i in key:
        if i in key_list:
            continue
        key_list.append(i)
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) in key_list:
            continue
        key_list.append(chr(i))
    return key_list


def monoalphabetic_encrypt(plain_text, key):
    key_list = make_keylist(key)
    enc_text = ""
    for i in plain_text:
        if i < 'A' or ('Z' < i < 'a') or i > 'z':
            enc_text += i
            continue
        if i.isupper():
            enc_text += key_list[KEYWORD.index(i.lower())].upper()
        else:
            enc_text += key_list[KEYWORD.index(i.lower())].lower()
    return enc_text


def monoalphabetic_decrypt(enc_text, key):
    key_list = make_keylist(key)
    plain_text = ""
    for i in enc_text:
        if i < 'A' or ('Z' < i < 'a') or i > 'z':
            plain_text += i
            continue
        if i.isupper():
            plain_text += KEYWORD[key_list.index(i.lower())].upper()
        else:
            plain_text += KEYWORD[key_list.index(i.lower())].lower()
    return plain_text


def monoalphabetic_info():
    print("---------------------------------------------单表代替密码简介---------------------------------------")
    print("简易替换加密是一种以特定方式改变字母表上字母顺序，并以此顺序书写的加密方式。这样一张改变了字母次序的字母表")
    print("即为‘替换表’。替换表可以以偏移或逆转（分别为凯撒密码和阿特巴希密码（英语：Atbash））或更复杂方式构造，此")
    print("时称之为‘混合表’。传统上会先把一个关键词写在字母表最前面，再删去重复字母，这样就能得到一个混合表。")
