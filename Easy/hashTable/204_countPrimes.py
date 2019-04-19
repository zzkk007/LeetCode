"""
    204. 计数质数

    统计所有小于非负数整数 n 的质数的数量。

    示例：
        输入：10
        输出：4
        解释：小于 10 的质数一共有 4 个，它们是 2, 3, 5, 7.

"""


class Solution(object):
    def countPrimes(self, n):

        return len([x for x in range(2, n) if self.gx(x)])

    def gx(self, m):

        for i in range(2, m//2 + 1):
            if m % i == 0:
                return False
        return True


if __name__ == "__main__":

    S = Solution()
    print(S.countPrimes(10))
