"""
    628: 三个数的最大乘积

    给定一个整数数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

    示例 1:

        输入: [1,2,3]
        输出: 6

    示例 2:

        输入: [1,2,3,4]
        输出: 24
        注意:

    给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
    输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

"""


# 先排序，然后比较三个最大的正数和最小的两个负数及最大正数大乘积即可
class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])


if __name__ == "__main__":
    S = Solution()
    print(S.maximumProduct([1, 2, 3, 4, 5]))
