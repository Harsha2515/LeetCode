class Solution:
    def hammingWeight(self, n: int) -> int:
        k = bin(n)[2:]
        count = 0

        for i in k:
            if i == '1':
                count += 1
        return count