
"""

    给定一个排序数组和一个目标值，在数组中找到这个值，并返回其索引。
    如果目标值不存在于数组中，返回它将要被按顺序插入的位置。

    你可以假设数组中无重复元素。

    示例 1：
        输入: [1, 3, 5, 6], 5
        输出: 2

    示例 2:
        输入: [1, 3, 5, 6], 2
        输出: 1

    示例 3:
        输入: [1, 3, 5, 6], 7
        输出: 4

    示例 4:

        输入: [1,3,5,6], 0
        输出: 0

"""
class Solution:
    def searchInsert(self, nums, target):

        if nums[0] > target:
            nums.insert(0,target)
            return 0
        if nums[-1] < target:
            nums.append(target)
            return len(nums) - 1

        for key, value in enumerate(nums):

            if value == target:
                return key

            if  target > nums[key - 1] and target < value:
                nums.insert(key, target)
                return key



if __name__ == "__main__":

    S = Solution()
    alist = [1, 3, 5, 6]
    print(alist)
    print(S.searchInsert(alist, 7))
    print(alist)






























