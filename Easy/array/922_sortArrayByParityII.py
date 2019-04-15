"""
    922. 按奇偶排序数组 II

    给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
    对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
    你可以返回任何满足上述条件的数组作为答案。

    示例：

        输入：[4,2,5,7]
        输出：[4,5,2,7]
        解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

    提示：

        2 <= A.length <= 20000
        A.length % 2 == 0
        0 <= A[i] <= 1000

"""

"""

class Solution(object):
    def sortArrayByParityII(self, A):
        i = 0
        while i < len(A):
            if i % 2 == 0 and A[i] % 2 != 0:
                j = i + 1
                while j < len(A):
                    if A[j] % 2 == 0:
                        break
                    j += 1

                A[i], A[j] = A[j],A[i]
                i += 1

            elif i % 2 != 0 and A[i] % 2 == 0:
                j = i + 1
                while j < len(A):
                    if A[j] % 2 != 0:
                        break
                    j += 1

                A[i], A[j] = A[j], A[i]
                i += 1
            else:

                i += 1

        return A

"""


class Solution(object):
    def sortArrayByParityII(self, A):
        ou = [i for i in A if i % 2]
        ji = [i for i in A if not i % 2]
        return [i for n in zip(ji, ou) for i in n]



if __name__ == "__main__":
    S = Solution()
    nums = [4, 2, 5, 7]
    print(S.sortArrayByParityII(nums))





