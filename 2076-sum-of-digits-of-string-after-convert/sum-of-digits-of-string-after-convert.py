class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''
        for i in s:
            num += str(ord(i) - 96)
        
        def add(S):
            sumF = 0
            for i in S:
                sumF += int(i)
            return sumF
        
        for i in range(k):
            p = add(num)
            num = str(p)

        return p