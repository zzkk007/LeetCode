"""
    697: 数组的度

    给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指
    数组里任一一个元素出现频数的最大值。

    你的任务是找到与 nums 用于相同大小的度的最短连续子数组，返回其长度。

    示例1：
        输入：[1, 2, 2, 3, 1]
        输出：2
        解释：
            输入数组的度是2，因为元素1和2的出现频数最大，均为2.
            连续子数组里面拥有相同度的有如下所示:
            [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
            最短连续子数组[2, 2]的长度为2，所以返回2.

    示例 2：

        输入: [1,2,2,3,1,4,2]
        输出: 6

    注意:

        nums.length 在1到50,000区间范围内。
        nums[i] 是一个在0到49,999范围内的整数。

"""

#用dict记录nums中每个元素出现的位置，
#度为出现位置最多的len，返回拥有相同度的元素中，min（首末位置最+1）


class Solution:
    def findShortestSubArray(self, nums):

        dict_map = dict()

        for i in range(len(nums)):
            if nums[i] not in dict_map:
                dict_map[nums[i]] = [i]
            else:
                dict_map[nums[i]].append(i)

        m = 0
        for i in dict_map:
            m = max(m, len(dict_map[i]))

        r = len(nums)
        for i in dict_map:
            if len(dict_map[i]) == m:
                r = min(r, dict_map[i][-1] - dict_map[i][0] + 1)
        return r

if __name__ == "__main__":
    S = Solution()
    print(S.findShortestSubArray([1, 2, 2, 3, 1]))

