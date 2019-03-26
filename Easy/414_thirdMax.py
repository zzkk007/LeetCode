"""
    给定一个非空数组，返回次数组中的第三大数，如果不存在，则返回数据中最大的数，
    要求算法时间复杂度必须是 O(n)

    示例1：
        输入：[3, 2, 1]
        输出：1
        解释：第三个大的数是 1

    示例2：

        输入：[1, 2]
        输出：2
        解释: 第三大的数不存在, 所以返回最大的数 2 .

    示例 3:

        输入: [2, 2, 3, 1]
        输出: 1
        解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
        存在两个值为2的数，它们都排第二。

"""

import heapq
class Solution:
    def thirdMax(self, nums):
        if len(set(nums)) < 3:
            return max(nums)
        return heapq.nlargest(3, set(nums)).pop()

if __name__ == "__main__":
    S = Solution()
    nums = [1,2]
    print(S.thirdMax(nums))

