"""
    给定一个整数数组，判断是否存在重复元素。
    如果任何值在数组中出现至少两次，函数返回 true。
    如果数组中每个元素都不相同，则返回 false。

    示例1：

        输入： [1, 2, 3, 1]
        输出：true

    示例2：

        输入: [1, 2, 3, 4]
        输出: false

    示例 3:

        输入: [1,1,1,3,3,4,3,2,4,2]
        输出: true

"""


from collections import  Counter
class Solution(object):


    def containsDuplicate(self, nums):
        '''
            for k, v in enumerate(nums):
                if v in nums[k+1:]:
                    return True
                else:
                    return False


            set1 = set(nums)
                if len(set1) == len(nums):
                    return False
                else:
                    return True

        '''

        if nums == []:
            return False
        c = Counter(nums)
        if c.most_common(1)[0][1] > 1:
            return True
        else:
            return False






if __name__ == "__main__":
    S = Solution()
    print(S.containsDuplicate([]))

