"""

    给定一个数组 nums, 编写一个函数将所有 0 移动到数组末尾
    同时保持非零数组的相对顺序。

    示例：
        输入：[0, 1, 0, 3, 12]
        输出：[1, 3, 12, 0, 0]

    说明：
        必须在原数组上操作，不能拷贝额外的数组。
        尽量减少操作次数。

"""


class Solution():
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i+1, len(nums)):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    j += 1





if __name__ == "__main__":
    S = Solution()
    numns = [0, 0, 1]
    print(numns)
    S.moveZeroes(numns)
    print(numns)