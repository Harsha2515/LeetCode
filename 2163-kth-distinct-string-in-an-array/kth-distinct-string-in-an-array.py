class Solution:
    from collections import Counter
    def kthDistinct(self, arr: list[str], k: int) -> str:
        freq = Counter(arr)

        for key, val in freq.items():
            if val == 1:
                k -= 1
            if k == 0:
                return key
        
        return ''