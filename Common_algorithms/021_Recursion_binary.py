"""
    递归实现进制转换

"""

def binary2(num):

    if num == 0:
        return '0'
    else:
        return binary2(num >> 1) + str(num & 1)
        # return binary(num//2) + str(num%2)


def binary64(num, base):
    Keycode = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_$"

    if num == 0:
        return '0'

    else:
        m = num%base
        return binary64(num//base, base) + Keycode[m]

if __name__ == "__main__":

    num = int(input("请输入一个十进制的数字:"))
    base = int(input("请输入一个base的数字:"))
    print(binary64(num,base))

