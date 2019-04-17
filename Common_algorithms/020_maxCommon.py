"""
    获取两个数的最大公约数、最小公倍数

"""

a = 36
b = 21

def maxCommon(a, b):
    while b:
        a, b = b, a%b
    return a

# 递归求最大公约数
def gcd(a, b):
    if b > a:
        b, a = a, b

    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# 递归求最小公倍数

def lcm(a, b, c):
    if b > a:
        a, b = b, a

    if a*c % b == 0:
        return a * c
    else:
        return lcm(a, b, c+1)





# 最小公倍数 = 两者乘积//最大公约数
def minCommon(a, b):
    c = a * b
    while b:
        a,b = b, a%b

    return c//a

if __name__ == "__main__":
    print(maxCommon(a, b))
    print(minCommon(a, b))
    print(gcd(a, b))
    print(lcm(a, b, 1))