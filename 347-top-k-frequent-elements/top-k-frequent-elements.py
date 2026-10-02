class Solution:
    from collections import Counter
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        Sortf = sorted(freq.items(),key = lambda x:x[1],reverse=True)

        result = []
        for i in range(k):
            result.append(Sortf[i][0])
        return result