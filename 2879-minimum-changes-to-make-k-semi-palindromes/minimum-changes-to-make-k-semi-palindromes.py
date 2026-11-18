
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # Step 1: Precompute divisors
        divisors = [[] for _ in range(n + 1)]

        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)

        # Step 2: Cost of each substring
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = float('inf')

                for d in divisors[length]:
                    changes = 0

                    for start in range(d):
                        left = i + start
                        right = i + start + (length // d - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        # Step 3: Dynamic Programming
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    dp[parts][end] = min(
                        dp[parts][end],
                        dp[parts - 1][start] + cost[start][end - 1]
                    )

        return dp[k][n]
