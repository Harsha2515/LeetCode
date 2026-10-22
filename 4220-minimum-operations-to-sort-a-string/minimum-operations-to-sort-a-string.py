class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        if n == 2:
            return -1

        smallest = min(s)
        largest = max(s)

        if s[0] == smallest or s[-1] == largest:
            return 1

        if any(s[i] == smallest for i in range(n - 1)):
            return 2

        if any(s[i] == largest for i in range(1, n)):
            return 2

        return 3