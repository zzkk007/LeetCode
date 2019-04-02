"""
    给定 n 个整数，找出平均数最大且长度为 k 最大连续子数组，并输出该最大平均数。

    示例：

        输入: [1,12,-5,-6,50,3], k = 4
        输出: 12.75
        解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

    注意：

        1 <= k <= n <= 30,000。
        所给数据范围 [-10,000，10,000]。

"""
"""
class Solution:
    def findMaxAverage(self, nums, k):
        window = []
        resMax = None
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            window.append(i)
            if i >= k - 1:
                sumMax = 0
                for j in range(k):
                    sumMax += nums[window[j]]
                
                if resMax is None:
                    resMax = sumMax
                if sumMax >= resMax:
                    resMax = sumMax
        return resMax / k   

"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        sumMax = sum(nums[0:k])
        temp = sumMax

        for i in range(k,len(nums)):
            sumMax = nums[i] + sumMax - nums[i - k]
            if sumMax > temp:
                temp = sumMax
        return temp / k



if __name__ == "__main__":
    S = Solution()
    nums = [-1]
    print(S.findMaxAverage(nums, 1))

