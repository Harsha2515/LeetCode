from math import gcd, lcm
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            p = 1
            g = 0
            l = 1

            for j in range(i, n):
                p *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])

                if p == g * l:
                    max_len = max(max_len, j - i + 1)

        return max_len