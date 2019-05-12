# -*- coding: UTF-8 -*-
import Hill
import Playfair
import Vigenere
import Monoalphabetic
import Caesar

EXE_MODE = 'DEBUG'


def playfair_menu():
    while True:
        print("-----Playfair密码-----")
        print("请选择你要进行的操作：")
        print("1.Playfair密码简介")
        print("2.Playfair密码加密")
        print("3.Playfair密码解密")
        print("4.返回上一级")
        crypto_operating = input("->")
        if crypto_operating == '1':
            Playfair.playfair_info()
        elif crypto_operating == '2':
            print("-----------------Playfair密码加密---------------")
            print("[Input]请输入您的明文：（加密结束后会丢失大小写与空格）")
            plain_text = input()
            print("[Input]请输入您的密钥：")
            key = input()
            print("[Info]加密正在进行。。。")
            try:
                enc_text = Playfair.playfair_encrypt(plain_text, key)
                print("[Success]加密成功！")
                print("[Info]密文为：" + enc_text)
            except BaseException as e:
                print("[ERROR]加密失败！")
                if EXE_MODE == 'DEBUG':
                    print(e)
                pass
        elif crypto_operating == '3':
            print("-----------------Playfair密码解密---------------")
            print("[Input]请输入您的密文：")
            enc_text = input()
            print("[Input]请输入您的密钥：")
            key = input()
            print("[Info]解密正在进行。。。")
            try:
                info = Playfair.playfair_decrypt(enc_text, key)
                if info == 40001:
                    print("[ERROR]解密失败！")
                    print("[ERR_info]请检查密文长度！密文必须为偶长度！")
                else:
                    print("[Success]解密成功！（大小写与空格需要自行根据语义恢复）")
                    print("[Info]明文为：" + info)
            except BaseException as e:
                print("[ERROR]解密失败！")
                if EXE_MODE == 'DEBUG':
                    print(e)
                pass
        elif crypto_operating == '4':
            return
        else:
            print("[ERROR]选择出错！")


def vigenere_menu():
    while True:
        print("-----Vigenere密码-----")
        print("请选择你要进行的操作：")
        print("1.Vigenere密码简介")
        print("2.Vigenere密码加密")
        print("3.Vigenere密码解密")
        print("4.返回上一级")
        crypto_operating = input("->")
        if crypto_operating == '1':
            Vigenere.vigenere_info()
        elif crypto_operating == '2':
            print("-----------------Vigenere密码加密---------------")
            print("[Input]请输入您的明文：")
            plain_text = input()
            print("[Input]请输入您的密钥：(密钥应为合法英文单词)")
            key = input()
            print("[Info]加密正在进行。。。")
            try:
                enc_text = Vigenere.vigenere_encrypt(plain_text, key)
                print("[Success]加密成功！")
                print("[Info]密文为：" + enc_text)
            except BaseException as e:
                print("[ERROR]加密失败！")
                if EXE_MODE == 'DEBUG':
                    print(e)
                pass
        elif crypto_operating == '3':
            print("-----------------Vigenere密码解密---------------")
            print("[Input]请输入您的密文：")
            enc_text = input()
            print("[Input]请输入您的密钥：(密钥应为合法英文单词)")
            key = input()
            print("[Info]解密正在进行。。。")
            try:
                plain_text = Vigenere.vigenere_decrypt(enc_text, key)
                print("[Success]解密成功！")
                print("[Info]明文为：" + plain_text)
            except BaseException as e:
                print("[ERROR]解密失败！")
                if EXE_MODE == 'DEBUG':
                    print(e)
                pass
        elif crypto_operating == '4':
            return
        else:
            print("[ERROR]选择出错！")


def hill_menu():
    while True:
        print("-----Hill密码-----")
        print("请选择你要进行的操作：")
        print("1.Hill密码简介")
        print("2.Hill密码加密")
        print("3.Hill密码解密")
        print("4.返回上一级")
        crypto_operating = input("->")
        if crypto_operating == '1':
            Hill.hill_info()
        elif crypto_operating == '2':
            print("----------------------Hill密码加密----------------------")
            print("[Input]请输入您的明文：（加密结束后会丢失大小写与空格）")
            plain_text = input()
            print("[Input]请输入您的密钥：(密钥应为一系列数字，空格分隔，依次输入)")
            key = input()
            print("[Input]请输入您的密钥阶数：")
            n = input()
            print("[Info]加密正在进行。。。")
            try:
                enc_text = Hill.hill_encrypt(plain_text, key.split(), int(n))
                print("[Success]加密成功！")
                print("[Info]密文为：" + enc_text)
            except BaseException as e:
                print("[ERROR]加密失败！")
                if EXE_MODE == 'DEBUG':
                    print(e)
                pass
        elif crypto_operating == '3':
            print("----------------------Hill密码解密----------------------")
            print("[Input]请输入您的密文：")
            enc_text = input()
            print("[Input]请输入您的密钥：(密钥应为一系列数字，空格分隔，依次输入)")
            print("(*密钥应为加密时使用的密钥)")
            key = input()
            print("[Input]请输入您的密钥阶数：")
            n = input()
            print("[Info]解密正在进行。。。")
            try:
                plain_text = Hill.hill_decrypt(enc_text, key.split(), int(n))
                print("[Success]解密成功！（大小写与空格需要自行根据语义恢复）")
                print("[Info]明文为：" + plain_text)
            except BaseException as e:
                print("[ERROR]解密失败！")
                if EXE_MODE == 'DEBUG':
                    print(e)
                pass
        elif crypto_operating == '4':
            return
        else:
            print("[ERROR]选择出错！")


def monoalphabetic_menu():
    while True:
        print("-----单表代替密码-----")
        print("请选择你要进行的操作：")
        print("1.单表代替密码简介")
        print("2.单表代替密码加密")
        print("3.单表代替密码解密")
        print("4.返回上一级")
        crypto_operating = input("->")
        if crypto_operating == '1':
            Monoalphabetic.monoalphabetic_info()
        elif crypto_operating == '2':
            print("----------------------单表代替加密----------------------")
            print("[Input]请输入您的明文：")
            plain_text = input()
            print("[Input]请输入您的密钥：(密钥应为合法英文单词)")
            key = input()
            print("[Info]加密正在进行。。。")
            try:
                enc_text = Monoalphabetic.monoalphabetic_encrypt(plain_text, key)
                print("[Success]加密成功！")
                print("[Info]密文为：" + enc_text)
            except BaseException as e:
                print("[ERROR]加密失败！")
                if EXE_MODE == 'DEBUG':
                    print(e)
                pass
        elif crypto_operating == '3':
            print("----------------------单表代替解密----------------------")
            print("[Input]请输入您的密文：")
            enc_text = input()
            print("[Input]请输入您的密钥：(密钥应为合法英文单词)")
            key = input()
            print("[Info]解密正在进行。。。")
            try:
                plain_text = Monoalphabetic.monoalphabetic_decrypt(enc_text, key)
                print("[Success]解密成功！")
                print("[Info]明文为：" + plain_text)
            except BaseException as e:
                print("[ERROR]解密失败！")
                if EXE_MODE == 'DEBUG':
                    print(e)
                pass
        elif crypto_operating == '4':
            return
        else:
            print("[ERROR]选择出错！")


def caesar_menu():
    while True:
        print("-------Caesar密码-------")
        print("请选择你要进行的操作：")
        print("1.Caesar密码简介")
        print("2.Caesar密码加密")
        print("3.Caesar密码解密")
        print("4.Caesar密码列举破解")
        print("5.返回上一级")
        crypto_operating = input("->")
        if crypto_operating == '1':
            Caesar.caesar_info()
        elif crypto_operating == '2':
            print("----------------------Caesar加密----------------------")
            print("[Input]请输入您的明文：")
            plain_text = input()
            print("[Input]请输入您的密钥：(密钥应为数字)")
            key = input()
            if type(key) != int:
                print("[ERROR]非法输入！")
                continue
            print("[Info]加密正在进行。。。")
            try:
                enc_text = Caesar.caesar_encrypt(plain_text, key)
                print("[Success]加密成功！")
                print("[Info]密文为：" + enc_text)
            except BaseException as e:
                print("[ERROR]加密失败！")
                if EXE_MODE == 'DEBUG':
                    print(e)
                pass
        elif crypto_operating == '3':
            print("----------------------Caesar解密----------------------")
            print("[Input]请输入您的密文：")
            enc_text = input()
            print("[Input]请输入您的密钥：(密钥应为数字)")
            key = input()
            if type(key) != int:
                print("[ERROR]非法输入！")
                continue
            print("[Info]解密正在进行。。。")
            try:
                plain_text = Caesar.caesar_decrypt(enc_text, key)
                print("[Success]解密成功！")
                print("[Info]明文为：" + plain_text)
            except BaseException as e:
                print("[ERROR]解密失败！")
                if EXE_MODE == 'DEBUG':
                    print(e)
                pass
        elif crypto_operating == '4':
            print("----------------------Caesar列举破解----------------------")
            print("[Input]请输入您的密文：")
            enc_text = input()
            print("[Info]列举破解正在进行。。。")
            try:
                plain_text_possible = Caesar.caesar_attack(enc_text)
                print("[Success]列举破解完成！")
                for j in plain_text_possible:
                    print("[Info]可能的明文为：" + j)
            except BaseException as e:
                print("[ERROR]列举破解失败！")
                if EXE_MODE == 'DEBUG':
                    print(e)
                pass
        elif crypto_operating == '5':
            return
        else:
            print("[ERROR]选择出错！")


def main_menu():
    while True:
        print("--------主菜单--------")
        print("请选择你要使用的密码：")
        print("1.Playfair密码")
        print("2.Vigenere密码")
        print("3.Hill密码")
        print("4.单表代替密码")
        print("5.Caesar密码")
        print("6.退出")
        crypto_type = input("[input]->")
        if crypto_type == '1':
            playfair_menu()
        elif crypto_type == '2':
            vigenere_menu()
        elif crypto_type == '3':
            hill_menu()
        elif crypto_type == '4':
            monoalphabetic_menu()
        elif crypto_type == '5':
            caesar_menu()
        elif crypto_type == '6':
            return
        else:
            print("[ERROR]选择出错！")


if __name__ == "__main__":
    main_menu()
