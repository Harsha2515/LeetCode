from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        free = [0] * n

        # Calculate free copies for each item
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        minPrice = min(price for factor, price in items)

        dp = [-1] * (budget + 1)
        dp[0] = 0

        # 0/1 Knapsack for first purchases
        for i in range(n):
            factor, price = items[i]
            value = 1 + free[i]

            for b in range(budget, price - 1, -1):
                if dp[b - price] != -1:
                    dp[b] = max(dp[b], dp[b - price] + value)

        # Spend remaining budget on cheapest item
        result = 0

        for b in range(budget + 1):
            if dp[b] != -1:
                remaining = budget - b
                extra = remaining // minPrice
                result = max(result, dp[b] + extra)

        return result