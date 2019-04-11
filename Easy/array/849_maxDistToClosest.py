"""
    849. 到最近的人的最大距离

    在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
    至少有一个空座位，且至少有一人坐在座位上。
    亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
    返回他到离他最近的人的最大距离。

    示例 1：

        输入：[1,0,0,0,1,0,1]
        输出：2

        解释：
            如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
            如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
            因此，他到离他最近的人的最大距离是 2 。

    示例 2：

        输入：[1,0,0,0]
        输出：3
        解释：
        如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
        这是可能的最大距离，所以答案是 3 。

    提示：

        1 <= seats.length <= 20000
        seats 中只含有 0 和 1，至少有一个 0，且至少有一个 1。


"""


# 对于开头结尾都是1的情况，实际上就是找到相邻 1 之间的最大间隔/2，
# 对于开头结尾非1的情况，需要特殊处理。对于[0,1]这种数据（开头非1），
# 我们需要找到第一个1（i位置），关于0位置的对称点（-i位置），认为这个位置有最初的一个虚拟1。
# 对于[1,0]这种数据（结尾非1），我们需要找到最后一个1（j位置），
# 关于len(seats)-1位置的对称点（2 * len(seats) - j - 2），认为这个位置有最后的一个虚拟1。

class Solution(object):

    def maxDistToClosest(self, seats):
        dis = []
        if seats[0] == 0:
            dis.append(-seats.index(1))

        for i in range(len(seats)):
            if seats[i] == 1:
                dis.append(i)

        if seats[-1] == 0:
            dis.append(2 * len(seats) - dis[-1] - 2)


        res = 0
        for i in range(1, len(dis)):
            res = max(res, dis[i] - dis[i-1])
        return res // 2


if __name__ == "__main__":

    S = Solution()
    seats = [1,0,0,0]
    #seats = [1,0,0,0,1,0,1]
    print(S.maxDistToClosest(seats))