"""
    变体四：查找最后一个小于等于给定值的元素：

    数组中存储 [3, 5, 6, 8, 9, 10], 最后一个小于等于 7 的元素就是 6，


"""

def binary_search(nums, val):

    low = 0
    high = len(nums) - 1

    while low <= high:

        mid = low + ((high - low) >> 1)

        if nums[mid] > val:
            high = mid - 1
        else:
            if mid == len(nums) - 1 or nums[mid + 1] > val:
                return mid
            else:
                low = mid + 1
    return -1

if __name__ == "__main__":

    print(binary_search([3, 4, 5, 6, 8, 9, 10], 7))