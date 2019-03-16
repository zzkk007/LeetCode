"""


    给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
    在杨辉三角中，每个数是它左上方和右上方的数的和。

    输入: 5
    输出:
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]


"""


class Solution:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)
        return triangle

if __name__ == "__main__":

    S = Solution()
    print(S.generate(5))