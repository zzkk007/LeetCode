"""
    674: 最长连续递增序列：

    给定一个未经排序的整数数组，找到最长且连续的递增序列。

    示例 1：

        输入：[1, 3, 5, 4, 7]
        输出：3

        解释：最长连续递增序列是 [1, 3, 5], 长度为 3。
        尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。

    示例 2:

        输入：[2, 2, 2, 2, 2]
        输出：1
        解释：最长连续递增序列是[2], 长度为 1

    注意数组长度不会超过 10000。

"""

class Sloution(object):
    def findLengthOfLCIS(self, nums):
        length = 0
        for i in range(len(nums)-1):
            pass






if __name__ == "__main__":
    nums = [1, 3, 5, 4, 7]
    S = Sloution()
    print(S.findLengthOfLCIS(nums))