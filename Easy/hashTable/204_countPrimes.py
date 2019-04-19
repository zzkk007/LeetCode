"""
    204. 计数质数

    统计所有小于非负数整数 n 的质数的数量。

    示例：
        输入：10
        输出：4
        解释：小于 10 的质数一共有 4 个，它们是 2, 3, 5, 7.

"""

"""
// 超时
class Solution(object):
    def countPrimes(self, n):

        return len([x for x in range(2, n) if self.gx(x)])

    def gx(self, m):

        for i in range(2, m//2 + 1):
            if m % i == 0:
                return False
        return True




class Solution(object):
    def countPrimes(self, n):
        isPrime = {}

        for i in range(2, n):
            isPrime[i] = True

        i = 2
        while i*i < n:
            if not isPrime[i]:
                continue

            j = i*i
            while j < n:
                isPrime[j] = False
                j += i

            i += 1

        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1

        return count

"""


class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        else:
            # 首先生成了一个全部为1的列表
            output = [1] * n
            # 因为0和1不是质数,所以列表的前两个位置赋值为0
            output[0], output[1] = 0, 0
            # 此时从index = 2开始遍历,output[2]==1,即表明第一个质数为2,然后将2的倍数对应的索引
            # 全部赋值为0. 此时output[3] == 1,即表明下一个质数为3,同样划去3的倍数.以此类推.
            for i in range(2, int(n ** 0.5) + 1):
                if output[i] == 1:
                    output[i * i:n:i] = [0] * len(output[i * i:n:i])
                    # 最后output中的数字1表明该位置上的索引数为质数,然后求和即可.
        return sum(output)

# 即i是从(2,int(n**0.5)+1)而非(2,n).这个技巧是可以验证的,比如说求9以内的质数个数,
# 那么只要划掉sqrt(9)以内的质数倍数,剩下的即全为质数.
# 所以在划去倍数的时候也是从i*i开始划掉,而不是i+i.






if __name__ == "__main__":

    S = Solution()
    print(S.countPrimes(10))
