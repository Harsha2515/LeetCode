class Solution:
    from collections import Counter
    def findDuplicates(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        result = []
        for key,val in freq.items():
            if val>1:
                result.append(key)
        return result