"""
    给定一个整数数组和一个整数 k, 判断数组中是否存在两个不同的索引 i 和 j,
    使得 nums[i] = nums[j], 并且 i 和 j 的差的绝对值最大位 k。

    示例1：
        输入： nunms = [1, 2, 3, 1], k = 3
        输出：true

    示例2：

        输入： nums = [1, 0, 1, 1], k = 1
        输出：true

    示例3：

        输入： nums = [1, 2, 3, 1, 2, 3], k = 2
        输出：false


"""

"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and j - i <= k:
                    return True
        return False

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        nums_len = len(nums)
        if nums_len <= 1:
            return False
        nums_dict = dict()
        for i in range(nums_len):
            if nums[i] in nums_dict:
                if i-nums_dict[nums[i]] == k:
                    return True
            nums_dict[nums[i]] = i
        return False

"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) <= 1:
            return False

        hase_map = dict()
        for i in range(len(nums)):
            if nums[i] in hase_map:
                if i - hase_map[nums[i]] <= k:
                    return True
            hase_map[nums[i]] = i
        return False


if __name__ == "__main__":
    S = Solution()
    print(S.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
