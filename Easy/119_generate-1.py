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
        for s in range(rowIndex + 1):
            next_line = [1] * (s + 1)
            print('--------')
            print(next_line)
            for i in range(len(line)):
                if i == 0:
                    continue
                next_line[i] = line[i] + line[i-1]
            line = next_line
            print(line)
            print('---------')

        return line



if __name__ == "__main__":


    S = Solution()
    print(S.getRow(3))

