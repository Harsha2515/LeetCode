from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        increasing = True
        decreasing = True

        for i in range(n - 1):
            diff = (nums[i + 1] - nums[i]) % n
            if diff != 1:
                increasing = False
            if diff != n - 1:
                decreasing = False

        k = nums.index(0)

        if increasing:
            return min(k, n - k + 2)

        if decreasing:
            return min(n - k, k + 2)

        return -1