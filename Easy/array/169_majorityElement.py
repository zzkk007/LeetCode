"""
169 求众数

    给定一个大小为 n 的数组，找到其中的众数，众数是指在数组中出现次数大于[n/2]的元素。
    你可以假设数组是非空的，并且给定的数组总是存在众数。

    示例：
        输入[3, 2, 3]
        输出 3

        输入[2,2,1,1,1,2,2]
        输出：2

"""
"""
class Solution(object):
    def majorityElement(self, nums):

        hase_map = dict()
        for num in nums:
            if num not in hase_map:
                hase_map[num] = 1
            else:
                hase_map[num] += 1

        for key, value in hase_map.items():
            if value > len(nums)/2:
                return key
"""

from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(Counter(nums), key=Counter(nums).get)


if __name__ == "__main__":
    S = Solution()
    nums = [3, 2, 3]
    print(S.majorityElement(nums))

