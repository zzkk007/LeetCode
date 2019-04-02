"""
    变体一：二分法查找第一个值等于给定值的元素

        有序集合中存在重复的数据，我们希望找到第一个值等于给定值的数据，
        比如这样一个有序数组 [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]，
        其中 a[5], a[6], a[7] 的值都等于 8，是重复的数据。我们希望
        查找到第一个等于 8 的数据，也就是下标是 5 的元素。


    对于下面的代码：

        nums[mid] 要跟查找的 val 的大小关系有三种情况，大于，小于，等于。
        当 nums[mid] = val 时：如果我们查找的是任意一个值等于给定值的元素，
        当 nums[mid] 等于要查找的值时， nums[mid] 就是我们要查找的元素。但是
        如果我们求解的是第一个值等于给定的元素，当 nums[mid] = val 时，我们
        就需求判断一下，这个 nums[mid] 是不是第一个值等于给定的元素。
        如果 mid = 0, 那么这个元素已经是数组的第一个元素，那肯定是我们要找到
        如果 mid 不等于 0，但 nums[mid-1]不等于 val, 那么也说明 nums[mid] 就是
        我们要找的第一个值等于给定值的元素。

        如果检查发现 nums[mid - 1] = val, 说明mid 不是我们要的元素，
        更新 high = mid - 1, 因为要找的元素肯定出现在[low, mid - 1]之间。






"""

def binary_search(nums, val):

    low = 0
    high = len(nums) - 1

    while low <= high:

        mid = low + ((high - low) >> 1)

        if nums[mid] > val:
            high = mid - 1
        elif nums[mid] < val:
            low = mid + 1
        else:
            if (mid == 0) or (nums[mid - 1] != val):
                return mid
            else:
                high = mid - 1

    return -1

if __name__ == "__main__":

    print(binary_search([1, 3, 4, 5, 6, 8, 8, 8, 11, 18], 8))