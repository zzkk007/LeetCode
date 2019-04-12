"""
    136. 只出现一次的数字

    给定一个非空整数数组，除了某个元素只出现一次外，其余每一个元素均出现两次，
    找出只出现一次的元素。

    说明：
        你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

    示例 1:

        输入: [2,2,1]
        输出: 1

    示例 2:

        输入: [4,1,2,1,2]
        输出: 4

"""

"""
class Solution(object):
    def singleNumber(self, nums):
        hash_table = dict()
        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            else:
                hash_table[nums[i]] += 1

        for k, v in hash_table.items():
            if v == 1:
                return k

"""
class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for num in nums:
            a = a ^ num
        return a



if __name__ == "__main__":
    S = Solution()
    nums = [2, 2, 1]
    print(S.singleNumber(nums))