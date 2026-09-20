class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        sumF = 0
        for i in range(n):
            sumF += (26-(ord(s[i])-ord('a'))) * (i+1)
        return sumF