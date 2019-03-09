# -*- coding: UTF-8 -*-+
def make_keymatrix(key):
    key_matrix = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in key[::-1]:
        if i in key_matrix:
            key_matrix.remove(i)
            key_matrix.insert(0, i)
    key_matrix.remove('J')
    return key_matrix


def text_slove(text):
    text = ''.join(text.split()).upper()
    text_list = list(text)
    for i in range(0, len(text), 2):
        if i + 1 == len(text) + 1:
            text_list.append('X')
        if text_list[i] == text_list[i + 1]:
            text_list.insert(i + 1, 'X')
    text = ''.join(text_list)
    text.replace('J', 'I')
    return text


def playfair_encrypt(plain_text, key):
    key = ''.join(key.split())
    key_matrix = make_keymatrix(key.upper())
    enc_text_list = []
    plain_text = text_slove(plain_text)
    for i in range(0, len(plain_text), 2):
        x_1 = key_matrix.index(plain_text[i]) / 5
        y_1 = key_matrix.index(plain_text[i]) % 5
        x_2 = key_matrix.index(plain_text[i + 1]) / 5
        y_2 = key_matrix.index(plain_text[i + 1]) % 5
        if x_1 != x_2 and y_1 != y_2:
            enc_text_list.append(key_matrix[x_1 * 5 + y_2])
            enc_text_list.append(key_matrix[x_2 * 5 + y_1])
        elif x_1 == x_2:
            if y_1 == 4:
                y_1 = -1
            if y_2 == 4:
                y_2 = -1
            enc_text_list.append(key_matrix[x_1 * 5 + y_1 + 1])
            enc_text_list.append(key_matrix[x_2 * 5 + y_2 + 1])
        elif y_1 == y_2:
            if x_1 == 4:
                x_1 = -1
            if x_2 == 4:
                x_2 = -1
            enc_text_list.append(key_matrix[(x_1 + 1) * 5 + y_1])
            enc_text_list.append(key_matrix[(x_2 + 1) * 5 + y_2])
    enc_text = ''.join(enc_text_list)
    return enc_text


def playfair_decrypt(enc_text, key):
    key = ''.join(key.split())
    key_matrix = make_keymatrix(key.upper())
    plain_text_list = []
    enc_text = ''.join(enc_text.split()).upper()
    if len(enc_text) % 2 != 0:
        return 40001
    for i in range(0, len(enc_text), 2):
        x_1 = key_matrix.index(enc_text[i]) / 5
        y_1 = key_matrix.index(enc_text[i]) % 5
        x_2 = key_matrix.index(enc_text[i + 1]) / 5
        y_2 = key_matrix.index(enc_text[i + 1]) % 5
        if x_1 != x_2 and y_1 != y_2:
            plain_text_list.append(key_matrix[x_1 * 5 + y_2])
            plain_text_list.append(key_matrix[x_2 * 5 + y_1])
        elif x_1 == x_2:
            if y_1 == 0:
                y_1 = 5
            if y_2 == 0:
                y_2 = 5
            plain_text_list.append(key_matrix[x_1 * 5 + y_1 - 1])
            plain_text_list.append(key_matrix[x_2 * 5 + y_2 - 1])
        elif y_1 == y_2:
            if x_1 == 0:
                x_1 = 5
            if x_2 == 0:
                x_2 = 5
            plain_text_list.append(key_matrix[(x_1 - 1) * 5 + y_1])
            plain_text_list.append(key_matrix[(x_2 - 1) * 5 + y_2])
    for i in range(len(plain_text_list) - 1):
        if plain_text_list[i] == 'X' and plain_text_list[i - 1] == plain_text_list[i + 1]:
            plain_text_list.pop(i)
    plain_text = ''.join(plain_text_list)
    return plain_text


def playfair_info():
    print("---------------------------------------------Playfair密码简介---------------------------------------")
    print("波雷费密码（英语：Playfair cipher）是一种对称式密码，是首种双字母取代的加密法。")
    print("用法：")
    print("1.选取一个英文字作密钥。除去重复出现的字母。将密钥的字母逐个逐个加入5×5的矩阵内，剩下的空间将未加入")
    print("的英文字母依a-z的顺序加入。（将Q去除，或将I和J视作同一字。）")
    print("2.将要加密的讯息分成两个一组。若组内的字母相同，将X（或Q）插入两字母之间，重新分组（例如 HELLO 将分")
    print("成 HE LX LO）。若剩下一个字，也加入X字。")
    print("3.在每组中，找出两个字母在矩阵中的地方。")
    print("若两个字母不在同一直行或同一横列，在矩阵中找出另外两个字母，使这四个字母成为一个长方形的四个角。")
    print("若两个字母在同一横列，取这两个字母右方的字母（若字母在最右方则取最左方的字母）。")
    print("若两个字母在同一直行，取这两个字母下方的字母（若字母在最下方则取最上方的字母）。")
