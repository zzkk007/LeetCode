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



class Solution(object):


    def findUnsortedSubarray(self, nums):

        min_index, max_index = 0, 0
        flag = True

        for i in range(len(nums)-1):
            if flag:
                if nums[i] > nums[i + 1]:
                    min_index = i
                    flag = False
            else:

                if nums[i] < nums[i + 1]:
                    max_index = i


        print(min_index, max_index)
        if flag:
            return 0
        if not flag and not max_index:
            return len(nums)

        return (max_index - min_index + 1)


if __name__ == "__main__":
    S = Solution()

    # nums = [1, 3, 2, 3, 3]
    # nums = [2, 6, 4, 8, 10, 9, 15]
    # nums = [2, 1]
    # nums = [5, 4, 3, 2, 1]
    nums = [1, 3, 2, 4, 5, 6, 7]
    print(S.findUnsortedSubarray(nums))
