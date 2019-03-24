"""
    给定一个包含 0, 1, 2, ..., n 中 n 个数的数列，找出0, ... n 中
    没有出现在序列中的那个数。

    示例 1：
        输入： [3, 0, 1]
        输出：2

    示例 2：
        输入： [9, 6, 4, 2, 3, 5, 7, 0, 1]
        输出：8

    说明：

        你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

class Solution:
    def missingNumber(self, nums):
        sum = len(nums)
        for i in range(len(nums)):
            sum ^= nums[i]
            sum ^= i

        return sum

"""


class Solution:
    def missingNumber(self, nums):
        sum = 0
        for num in nums:
            sum += num

        realSum = (len(nums) * (len(nums)+1))/2
        print(sum, realSum)
        return realSum - sum




if __name__ == "__main__":
    S = Solution()
    print(S.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

