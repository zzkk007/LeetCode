"""
    532: 数组中的 K-diff 数对

    给定一个整数数组和一个整数k, 你需要在数据中找到不同的 k-diff 数对。
    这里将 k-diff 数对定义为一个整数对(i,j)，其中 i和j 都是数组中的数字，
    切两数之差的绝对值是 k。

    示例 1:

        输入: [3, 1, 4, 1, 5], k = 2
        输出：2
        解释：数组中有两个 2-diff 数对，(1, 3) 和 (3, 5)
        尽量数组中有两个 1，但我们只应返还不同的数对的数量。

    示例 2:

        输入: [1, 2, 3, 4, 5], k = 1
        输出：4
        解释: 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。

    示例 3：

        输入：[1, 3, 1, 5, 4], k = 0
        输出: 1
        解释: 数组中只有一个 0-diff 数对，(1, 1)。

    注意:
        数对 (i, j) 和数对 (j, i) 被算作同一数对。
        数组的长度不超过10,000。
        所有输入的整数的范围在 [-1e7, 1e7]。

"""

"""
# 超出时间限制

class Solution(object):

    def findPairs(self, nums, k):
        alist = list()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    if (nums[i], nums[j]) not in alist and (nums[j], nums[i]) not in alist:
                        alist.append((nums[i], nums[j]))

        print(alist)
        return len(alist)

class Solution(object):

    def findPairs(self, nums, k):
        hase_map = dict()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    if (nums[i], nums[j]) not in hase_map and (nums[j], nums[i]) not in hase_map:
                        hase_map[(nums[i],nums[j])] = None

        print(hase_map)
        return len(hase_map)

"""


class Solution(object):
    def findPairs(self, nums, k):
        nums.sort()
        sumMax = 0

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                low = i + 1
                high = len(nums) - 1
                while low <= high:
                    mid = (low + high)//2
                    if nums[mid] == (nums[i] + k):
                        sumMax += 1
                        break
                    elif nums[mid] > nums[i] + k:
                        high = mid - 1
                    else:
                        low = mid + 1

        return sumMax


if __name__ == "__main__":
    S = Solution()
    alist = [1, 3, 1, 5, 4]
    print(S.findPairs(alist, 0))