class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        # Count eligible free items for each factor
        free = [0] * (n + 1)

        for i in range(1, n + 1):
            if freq[i] == 0:
                continue

            for j in range(i, n + 1, i):
                free[i] += freq[j]

            # Exclude the purchased item itself
            free[i] -= 1

        min_price = min(price for factor, price in items)

        items.sort(key=lambda x: x[1])

        ans = 0

        for factor, price in items:
            if price >= 2 * min_price:
                break

            # Number of purchases that can give free items
            count = min(free[factor], budget // price)

            ans += 2 * count
            budget -= count * price

        # Buy remaining items at the cheapest price
        ans += budget // min_price

        return ans