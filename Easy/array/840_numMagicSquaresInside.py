"""
    840. 矩阵中的幻方

    3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，
    其中每行，每列以及两条对角线上的各数之和都相等。

    给定一个由整数组成的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。



    示例：

        输入:[[4,3,8,4],
              [9,5,1,9],
              [2,7,6,2]]
        输出: 1
        解释:
        下面的子矩阵是一个 3 x 3 的幻方：
        438
        951
        276

        而这一个不是：
        384
        519
        762

    总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
    提示:

    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    0 <= grid[i][j] <= 15


"""


class Solution(object):
    def numMagicSquaresInside(self, grid):
        r = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if set((grid[i][j],grid[i][j+2],grid[i+2][j],grid[i+2][j+2])) == set((2,4,6,8)) and grid[i+1][j+1] == 5:
                    if sum(grid[i][j:j+3]) == sum(grid[i+2][j:j+3])==grid[i][j]+grid[i+1][j]+grid[i+2][j] == 15:
                        r += 1
        return r








if __name__ == "__main__":

    S = Solution()
    grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
    print(S.numMagicSquaresInside(grid))
