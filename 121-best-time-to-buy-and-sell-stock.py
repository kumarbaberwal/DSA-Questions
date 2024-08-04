"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buyPrice = prices[0]
        maxProfit = 0
        for price in prices[1:]:
            if buyPrice > price:
                buyPrice = price
            maxProfit = max(maxProfit, price - buyPrice)
        return maxProfit


        # i, j = 0, len(prices) - 1
        # maxProfit = 0
        # while j > 0:
        #     i = 0
        #     while i < j:
        #         if prices[i] < prices[j]:
        #             maxProfit = max(maxProfit, prices[j] - prices[i])
        #         i += 1
        #     j -= 1
        # return maxProfit
        
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]
    # prices = [1,2]
    # print(len(prices))
    print(Solution().maxProfit(prices))