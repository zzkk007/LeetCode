"""
    给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
    在杨辉三角中，每个数是它左上方和右上方的数的和。

    示例:

    输入: 3
    输出: [1,3,3,1]

"""



class Solution(object):

    def getRow(self, rowIndex):
        line = [1]
        for n in range(rowIndex + 1):
            new_line = [1] * (n + 1)

            for i in range(len(line)):
                if i == 0:
                    continue
                else:
                    new_line[i] = line[i-1] + line[i]
            line = new_line
        return line

if __name__ == "__main__":


    S = Solution()
    print(S.getRow(3))

