"""
    二分法查找变体三：查找第一个大于等于给定值的元素：

        在有序数组中，查找第一个大于等于给定值的元素，比如，数组中存储的这样一个序列
        [3, 4, 6, 7, 10] 如果查找第一个大于等于 5 的元素，那就是 6。

        实际上，实现的思路更前面的两种变形问题的实现思路类似：

        如果 a[mid - 1] 也是大于等于要查找的值 val, 说明要查找的元素在[low, mid-1]之间，
        所以，我们将 high = mid - 1。
"""

def binary_search(nums, val):

    low = 0
    high = len(nums) - 1

    while low <= high:

        mid = low + ((high - low) >> 1)

        if nums[mid] >= val:
            if mid == 0 or nums[mid - 1] < val:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1

    return -1

if __name__ == "__main__":

    print(binary_search([3, 4, 6, 7, 10], 5))