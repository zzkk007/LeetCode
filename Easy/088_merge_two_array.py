"""
    88: 合并两个有序数组

    给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
    说明:

        初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
        你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

    输入:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

    输出: [1,2,2,3,5,6]

"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = 0, 0
        result = []

        while l < m and r < n:

            if nums1[l] < nums2[r]:
                result.append(nums1[l])
                l += 1
            else:
                result.append(nums2[r])
                r += 1

        result += nums1[l:]
        result += nums2[r:]
        return result


if __name__ == "__main__":

    num1 = [1,2,3,4]
    num2 = [2,3,5,6,7]

    S = Solution()
    aaa=S.merge(num1,4,num2,5)
    print(aaa)

















