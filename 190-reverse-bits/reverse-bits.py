class Solution:
    def reverseBits(self, n: int) -> int:
        k = bin(n)[2:].zfill(32)
        
        return int(k[::-1],2) 