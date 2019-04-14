"""
    905. 按奇偶排序数组

    给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。
    你可以返回满足此条件的任何数组作为答案。



    示例：

    输入：[3,1,2,4]

    输出：[2,4,3,1]
    输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。


    提示：

    1 <= A.length <= 5000
    0 <= A[i] <= 5000


"""


"""
class Solution(object):
    def sortArrayByParity(self, A):
        i = 0
        for j in range(len(A)):
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A

"""


class Solution(object):
    def sortArrayByParity(self, A):
        result = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                result.insert(0,A[i])
            else:
                result.append(A[i])

        return result




if __name__ == "__main__":

    S = Solution()
    A = [3, 1, 2, 4]
    print(S.sortArrayByParity(A))











