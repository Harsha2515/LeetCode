class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        p1 = max(nums)
        nums.remove(p1)
        p2 = max(nums)
        nums.remove(p2)

        l1 = min(nums)
        nums.remove(l1)
        l2 = min(nums)
        nums.remove(l2)

        return (p1 * p2) - (l1*l2)