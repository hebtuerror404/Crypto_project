def caesar_decrypt(enc_text, key):
    plain_text = ""
    for i in enc_text:
        if not i.isalpha():
            plain_text += i
        elif i.isupper():
            if (ord(i) - key) < ord('A'):
                plain_text += chr(ord('Z') - (key - ord(i) + ord('A') - 1) % 26)
            else:
                plain_text += chr(ord(i) - key)
        else:
            if (ord(i) - key) < ord('a'):
                plain_text += chr(ord('z') - (key - ord(i) + ord('a') - 1) % 26)
            else:
                plain_text += chr(ord(i) - key)
    return plain_text


def caesar_encrypt(plain_text, key):
    enc_text = ""
    for i in plain_text:
        if not i.isalpha():
            enc_text += i
        elif i.isupper():
            if (ord(i) + key) > ord('Z'):
                enc_text += chr(ord('A') + (key - ord('Z') + ord(i) - 1) % 26)
            else:
                enc_text += chr(ord(i) + key)
        else:
            if (ord(i) + key) > ord('z'):
                enc_text += chr(ord('a') + (key - ord('z') + ord(i) - 1) % 26)
            else:
                enc_text += chr(ord(i) + key)
    return enc_text


def caesar_info():
    print("---------------------------------------------Caesar密码简介---------------------------------------")
    print("在密码学中，凯撒密码（英语：Caesar cipher），或称凯撒加密、凯撒变换、变换加密，是一种最简单且最广为人知的加密技术。")
    print("它是一种替换加密的技术，明文中的所有字母都在字母表上向后（或向前）按照一个固定数目进行偏移后被替换成密文。")
    print("例如，当偏移量是3的时候，所有的字母A将被替换成D，B变成E，以此类推。")
    print("根据偏移量的不同，还存在若干特定的恺撒密码名称：")
    print("偏移量为10：Avocat(A→K)")
    print("偏移量为13：ROT13")
    print("偏移量为-5：Cassis (K 6)")
    print("偏移量为-6：Cassette (K 7)")


def caesar_attack(enc_text):
    plain_text_possible = []
    for key_possible in range(26):
        plain_text_possible.append(caesar_decrypt(enc_text, key_possible))
    return plain_text_possible
