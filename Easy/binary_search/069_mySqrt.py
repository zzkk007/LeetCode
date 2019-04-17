"""

    实现 int sqrt(int x) 函数。

    计算并返回 x 的平方根，其中 x 是非负整数。
    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

    示例 1:

        输入: 4
        输出: 2

    示例 2:

        输入: 8
        输出: 2
        说明: 8 的平方根是 2.82842...,
             由于返回类型是整数，小数部分将被舍去。

"""

class Solution(object):
    def mySqrt(self, x):

        minNum = 1.0
        maxNum = float(x)

        for i in range(10000):
            middle = float((minNum + maxNum) / 2)
            square = float(middle * middle)
            delta = float(abs((square/x) - 1))

            if delta <= 0.00001:
                return middle
            else:
                if square > x:
                    maxNum = middle
                else:
                    minNum = middle

if __name__ == "__main__":
    S = Solution()
    print(S.mySqrt(36))