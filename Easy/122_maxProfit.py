"""
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    设计一个算法计算你所能获取的最大利润，你可以尽可能的完成更多的交易(多次买卖一支股票)
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    示例1:

        输入: [7,1,5,3,6,4]
        输出: 7
        解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出,
        这笔交易所能获得利润 = 5-1 = 4 。
        随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出,
        这笔交易所能获得利润 = 6-3 = 3 。

    示例 2:

        输入: [1,2,3,4,5]
        输出: 4
        解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出,
        这笔交易所能获得利润 = 5-1 = 4 。
        注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
        因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

    示例 3:

        输入: [7,6,4,3,1]
        输出: 0
        解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

    方法二: 峰谷法：

        假设给定的数组为：
        [7, 1, 5, 3, 6, 4]

        我们的兴趣点事连续的峰和谷。
        用数学语言描述为：TotalProfit = ∑i(height(peak) - height(valley))

        关键是我们需要考虑到紧跟谷的每个峰值以最大化利润，如果我们试图跳过其中
        一个峰值来获取更多利润，那么我们将最终失去其中一笔交易中获得的利润，
        从而导致总利润的降低。

        时间复杂度：O(n)O(n)。遍历一次。
        空间复杂度：O(1)O(1)。需要常量的空间。

    方法三：

        该解决方案遵循 方法二 的本身使用的逻辑，但有一些轻微的变化。
        在这种情况下，我们可以简单地继续在斜坡上爬升并持续增加从连续交易中获得的利润，
        而不是在谷之后寻找每个峰值。最后，我们将有效地使用峰值和谷值，
        但我们不需要跟踪峰值和谷值对应的成本以及最大利润，
        但我们可以直接继续增加加数组的连续数字之间的差值，
        如果第二个数字大于第一个数字，我们获得的总和将是最大利润。
        这种方法将简化解决方案。



"""

# 方法二
"""
class Solution():

    def maxprofit(self, prices):
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0

        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            print("i[%d] ---> valley[%d]:"%(i, valley))
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            print("i[%d] ---> peak[%d]"%(i, peak))
            maxprofit += peak - valley
        return maxprofit

"""

# 方法三
class Solution():

    def maxprofit(self, prices):
        maxprofit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxprofit += prices[i] - prices[i-1]
        return maxprofit


if __name__ == "__main__":
    S = Solution()
    alist = [7,1,5,3,6,9]
    print(S.maxprofit(alist))

