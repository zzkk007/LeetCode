
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，
并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""

"""
    1 暴力破解法:

        时间复杂度：O(n^2)：

            对于每个元素，我们试图通过遍历数组的其余部分来
            寻找它所对应的目标元素，这将耗费 O(n)O(n) 的时间。
            因此时间复杂度为 O(n^2)

        空间复杂度：O(1)。

"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]

"""
    2 两遍哈希表：
        
        为了对运行时间复杂度进行优化，我们需要一种更有效的方法来检查数组中是否存在目标元素。
        如果存在，我们需要找到他的索引。
        保持数组中每个元素与其索引相互对应的最好办法是哈希表。
        
        通过以空间换取速度的方式，我们可以将查找时间从 O(n)O(n) 降低到 O(1)O(1)。
        哈希表正是为此目的而构建的，它支持以 近似 恒定的时间进行快速查找。
        我用“近似”来描述，是因为一旦出现冲突，查找用时可能会退化到 O(n)O(n)。
        但只要你仔细地挑选哈希函数，在哈希表中进行查找的用时应当被摊销为 O(1)O(1)。        
        
        一个简单的使用两次迭代，在第一个迭代中，我们将每个元素的值和它的索引添加到表中。
        然后，在第二次迭代中，在第二次迭代中，我们将检查每个元素对应的目标元素
        (target - nums[i])是否存在于表中。
        注意，改目标不能是 nums[i]本身！
        
        
        复杂度分析：

            时间复杂度：O(n)O(n)， 我们把包含有 nn 个元素的列表遍历两次。
            由于哈希表将查找时间缩短到 O(1)O(1) ，所以时间复杂度为 O(n)。

            空间复杂度：O(n)， 所需的额外空间取决于哈希表中存储的元素数量，
            该表中存储了 nn 个元素。
"""

class Solution2:

    def twoSum(self, nums, target):

        hash_map = dict()

        for key, value in enumerate(nums):
            hash_map[value] = key

        for i in range(len(nums)):
            number = target - nums[i]

            if number in hash_map and i != hash_map[number]:
                return [i, hash_map[number]]

"""
    3 一遍哈希表：
    
        事实证明，我们可以一次完成。在进行迭代并将元素插入到表中的同时，
        我们还会回过头来检查表中是否已经存在当前元素所对应的目标元素。
        如果它存在，那我们已经找到了对应解，并立即将其返回。

"""

class Solution3():
    def twoSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """

        hash_map = dict()
        for index, x in  enumerate(nums):
            if target - x in hash_map:
                return [index, hash_map[target - x]]
            else:
                hash_map[x] = index

if __name__ == "__main__":

    twoS = Solution3()
    list1 = [2, 7, 9, 11, 33]
    print(twoS.twoSum(list1, 9))












