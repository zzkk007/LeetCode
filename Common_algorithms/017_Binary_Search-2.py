"""
        变体而：二分法查找最后一个值等于给定值的元素

        有序集合中存在重复的数据，我们希望找到最后值等于给定值的数据，
        比如这样一个有序数组 [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]，
        其中 a[5], a[6], a[7] 的值都等于 8，是重复的数据。我们希望
        查找到最后等于 7 的数据，也就是下标是 8 的元素。


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
            if (mid == len(nums) - 1) or (nums[mid + 1] != val):
                return mid
            else:
                low = mid + 1

    return -1

if __name__ == "__main__":

    print(binary_search([1, 3, 4, 5, 6, 8, 8, 8, 11, 18], 8))