class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.bit[i]
            i -= i & -i
        return ans

    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)

        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            step >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:

        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        m = len(vals)

        mp = {v: i + 1 for i, v in enumerate(vals)}

        # Two Fenwick trees: counts and sums
        count = Fenwick(m)
        sums = Fenwick(m)

        window_sum = 0
        costs = []

        # Sliding window
        for i in range(n):

            idx = mp[nums[i]]
            count.update(idx, 1)
            sums.update(idx, nums[i])
            window_sum += nums[i]

            if i >= x:
                old = nums[i - x]
                idx = mp[old]

                count.update(idx, -1)
                sums.update(idx, -old)
                window_sum -= old

            if i >= x - 1:

                # Find median (lower median)
                mid = count.kth((x + 1) // 2)
                median = vals[mid - 1]

                # Elements <= median
                left_count = count.query(mid)
                left_sum = sums.query(mid)

                right_count = x - left_count
                right_sum = window_sum - left_sum

                cost = (
                    median * left_count - left_sum
                    + right_sum - median * right_count
                )

                costs.append(cost)

        # DP with O(n) space
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):

            curr = [INF] * (n + 1)

            for i in range(j * x, n + 1):

                # Skip current element
                curr[i] = curr[i - 1]

                # Select subarray [i-x, i-1]
                curr[i] = min(
                    curr[i],
                    prev[i - x] + costs[i - x]
                )

            prev = curr

        return prev[n]