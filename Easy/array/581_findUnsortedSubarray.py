"""
    581、 最短无序连续子数组

    给定一个整数数组，你需要寻找一个连续的子数组，
    如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

    你找到这个子数组应是最短的，请输出它的长度。

    示例：
        输入: [2, 6, 4, 8, 10, 9, 15]
        输出：5
        解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

    说明：
        输入的数组长度范围在 [1, 10,000]。
        输入的数组可能包含重复元素 ，所以升序的意思是<=。

"""


'''
    思路是：从左往右找到正确顺序的一边，end右边
           从右往左找到正确顺序的一边，start 左边
    
'''

class Solution(object):
    def findUnsortedSubarray(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        start, end = 0, -1
        max, min = nums[0], nums[-1]

        for i in range(1, len(nums)):
            if max > nums[i]:
                end = i
            else:
                max = nums[i]


            if min < nums[len(nums) - 1 - i]:
                start = len(nums) - 1 - i
            else:
                min = nums[len(nums)-1 - i]


        return end - start + 1




if __name__ == "__main__":
    S = Solution()

    nums = [1, 3, 2, 3, 3]
    # nums = [2, 6, 4, 8, 10, 9, 15]
    # nums = [2, 1]
    # nums = [5, 4, 3, 2, 1]
    # nums = [1, 3, 2, 4, 5, 6, 7]
    # nums = [1, 3, 2, 2, 2]
    print(S.findUnsortedSubarray(nums))
